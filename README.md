# The AML Cure Campaign

An open, citation-disciplined evidence base and research agenda aimed at one question:

> **Why is acute myeloid leukemia still not curable for most people who get it — and what would it actually take to change that?**

AML is the most common acute leukemia in adults. Despite roughly a dozen new drug
approvals since 2017, the majority of patients — especially those over 60 — still die of
the disease. Remissions have improved substantially. **Cures have not improved nearly as
much.** This repository exists to hold that distinction steady and work the gap.

## What this repository is

| Part | Purpose |
| --- | --- |
| [`literature/`](literature/) | A structured, per-domain review of the AML literature. Every file is independently citation-audited. |
| [`literature/00-synthesis-and-cure-roadmap.md`](literature/00-synthesis-and-cure-roadmap.md) | Cross-domain synthesis: where we are, the root barriers to cure, and ranked research directions. |
| [`campaign/`](campaign/) | The campaign itself: goals, workstreams, how to contribute, and how progress is measured. |
| [`METHODOLOGY.md`](METHODOLOGY.md) | How the corpus was built, what its evidence standards are, and what it cannot establish. |

## What this repository is not

- **Not medical advice.** Nothing here should be used to make a treatment decision. See [DISCLAIMER.md](DISCLAIMER.md).
- **Not a systematic review.** It is a broad, structured, source-verified sweep. It has not been
  through PRISMA-style protocol registration, dual independent screening, or expert peer review.
  See [METHODOLOGY.md](METHODOLOGY.md) for exactly what that means for how much weight to put on it.
- **Not finished.** It is a starting position, deliberately written to be argued with.

## Start here

1. Read [`literature/00-synthesis-and-cure-roadmap.md`](literature/00-synthesis-and-cure-roadmap.md) — the whole argument in one file.
2. Then the domain file closest to your expertise, and try to break it. Corrections are the most valuable contribution here.
3. Then [`campaign/CONTRIBUTING.md`](campaign/CONTRIBUTING.md).

## Evidence rules (non-negotiable)

Every claim in this repository must be traceable to a real, retrievable source. Specifically:

- No citation may be included unless it was actually retrieved. No invented PMIDs, DOIs, NCT numbers, or author lists.
- Efficacy numbers carry their trial, cohort, N, and endpoint definition — or they do not go in.
- **Negative and failed trials are recorded with the same prominence as successes.** An evidence base that
  only remembers wins is worse than useless for planning research; it actively misdirects it.
- Evidence tiers are stated explicitly: approved / phase 3 positive / phase 1–2 signal / preclinical / hypothesis.
- Anything not fully verifiable is marked `[unverified]` rather than quietly asserted.

If you find a violation of any of these, that is a bug. Please [open an issue](../../issues/new).
