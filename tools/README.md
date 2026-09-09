# tools/

## `check_references.py`

Mechanical enforcement of the evidence rules in [../README.md](../README.md). Run it before
opening a pull request that touches the corpus.

```bash
# Structural checks — fast, no network. This is what CI runs on every push.
python3 tools/check_references.py literature reference

# Additionally resolve every PMID, DOI and NCT number over the network.
# This is the check that catches a fabricated citation.
python3 tools/check_references.py literature reference --online

# Treat warnings as failures too.
python3 tools/check_references.py literature reference --strict
```

### What it checks

| Check | Severity | Why it exists |
| --- | --- | --- |
| Every inline `[n]` resolves to a reference entry | error | A marker with no source is an uncited claim wearing a citation's clothes. |
| Reference numbering is contiguous | error | A gap is the fingerprint of an audit deletion that never renumbered, which silently shifts every later marker onto the wrong source. |
| Every entry has a PMID / DOI / NCT / URL | error | An identifier-free reference cannot be verified by anyone, including a future auditor. |
| Identifiers actually resolve (`--online`) | error | This is the fabrication check. A fake PMID looks exactly like a real one until something dereferences it. |
| Identifiers that could not be reached | reported | Counted separately and named in the summary line. An unreached identifier is **not** a passed one. |
| Substantive file has a References section | error | Long files with no sources are the failure mode this project is organized against. |
| Entries that are never cited | warning | Usually harmless, sometimes the residue of deleted text. |
| Reference density for long files | warning | Cheap proxy for "asserted more than it sourced". |
| Evidence-tier vocabulary present | warning | Files should say whether something is approved, phase N, or preclinical. |
| `[unverified]` markers | counted | **Not a failure.** Marking a claim unverified is the honest option and is encouraged. The count exists so a mostly-unverified file is visible as such. |

### What it deliberately does not check

Scientific validity. A verified citation to a badly designed trial is still a verified citation, and
no script can tell the difference. That is expert review — workstream W3 in
[../campaign/CAMPAIGN.md](../campaign/CAMPAIGN.md) — and it is the corpus's largest open weakness.

Network failures in `--online` mode are reported as warnings, never errors: a flaky proxy or a
rate-limited API must not be able to fail CI, because a linter that cries wolf gets switched off.
Only a definitive negative (a 404, or PubMed reporting no such record) is an error.

**But an unreachable identifier is never counted as verified.** Requests are spaced (~0.4s, inside
NCBI's 3/second guidance) and retried with exponential backoff on HTTP 429 and 503, honouring
`Retry-After`. Anything still unreachable after retries is listed by number and subtracted from the
coverage figure printed at the end:

```
identifier resolution: ON — 605/633 identifiers actually dereferenced, 28 could not be reached
  NOTE: unreached identifiers are NOT verified. Re-run before claiming the corpus is checked.
```

This distinction is the point. The first run of this tool over the corpus returned 28 HTTP 429s that
the earlier version folded into a generic "not counted" warning — which, at a glance, looked like a
clean pass. A linter that has quietly stopped linting is worse than no linter, because it still
reports success.
