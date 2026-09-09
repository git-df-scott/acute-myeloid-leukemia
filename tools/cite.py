#!/usr/bin/env python3
"""Retrieve a citation before you write it.

The one rule in this repository is that no citation is written without having
been retrieved. This script makes retrieval the easy path: give it a PMID, DOI,
NCT number, or a PubMed search, and it prints a reference entry in the exact
format the corpus uses, built only from what the source database returned.

    python3 tools/cite.py 31821784 10.1056/NEJMoa2012971 NCT04065399
    python3 tools/cite.py --abstract 31821784
    python3 tools/cite.py --search "venetoclax azacitidine VIALE-A phase 3" --max 8
    python3 tools/cite.py --nct-detail NCT04065399

Sources: NCBI E-utilities (PubMed), Crossref (DOI), ClinicalTrials.gov API v2
(NCT). Requests are spaced (~0.4 s) to stay inside NCBI's rate guidance and are
retried with backoff on 429/503.

It prints what the database says. It does not, and cannot, tell you whether the
paper supports the claim you are about to attach it to — read the abstract
(--abstract) or the paper for that.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
CROSSREF = "https://api.crossref.org/works/"
CTGOV = "https://clinicaltrials.gov/api/v2/studies/"
UA = "aml-cure-campaign-cite/1.0 (https://github.com/git-df-scott/acute-myeloid-leukemia)"

_last = 0.0


def _get(url: str, timeout: float = 30.0) -> bytes:
    global _last
    wait = 0.4 - (time.monotonic() - _last)
    if wait > 0:
        time.sleep(wait)
    delay = 1.0
    for attempt in range(5):
        _last = time.monotonic()
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code in (429, 503) and attempt < 4:
                ra = e.headers.get("Retry-After")
                time.sleep(float(ra) if ra and ra.isdigit() else delay)
                delay *= 2
                continue
            raise
        except (urllib.error.URLError, TimeoutError):
            if attempt < 4:
                time.sleep(delay)
                delay *= 2
                continue
            raise
    raise RuntimeError("unreachable")


# ---------------------------------------------------------------- PubMed ----

def pubmed_fetch(pmids: list[str]) -> list[dict]:
    if not pmids:
        return []
    url = EUTILS + "efetch.fcgi?" + urllib.parse.urlencode(
        {"db": "pubmed", "id": ",".join(pmids), "retmode": "xml"}
    )
    root = ET.fromstring(_get(url))
    out = []
    for art in root.findall(".//PubmedArticle"):
        rec: dict = {}
        med = art.find("MedlineCitation")
        rec["pmid"] = (med.findtext("PMID") or "").strip()
        a = med.find("Article")
        rec["title"] = "".join(a.find("ArticleTitle").itertext()).strip().rstrip(".") if a.find("ArticleTitle") is not None else ""
        j = a.find("Journal")
        rec["journal"] = (j.findtext("ISOAbbreviation") or j.findtext("Title") or "").strip() if j is not None else ""
        ji = j.find("JournalIssue") if j is not None else None
        rec["volume"] = (ji.findtext("Volume") or "").strip() if ji is not None else ""
        rec["issue"] = (ji.findtext("Issue") or "").strip() if ji is not None else ""
        year = ""
        if ji is not None:
            pd = ji.find("PubDate")
            if pd is not None:
                year = (pd.findtext("Year") or "").strip()
                if not year:
                    md = (pd.findtext("MedlineDate") or "").strip()
                    m = re.search(r"\d{4}", md)
                    year = m.group(0) if m else ""
        if not year:
            for d in art.findall(".//PubMedPubDate"):
                if d.get("PubStatus") in ("pubmed", "entrez"):
                    year = (d.findtext("Year") or "").strip()
                    break
        rec["year"] = year
        rec["pages"] = (a.findtext("Pagination/MedlinePgn") or "").strip()
        rec["eloc"] = ""
        for e in a.findall("ELocationID"):
            if e.get("EIdType") == "doi":
                rec["doi"] = (e.text or "").strip()
            elif e.get("EIdType") == "pii" and not rec["pages"]:
                rec["eloc"] = (e.text or "").strip()
        if "doi" not in rec:
            for aid in art.findall(".//ArticleIdList/ArticleId"):
                if aid.get("IdType") == "doi":
                    rec["doi"] = (aid.text or "").strip()
        rec.setdefault("doi", "")
        authors = []
        for au in a.findall("AuthorList/Author"):
            ln = au.findtext("LastName")
            ini = au.findtext("Initials")
            coll = au.findtext("CollectiveName")
            if ln:
                authors.append(f"{ln} {ini}".strip())
            elif coll:
                authors.append(coll.strip())
        rec["authors"] = authors
        rec["pubtypes"] = [pt.text for pt in a.findall("PublicationTypeList/PublicationType") if pt.text]
        abs_parts = []
        for ab in a.findall("Abstract/AbstractText"):
            label = ab.get("Label")
            txt = "".join(ab.itertext()).strip()
            abs_parts.append(f"{label}: {txt}" if label else txt)
        rec["abstract"] = "\n".join(abs_parts)
        out.append(rec)
    return out


def pubmed_search(term: str, maxn: int) -> list[str]:
    url = EUTILS + "esearch.fcgi?" + urllib.parse.urlencode(
        {"db": "pubmed", "term": term, "retmode": "json", "retmax": str(maxn), "sort": "relevance"}
    )
    data = json.loads(_get(url))
    return data.get("esearchresult", {}).get("idlist", [])


def fmt_pubmed(rec: dict, n: int | None, max_authors: int = 30) -> str:
    au = rec["authors"]
    if len(au) > max_authors:
        au = au[:max_authors] + ["et al"]
    authors = ", ".join(au) if au else "[no author list in PubMed record]"
    vol = rec["volume"]
    if rec["issue"]:
        vol += f"({rec['issue']})"
    pages = rec["pages"] or rec["eloc"]
    cite = f"{rec['year']};{vol}:{pages}" if vol or pages else rec["year"]
    parts = [authors, rec["title"], rec["journal"], cite, f"PMID {rec['pmid']}"]
    if rec["doi"]:
        parts.append(f"DOI {rec['doi']}")
    line = " — ".join(p for p in parts if p)
    return f"{n}. {line}" if n is not None else line


# --------------------------------------------------------------- Crossref ----

def crossref_fetch(doi: str) -> dict:
    data = json.loads(_get(CROSSREF + urllib.parse.quote(doi, safe="")))["message"]
    rec: dict = {"doi": data.get("DOI", doi)}
    rec["title"] = (data.get("title") or [""])[0].strip().rstrip(".")
    rec["journal"] = (data.get("container-title") or data.get("short-container-title") or [""])[0]
    rec["volume"] = data.get("volume", "") or ""
    rec["issue"] = data.get("issue", "") or ""
    rec["pages"] = data.get("page", "") or data.get("article-number", "") or ""
    y = ""
    for k in ("published-print", "published-online", "issued", "created"):
        dp = data.get(k, {}).get("date-parts", [[None]])
        if dp and dp[0] and dp[0][0]:
            y = str(dp[0][0])
            break
    rec["year"] = y
    rec["type"] = data.get("type", "")
    authors = []
    for a in data.get("author", []) or []:
        if "family" in a:
            given = a.get("given", "")
            ini = "".join(w[0] for w in re.split(r"[\s\-]+", given) if w)
            authors.append(f"{a['family']} {ini}".strip())
        elif "name" in a:
            authors.append(a["name"])
    rec["authors"] = authors
    rec["abstract"] = re.sub(r"<[^>]+>", "", data.get("abstract", "") or "")
    return rec


def fmt_crossref(rec: dict, n: int | None, max_authors: int = 30) -> str:
    au = rec["authors"]
    if len(au) > max_authors:
        au = au[:max_authors] + ["et al"]
    authors = ", ".join(au) if au else "[no author list in Crossref record]"
    vol = rec["volume"]
    if rec["issue"]:
        vol += f"({rec['issue']})"
    cite = f"{rec['year']};{vol}:{rec['pages']}" if vol or rec["pages"] else rec["year"]
    parts = [authors, rec["title"], rec["journal"], cite, f"DOI {rec['doi']}"]
    line = " — ".join(p for p in parts if p)
    return f"{n}. {line}" if n is not None else line


# ------------------------------------------------------- ClinicalTrials.gov ----

def ctgov_fetch(nct: str) -> dict:
    fields = ",".join([
        "NCTId", "BriefTitle", "OfficialTitle", "OverallStatus", "Phase", "EnrollmentInfo",
        "StartDate", "PrimaryCompletionDate", "CompletionDate", "LeadSponsorName",
        "PrimaryOutcome", "Condition", "InterventionName", "StudyType", "DesignAllocation",
        "DesignInfo", "ArmGroup", "ResultsFirstPostDate", "LastUpdatePostDate", "WhyStopped",
    ])
    data = json.loads(_get(CTGOV + nct + "?" + urllib.parse.urlencode({"fields": fields})))
    ps = data.get("protocolSection", {})
    idm = ps.get("identificationModule", {})
    st = ps.get("statusModule", {})
    dm = ps.get("designModule", {})
    om = ps.get("outcomesModule", {})
    return {
        "nct": idm.get("nctId", nct),
        "title": idm.get("briefTitle", ""),
        "official": idm.get("officialTitle", ""),
        "status": st.get("overallStatus", ""),
        "why_stopped": st.get("whyStopped", ""),
        "start": st.get("startDateStruct", {}).get("date", ""),
        "pcd": st.get("primaryCompletionDateStruct", {}).get("date", ""),
        "results_posted": st.get("resultsFirstPostDateStruct", {}).get("date", ""),
        "last_update": st.get("lastUpdatePostDateStruct", {}).get("date", ""),
        "phases": dm.get("phases", []),
        "allocation": dm.get("designInfo", {}).get("allocation", ""),
        "enrollment": dm.get("enrollmentInfo", {}),
        "sponsor": ps.get("sponsorCollaboratorsModule", {}).get("leadSponsor", {}).get("name", ""),
        "conditions": ps.get("conditionsModule", {}).get("conditions", []),
        "interventions": [i.get("name", "") for i in ps.get("armsInterventionsModule", {}).get("interventions", [])],
        "arms": [(a.get("label", ""), a.get("type", "")) for a in ps.get("armsInterventionsModule", {}).get("armGroups", [])],
        "primary_outcomes": [o.get("measure", "") for o in om.get("primaryOutcomes", [])],
    }


def fmt_ctgov(rec: dict, n: int | None) -> str:
    e = rec["enrollment"]
    enr = f"{e.get('count', '?')} ({e.get('type', '').lower()})" if e else "?"
    ph = "/".join(p.replace("PHASE", "phase ") for p in rec["phases"]) or "phase not stated"
    line = (
        f"ClinicalTrials.gov — {rec['title']} — {rec['nct']} — {ph}; status {rec['status']}"
        f"; enrollment {enr}; sponsor {rec['sponsor']} — https://clinicaltrials.gov/study/{rec['nct']}"
    )
    return f"{n}. {line}" if n is not None else line


def print_ctgov_detail(rec: dict) -> None:
    print(fmt_ctgov(rec, None))
    for k in ("official", "status", "why_stopped", "start", "pcd", "results_posted", "last_update",
              "allocation", "conditions", "interventions", "arms", "primary_outcomes"):
        v = rec.get(k)
        if v:
            print(f"  {k}: {v}")


# ------------------------------------------------------------------- main ----

def classify(tok: str) -> tuple[str, str]:
    t = tok.strip()
    if re.fullmatch(r"NCT\d{8}", t, re.IGNORECASE):
        return "nct", t.upper()
    if re.fullmatch(r"\d{5,9}", t):
        return "pmid", t
    if re.match(r"10\.\d{4,9}/", t):
        return "doi", t
    m = re.search(r"pubmed\.ncbi\.nlm\.nih\.gov/(\d+)", t)
    if m:
        return "pmid", m.group(1)
    m = re.search(r"doi\.org/(10\.\S+)", t)
    if m:
        return "doi", m.group(1)
    return "unknown", t


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ids", nargs="*", help="PMIDs, DOIs, NCT numbers, or PubMed/DOI URLs")
    ap.add_argument("--search", help="PubMed search term (esearch syntax)")
    ap.add_argument("--max", type=int, default=10, help="max search hits")
    ap.add_argument("--abstract", action="store_true", help="also print abstracts")
    ap.add_argument("--nct-detail", action="store_true", help="print full trial registry detail for NCT numbers")
    ap.add_argument("--start", type=int, default=None, help="number entries starting here")
    ap.add_argument("--json", action="store_true", help="emit raw JSON records")
    args = ap.parse_args()

    if not args.ids and not args.search:
        ap.print_help()
        return 2

    ids = list(args.ids)
    if args.search:
        found = pubmed_search(args.search, args.max)
        if not found:
            print(f"# PubMed search returned nothing for: {args.search}", file=sys.stderr)
        ids = found + ids

    n = args.start
    pmids = [classify(t)[1] for t in ids if classify(t)[0] == "pmid"]
    pm = {r["pmid"]: r for r in pubmed_fetch(pmids)} if pmids else {}

    rc = 0
    for tok in ids:
        kind, val = classify(tok)
        try:
            if kind == "pmid":
                rec = pm.get(val)
                if rec is None:
                    print(f"# PMID {val}: NOT FOUND in PubMed — do not cite", file=sys.stderr)
                    rc = 1
                    continue
                print(json.dumps(rec, ensure_ascii=False) if args.json else fmt_pubmed(rec, n))
                if args.abstract:
                    print("   " + (rec["abstract"] or "[no abstract in record]").replace("\n", "\n   "))
                    print()
            elif kind == "doi":
                rec = crossref_fetch(val)
                print(json.dumps(rec, ensure_ascii=False) if args.json else fmt_crossref(rec, n))
                if args.abstract and rec.get("abstract"):
                    print("   " + rec["abstract"])
                    print()
            elif kind == "nct":
                rec = ctgov_fetch(val)
                if args.json:
                    print(json.dumps(rec, ensure_ascii=False))
                elif args.nct_detail:
                    print_ctgov_detail(rec)
                else:
                    print(fmt_ctgov(rec, n))
            else:
                print(f"# {tok}: not a PMID, DOI or NCT — not looked up", file=sys.stderr)
                rc = 1
                continue
        except urllib.error.HTTPError as e:
            print(f"# {tok}: HTTP {e.code} — NOT retrieved, do not cite", file=sys.stderr)
            rc = 1
            continue
        except Exception as e:  # noqa: BLE001
            print(f"# {tok}: {e.__class__.__name__}: {e} — NOT retrieved, do not cite", file=sys.stderr)
            rc = 1
            continue
        if n is not None:
            n += 1
    return rc


if __name__ == "__main__":
    sys.exit(main())
