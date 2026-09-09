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

## Review layer — `literature/`

_Populated on publication of the review layer._

| File | Refs checked | Removed | Verdict | Open concerns |
| --- | --- | --- | --- | --- |

## Reference layer — `reference/`

_Populated on publication of the reference layer._

| File | Refs checked | Removed | Verdict | Open concerns |
| --- | --- | --- | --- | --- |

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
