# The Campaign

## The premise

Between 2017 and 2026, AML gained more newly approved drugs than in the preceding forty years.
Over the same period, five-year survival for the median AML patient — a person in their late
sixties — improved far less than that approval count suggests it should have.

That gap is the campaign's entire subject. It implies the field's bottleneck is **not** primarily a
shortage of active agents. Something else is limiting cure: which cells survive therapy, how
heterogeneous and evolvable the disease is, how little of the population can tolerate the therapies
that do cure, how late we detect the failure, and who can actually reach modern care.

## Goal

Produce, maintain, and openly publish the clearest available answer to *what stands between current
AML care and cure*, at a level of specificity that can be turned into grant aims, trial hypotheses,
and funding decisions — and keep it honest, including where it is weak.

This repository does not cure AML. It is upstream of that: an attempt to make the target legible so
that people with laboratories, clinics, patients, and money can aim better.

## Workstreams

### W1 — Evidence base (active)
Maintain the 15-domain literature corpus. Keep it current, keep it audited, keep negative results in it.
- **Definition of done, ongoing:** every domain file reviewed within the last 6 months; every audit
  finding either resolved or logged as open.

### W2 — Barrier decomposition (active)
Convert the synthesis document's root barriers into precisely stated problems. For each barrier:
what is known, what the decisive experiment would be, what would count as success, and what it
would cost. A barrier that cannot be written this way is not yet understood well enough.

### W3 — Expert review (open — help wanted)
The corpus has been citation-audited but not peer reviewed. This is its single largest weakness.
The goal is named domain experts reviewing individual files and disagreeing in public, on the record.

### W4 — Trial and endpoint reform (open)
Track and argue the case on the measurement problem: event-free survival definitions, measurable
residual disease as a regulatory endpoint, the accelerated-approval confirmatory record in AML,
and platform/master-protocol designs. If we cannot measure cure early, we cannot iterate toward it.

### W5 — Access and equity (open)
Modern AML care is unevenly reachable — by age, geography, insurance, race, and income, and radically
so between high-income and low- and middle-income countries. A cure that reaches 15% of the people who
need it has not solved the problem. Track the gap; make it costly to ignore.

### W6 — Patient and caregiver voice (open)
AML is an emergency at diagnosis. Decisions get made in days, often by frightened people with poor
information. What patients and caregivers actually need to know, and what the literature does and does
not answer for them, belongs in this record.

## Milestones

| # | Milestone | Status |
| --- | --- | --- |
| M1 | 15-domain corpus written and independently citation-audited | done |
| M2 | Cross-domain synthesis and barrier list published | done |
| M3 | Audit outcomes and open concerns logged transparently | done |
| M4 | Each root barrier written as a decisive-experiment specification | open |
| M5 | ≥1 named external expert review per domain file | open |
| M6 | Public, maintained index of active AML trials mapped to barriers | open |
| M7 | Access/equity gap quantified with sources, per region | open |

## How this can fail

Stated up front, so it can be watched for:

1. **Optimism drift.** Evidence bases about diseases tend to accumulate hopeful framing and shed
   negative results. The evidence rules exist specifically to resist this. Enforce them.
2. **Staleness masquerading as authority.** A confident, well-formatted, two-year-old document is more
   dangerous than an obviously incomplete one.
3. **Unverified AI-generated content treated as settled.** See [METHODOLOGY.md](../METHODOLOGY.md). Until W3
   lands, treat every specific number as needing confirmation before it is relied on.
4. **Breadth without decision value.** If a file grows without making any research choice clearer,
   it is decoration. Cut it.
