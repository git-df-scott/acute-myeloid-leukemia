# Methodology

## How the corpus was built

The literature base in [`literature/`](literature/) was assembled in a structured, multi-stage
process rather than as a single pass of writing.

**1. Domain decomposition.** The AML field was partitioned into 15 domains chosen to be
jointly exhaustive rather than merely convenient — covering epidemiology and classification,
disease biology, each major therapeutic modality, transplant, measurable residual disease,
pediatric disease, and the non-bench factors (trial design, equity, access, models, pipeline)
that decide whether a scientific advance reaches a patient.

**2. Independent research per domain.** Each domain was researched independently by a separate
agent with web search and page-retrieval access, working from an explicit scope statement and a
fixed set of evidence rules (below). Independence is deliberate: it produces overlap at the
domain boundaries, and overlap is where contradictions become visible.

**3. Adversarial citation audit.** Every domain file was then handed to a *separate* auditor whose
only job was to break it — verify each reference actually exists and says what was claimed, check
every efficacy figure and approval date against a retrieved source, delete unverifiable citations,
and demote anything where a phase 1–2 signal or press release had been dressed up as phase 3 or
approved. The audit outcome for each file is recorded in [`campaign/AUDIT-LOG.md`](campaign/AUDIT-LOG.md).

**4. Completeness criticism.** Three critics then read across the whole corpus with distinct lenses —
basic/translational science, clinical evidence, and frontier-plus-access — tasked with finding what
was *absent*. Gaps they could close with verified sources were appended to the relevant files;
gaps they could not close are recorded as open.

**5. Synthesis.** Only then was the cross-domain roadmap written, from the audited corpus.

## Evidence rules applied at every stage

1. No citation is included unless it was actually retrieved. Invented identifiers are treated as the
   worst possible failure mode — worse than an omission, because an omission is visible and a
   plausible fake reference is not.
2. Primary sources (pivotal trial publications, guideline documents, regulatory records,
   ClinicalTrials.gov entries) are preferred. Where only secondary coverage was available, it is cited
   *as* secondary coverage rather than upgraded.
3. Numbers travel with their context: trial name, cohort, N, and endpoint definition.
4. Negative, failed, and discontinued programs are recorded with equal prominence.
5. Evidence tier is stated explicitly: approved / phase 3 positive / phase 1–2 signal / preclinical / hypothesis.
6. Unverifiable-but-substantive claims are marked `[unverified]` inline rather than deleted or asserted.
7. Where the evidence trail goes cold, the file says so instead of implying completeness.

## What this methodology cannot establish — read this part

Being candid about the ceiling here matters more than the process description above.

- **This is not a systematic review.** There is no registered protocol, no PRISMA flow diagram, no
  dual independent screening of a defined search yield, and no formal risk-of-bias assessment. Do not
  cite it as one.
- **Search coverage is web-mediated and therefore uneven.** Open-access and heavily-covered literature
  is over-represented. Paywalled primary papers, non-English literature, and conference material that
  never reached indexed publication are under-represented. Negative results are systematically
  under-published in the source literature itself — the audit stage can enforce honesty about what was
  found, but it cannot recover trials nobody wrote up.
- **Citation auditing verifies existence and characterization, not scientific validity.** A verified
  citation to a badly-designed trial is still a verified citation. Assessing trial quality is expert work
  and has not been done here.
- **Recency is a weak point.** Very recent conference data may be captured only through secondary
  reporting, which is where numbers most often drift. Anything from the last ~12 months should be
  confirmed against the primary abstract or publication before use.
- **AI assistance is pervasive.** This corpus was produced by AI agents under the rules above. The
  audit stage substantially reduces fabrication risk; it does not eliminate it. Before any of this is
  used for grant writing, trial design, or clinical planning, a domain expert must verify the specific
  claims being relied on.

## Reproducing or extending it

The domain decomposition, per-domain scope statements, and the exact evidence rules are all in the
workflow script that generated the corpus. To extend: add a domain, run the same research → audit →
gap-critique → synthesis sequence, and log the audit outcome. Corrections to existing files should
come with the retrieved source that motivates them.
