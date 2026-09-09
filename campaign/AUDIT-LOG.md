# Audit log

Every file in this repository has passed an adversarial citation audit before publication:
a reviewer independent of the author verified each reference exists and says what was claimed,
checked every number against a retrieved source, deleted unverifiable citations, and demoted
any claim where an early-phase signal or press release had been presented as phase 3 or approved.

This log records the outcome, including what the auditor **could not** resolve. Unresolved
concerns are published rather than buried — a corpus that only publishes its clean results has
the same problem as a literature that only publishes positive trials.

## How to read a row

- **Removed** — citations deleted because they could not be verified to exist. A non-zero number
  here is the audit working, not the corpus failing.
- **Verdict** — `CLEAN`: every remaining citation and headline number was verified against a real
  source. `FLAGGED`: something remains unresolved; see the concerns column.
- **Open concerns** — carried forward as work. These are the highest-priority targets for
  external expert review (workstream W3).

## Mechanical verification — 2026-09-09

The first full network pass over the corpus. Every PMID, DOI, and NCT number was
dereferenced against PubMed, doi.org, and ClinicalTrials.gov.

| Metric | Result |
| --- | --- |
| Files checked | 9 |
| Words | 50,682 |
| References | 633 |
| **Identifiers dereferenced** | **633 / 633 (100%)** |
| **Fabricated or unresolvable citations** | **0** |
| Unreachable after retries | 0 |
| Explicit `[unverified]` markers | 15 |
| Files failing structural checks | 0 |

**What this establishes:** no citation in the corpus is invented. Every reference points at a
real, retrievable record.

**What this does NOT establish, and must not be read as:** that the citations are *correctly
characterized*. A genuine PMID attached to the wrong efficacy figure, the wrong cohort, or the
wrong trial phase passes this check without difficulty. Nor does it say anything about whether
the underlying trials were well designed. Those are the jobs of the adversarial citation audit
and of expert review respectively — **neither of which has run on any file in this corpus.**

### One correction made as a result

`literature/05-menin-inhibitors.md` reference 63 bundled eleven ASH 2025 abstracts with no
dereferenceable identifier. The entry was already honest that the abstracts were not
independently retrieved. It has been anchored to the review it was actually taken from
(PMID 42321887) and marked `[unverified]`, so the claim is now checkable against the source
that genuinely backs it.

### One tooling defect found and fixed

The first run returned 28 HTTP 429 rate-limit responses, which the checker folded into a generic
"not counted" warning — making a partially-checked run look like a clean one. The tool now spaces
requests, retries with backoff, and prints real coverage. Re-run reached 633/633.

## Review layer — `literature/`

_Populated on publication of the review layer._

| File | Refs | Identifiers resolved | Adversarial audit | Open concerns |
| --- | --- | --- | --- | --- |
| `01-epidemiology-classification-risk.md` | 58 | 58/58 | **NOT RUN** | 3 figures marked `[unverified]`: GBD 2040 projection, ELN 3–5 day turnaround target, C-index 0.63 vs 0.59 |
| `02-disease-biology-genomics.md` | 117 | 117/117 | **NOT RUN** | 16 references present but never cited in body |
| `03-intensive-chemotherapy-backbone.md` | 81 | 81/81 | **NOT RUN** | — |
| `04-venetoclax-bcl2-lower-intensity.md` | 102 | 102/102 | **NOT RUN** | 6 `[unverified]`: PARADIGM safety numbers, AZD5991 clinical hold, VIALE-A approval basis, VIALE-A eligibility generalisability |
| `05-menin-inhibitors.md` | 76 | 76/76 | **NOT RUN** | 3 `[unverified]`: AUGMENT-102 efficacy, bundled ASH 2025 abstracts (ref 63); 22 uncited references |

## Reference layer — `reference/`

| File | Refs | Identifiers resolved | Adversarial audit | Open concerns |
| --- | --- | --- | --- | --- |
| `genes/npm1.md` | 48 | 48/48 | **NOT RUN** | 2 `[unverified]`: ClinVar germline submissions, one risk-category assertion |
| `genes/flt3.md` | 45 | 45/45 | **NOT RUN** | — |
| `genes/kmt2a-nup98-fusions.md` | 45 | 45/45 | **NOT RUN** | — |
| `genes/core-binding-factor.md` | 61 | 61/61 | **NOT RUN** | 1 `[unverified]` risk-category assertion |

**Every row reads NOT RUN in the audit column.** The research fleet hit an account usage limit
and all fifteen citation auditors were killed before executing. Until that column changes, the
corpus has been checked for fabrication and nothing else.

## Mechanical checks

Independent of human or agent audit, every change is checked by
[`tools/check_references.py`](../tools/check_references.py) in CI: marker/reference integrity,
contiguous numbering, presence of an identifier on every entry, and — on a weekly schedule —
live resolution of every PMID, DOI, and NCT number. See [`tools/README.md`](../tools/README.md).

A mechanical pass means no citation is fabricated or dangling. It does not mean the science is
sound. Those are different claims and this project keeps them separate.

## Corrections after publication

Post-publication corrections belong here too, with the date, what was wrong, and the source that
settled it. A visible correction history is the only honest signal that a document is maintained.

| Date | File | Correction | Source |
| --- | --- | --- | --- |
