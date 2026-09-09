# NPM1 mutation

> Reference monograph. Evidence current to **9 September 2026**; points where the evidence
> trail goes cold are flagged. Every number carries its cohort and endpoint. Evidence tiers
> stated inline: **[approved]**, **[phase 3 positive]**, **[phase 1-2 signal]**,
> **[preclinical]**, **[hypothesis]**. Not medical advice — see `../../DISCLAIMER.md`.

**At a glance**

| Field | Value |
|---|---|
| Gene / lesion | *NPM1* (nucleophosmin 1), HGNC:7910, 5q35.1, RefSeq NM_002520, UniProt P06748 [1]. Somatic frameshift insertion/duplication, almost always exon 12; canonical p.Trp288fs [2,3] |
| Frequency (adult AML) | Cytoplasmic NPM by IHC in **208/591 (35.2%)** primary adult AML; **0/135** secondary AML, **0/980** non-AML neoplasms [2]. **53% of 872** cytogenetically normal AML aged <60 y [4]. Reviews: 30–35% of adult AML, 40–50%+ of normal-karyotype AML [3,5,6] |
| Frequency (pediatric AML) | **7.6% of 869** children (TARGET), rising with age [7]; review estimate ~5% [6] |
| ELN 2022 risk | **Favorable** without *FLT3*-ITD; **Intermediate** with *FLT3*-ITD (allelic ratio no longer used); **Adverse** with adverse-risk cytogenetics [8] |
| WHO 2022 / ICC 2022 entity | Distinct entity in both. WHO 5th ed. "AML with *NPM1* mutation" — **no blast threshold** [9]. ICC 2022 "AML with mutated *NPM1*" — **≥10% blasts**; <10% is *NPM1*-mutated MDS [10,11] |
| Actionable targeted therapy | **Yes.** Two menin inhibitors FDA-approved for R/R *NPM1*-mutant AML: **revumenib** (24 Oct 2025) [12] and **ziftomenib** (13 Nov 2025) [13] **[approved]**. No randomized phase 3 readout for either as of 9 Sep 2026 |
| MRD suitability | **Excellent** — reference-standard molecular MRD target by RT-qPCR; mutation retained at relapse in **69/70** patients [16]; endorsed by ELN MRD guidance [17] |
| Germline relevance | **None established.** Exon-12 *NPM1* mutations are somatic and AML-restricted [2]; *NPM1* is not a germline predisposition entity in WHO 2022 or ICC 2022 [9,10]. Isolated germline submissions exist in ClinVar [18] — **[unverified]** as a predisposition syndrome |

---

## Biology

NPM1 is the most abundant nucleolar protein: a pentameric nucleocytoplasmic shuttling
chaperone whose functions span nucleolar formation by liquid–liquid phase separation,
ribosome biogenesis and export, histone chaperoning, centrosome duplication, DNA repair,
nucleolar stress response, and sequestration of the tumour suppressor ARF to protect it from
degradation [1,5].

Architecture determines the disease. The hydrophobic N-terminus carries two leucine-rich
nuclear export signals (NES); the basic C-terminus carries tryptophans **W288 and W290**,
which fold a three-helix bundle constituting the nucleolar localisation signal (NoLS) [5].
Exon-12 frameshifts delete W288 and W290 (or W290 alone), unfolding that bundle and
destroying the NoLS while creating a **new leucine-rich NES** in the altered tail [5]. The
result is XPO1/CRM1-dependent export and **aberrant cytoplasmic accumulation of both mutant
and wild-type NPM1** — the defining lesion, and the basis of the original
immunohistochemical discovery [2].

