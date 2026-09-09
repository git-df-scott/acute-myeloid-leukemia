# Working in this repository

This is an evidence base about acute myeloid leukemia, aimed at making the barriers to *cure*
legible. Read [METHODOLOGY.md](METHODOLOGY.md) before contributing content.

## The one rule that matters most

**Never write a citation you have not actually retrieved.** No invented PMIDs, DOIs, NCT numbers,
authors, journals, years, approval dates, doses, or efficacy figures. A plausible fabricated
reference is the worst possible failure here, because unlike an omission it is invisible and it
propagates. If you cannot retrieve a source, either leave the claim out or mark it `[unverified]`.

`[unverified]` is a fully acceptable outcome. Fabrication is not.

## Content rules

1. Search before writing. Use web search extensively; prefer primary sources (trial publications,
   guideline documents, regulatory records, ClinicalTrials.gov) over news coverage. Cite secondary
   coverage *as* secondary coverage — never upgrade a press release into a trial result.
2. Numbers carry context: trial name, cohort, N, endpoint definition. "ORR 63%" alone is not acceptable.
3. State the evidence tier explicitly: approved / phase 3 positive / phase 1–2 signal / preclinical / hypothesis.
4. Record negative, failed, and discontinued programs with the same prominence as successes. An
   evidence base that only remembers wins actively misdirects research.
5. Frequencies name their population (adult vs pediatric, de novo vs secondary) and cohort.
6. Say when the evidence trail goes cold rather than implying completeness.
7. Nothing in this repository is medical advice, and no file may read as a treatment recommendation.
   `reference/patient-and-caregiver-guide.md` in particular must stay non-directive.

## Before committing content

```bash
python3 tools/check_references.py literature reference          # structural, fast
python3 tools/check_references.py literature reference --online # resolves every identifier
```

The `--online` pass is the fabrication check. Run it on any file you added or edited. See
[tools/README.md](tools/README.md).

Log audit outcomes and post-publication corrections in
[campaign/AUDIT-LOG.md](campaign/AUDIT-LOG.md), including concerns you could **not** resolve.
Publishing unresolved concerns is deliberate.

## Layers

- `literature/` — the **review layer**: argued synthesis per research domain.
- `reference/` — the **reference layer**: per-lesion and per-agent look-up monographs, plus primers.
- `campaign/` — goals, workstreams, contribution rules, audit log.
- `tools/` — mechanical enforcement of the rules above.

Cross-link between layers with relative paths. Reference-layer files state facts; review-layer
files make arguments. Keep that distinction — it is what makes either usable.

## Tone

Direct about uncertainty. "The evidence does not establish this" is a complete sentence and a
welcome one. Confidence that outruns the evidence is the specific failure this project exists to
resist, and it creeps in through optimistic framing far more often than through outright error.
