#!/usr/bin/env python3
"""Enforce this repository's evidence rules mechanically.

The rules in README.md are only worth as much as they are checked. This script
checks the ones a machine can check:

  1. Every inline [n] marker resolves to a numbered entry in that file's References section.
  2. Every numbered reference entry is actually cited somewhere in the body.
  3. Every reference entry carries a resolvable identifier (PMID / DOI / NCT / URL).
  4. Reference numbering is contiguous with no gaps or duplicates (a gap is the
     signature of an audit deletion that did not renumber).
  5. Files that make claims but cite nothing are reported.
  6. [unverified] markers are counted, not punished — they are the honest option,
     but a file that is mostly unverified should be visible as such.

It deliberately does NOT judge scientific validity. No script can.

With --online, identifiers are additionally resolved over the network:
PMIDs against NCBI E-utilities, DOIs against doi.org, NCT numbers against
ClinicalTrials.gov. Offline is the default so CI stays fast and hermetic.

Exit status: 0 = clean, 1 = violations found, 2 = usage error.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field

# A citation marker is [n], [n,m,...] or [n-m] / [n–m]; whitespace tolerated.
INLINE_MARKER = re.compile(r"\[(\d{1,3}(?:\s*[,\-\u2013]\s*\d{1,3})*)\]")
REF_ENTRY = re.compile(r"^\s{0,3}(?:\[)?(\d{1,3})(?:\])?[.)]?\s+(.*)$")
REFS_HEADING = re.compile(r"^#{1,4}\s*(?:\d+\.\s*)?references\b", re.IGNORECASE)
ANY_HEADING = re.compile(r"^#{1,4}\s+")

PMID = re.compile(r"\bPMID:?\s*(\d{5,9})\b", re.IGNORECASE)
DOI = re.compile(r"\b(10\.\d{4,9}/[-._;()/:A-Za-z0-9]+)", re.IGNORECASE)
NCT = re.compile(r"\b(NCT\d{8})\b")
URL = re.compile(r"https?://[^\s)>\]]+")
UNVERIFIED = re.compile(r"\[unverified\]", re.IGNORECASE)

# Tier vocabulary from README's evidence rules.
TIER_WORDS = re.compile(
    r"\b(approved|phase\s*(?:1|2|3|I|II|III)|preclinical|hypothes\w+|in vitro|xenograft)\b",
    re.IGNORECASE,
)


@dataclass
class FileReport:
    path: str
    refs: dict = field(default_factory=dict)
    cited: set = field(default_factory=set)
    errors: list = field(default_factory=list)
    warnings: list = field(default_factory=list)
    unverified: int = 0
    words: int = 0
    unresolved: list = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


def split_body_and_refs(lines: list[str]) -> tuple[list[str], list[str]]:
    """Return (body_lines, reference_lines). Reference section runs from the
    References heading to the next heading of equal-or-higher level, or EOF."""
    start = None
    for i, line in enumerate(lines):
        if REFS_HEADING.match(line.strip()):
            start = i
            break
    if start is None:
        return lines, []
    level = len(lines[start]) - len(lines[start].lstrip("#"))
    end = len(lines)
    for j in range(start + 1, len(lines)):
        m = ANY_HEADING.match(lines[j])
        if m:
            this_level = len(lines[j]) - len(lines[j].lstrip("#"))
            if this_level <= level:
                end = j
                break
    return lines[:start], lines[start + 1 : end]


def parse_references(ref_lines: list[str]) -> dict[int, str]:
    refs: dict[int, str] = {}
    current = None
    for raw in ref_lines:
        line = raw.rstrip()
        if not line.strip():
            continue
        m = REF_ENTRY.match(line)
        if m and not line.lstrip().startswith(("|", ">", "#")):
            current = int(m.group(1))
            refs[current] = m.group(2).strip()
        elif current is not None and line.startswith((" ", "\t")):
            refs[current] += " " + line.strip()
    return refs


def has_identifier(entry: str) -> bool:
    return bool(PMID.search(entry) or DOI.search(entry) or NCT.search(entry) or URL.search(entry))


def check_file(path: str, min_refs: int) -> FileReport:
    rep = FileReport(path=path)
    with open(path, "r", encoding="utf-8") as fh:
        text = fh.read()
    lines = text.splitlines()
    body, ref_lines = split_body_and_refs(lines)
    body_text = "\n".join(body)

    rep.words = len(body_text.split())
    rep.unverified = len(UNVERIFIED.findall(text))
    rep.refs = parse_references(ref_lines)

    # Strip fenced code and inline code before hunting for markers, so that a
    # literal [3] in a code sample is not mistaken for a citation.
    scrub = re.sub(r"```.*?```", "", body_text, flags=re.DOTALL)
    scrub = re.sub(r"`[^`]*`", "", scrub)
    # Markdown links like [text](url) and reference-style [1]: are not citations.
    scrub = re.sub(r"\]\([^)]*\)", "]", scrub)
    rep.cited = set()
    for group in INLINE_MARKER.findall(scrub):
        for part in re.split(r"\s*,\s*", group):
            if re.search(r"[\-\u2013]", part):
                lo, hi = (int(x) for x in re.split(r"\s*[\-\u2013]\s*", part))
                rep.cited.update(range(lo, hi + 1))
            else:
                rep.cited.add(int(part))

    if not rep.refs:
        if rep.words > 400:
            rep.errors.append(
                f"substantive file ({rep.words} words) has no parseable References section"
            )
        return rep

    dangling = sorted(rep.cited - set(rep.refs))
    if dangling:
        rep.errors.append(
            "inline markers with no reference entry: " + ", ".join(f"[{n}]" for n in dangling)
        )

    uncited = sorted(set(rep.refs) - rep.cited)
    if uncited:
        rep.warnings.append(
            "reference entries never cited in the body: " + ", ".join(str(n) for n in uncited)
        )

    numbers = sorted(rep.refs)
    expected = list(range(1, len(numbers) + 1))
    if numbers != expected:
        missing = sorted(set(expected) - set(numbers))
        rep.errors.append(
            "reference numbering is not contiguous (audit deletion without renumbering?): "
            f"have {numbers[0]}..{numbers[-1]}, gaps at {missing or 'n/a'}"
        )

    no_id = [n for n, e in rep.refs.items() if not has_identifier(e)]
    if no_id:
        rep.errors.append(
            "reference entries with no PMID/DOI/NCT/URL identifier: "
            + ", ".join(str(n) for n in sorted(no_id))
        )

    if len(rep.refs) < min_refs and rep.words > 1200:
        rep.warnings.append(
            f"only {len(rep.refs)} references for {rep.words} words (expected >= {min_refs})"
        )

    if rep.words > 1200 and not TIER_WORDS.search(body_text):
        rep.warnings.append(
            "no evidence-tier vocabulary found (approved / phase N / preclinical / hypothesis)"
        )

    return rep


# NCBI asks for <=3 requests/second without an API key. Being a good citizen
# is also self-interested: hammering the endpoint earns HTTP 429s, and a mass
# of 429s silently degrades this whole check into "not counted" — a linter that
# has quietly stopped linting is worse than no linter, because it still reports
# success.
_MIN_INTERVAL = 0.4
_last_request = [0.0]


def _throttled_open(url: str, timeout: float, headers: dict | None = None):
    """Open a URL, spacing requests and retrying on rate limiting.

    429 and 503 are retried with exponential backoff, honouring Retry-After
    when the server sends it. Every other status is raised to the caller,
    which decides whether it means "fabricated" or merely "unreachable".
    """
    delays = [1.0, 3.0, 8.0]
    for attempt in range(len(delays) + 1):
        wait = _MIN_INTERVAL - (time.monotonic() - _last_request[0])
        if wait > 0:
            time.sleep(wait)
        req = urllib.request.Request(url, headers=headers or {})
        try:
            resp = urllib.request.urlopen(req, timeout=timeout)
            _last_request[0] = time.monotonic()
            return resp
        except urllib.error.HTTPError as exc:
            _last_request[0] = time.monotonic()
            if exc.code in (429, 503) and attempt < len(delays):
                retry_after = exc.headers.get("Retry-After") if exc.headers else None
                try:
                    backoff = float(retry_after) if retry_after else delays[attempt]
                except ValueError:
                    backoff = delays[attempt]
                time.sleep(min(backoff, 30.0))
                continue
            raise


def resolve_online(rep: FileReport, timeout: float) -> None:
    """Best-effort network resolution of identifiers. Network failures are
    reported as warnings, never errors — a flaky proxy must not fail CI."""
    for n, entry in sorted(rep.refs.items()):
        pmid = PMID.search(entry)
        nct = NCT.search(entry)
        doi = DOI.search(entry)
        try:
            if pmid:
                url = (
                    "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
                    f"?db=pubmed&retmode=json&id={pmid.group(1)}"
                )
                with _throttled_open(url, timeout) as r:
                    data = json.load(r)
                result = data.get("result", {})
                rec = result.get(pmid.group(1))
                if not rec or "error" in rec:
                    rep.errors.append(f"[{n}] PMID {pmid.group(1)} does not resolve in PubMed")
            elif nct:
                url = f"https://clinicaltrials.gov/api/v2/studies/{nct.group(1)}"
                with _throttled_open(url, timeout, {"Accept": "application/json"}) as r:
                    if r.status != 200:
                        rep.errors.append(f"[{n}] {nct.group(1)} not found on ClinicalTrials.gov")
            elif doi:
                url = "https://doi.org/api/handles/" + urllib.parse.quote(doi.group(1))
                with _throttled_open(url, timeout) as r:
                    data = json.load(r)
                if data.get("responseCode") != 1:
                    rep.errors.append(f"[{n}] DOI {doi.group(1)} does not resolve")
        except urllib.error.HTTPError as exc:
            if exc.code in (404, 400):
                rep.errors.append(f"[{n}] identifier lookup returned {exc.code} — likely not real")
            elif exc.code in (429, 503):
                rep.unresolved.append(n)
                rep.warnings.append(
                    f"[{n}] STILL RATE-LIMITED after retries — NOT VERIFIED, re-run needed"
                )
            else:
                rep.warnings.append(f"[{n}] lookup failed with HTTP {exc.code} (not counted)")
        except Exception as exc:  # network, TLS, timeout, malformed JSON
            rep.unresolved.append(n)
            rep.warnings.append(
                f"[{n}] lookup could not complete ({type(exc).__name__}) — NOT VERIFIED"
            )


def collect(paths: list[str]) -> list[str]:
    out: list[str] = []
    for p in paths:
        if os.path.isdir(p):
            for root, _dirs, files in os.walk(p):
                for f in sorted(files):
                    if f.endswith(".md"):
                        out.append(os.path.join(root, f))
        elif p.endswith(".md"):
            out.append(p)
    return sorted(set(out))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="*", default=["literature", "reference"],
                    help="markdown files or directories (default: literature reference)")
    ap.add_argument("--online", action="store_true",
                    help="resolve PMIDs, DOIs and NCT numbers over the network")
    ap.add_argument("--timeout", type=float, default=15.0)
    ap.add_argument("--min-refs", type=int, default=15,
                    help="warn below this reference count for long files (default 15)")
    ap.add_argument("--strict", action="store_true", help="treat warnings as failures")
    args = ap.parse_args()

    files = collect(args.paths)
    if not files:
        print("no markdown files found in: " + ", ".join(args.paths), file=sys.stderr)
        return 2

    reports = []
    for path in files:
        rep = check_file(path, args.min_refs)
        if args.online and rep.refs:
            resolve_online(rep, args.timeout)
        reports.append(rep)

    total_refs = sum(len(r.refs) for r in reports)
    total_words = sum(r.words for r in reports)
    total_unverified = sum(r.unverified for r in reports)
    total_unresolved = sum(len(r.unresolved) for r in reports)
    failed = [r for r in reports if r.errors or (args.strict and r.warnings)]

    for rep in reports:
        if not rep.errors and not rep.warnings:
            print(f"  ok    {rep.path}  ({len(rep.refs)} refs, {rep.words} words)")
            continue
        mark = "FAIL" if rep.errors else "warn"
        print(f"{mark:>6}  {rep.path}  ({len(rep.refs)} refs, {rep.words} words)")
        for e in rep.errors:
            print(f"          error: {e}")
        for w in rep.warnings:
            print(f"          warn:  {w}")

    print()
    print(f"{len(reports)} files | {total_words:,} words | {total_refs} references "
          f"| {total_unverified} [unverified] markers | {len(failed)} failing")
    if args.online:
        checked = total_refs - total_unresolved
        print(f"identifier resolution: ON — {checked}/{total_refs} identifiers actually "
              f"dereferenced, {total_unresolved} could not be reached")
        if total_unresolved:
            print("  NOTE: unreached identifiers are NOT verified. Re-run before "
                  "claiming the corpus is checked.")
    else:
        print("identifier resolution: OFF — run with --online to verify identifiers actually resolve")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