Mislocalisation is required continuously, not merely initiating. Relocalising NPM1c to the
nucleus or degrading it causes **immediate HOX gene downregulation followed by
differentiation**; XPO1 inhibition relocalises NPM1c and prolongs survival of *Npm1*-mutant
leukemic mice **[preclinical]** [19]. Mechanistically, NPM1c **directly binds chromatin** at
targets co-occupied by the histone methyltransferase KMT2A (MLL1), and its degradation strips
RNA polymerase II and activating histone marks from those sites [20]. A 2026 synthesis frames
this as mutant NPM1 organising **phase-separated nuclear transcriptional condensates** that
concentrate regulators at active chromatin to sustain the pathogenic HOX/MEIS1 program [21] —
the explanation for menin-KMT2A inhibitor activity in a leukemia carrying no *KMT2A*
rearrangement. The downstream signature (high *HOXA*/*HOXB* with cofactors **MEIS1** and
**PBX3**, plus stem-cell maintenance genes) is the dependency menin inhibition attacks
[3,20,21]. In *Npm1c/Dnmt3a* knock-in mice the menin-MLL1 inhibitor VTP-50469 **reversed
preleukemic progenitor self-renewal** and prevented AML, raising a clinically untested
prospect of preventive epigenetic therapy **[preclinical]** [22].

Clonal ordering matters for interpretation: *NPM1* mutations are typically **late** events. In
120 *NPM1*-mutated cases *NPM1* was never the sole mutation and had median VAF **16.8%**,
below co-mutated DNA-methylation, splicing and cohesin genes at **≥40%** [23].

Rare **NPM1 rearrangements** (*NPM1::MLF1*, ~0.2–0.5% of AML; also *CCDC28A*, *HAUS1*, *RARA*)
converge on the same mechanism, and *NPM1::CCDC28A* cells were menin-inhibitor sensitive
**[preclinical]** [6].

### Mutation types

All variants converge on the same C-terminal consequence, which is why they behave as one
entity. Frequencies are from **660 newly diagnosed intermediate-risk adults** [24]:

| Type | Nucleotide change | Frequency (n=660) |
|---|---|---|
| **A** | c.860_863dup (ClinVar VCV000013998; also written c.863_864insTCTG / 956_959dupTCTG), p.Trp288fs [18] | **458 (69%)** |
| **B** | c.863_864insCATG, p.Trp288fs | **72 (11%)** |
| **D** | c.863_864insCCTG, p.Trp288fs | **51 (8%)** |
| Other | many rarer variants [25,26] | **79 (12%)** |

Subtype is not biologically inert. In that cohort *DNMT3A* co-mutation was more frequent in
type A (**59%**) than B (**31%**) or D (**37%**); *WT1* was less frequent in type A (**4%** vs
**17%** in B); *IDH2*-R140 was enriched in D (**26%** vs **10%** in B). OS for type A versus
rarer types was 44 vs 63 months (**P = 0.052**, not significant) [24].

Rarer classes matter for assay design: **non-A/B/D exon-12 subtypes** [25] and **novel exon-5
mutations** producing the same *NPM1*-mutant expression signature outside the canonical
hotspot [26]. Assays restricted to the exon-12 hotspot will miss these.

## Epidemiology and co-mutation landscape

The lesion is **AML-specific**: cytoplasmic NPM was absent from 135 secondary AMLs and 980
other neoplasms in the original series [2]. Adult frequency is ~30–35% of AML and 40–50%+ of
normal-karyotype AML [3,5,6], with **53% of 872** cytogenetically normal patients aged <60 y
[4]. Pediatric frequency is far lower: **7.6% of 869** children, increasing with age [7].

Co-mutations, cohorts named:

- **FLT3-ITD** — **41%** of 660 *NPM1*-mutated adults [24]; ~40% in review synthesis [3].
- **DNMT3A** — **43%** of 107 therapy-related and **48%** of 88 de novo cases [27]; **59%** in
  type A [24].
- **TET2** — **40%** (therapy-related) and **30%** (de novo) in the same paired series [27].
- **IDH1/IDH2** — ~25% in review synthesis [3]. *NPM1* and **IDH2-R172 are mutually
  exclusive** (0 co-occurrences in 120 cases) [23].
- **NRAS ~20%**; signalling mutations (*FLT3*, *NRAS*, *PTPN11*) sit at low VAF **7.0–11.9%**,
  i.e. as subclones [3,23].
- **Cohesin complex** (*STAG2*, *RAD21*, *SMC1A*, *SMC3*) — nearly all *NPM1*-mutated cases
  carry a DNA-methylation, splicing **or cohesin** co-mutation at higher VAF than *NPM1*
  itself [23]. In **1,615** intensively treated AML patients, mutated *RAD21* associated with
  normal karyotype and with *NPM1*, *EZH2*, *KRAS*, *CBL*, whereas *STAG2* associated with
  *IDH2*, *RUNX1*, *BCOR*, *ASXL1*, *SRSF2*. Cohesin subunit alterations were **almost
  completely mutually exclusive**, and none of the four had an independent effect on CR, EFS,
  RFS or OS in that cohort [28].
- **Myelodysplasia-related (MR) genes** — **655/4,363 (15.0%)** of pooled *NPM1*-mutated
  patients [29].

**Therapy-related *NPM1*-mutated AML behaves like de novo disease.** Normal karyotype in
**78/96 (88%)** of t-*NPM1* AML versus **103/390 (28%)** of *NPM1*-wild-type t-AML; *TP53* and
*PPM1D* were wild-type in **97%** and **96%** of t-*NPM1* cases. 3-year OS was **54%**
(t-*NPM1*, n=96), **60%** (de novo *NPM1*, n=2,394) and **31%** (t-AML, n=390), with no
multivariable OS difference between the *NPM1*-mutated groups (HR 0.9, 95% CI 0.65–1.25,
P=.45) [27].

## Prognostic significance

**Alone it is favorable.** In 872 CN-AML patients <60 y, *NPM1*-mutated **without** *FLT3*-ITD
carried HR **0.44** (95% CI 0.32–0.61) for relapse or death in CR; transplant benefit was
confined to adverse genotypes [4].

**ELN across revisions:**

| | *NPM1*-mut, no *FLT3*-ITD | *NPM1*-mut + *FLT3*-ITD | + adverse cytogenetics |
|---|---|---|---|
| **ELN 2017** [30] | Favorable | ITD^low **Favorable**; ITD^high **Intermediate** | not specified as adverse |
| **ELN 2022** [8] | Favorable | **Intermediate**, irrespective of allelic ratio | **Adverse** |

ELN 2022 dropped the allelic ratio because of assay standardisation problems, the modifying
effect of midostaurin, and the growing role of MRD [8]. Real-world impact: in **546**
intensively treated PETHEMA patients, **20 (3.7%)** moved favorable → intermediate (all
*NPM1*-mut with low-ratio *FLT3*-ITD). 2-year OS was **75.1%** for
*NPM1*-mut/*FLT3*-ITD-negative versus **47.9%** for *FLT3*-ITD-positive [31].

**A co-mutation classifier now outperforms ELN 2022 for this genotype.** The HARMONY Alliance
classification, built on *FLT3*-ITD, *DNMT3A*, *IDH1/IDH2* and *TET2* combinations (training
n=1,001 trial patients; internal validation n=762 real-world; external validation n=585
UK-NCRI), split *NPM1*-mutated AML into **51.8% favorable (median OS 14.4 years)**, **24.8%
intermediate (2.2 years)** and **23.4% adverse (0.9 years)** — reclassifying **42.7%** of
patients out of their ELN 2022 category, with allo-HSCT in CR1 benefiting the adverse
subgroup most [32]. Retrospective and registry-based; **not yet in any guideline**.

**DNMT3A**, often called adverse, needs care. In 164 *NPM1*-mutated CETLAM patients *DNMT3A*
status did **not** alter OS (P=.2) and the *FLT3*-ITD gradient held regardless. What it did do
was **delay MRD clearance** — all *DNMT3A*-mutated patients were MRD-positive after first
consolidation (P<.001), with a trend to more molecular relapse (P=.054) — plausibly offset by
MRD-driven pre-emptive intervention [33].

**MR gene co-mutations are an unresolved conflict.** A meta-analysis of **4,363**
*NPM1*-mutated patients (10 cohorts, 9 studies) found MR mutations associated with inferior
OS (pooled HR **1.30**, 95% CI 1.11–1.51, P<0.001), shorter EFS (HR **1.43**, 95% CI
1.11–1.85) and lower CR (RR **0.94**, 95% CI 0.90–0.99), including within ELN-2022
favorable-risk patients [29]. A separate 221-patient favorable-risk cohort found **no** OS/LFS
effect for a single MR mutation, with worse LFS only at **≥2** [34]. Not reconciled as of
9 Sep 2026.

**Pediatric prognosis diverges from adult.** In 869 children *NPM1* mutation independently
predicted better EFS (P=0.004) and OS (P=0.012), and this **persisted with *FLT3*-ITD**; SCT
had no significant survival effect in the double-mutant group [7]. Retrospective TARGET
analysis that contradicts adult practice — treat with caution.

## Diagnostic testing and MRD

**Detection.** Molecular testing (NGS or PCR) of *NPM1* exon 12 is standard; immunohistochemistry
for cytoplasmic NPM is a validated surrogate that also flags variants outside the sequenced
region [2]. Hotspot-only assays miss non-A/B/D and non-exon-12 variants [25,26].

**Classification threshold — the one place WHO and ICC disagree.** WHO 5th edition diagnoses
"AML with *NPM1* mutation" **irrespective of blast count** (only AML with *BCR::ABL1* and AML
with *CEBPA* mutation retain the 20% requirement) [9]. ICC 2022 requires **≥10% blasts**;
below 10% the case is *NPM1*-mutated **MDS** [10,11]. Empirical support for the WHO position:
among **54** patients with *NPM1*-mutated myeloid neoplasms and <20% marrow blasts, median OS
did **not** differ across blast strata (<10% / 10–19% / ≥20%: 32.2 months / not reached /
46.9 months, **P=0.700**); intensive chemotherapy gave higher CR than low-intensity therapy
(**75% vs 27%**, P=.006); and **23/54 (43%)** progressed to ≥20% blasts [35]. N is small; the
entity question remains live.

**MRD by qPCR is the strongest single prognostic tool in this genotype** — quantifiable to
~10⁻⁵, leukemia-specific rather than a clonal-hematopoiesis marker, and retained at relapse
[16]. In **346** *NPM1*-mutated AML17 patients (**2,569** samples), persistent *NPM1*
transcripts in **blood** after cycle 2 were present in **15%** and predicted 3-year relapse
**82% vs 30%** (HR 4.80, 95% CI 2.95–7.80, P<0.001) and 3-year survival **24% vs 75%**
(HR 4.38, 95% CI 2.57–7.47, P<0.001); MRD was the only independent prognostic factor for
death, and *NPM1* mutations were detected in **69/70** patients at relapse [16]. The **2025
ELN-DAVID update** adds qualitative response categories (optimal / warning / high risk of
treatment failure) [17].

**MRD, not *FLT3*-ITD, should drive the transplant decision.** In **737** patients achieving
remission on UK NCRI AML17/AML19, peripheral-blood *NPM1* MRD after two inductions was
positive in **19%**. CR1 allografting improved OS **only** in MRD-positive patients (3-year OS
**61% vs 24%**; HR 0.39, 95% CI 0.24–0.64, P<0.001) and gave **no** benefit if MRD-negative
(**79% vs 82%**; HR 0.82, 95% CI 0.50–1.33, P=.4). Restricted to *FLT3*-ITD co-mutated
patients the pattern held (MRD+: 45% vs 18%; MRD−: 83% vs 76%), with **no interaction with
*FLT3* allelic ratio** [36].

MRD retains power under **non-intensive** therapy: in **76** previously untreated
*NPM1*-mutated patients achieving CR/CRi on venetoclax + HMA or LDAC, **58%** reached bone
marrow MRD-negativity; MRD-negative by end of cycle 4 gave 2-year OS **84% vs 46%**; and 22
patients electively stopping therapy in MRD-negative remission had 2-year treatment-free
remission of **88%** [37].

## Therapeutic implications

**Intensive chemotherapy [phase 3 positive, historical].** *NPM1*-mutated/*FLT3*-ITD-negative
AML responds well to standard induction [2,4]. Transplant in CR1 is **not** indicated for
MRD-negative patients, including those with *FLT3*-ITD [36].

**Venetoclax + azacitidine [phase 3 positive, not *NPM1*-specific].** VIALE-A randomised
**431** induction-ineligible patients: composite CR **66.4% vs 28.3%** and median OS **14.7 vs
9.6 months** versus azacitidine alone (HR 0.66, 95% CI 0.52–0.85, P<0.001) [38]. The trial was
not powered for a definitive *NPM1* subgroup effect size.

**Menin inhibitors — two approvals, both relapsed/refractory [approved].**

| | **Revumenib** (Revuforj, Syndax) | **Ziftomenib** (Komzifti, Kura/Kyowa Kirin) |
|---|---|---|
| FDA approval | **24 Oct 2025** [12] | **13 Nov 2025** [13] |
| Indication | R/R AML with susceptible *NPM1* mutation, adults **and pediatric ≥1 year**, no satisfactory alternative | R/R AML with susceptible *NPM1* mutation, **adults**, no satisfactory alternative |
| Trial | AUGMENT-101, NCT04065399 [12,15] | KO-MEN-001 / KOMET-001, NCT04067336 [13] |
| Efficacy population | **n=65** [14] | **n=112** [13] |
| **CR + CRh** | **23.1%** (95% CI 13.5–35.2) [12,14] | **21.4%** (95% CI 14.2–30.2) [13] |
| Median duration CR+CRh | **4.5 months** (95% CI 1.2–8.1) [12,14] | **5.0 months** (95% CI 1.9–8.1) [13] |
| Dose | 270 mg BID if ≥40 kg (160 mg BID with strong CYP3A4 inhibitor); 160 mg/m² BID if <40 kg [14] | **600 mg** once daily [13] |
| **Boxed warning** | **Differentiation syndrome** (can be fatal) **and QTc prolongation / torsades de pointes** [14] | **Differentiation syndrome** (fatal or life-threatening) [13] |
| Differentiation syndrome | **60/241 (25%)** across R/R acute leukemia; **18%** in *NPM1*-mutated AML [14] | **29/112 (26%)**; grade 3 **13%**; **2 fatal** [13] |
| QTc | Adverse reaction in **86/241 (36%)**; grade 3 **15%**, grade 4 **2%** [14] | Warning; interrupt if QTc >500 ms [13] |

Both approvals rest on **single-arm** CR+CRh of roughly one in five with median response
durations under six months. **No randomized phase 3 result exists for either drug in
*NPM1*-mutated AML as of 9 September 2026.** Confirmatory phase 3 trials are recruiting:
**KOMET-017** (NCT07007312, planned n=1,300, ziftomenib + Ven/Aza or 7+3 in untreated
*NPM1*-m or *KMT2A*-r AML) and **NCT06652438** (planned n=448, revumenib + azacitidine +
venetoclax) [39].

**Menin-inhibitor combinations [phase 1-2 signal].**

- **Azacitidine + venetoclax + revumenib**, age ≥60, newly diagnosed *NPM1*-m or *KMT2A*-r,
  n=43 (NCT03013998): ORR **88.4%** (95% CI 74.9–96.1; *NPM1*-m 85.3%), composite CR
  **81.4%**, CR **67.4%** (*NPM1*-m 65%); no MTD; differentiation syndrome **19%**, QTcF
  prolongation **44%**, neither forcing permanent discontinuation; **all 37** MRD-evaluable
  patients MRD-negative by central flow [40].
- **Ziftomenib + venetoclax/azacitidine in R/R *NPM1*-m AML**, KOMET-007, n=67 (NCT05735184):
  at 600 mg, composite CR **46% (22/48)** — but **70% (16/23)** in venetoclax-naïve versus
  **24% (6/25)** in venetoclax-exposed patients; median duration of response **8.6 months**;
  grade 3 differentiation syndrome in 2 [41].
- Pooled across **14 studies / 784 treated R/R AML patients** (22 response-evaluable cohorts,
  n=579): ORR **54.6%** (95% CI 46.4–62.6), CR **29.3%**, CR+CRh **28.5%**; menin inhibitor +
  HMA + venetoclax gave higher CR than monotherapy (**43.3% vs 19.5%**, P=0.002);
  differentiation syndrome **14.6%**; treatment-related mortality **5.0%** [42].
- **Bleximenib** (JNJ-75276617) is active in *KMT2A*- and *NPM1*-altered models
  **[preclinical]** [43]; phase 1b combination data were presented at EHA 2025 —
  **congress/press material, cited as secondary, not a trial publication**.

**XPO1 inhibition** has a clean rationale (nuclear relocalisation of NPM1c → HOX collapse →
differentiation) but remains **[preclinical]**; no XPO1 inhibitor is approved for this
indication [19]. **Immunotherapy against the NPM1c neoepitope** (CAR-T, neoepitope CARs) is
**[preclinical]** only [3].

**Negative and terminated programs.** The SYK inhibitor **entospletinib** reached a
registrational phase 3 (**AGILITY**, NCT05020665) in newly diagnosed *NPM1*-mutated AML with
an MRD-negativity primary endpoint. It was **TERMINATED** after enrolling only **15**
patients; the sponsor-stated reason is "significant challenges associated with study
enrollment in a genetic subset of fit participants in the front-line [AML] setting and other
challenges associated with post-COVID impacts" — **feasibility, not a reported efficacy or
safety failure** [39]. No efficacy readout exists.

**Open randomized question in fit patients.** **VINCENT** (NCT05904106, phase 2
non-inferiority, n=146) randomises fit adults 18–70 with newly diagnosed
*NPM1*-mutated/*FLT3*-wild-type AML to venetoclax + azacitidine versus 7+3 + gemtuzumab
ozogamicin, primary endpoint modified EFS. **Recruiting; no results as of 9 Sep 2026** [44].

## Resistance and relapse

**Relapse with loss of the *NPM1* mutation is real but uncommon, and it limits MRD.** In
**104** paired diagnosis/relapse samples, **14 (13%)** relapsed with wild-type *NPM1*. Those
patients differed at diagnosis (median WBC **3 vs 30 ×10⁹/L**, P=.008; platelets **128 vs
66 ×10⁹/L**, P=.018), relapsed **later** (median **43 vs 14 months**, P=.004), more often
carried *DNMT3A* (P=.035) and less often *FLT3*-ITD (P=.029). Co-occurring mutations persisted
through molecular remission, implicating a **pre-existing clonal hematopoiesis** reservoir;
the authors argue *NPM1*-wild-type relapse is a distinct disease [45]. This sits in tension
with AML17, where *NPM1* was retained in **69/70** relapses [16] — different cohorts, assays
and follow-up. Practically: *NPM1* MRD negativity is highly reassuring but not absolutely so,
particularly for late events in *DNMT3A*-mutated patients.

**Menin-inhibitor resistance is target-site mutation.** Sequencing of four patients who
responded to revumenib then progressed found **MEN1 mutations in all four**, at residues
**M327, T349, G331 and S160**, disrupting inhibitor binding while preserving the menin–MLL1
interaction [46]. **Prior venetoclax exposure also blunts combinations**: composite CR **24%**
in venetoclax-exposed versus **70%** in venetoclax-naïve R/R patients on ziftomenib + Ven/Aza
[41]. Low-VAF signalling subclones (*FLT3*, *NRAS*, *PTPN11*) present at diagnosis are a
plausible additional escape route [23] **[hypothesis]**.

**Pre-emptive treatment of molecular relapse looks better than salvage, but is not
randomized.** In **303** CBF or *NPM1*-mutated patients monitored after first-line intensive
therapy, **31%** had molecular relapse; pre-emptive therapy gave 3-year OS **78%** versus
**51%** for salvage after progression to morphologic relapse (P=0.01) — allocation was
non-random [47]. Venetoclax-based therapy for molecular failure produced ≥1-log MRD reduction
in **66/79 (84%)** and MRD negativity in **56/79 (71%)** in a retrospective international
cohort, with lower response when *FLT3*-ITD was present (**64% vs 91%**, P<.01) [48].

## Open questions

1. **No randomized evidence supports either approved menin inhibitor** — both rest on
   single-arm CR+CRh of 21–23% with median response duration 4.5–5.0 months [12,13,14].
   KOMET-017 and NCT06652438 are the tests [39].
2. **Do MR gene co-mutations override ELN 2022 favorable status?** A 4,363-patient
   meta-analysis says yes (OS HR 1.30) [29]; a 221-patient cohort says only at ≥2 [34].
3. **Does the HARMONY co-mutation classifier belong in guidelines?** It reclassifies 42.7% of
   patients and separates median OS of 14.4 vs 2.2 vs 0.9 years, but is retrospective [32].
4. **WHO vs ICC blast threshold.** No threshold [9] versus ≥10% [10] makes the same cytopenic
   patient AML in one system and MDS in the other; the supporting outcome data are from **54**
   patients [35].
5. **Frontline choice in fit patients** — intensive chemotherapy versus venetoclax/azacitidine
   is genuinely open pending VINCENT [44].
6. **Can menin inhibition move earlier** — frontline, MRD-preemptive, or preventive in
   *NPM1*-mutant clonal hematopoiesis? The prevention concept is **[preclinical]** [22].
7. **Optimal MRD thresholds and timepoints for pre-emptive therapy**, given that the
   supporting comparison is non-randomized [47,48].
8. **Pediatric management conflicts with adult practice** — whether *NPM1*+*FLT3*-ITD children
   truly need no transplant rests on retrospective TARGET data [7].
9. **True frequency of *NPM1*-loss relapse** (13% [45] vs ~1% [16]) and how to monitor those
   patients.
10. **Are rare non-exon-12 variants and *NPM1* rearrangements menin-inhibitor sensitive?**
    Mechanistically plausible and preclinically supported [6,26], clinically untested — and
    both labels say "**susceptible** *NPM1* mutation" without enumerating variants [12,13].

---

## References

All entries were retrieved during preparation. PMIDs and DOIs were verified against NCBI
E-utilities; NCT records against the ClinicalTrials.gov API; approval records against FDA.gov.

1. HGNC:7910 *NPM1* (nucleophosmin 1), 5q35.1, NM_002520, UniProt P06748. https://rest.genenames.org/fetch/symbol/NPM1 · NCBI Gene 4869. https://www.ncbi.nlm.nih.gov/gene/4869
2. Falini B, Mecucci C, Tiacci E, et al. Cytoplasmic nucleophosmin in acute myelogenous leukemia with a normal karyotype. *N Engl J Med.* 2005;352(3):254-66. PMID 15659725. doi:10.1056/NEJMoa041974
3. Falini B, Brunetti L, Sportoletti P, Martelli MP. NPM1-mutated acute myeloid leukemia: New pathogenetic and therapeutic insights and open questions. *Am J Hematol.* 2023;98(9):1452-1464. PMID 37317978. doi:10.1002/ajh.26989
4. Schlenk RF, Döhner K, Krauter J, et al. Mutations and treatment outcome in cytogenetically normal acute myeloid leukemia. *N Engl J Med.* 2008;358(18):1909-18. PMID 18450602. doi:10.1056/NEJMoa074306
5. Falini B, Sportoletti P, Martelli MP, Brunetti L. Functions of the native NPM1 protein and its leukemic mutant. *Leukemia.* 2025;39(2):276-290. PMID 39690184. doi:10.1038/s41375-024-02476-4
6. Shimosato Y, Goyama S. NPM1-rearranged AML: clinical features, molecular pathogenesis, and therapeutic perspectives. *Int J Hematol.* 2026;124(3):303-310. PMID 42247117. doi:10.1007/s12185-026-04234-x
7. Xu LH, Fang JP, Liu YC, et al. Nucleophosmin mutations confer an independent favorable prognostic impact in 869 pediatric patients with acute myeloid leukemia. *Blood Cancer J.* 2020;10(1):1. PMID 31915364. doi:10.1038/s41408-019-0268-7
8. Döhner H, Wei AH, Appelbaum FR, et al. Diagnosis and management of AML in adults: 2022 recommendations from an international expert panel on behalf of the ELN. *Blood.* 2022;140(12):1345-1377. PMID 35797463. doi:10.1182/blood.2022016867
9. Khoury JD, Solary E, Abla O, et al. The 5th edition of the World Health Organization Classification of Haematolymphoid Tumours: Myeloid and Histiocytic/Dendritic Neoplasms. *Leukemia.* 2022;36(7):1703-1719. PMID 35732831. doi:10.1038/s41375-022-01613-1
10. Arber DA, Orazi A, Hasserjian RP, et al. International Consensus Classification of Myeloid Neoplasms and Acute Leukemias: integrating morphologic, clinical, and genomic data. *Blood.* 2022;140(11):1200-1228. PMID 35767897. doi:10.1182/blood.2022015850
11. Park HS. What is new in acute myeloid leukemia classification? *Blood Res.* 2024;59(1):15. PMID 38616211. doi:10.1007/s44313-024-00016-8
12. FDA. FDA approves revumenib for relapsed or refractory acute myeloid leukemia with a susceptible NPM1 mutation. 24 October 2025. https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-revumenib-relapsed-or-refractory-acute-myeloid-leukemia-susceptible-npm1-mutation
13. FDA. FDA approves ziftomenib for relapsed or refractory acute myeloid leukemia with a NPM1 mutation. 13 November 2025. https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-ziftomenib-relapsed-or-refractory-acute-myeloid-leukemia-npm1-mutation
14. REVUFORJ (revumenib) full prescribing information, DailyMed / FDA label. https://dailymed.nlm.nih.gov/dailymed/fda/fdaDrugXsl.cfm?setid=6eb3cdbc-0e74-477d-82d6-3bb172d3f63f&type=display
15. Arellano ML, Issa GC, Madanat YF, et al. Menin inhibition with revumenib for NPM1-mutated relapsed or refractory acute myeloid leukemia: the AUGMENT-101 study. *Blood.* 2025;146(9):1065-1077. PMID 40332046. doi:10.1182/blood.2025028357
16. Ivey A, Hills RK, Simpson MA, et al. Assessment of Minimal Residual Disease in Standard-Risk AML. *N Engl J Med.* 2016;374(5):422-33. PMID 26789727. doi:10.1056/NEJMoa1507471
17. Cloos J, Freeman SD, Ossenkoppele GJ, et al. 2025 update on MRD in acute myeloid leukemia: a consensus document from the ELN-DAVID MRD Working Party. *Blood.* 2026;147(11):1147-1167. PMID 41397238. doi:10.1182/blood.2025031480
18. ClinVar VCV000013998 — NM_002520.7(NPM1):c.860_863dup (p.Trp288fs), pathogenic, "Mutation A". https://www.ncbi.nlm.nih.gov/clinvar/variation/13998/
19. Brunetti L, Gundry MC, Sorcini D, et al. Mutant NPM1 Maintains the Leukemic State through HOX Expression. *Cancer Cell.* 2018;34(3):499-512.e9. PMID 30205049. doi:10.1016/j.ccell.2018.08.005
20. Uckelmann HJ, Haarer EL, Takeda R, et al. Mutant NPM1 Directly Regulates Oncogenic Transcription in Acute Myeloid Leukemia. *Cancer Discov.* 2023;13(3):746-765. PMID 36455613. doi:10.1158/2159-8290.CD-22-0366
21. Uckelmann HJ, et al. Nuclear transcriptional condensates as drivers and therapeutic targets in NPM1-mutated AML. *Blood.* 2026;147(20):2291-2297. PMID 41949617. doi:10.1182/blood.2025031880
22. Uckelmann HJ, Kim SM, Wong EM, et al. Therapeutic targeting of preleukemia cells in a mouse model of NPM1 mutant acute myeloid leukemia. *Science.* 2020;367(6477):586-590. PMID 32001657. doi:10.1126/science.aax5863
23. Patel JL, Schumacher JA, Frizzell K, et al. Coexisting and cooperating mutations in NPM1-mutated acute myeloid leukemia. *Leuk Res.* 2017;56:7-12. PMID 28152414. doi:10.1016/j.leukres.2017.01.027
24. Alpermann T, Schnittger S, Eder C, et al. Molecular subtypes of NPM1 mutations have different clinical profiles, specific patterns of accompanying molecular mutations and varying outcomes in intermediate risk acute myeloid leukemia. *Haematologica.* 2016;101(2):e55-8. PMID 26471486. doi:10.3324/haematol.2015.133819
25. Mutti M, et al. Characteristics and clinical behavior of acute myeloid leukemia harboring rare non-A/B/D nucleophosmin (NPM1) gene mutation subtypes: a single-center experience and review of the literature. *Leuk Lymphoma.* 2024;65(4):511-515. PMID 38112426. doi:10.1080/10428194.2023.2294695
26. Lisi V, Blanchard È, Vladovsky M, et al. Unified gene expression signature of novel NPM1 exon 5 mutations in acute myeloid leukemia. *Blood Adv.* 2022;6(17):5160-5164. PMID 35849707. doi:10.1182/bloodadvances.2022007300
27. Othman J, Meggendorfer M, Tiacci E, et al. Overlapping features of therapy-related and de novo NPM1-mutated AML. *Blood.* 2023;141(15):1846-1857. PMID 36508705. doi:10.1182/blood.2022018108
28. Eckardt JN, Stasik S, Röllig C, et al. Alterations of cohesin complex genes in acute myeloid leukemia: differential co-mutations, clinical presentation and impact on outcome. *Blood Cancer J.* 2023;13(1):18. PMID 36693840. doi:10.1038/s41408-023-00790-1
29. Chang YS, et al. Prognostic implications of myelodysplasia-related gene mutations in NPM1-mutated acute myeloid leukemia: a systematic review and meta-analysis. *Haematologica.* 2026;111(9):2935-2945. PMID 41742883. doi:10.3324/haematol.2025.288081
30. Döhner H, Estey E, Grimwade D, et al. Diagnosis and management of AML in adults: 2017 ELN recommendations from an international expert panel. *Blood.* 2017;129(4):424-447. PMID 27895058. doi:10.1182/blood-2016-08-733196
31. Sargas C, Ayala R, Larráyoz MJ, et al. Comparison of the 2022 and 2017 European LeukemiaNet risk classifications in a real-life cohort of the PETHEMA group. *Blood Cancer J.* 2023;13(1):77. PMID 37173322. doi:10.1038/s41408-023-00835-5
32. Hernández-Sánchez A, et al. Unravelling co-mutational patterns with prognostic implications in NPM1 mutated adult acute myeloid leukemia — a HARMONY study. *Leukemia.* 2026;40(2):418-428. PMID 41535568. doi:10.1038/s41375-025-02851-9
33. Oñate G, Bataller A, Garrido A, et al. Prognostic impact of DNMT3A mutation in acute myeloid leukemia with mutated NPM1. *Blood Adv.* 2022;6(3):882-890. PMID 34516636. doi:10.1182/bloodadvances.2020004136
34. Zhang L, et al. Prognostic impact of myelodysplasia-related gene mutations in ELN-2022 favorable-risk acute myeloid leukemia subtypes. *Ann Med.* 2026;58(1):2636337. PMID 41797681. doi:10.1080/07853890.2026.2636337
35. Gener-Ricos G, Bataller A, Urrutia S, et al. NPM1-mutated myeloid neoplasms are a unique entity not defined by bone marrow blast percentage. *Cancer.* 2024;130(20):3452-3462. PMID 38896064. doi:10.1002/cncr.35433
36. Othman J, Potter N, Ivey A, et al. Postinduction molecular MRD identifies patients with NPM1 AML who benefit from allogeneic transplant in first remission. *Blood.* 2024;143(19):1931-1936. PMID 38364112. doi:10.1182/blood.2023023096
37. Othman J, Tiong IS, O'Nions J, et al. Molecular MRD is strongly prognostic in patients with NPM1-mutated AML receiving venetoclax-based nonintensive therapy. *Blood.* 2024;143(4):336-341. PMID 37647641. doi:10.1182/blood.2023021579
38. DiNardo CD, Jonas BA, Pullarkat V, et al. Azacitidine and Venetoclax in Previously Untreated Acute Myeloid Leukemia. *N Engl J Med.* 2020;383(7):617-629. PMID 32786187. doi:10.1056/NEJMoa2012971 · VIALE-A, NCT02993523
39. ClinicalTrials.gov records (accessed 9 Sep 2026 via API): **NCT07007312** KOMET-017, phase 3, recruiting, n=1,300; **NCT06652438** revumenib + azacitidine + venetoclax, phase 3, recruiting, n=448; **NCT04065399** AUGMENT-101, phase 1/2, recruiting; **NCT04067336** ziftomenib first-in-human, phase 1/2; **NCT05735184** KOMET-007, phase 1; **NCT05020665** AGILITY (entospletinib), phase 3, **TERMINATED**, 15 enrolled. https://clinicaltrials.gov/
40. Zeidner JF, Lin TL, Curran E, et al. Azacitidine, Venetoclax, and Revumenib for Newly Diagnosed NPM1-Mutated or KMT2A-Rearranged AML. *J Clin Oncol.* 2025;43(23):2606-2615. PMID 40504618. doi:10.1200/JCO-25-00914 · NCT03013998
41. Wang ES, et al. Ziftomenib with venetoclax and azacitidine in relapsed/refractory NPM1-mutated acute myeloid leukemia. *Blood.* 2026 (online 2 June 2026). PMID 42227701. doi:10.1182/blood.2026034043 · KOMET-007
42. Alhajahjeh A, et al. Menin inhibitors for patients with relapsed/refractory acute myeloid leukemia (AML): a systematic review and meta-analysis. *Leuk Lymphoma.* 2026;67(8):1662-1674. PMID 42251692. doi:10.1080/10428194.2026.2682397
43. Kwon MC, et al. Preclinical efficacy of the potent, selective menin-KMT2A inhibitor JNJ-75276617 (bleximenib) in KMT2A- and NPM1-altered leukemias. *Blood.* 2024;144(11):1206-1220. PMID 38905635. doi:10.1182/blood.2023022480
44. Kretschmer L, Ruhnke L, Schliemann C, et al. VINCENT: A randomized-controlled trial evaluating venetoclax plus azacitidine versus intensive chemotherapy in patients with newly diagnosed, NPM1-mutated AML. *Ann Hematol.* 2025;104(7):3647-3654. PMID 40629154. doi:10.1007/s00277-025-06496-7 · NCT05904106, recruiting
45. Höllein A, Nadarajah N, Meggendorfer M, et al. NPM1 mutated AML can relapse with wild-type NPM1: persistent clonal hematopoiesis can drive relapse. *Blood Adv.* 2018;2(22):3118-3125. PMID 30455361. doi:10.1182/bloodadvances.2018023432
46. Perner F, Stein EM, Wenge DV, et al. MEN1 mutations mediate clinical resistance to menin inhibition. *Nature.* 2023;615(7954):913-919. PMID 36922589. doi:10.1038/s41586-023-05755-9
47. Orvain C, Bertoli S, Peterlin P, et al. Molecular relapse after first-line intensive therapy in patients with CBF or NPM1-mutated acute myeloid leukemia — a FILO study. *Leukemia.* 2024;38(9):1949-1957. PMID 39020060. doi:10.1038/s41375-024-02335-2
48. Jimenez-Chillon C, Othman J, Taussig D, et al. Venetoclax-based low intensity therapy in molecular failure of NPM1-mutated AML. *Blood Adv.* 2024;8(2):343-352. PMID 38039513. doi:10.1182/bloodadvances.2023011106

### Notes on evidence limits

- **Author strings** for some entries are abbreviated to first author + "et al."; journal,
  volume, pages, year, PMID and DOI were verified for every entry.
- The **ICC 2022 blast threshold** could not be read from the primary Blood article (publisher
  returned HTTP 403). The ≥10% figure is taken from ref [11] and was independently
  cross-checked against a second secondary source; the primary ICC paper [10] is cited as the
  authority for the entity itself.
- The **VIALE-A *NPM1* subgroup** effect size (composite CR and median OS restricted to
  *NPM1*-mutated patients) is widely quoted in secondary coverage but was **not** verified
  against a primary publication, and is therefore **omitted** rather than reproduced.
- **Bleximenib** phase 1b combination results existed only as 2025 congress abstracts and
  sponsor press releases at the time of writing; only the peer-reviewed preclinical paper [43]
  is cited as evidence.
- **NCCN** listing of menin inhibitors for *NPM1*-mutant R/R AML was reported in trade
  coverage; the **NCCN guideline document itself was not retrieved**, so no NCCN category is
  asserted here — **[unverified]**.
- **Pediatric frequency** rests on a single retrospective TARGET analysis (n=869) [7] plus
  review estimates [6]; no prospective pediatric registry figure was retrieved.
