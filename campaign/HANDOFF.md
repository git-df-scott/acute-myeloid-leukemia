# Handoff — state of the AML cure campaign

**Date:** 2026-09-09 · **Branch:** `claude/wonderful-cori-m8j7n8` (also the repository's default branch)
· **Repository:** public

This document exists so that a person or session picking this up cold knows exactly what is here,
what is verified, what is missing, and what is blocked. Read it before writing anything new.

---

## 1. Bottom line

Nine substantive documents exist — **50,682 words, 633 references, every single identifier
dereferenced against a live registry, zero fabricated citations.** That is roughly a third of the
planned corpus.

**Nothing has been audited for accuracy, and nothing has been reviewed by an expert.** The
fabrication check proves the citations are *real*; it says nothing about whether they are
*correctly characterized*. A genuine PMID attached to the wrong efficacy figure passes it without
difficulty.

Everything is committed and pushed. Nothing is at risk of loss.

---

## 2. Repository state

| Item | State |
| --- | --- |
| Commits on branch | 7, all pushed; working tree clean |
| Default branch | `claude/wonderful-cori-m8j7n8` — the repo was empty, so the first push became default |
| Open pull request | **None, and none is possible** — a PR needs a base branch different from head, and this is the only branch |
| Visibility | **Public** |

### Two decisions left open for the owner

1. **Repo structure.** There is no `main`. If you want a conventional trunk plus PR review flow,
   someone must create `main` and re-point the default branch. Not done here because pushing to a
   branch other than the designated one was outside what was authorized.
2. **Visibility.** The repository is public and now contains AI-assisted, unaudited medical
   content. `README.md` carries a status table and `DISCLAIMER.md` states it is not medical advice,
   so this is disclosed rather than hidden — but whether it should be public *at this maturity* is a
   judgment call that belongs to the owner.

---

## 3. What exists

### Infrastructure (complete)

| File | Purpose |
| --- | --- |
| `README.md` | Framing, evidence rules, and a front-page status table showing what is unverified |
| `METHODOLOGY.md` | How the corpus is built; candid section on what this method cannot establish |
| `CLAUDE.md` | Evidence rules encoded so future sessions inherit them |
| `DISCLAIMER.md` | Not medical advice; AI-assisted; not peer reviewed |
| `LICENSE` | CC BY 4.0 for the corpus, MIT for tooling |
| `campaign/CAMPAIGN.md` | Goal, six workstreams, milestones, "how this could fail" |
| `campaign/CONTRIBUTING.md` | Corrections ranked as the highest-value contribution |
| `campaign/AUDIT-LOG.md` | Per-file verification status, including unresolved concerns |
| `tools/check_references.py` | Mechanical enforcement of the evidence rules |
| `.github/workflows/evidence-check.yml` | Structural checks per push; network resolution weekly |

### Corpus (9 of ~37 planned files)

**Review layer** — `literature/`, argued synthesis per domain:

| File | Words | Refs |
| --- | --- | --- |
| `01-epidemiology-classification-risk.md` | 6,418 | 58 |
| `02-disease-biology-genomics.md` | 6,088 | 117 |
| `03-intensive-chemotherapy-backbone.md` | 8,184 | 81 |
| `04-venetoclax-bcl2-lower-intensity.md` | 10,463 | 102 |
| `05-menin-inhibitors.md` | 6,273 | 76 |

**Reference layer** — `reference/genes/`, per-lesion look-up monographs:

| File | Words | Refs |
| --- | --- | --- |
| `npm1.md` | 3,203 | 48 |
| `flt3.md` | 3,248 | 45 |
| `kmt2a-nup98-fusions.md` | 3,327 | 45 |
| `core-binding-factor.md` | 3,478 | 61 |

---

## 4. Verification status

Run `python3 tools/check_references.py literature reference --online` to reproduce.

| Metric | Result |
| --- | --- |
| Identifiers dereferenced (PubMed / doi.org / ClinicalTrials.gov) | **633 / 633** |
| Fabricated or unresolvable citations | **0** |
| Files failing structural checks | 0 |
| Explicit `[unverified]` markers | 15 |
| **Files passed adversarial citation audit** | **0 of 9** |
| **Files expert-reviewed** | **0 of 9** |

A defect was found and fixed in the checker itself: the first pass returned 28 HTTP 429s that were
folded into a generic warning, making a partial check look complete. It now backs off, retries, and
prints true coverage. **First reported figure was 605/633, not 633/633** — the gap was invisible
until inspected.

### The 15 `[unverified]` claims, by file

- **01** — GBD 2040 projection (~184,000 cases / ~166,000 deaths); ELN "3–5 day" molecular
  turnaround target; C-index 0.63 vs 0.59 for a refined ELN 2024 model.
- **04** — PARADIGM safety numbers; AMG 397 / AZD5991 FDA clinical hold (trade press only);
  VIALE-A 2020 regular-approval basis; the "~66% would have met VIALE-A eligibility" figure
  (21-patient cohort, quoted as signal only).
- **05** — AUGMENT-102 efficacy (~50–56% composite CR, secondary coverage only); ref 63, a bundle
  of eleven ASH 2025 abstracts not independently retrieved, now anchored to PMID 42321887.
- **npm1 / core-binding-factor** — ClinVar germline submissions; two risk-category assertions.

---

## 5. Substantive findings

Drawn from the structured returns of 7 of the 9 authoring agents. The menin-inhibitor and
core-binding-factor agents wrote their files but died before returning summaries — **their content
is on disk and is not represented below.** All of this is **unaudited**; verify before relying on it.

### 5.1 The central fact

Survival gains are real but almost entirely confined to the young. Across 29,107 SEER de novo AML
patients, 5-year OS rose 9% → 15% → 22% → 28% across the 1980s/90s/2000s/2010–17, reaching **63% in
ages 15–39 — and remaining 5% in patients aged 70+**, with 4-week mortality still 20–45%. SEER
projects 22,720 new US cases and 11,500 deaths in 2026; median age at diagnosis is 70.

Global burden is rising on demographics alone: GBD 2021 reports incident AML up 82% (79,372 → 144,645
between 1990 and 2021) and deaths up 74%.

**Undertreatment is a first-order problem, not a footnote.** Among 7,665 SEER-Medicare patients
aged 65+, **31% received neither antileukemic therapy nor supportive care**; 95.3% were dead by 180 days.

### 5.2 Root barriers to cure, as the corpus states them

1. **The relapse reservoir is invisible to every endpoint we use.** CR is defined morphologically
   and by bulk MRD, but regenerating cells are rare, quiescent, sometimes preleukemic rather than
   leukemic.
2. **Preleukemic HSCs are too normal to target.** DNMT3A/TET2/ASXL1-mutant HSCs sit inside a
   normal-looking multilineage compartment with a competitive advantage; eradicating them risks
   marrow failure. No agent distinguishes them from wild-type HSCs.
3. **Resistance converges phenotypically from independent routes.** RAS activation arrives by
   mutation, by transcriptional upregulation, *or* by monocytic differentiation shift — three paths
   to one phenotype, which defeats sequential single-target strategies.
4. **Differentiation state often beats genotype as the determinant of drug response**, yet
   stratification remains genotype-based — and ELN 2022 demonstrably fails under the most widely
   used lower-intensity regimen.
5. **BAX is a single point of failure for the whole BH3-mimetic class.** Inactivating BAX mutations
   arise in 17% of post-venetoclax relapses; no BCL-2, MCL-1, or BCL-xL inhibitor can kill a
   BAX-null cell.
6. **TP53-mutant AML remains untouched.** Median OS ~6 months whether treated with VEN+HMA,
   intensive chemotherapy, or HMA alone. Magrolimab, developed for this population, failed in both
   ENHANCE-2 and ENHANCE-3.
7. **The cytotoxic dose-response curve is flat.** Four independent randomizations converge on
   plateau; intensification cannot deepen remission, and the therapeutic index is set by neutropenia
   duration rather than leukemia biology.
8. **Immune escape is decoupled from genotype.** MHC class II downregulation drives post-transplant
   relapse with the target antigen intact.
9. **Cure as currently defined does not restore normal hematopoiesis.** 61.9% of 373 long-term AML
   survivors carried clonal hematopoiesis variants.
10. **Evidence is generated in a population that is not the disease population.** Reference genomic
    cohorts are dominated by intensive-therapy-fit patients; only 23.3% of AML randomized trials
    reported race/ethnicity, and among those, participants were 80.8% White (enrollment incidence
    ratios: 0.28 Hispanic, 0.16 Asian, 1.23 White).

### 5.3 Measurement and classification problems

- **WHO-HAEM5 and ICC 2022 are not interchangeable.** In 1,001 real-world patients, reclassification
  versus WHO 2016 was 22.8% (WHO 2022) and 23.7% (ICC), with **13.1% of patients distributed
  differently between the two 2022 systems.** No harmonized successor was located as of 2026-09-09.
  This propagates into eligibility criteria and historical controls.
- **ELN 2022 absorbs 72.8–78% of the venetoclax-era population into a single adverse category** —
  losing resolution exactly where the epidemiologic mass of the disease sits.
- **Composite CR is not tracking survival.** Single-arm triplets advance on CRc 80–96% while
  PEVENAZA (EFS HR 0.99) and ENHANCE-3 (OS HR 1.178) failed; VERONA improved ORR by 18.5 absolute
  points with OS HR 0.908. The discovery pipeline may be optimizing the wrong endpoint.
- **No risk model has been shown in a randomized design to improve survival by changing treatment
  allocation.**

### 5.4 Negative results worth preserving

These are the entries most likely to be lost from an optimistic literature:

- **Every clinical-stage MCL-1 inhibitor is terminated**, cardiac toxicity the recurring signal.
  S64315 produced **no objective responses** at cardiac-limited doses. Two reviews now call the
  toxicity class-wide rather than compound-specific.
- **Magrolimab failed twice** in TP53-mutant disease (ENHANCE-2, ENHANCE-3); ENHANCE-3's excess
  mortality was driven by grade 5 infections.
- **LACEWING** stopped for futility despite CRc 58.1% vs 26.5% — a clean demonstration that response
  rate does not imply survival.
- **Pinometostat** (DOT1L inhibitor): 51 adults with KMT2Ar leukemia, only **two** complete remissions.
- **CPX-351 was actively harmful in chemosensitive genotypes** — worse than DA in NPM1-mutated
  (HR 2.83) and FLT3-mutated (HR 2.14) older adults, and raised 2-year relapse in low-risk pediatric
  AML (39.9% vs 23.6%).
- **Allo-HSCT in CR1 did not improve OS** in 1,130 children with KMT2Ar AML — discordant with adult
  practice.
- **Luveltamab tazevibulin**, lead asset for CBFA2T3::GLIS2 AML, deprioritised for business reasons;
  REFRαME-P1 terminated. An access failure, not a science failure.
- **IACS-010759** could not maintain target exposure without lactic acidosis and peripheral neuropathy.

### 5.5 Practice-changing positives

- **Two menin inhibitors approved**, both verified on fda.gov: **revumenib** (Revuforj) 24 Oct 2025
  for R/R NPM1-mutant AML in adults *and* children ≥1 year — earlier approved 15 Nov 2024 for
  KMT2A-translocated acute leukemia; **ziftomenib** (Komzifti) 13 Nov 2025, **adults only, NPM1 only
  — not KMT2Ar.** Revumenib carries a *double* boxed warning (differentiation syndrome, QTc/torsades);
  differentiation syndrome occurred in 25% of treated patients.
- **MRD, not FLT3-ITD, should drive the CR1 transplant decision.** In 737 patients on NCRI
  AML17/AML19, CR1 allografting improved OS **only** in MRD-positive patients (3-year OS 61% vs 24%;
  HR 0.39) with **no benefit** in MRD-negative patients.
- **PARADIGM**: azacitidine+venetoclax beat intensive chemotherapy on EFS in transplant-eligible
  patients (14.5 vs 6.2 months, HR 0.57) — though it excluded CBF, FLT3-mutated, and (under 60)
  NPM1-mutated disease.
- **ELN-DAVID 2025 MRD consensus** now recommends ultra-high-sensitivity NGS FLT3-ITD MRD after
  intensive chemotherapy and before allo-HCT.

---

## 6. What is missing

**Review layer — 10 of 15 domains unwritten:** FLT3-targeted therapy · IDH and metabolic targeting ·
TP53 and adverse-risk · immunotherapy and cell therapy · transplant and graft-versus-leukemia ·
measurable residual disease · epigenetics and differentiation therapy · relapse/resistance/supportive
care · pediatric and AYA · trials/equity/pipeline/models.

**Reference layer — 10 of 14 lesion monographs unwritten:** TP53 · IDH1/IDH2 · DNMT3A/TET2/ASXL1 ·
splicing factors · RAS pathway and KIT · RUNX1/CEBPA/GATA2 · germline predisposition · cytogenetics ·
clonal hematopoiesis · APL/PML-RARA.

**All 15 drug monographs unwritten.** **All 8 foundational primers unwritten** — including the
glossary and the plain-language patient guide. **The cure-roadmap synthesis is unwritten.**

**Zero audits and zero expert reviews have run on anything.**

---

## 7. Why it stopped

The account hit its **weekly usage limit** (resets 18:00 UTC). Of 64 agents launched across two
workflows, **57 were killed** — including every one of the 15 citation auditors, all three
completeness critics, and the synthesis agent. This was a quota exhaustion, not a failure of the
work.

Both workflow scripts are saved and **resumable**, which replays completed agents from cache and
re-runs only what failed:

```
Workflow({scriptPath: ".../aml-cure-literature-wf_72e12574-bd8.js",  resumeFromRunId: "wf_72e12574-bd8"})
Workflow({scriptPath: ".../aml-reference-layer-wf_8edcf078-a37.js",  resumeFromRunId: "wf_8edcf078-a37"})
```
Full paths are in the session transcript; scripts live under
`~/.claude/projects/.../workflows/scripts/`. **Caveat:** resume is same-session only. From a new
session, re-run the scripts fresh rather than resuming.

---

## 8. Recommended next steps

**Audit before breadth.** The corpus's weakest claim is not that it is incomplete — it is that
nothing in it has been checked for accuracy. Ten more unaudited files makes that worse, not better.

1. **Run the audit pass over the existing nine files.** Highest value per token available.
2. **Write the synthesis** from those nine, so the campaign has an argument, not just an archive.
3. **Then** resume breadth — prioritising TP53, immunotherapy, MRD, and transplant, which carry the
   heaviest barrier weight in §5.2.
4. **Foundational primers early**, especially the glossary — every other file assumes it.
5. **Seek one named expert reviewer per domain** (workstream W3). This is the gap no amount of
   compute closes.

---

## 9. Standing risks

- **Optimism drift.** Evidence bases about diseases accumulate hopeful framing and shed negative
  results. §5.4 exists to resist this; keep it populated.
- **Unverified content reading as settled** because it is well-formatted and confident. The front-page
  status table is the countermeasure; keep it accurate as files are added.
- **Staleness.** Menin-inhibitor approvals moved twice in 13 months. Anything here from the last
  ~12 months should be re-confirmed against primary sources before use.
- **The checker verifies existence, not accuracy.** Do not let a green CI badge be mistaken for
  a validated corpus.
