# KMT2A rearrangements, NUP98 fusions, and other fusion oncogenes

> Reference monograph. Evidence current to **9 September 2026**; points where the evidence
> trail goes cold are flagged. Every number carries its cohort and endpoint. Evidence tiers
> stated inline: **[approved]**, **[phase 3 positive]**, **[phase 1-2 signal]**,
> **[preclinical]**, **[hypothesis]**. Not medical advice — see `../../DISCLAIMER.md`.

This file covers the *fusion-oncogene* axis of AML: rearrangements creating a chimeric
transcription/chromatin regulator that locks in a stem-cell program. They are grouped together
because they converge mechanistically (most drive *HOXA*/*MEIS1*), because several are
**invisible to karyotype**, and because they now share a drug class.

**At a glance**

| Field | Value |
|---|---|
| Gene / lesion | *KMT2A* (formerly *MLL*), HGNC:7132, 11q23.3, NM_005933, OMIM 159555, UniProt Q03164 [1]; *NUP98*, HGNC:8068, 11p15.4, NM_016320, OMIM 601021, UniProt P52948 [1]. **107 in-frame *KMT2A* fusion partners** described (37 recurrent, 63 seen once) plus partial tandem duplication (PTD) [2]. Also covered: *CBFA2T3::GLIS2*, *DEK::NUP214*, *KAT6A::CREBBP*, *MECOM*/*EVI1*, *NPM1* fusions |
| Frequency (adult AML) | *KMT2A*r **172/9,465 (2%)** newly diagnosed adult AML, MD Anderson [3]; 5.7% *KMT2A*r + 2.3% *KMT2A*-PTD among 730 adults, Cleveland Clinic, as reported in review [4]. *KMT2A*-PTD **32/387 (8.3%)** of adult de novo AML with non-favourable cytogenetics [5]. *NUP98*r **13/260 (5.0%)** newly diagnosed adult AML, single Korean centre [6]; ~2.5% single-institution estimate [7]. inv(3)/t(3;3) **~1.2%** of newly diagnosed AML [8]. *DEK::NUP214* **1–2%** of AML [31]. t(8;16)/*KAT6A::CREBBP* is **very rare** — 62 pediatric cases required an 18-country I-BFM collaboration to assemble [10] |
| Frequency (pediatric AML) | *KMT2A*r **215/1,022 (21%)** COG AAML0531 [11]; ~40% of AML in children <3 y, 10–15% in older children/AYA (review) [12]. *NUP98*r **160/2,235 (7.2%)** COG transcriptome cohort — *NSD1* 4.8%, *KDM5A* 1.4%, *NUP98*-X 0.9% [13]; review estimate ~4% [12]. *CBFA2T3::GLIS2* ~20–30% of non-Down-syndrome AMKL [14] |
| ELN 2022 risk | **Intermediate**: t(9;11)(p21.3;q23.3)/*MLLT3::KMT2A*. **Adverse**: t(v;11q23.3)/*KMT2A*-rearranged; t(6;9)/*DEK::NUP214*; inv(3)/t(3;3) and other t(3q26.2;v)/*MECOM(EVI1)*-rearranged; t(8;16)/*KAT6A::CREBBP* [4,15]. *NUP98* fusions and *CBFA2T3::GLIS2* are **not in the ELN 2022 table** — a recognised gap [14,16] |
| WHO 2022 / ICC 2022 entity | Both recognise **AML with *KMT2A* rearrangement**, **AML with *MECOM* rearrangement**, **AML with *NUP98* rearrangement** (WHO 5th ed.; also ICC per [16]), **AML with *DEK::NUP214***, **AML with *CBFA2T3::GLIS2***, **AML with *KAT6A::CREBBP*** [17,18]. WHO 5th ed. imposes **no blast threshold** for AML with defining genetic abnormalities; ICC 2022 requires **≥10% blasts** [16] |
| Actionable targeted therapy | **Yes, for *KMT2A*r only.** **Revumenib** (Revuforj) FDA-approved **15 Nov 2024** for R/R acute leukemia with a *KMT2A* translocation, ages ≥1 y **[approved]** [19]. Ziftomenib's approval (13 Nov 2025) is **NPM1-only, adults only** — *not* *KMT2A*r [20]. No approved therapy for *NUP98*r, *CBFA2T3::GLIS2*, *DEK::NUP214*, *MECOM*r, or *KAT6A::CREBBP* as of 9 Sep 2026 |
| MRD suitability | **Good for fusion-positive disease.** Pretransplant *KMT2A* fusion-transcript MRD ≥0.001% by RT-qPCR: 2-y RFS **17% vs 59%**, 2-y CIR **75% vs 25%** [21]. Flow-MRD at end of induction 2 independently prognostic in 1,130 children [22]. ELN MRD Working Party endorses RT-qPCR for *KMT2A::MLLT3* [23]. **Not applicable to *KMT2A*-PTD** (no fusion junction) |
| Germline relevance | **None established for *KMT2A*r, *NUP98*r, or *CBFA2T3::GLIS2*** — these are somatic events, and none of these loci appears as a germline-predisposition entity in WHO 2022 or ICC 2022 [17,18]. Germline *MECOM* variants cause **radioulnar synostosis with amegakaryocytic thrombocytopenia (RUSAT-2)**, a bone-marrow-failure syndrome distinct from somatic 3q26 rearrangement; leukaemia predisposition in RUSAT-2 is **not** established [24] |

---

## Biology

**KMT2A.** Rearrangement invariably retains the **N-terminus** — including the menin-binding
motif (MBM) and the LEDGF/PSIP1-binding domain — and **discards the C-terminal SET
methyltransferase domain**, fusing in one of >100 partners [2]. The chimera is therefore a
**mistargeted transcriptional activator**, not a hyperactive methyltransferase. Menin tethers it
to LEDGF, whose PWWP domain reads H3K36me2/3 at active gene bodies; the complex also recruits
PAF1c and, via the partner (typically an AF4/ENL/AF9-family super-elongation-complex member),
DOT1L and pTEFb. The output is fixed, high-level **HOXA9, HOXA10 and MEIS1** transcription,
enforcing self-renewal and blocking differentiation [4].

That dependency chain is the drug target: because the menin interaction is *required for
chromatin occupancy* rather than for catalysis, small molecules occupying the menin MBM pocket
evict the fusion from its targets and trigger differentiation [25].

**KMT2A-PTD** is a mechanistically separate lesion: an in-frame internal duplication (commonly
exons 2/3 through 6 or 8–11) of the *KMT2A* 5′ region on one allele, producing an elongated
but intact KMT2A protein, not a chimera. It is **invisible to conventional karyotype** and to
break-apart FISH, and requires RT-qPCR, long-range PCR or targeted NGS [5]. It was
**explicitly excluded** from the revumenib registration cohort [19].

**NUP98.** Fusion retains NUP98's N-terminal FG/GLFG repeats — an intrinsically disordered
region providing transactivation and multivalent self-association — and appends a
chromatin-reading or -writing partner that supplies locus specificity: **NSD1** (H3K36
methyltransferase) and **KDM5A** (H3K4 demethylase, PHD finger reading H3K4me3) are the two
commonest. Net effect is again a locked *HOXA* program, and one that also depends on menin —
a preclinical rationale for menin inhibition in *NUP98*r disease [26].

**CBFA2T3::GLIS2** arises from a **cryptic inv(16)(p13.3q24.3)** — normal karyotype in a large
fraction of cases — and fuses the ETO-family corepressor CBFA2T3 to the Hedgehog-pathway zinc
finger GLIS2. It drives a megakaryocytic/RAM-phenotype program (bright CD56, dim-to-negative
CD45 and CD38, HLA-DR–negative) and high surface **FOLR1 (folate receptor α)** [14,27].

**MECOM/EVI1.** inv(3)(q21.3q26.2)/t(3;3) is the archetype of **enhancer hijacking**: a distal
*GATA2* enhancer is repositioned next to *MECOM*, driving EVI1 overexpression from the
rearranged allele while *GATA2* becomes monoallelic from the intact allele; full-length
*MDS1-EVI1* is lost. In 33 AML cases with **atypical 3q26 rearrangements** the same signature
was reproduced — EVI1 high, MDS1-EVI1 absent, superenhancer capture (*CD164, PROM1, CDK6,
MYC*), frequent allele-specific *GATA2* expression — supporting a single 3q26-rearranged entity
rather than inv(3)/t(3;3) alone [28].

**DEK::NUP214** (t(6;9)) acts as an XPO1-dependent transcriptional activator with an altered
HOX/MEIS axis resembling *FLT3*-ITD/*NPM1* AML [9]. **KAT6A::CREBBP** (t(8;16)) fuses two
histone acetyltransferases; its expression signature clusters near but distinct from *KMT2A*r
AML, with high *HOXA11*/*HOXA10* [10]. **NPM1 fusions** (*NPM1::MLF1* from t(3;5),
*NPM1::CCDC28A*) phenocopy NPM1c: they bind the *HOX* cluster and activate *HOXA*/*HOXB* with
MEIS1/PBX3 in an **XPO1-dependent** manner; selinexor suppressed this in vitro and
*NPM1::CCDC28A* cells were menin-inhibitor sensitive **[preclinical]** [29].

## Epidemiology and co-mutation landscape

Two age peaks dominate *KMT2A*r AML: **infants and young children**, where it accounts for
roughly 40% of AML under age 3 [12], and **adults**, where a large minority is
**therapy-related**: 40% of 172 *KMT2A*r cases at MD Anderson were t-AML, with median OS 0.7 y
versus 1.4 y for de novo *KMT2A*r [3]. The classical exposure is **topoisomerase II inhibition**
(etoposide, anthracyclines), with short latency and a balanced translocation typically arising
without a preceding MDS phase [2,3].

Partner distribution differs by lineage and age. Among **1,116 AML cases** in the KMT2A
recombinome: *MLLT3* 30.4%, *MLLT10* 18.7%, **KMT2A-PTD 10.7%**, *ELL* 10.1%, *AFDN* 8.1%,
*MLLT1* 4.2%, *MLLT11* 2.4%; seven partners plus PTD account for >90% of all recombinations
[2]. In adults specifically, t(9;11) is 49–57% of *KMT2A*r [3,30].

**Co-mutations are sparse and RAS-dominated.** In the HARMONY cohort of 205 adult *KMT2A*r
AML (185 with NGS; median age 48.1 y; 72.2% de novo): *NRAS* 21%, *KRAS* 19.5%, RAS-pathway
combined 42.1%, *FLT3*-TKD 13.3%, *TP53* 8.6%, *TET2* 8.1%, *DNMT3A* 6.5% [30]. *KRAS*
mutations are enriched in t(6;11)/*KMT2A::AFDN* [30]. None of the *KMT2A*-PTD-positive
patients in that adult series carried an *NPM1* mutation, a *CEBPA*-bZIP in-frame mutation, or a
*KMT2A* rearrangement [5].

*NUP98*r co-mutations are partner-specific: **NUP98::NSD1** carries *FLT3*-ITD in **74%** and
*WT1* mutation in **42%**; **NUP98::KDM5A** is instead enriched for **chromosome 13
aberrations (63.3%)**; *NUP98*-X variants associate with *WT1* mutation (25%) [13].
*NUP98::KDM5A* is the younger lesion (median 2.7 y vs 10.2 y for *NSD1*) and skews
erythroid/megakaryocytic [13].

inv(3)/t(3;3) AML carries **SF3B1 in 50%**, RAS/MAPK-pathway mutations in **71%**, and
**monosomy 7 in 44%** (n=108, MD Anderson) [8]. *DEK::NUP214* carries *FLT3*-ITD in **62%** of
178 adults [31].

## Prognostic significance

**Partner identity matters more in children than in adults.** In 756 children with
11q23/*KMT2A*r AML (median age 2.2 y), 5-year EFS was 44% and OS 56% overall, but ranged from
**92% EFS / 100% OS in t(1;11)(q21;q23) (n=25)** to **11% EFS / 22% OS in
t(6;11)/*KMT2A::AFDN* (n=35)**; t(10;11)(p12;q23) (n=98) 31% EFS and t(10;11)(p11.2;q23)
(n=12) 17% EFS were also adverse. This study **did not confirm** a favourable outcome for
t(9;11) versus other partners overall [32]. A COG AAML0531 analysis reported 5-year
EFS/OS of 54%/70% for *KMT2A::MLLT3*, 33%/54% for *MLLT10*, 45%/68% for *ELL*, 23%/39% for
*MLLT4*/*AFDN*, and 35%/52% for *MLLT1* [12].

In **adults**, partner identity largely washes out once other factors are controlled. HARMONY
found **no OS difference across fusion partners (P=0.756)**; independent adverse factors were
age >60 y (HR 2.1), secondary AML (HR 2.2), *KRAS* (HR 2.0) and *DNMT3A* (HR 2.1) mutation, and
in de novo patients <60 y (n=115) *KRAS*- or *TP53*-mutated cases had CR 50% vs 85.5% and median
OS 7 vs 30 months [30]. In the MD Anderson series translocation subtype did **not**
independently predict survival (age, platelets, creatinine and allo-HSCT did) [3], and TROPHY
found 3-year post-transplant OS 74.3% for *KMT2A::MLLT3* vs 77.5% for other partners (P=0.97)
[33]. ELN 2022 nonetheless keeps t(9;11) in intermediate risk and all other *KMT2A*
rearrangements in adverse risk [15]; that split rests on older data and remains contested [4,30].

**Transplant.** Adult evidence supports allo-HSCT in CR1: 5-year OS 52% with versus 14%
without transplant in CR1 (MD Anderson, non-randomised) [3]; allo-HSCT was an independent
favourable factor for OS (HR 0.56) and relapse (HR 0.01) in TROPHY [33]. **Pediatric evidence
does not agree.** In 1,130 children with *KMT2A*r AML (I-BFM-SG), allo-HSCT in CR1 reduced
relapse only in the high-risk-partner group (HR 0.5) and **did not improve OS** — recorded here
with full prominence as a negative result [22].

**KMT2A-PTD prognosis is unsettled and the most recent data are negative.** In 387 consecutive
adult de novo AML with non-favourable cytogenetics, *KMT2A*-PTD (8.3%) co-occurred with
*FLT3*-ITD, *RUNX1* and *DNMT3A* mutations and normal karyotype, but had **no effect on CR,
RFS or OS** overall or within any subgroup [5]. Older reports of adverse impact in
normal-karyotype AML are not reproduced here.

**Other fusions.** *NUP98::NSD1* 5-year EFS 17% / OS 36%; *NUP98::KDM5A* OS 30%; *NUP98*-X OS
35% (n=2,235 pediatric COG) — with abnormal chromosome 13 the exception carrying better
outcome [13]. **CBFA2T3::GLIS2** is among the worst: 5-year EFS 8%, OS 14% [12]; >75% of
fusion-positive cases relapse within two years [14]. inv(3)/t(3;3): median OS 7.9 months
(newly diagnosed, n=53) and 5.9 months (R/R, n=55); 3-year OS 8.8%/7.1%; 3-year cumulative
relapse 81.7%; 5-year OS 44% with versus 6% without HSCT in CR1, though only 10% reached
transplant [8]. *DEK::NUP214*: 5-year OS 38% in 178 adults, rising to 53% with allo-HSCT in CR1
versus 23% with consolidation chemotherapy [31]; in 544 EBMT transplant recipients, 2-year OS
65.7% overall and 71.7% in CR1, with *FLT3*-ITD tripling relapse risk without changing OS [34].
Pediatric t(8;16) (n=62, I-BFM): median age 1.2 years, erythrophagocytosis 70%, leukaemia cutis
58%, DIC 39%, **spontaneous remission in 7 neonates (3 in continuous remission)**, 5-year OS
59% — not different from the reference cohort [10].

## Diagnostic testing and MRD

Because WHO 5th edition [17] and ICC 2022 [18] both make these fusions *disease-defining*,
detecting them is a classification requirement rather than an optional add-on — and
**karyotype under-ascertains this entire family**. Break-apart FISH for *KMT2A* detects the
rearrangement but **not the partner**, which is what pediatric risk stratification needs.
*KMT2A::MLLT10*, *NUP98::NSD1*, *NUP98::KDM5A* and *CBFA2T3::GLIS2* are frequently cryptic.

The quantitative case for **RNA sequencing** is now firm. In 241 children in the AML-BFM 2017
registry, panel-based RNA fusion sequencing changed risk assignment in **25/241 (10.4%)** — 24
moved into high risk — and found risk-relevant fusions missed by karyotype/FISH in 8.3%. All 10
*NUP98::NSD1* and all 3 *CBFA2T3::GLIS2* cases were detected **only** by RNA-FS, and 9
*KMT2A::MLLT10* cases had their partner resolved only by RNA-FS [35]. In adults, *NUP98*r has
**>40 described partners** and is "often cryptic on karyotype", so it is underdiagnosed without
dedicated RNA-based NGS, *NUP98* break-apart FISH or fusion-specific RT-qPCR [7].

Practical implication: **a normal karyotype is not evidence against a fusion oncogene**, and an
RNA-based assay belongs in the diagnostic algorithm for infant AML, for AMKL and erythroid AML,
and for any AML in which a menin inhibitor is being considered.

**Regulatory diagnostics.** FDA granted de novo authorisation **DEN240067** on 19 Sep 2025 to
the **KMT2A Breakapart FISH Probe Kit PDx (Cytocell/Oxford Gene Technology)**, classified as a
"revumenib eligibility detection system" [36]. Note the asymmetry: the authorised test detects
*KMT2A* breakapart, not the partner; and no FDA-approved companion diagnostic exists for the
*NPM1* indication [19].

**MRD.** Fusion transcripts are excellent molecular MRD targets. ELN MRD Working Party
guidance covers RT-qPCR for *KMT2A::MLLT3* with sensitivity ≥1×10⁻⁴ [23]. Pretransplant
*KMT2A*r MRD ≥0.001% by qPCR predicted 2-year RFS 17% vs 59% and CIR 75% vs 25% (P=.0004)
[21]; in TROPHY, detectable pretransplant *KMT2A*r MRD independently predicted inferior EFS
(HR 2.46) [33]. Flow-MRD ≥0.1% at end of induction 2 was independently prognostic in 1,130
children (5-year EFS 47.6% vs 16.3%; OS 66.0% vs 27.9%) [22]. Breakpoint heterogeneity is the
main technical obstacle; *KMT2A*-PTD has **no fusion junction** and is not MRD-trackable by
this route.

## Therapeutic implications

**Approved.** **Revumenib** (Revuforj), 15 Nov 2024, for R/R acute leukemia with a *KMT2A*
translocation in patients ≥1 year **[approved]** [19]. Registration cohort SNDX-5613-0700
(AUGMENT-101, NCT04065399), n=104, median age 37 y (range 1–79), 83% AML / 15% ALL / 2% MPAL,
59% refractory relapse, 44% prior transplant: **CR+CRh 21.2% (95% CI 13.8–30.3)**, median
duration 6.4 months, median time to response 1.9 months; 12/83 (14%) transfusion-dependent
patients became independent. *KMT2A*-PTD was an exclusion criterion [19]. The phase 2
publication reports **ORR 63.2%**, CR+CRh **22.8%** (24.5% AML, 14.3% ALL), MRD-negativity in
**70%** of evaluable CR+CRh responders, and median OS **8.0 months** [37]. Twenty-five of the
104 registration patients (24%) were under 17 years old and 24 (23%) proceeded to transplant
after revumenib; the label gives no separately powered pediatric efficacy estimate [19].

**Black-box safety must travel with the efficacy.** Revuforj carries a **BOXED WARNING for
differentiation syndrome and for QTc prolongation/Torsades de Pointes** [19]. Differentiation
syndrome occurred in **60/241 (25%)** treated at the recommended dose — 33% of *KMT2A*-translocated
AML, 33% of MPAL, 9% of ALL — grade 3/4 in 12%, **fatal in two patients**, median onset day 9.
QTc prolongation occurred in **86/241 (36%)** (grade 3 in 15%, grade 4 in 2%), QTcF >500 ms in
10%, with one fatal cardiac arrest and one non-sustained Torsades; incidence rose with age (21%
under 17 y, 46% at ≥65 y) [19].

**Not approved for KMT2Ar.** Ziftomenib (Komzifti, 13 Nov 2025) is licensed only for **adults**
with R/R **NPM1**-mutated AML; its label carries a boxed warning for differentiation syndrome
[20]. In KOMET-001 phase 1 (n=83), **differentiation-syndrome rate and severity caused
enrolment of *KMT2A*-rearranged patients to be halted**; at the 600 mg RP2D, 9/36 (25%) of
*KMT2A*r-or-*NPM1*m patients achieved CR/CRh, and CR was reported in 7/20 (35%) *NPM1*m
patients — the *KMT2A*r-specific signal was weak [38]. This is a genuine class asymmetry, not a
reporting artefact.

**Combinations [phase 1-2 signal].** Revumenib + azacitidine + venetoclax, newly diagnosed
patients ≥60 y (Beat AML substudy, NCT03013998, n=43; 34 *NPM1*m, 9 *KMT2A*r): overall CR
67.4%, CRc 81.4%, ORR 88.4%; in the 9 *KMT2A*r patients CR 78%, CRc 89%, ORR 100%, all 37
evaluated patients MRD-negative. Differentiation syndrome 19%, QTc prolongation 44%, 30-day
mortality 7% — but **median follow-up was only 6.9 months**, so no durability inference is
available [39]. In R/R disease the all-oral SAVE regimen (revumenib + decitabine/cedazuridine +
venetoclax; phase 1-2, n=42; 40% *KMT2A*r, 38% *NPM1*m, 21% *NUP98*r) gave CRc 71% and CR/CRh
60% with 80% flow-MRD negativity; median CR/CRh duration was **not reached in *KMT2A*r**, 10.7
months in *NPM1*m, 5.9 months in *NUP98*r; differentiation syndrome 10% [40].

**Other menin inhibitors in development** (per review [4]): bleximenib (cAMELot-1,
NCT04811560) and enzomenib (Horizen-1, NCT04988555), both recruiting as of 9 Sep 2026 [45]. Their combination data exist only in
company press releases and conference abstracts — **secondary and unpublished** — and are not
reproduced here as trial results.

**Not menin-targetable.** For *CBFA2T3::GLIS2*, the lead clinical asset was the FOLR1-directed
antibody–drug conjugate **luveltamab tazevibulin**, with a registration-directed pediatric
trial (REFRαME-P1, NCT06679582). **The sponsor deprioritised the molecule for business reasons
in 2025; the trial record now reads TERMINATED, and in June 2026 the nonprofit Blood Cancer
United acquired the remaining drug supply and the IND to run a no-cost compassionate-use
programme while stock lasts** [41,CTGOV]. This is a programme withdrawal, not an efficacy failure, and it is the single
most consequential access problem in this file: the disease affects roughly 17 US children per
year [41]. Preclinical FOLR1-directed CAR-T constructs against this fusion remain
**[preclinical]** [27]. For inv(3)/*MECOM*r, no targeted agent exists; CRc was 46% with
intensive chemotherapy, 47% with hypomethylating agents and **33% with venetoclax-based
regimens** (n=108) — venetoclax does not rescue this subtype [8]. For *DEK::NUP214*, allo-HSCT
in CR1 remains the intervention with the strongest supporting data [31,34].

**Non-targeted but genotype-informative:** in COG AAML0531 (n=1,022; 215 *KMT2A*r), adding
**gemtuzumab ozogamicin** improved 5-year EFS in *KMT2A*r AML (48% vs 29%, P=.003) with OS not
significantly different (63% vs 53%, P=.054); multivariable HRs were 0.52 for EFS, 0.47 for DFS
and 0.45 for relapse risk **[phase 3, secondary analysis]** [11].

**Failed program.** The DOT1L inhibitor **pinometostat (EPZ-5676)** targeted the same
elongation complex. In 51 adults with advanced *KMT2A*r leukemia (NCT01684150) it was tolerable
and reduced H3K79 methylation but produced only **two complete remissions**, both in t(11;19) —
a negative single-agent result [42].

## Resistance and relapse

Three resistance routes are documented for menin inhibition:

1. **On-target *MEN1* mutation.** Somatic mutations at the drug-binding residues **M327, G331
   and T349** were found in patients progressing on revumenib in AUGMENT-101 and reduce
   inhibitor binding; M327I/V reduces binding across the class (~30–300-fold), i.e. a class
   effect rather than a compound-specific one [43]. Emergent menin-binding-site mutations
   occurred in **13%** of SAVE-trial patients [40]. A 2026 report describes **overcoming
   *MEN1*-mediated resistance by switching menin inhibitor** (revumenib → bleximenib), making
   mutation-guided switching a testable strategy **[phase 1-2 signal / case-level]** [44].
2. **TP53 inactivation**, linked to MCL1 upregulation **[preclinical]** [4].
3. **Non-genetic transcriptional adaptation** with loss of UTX-dependent tumour suppression,
   reversible with CDK4/6 inhibition in models **[preclinical]** [4].

Beyond drug resistance: *KMT2A* fusion transcripts stay detectable and prognostic in the
pre-relapse setting, which is what makes them usable MRD targets [21,33], and RAS-pathway
mutations are the commonest cooperating and outcome-modifying events [30]. *CBFA2T3::GLIS2* relapse can be extramedullary and
histologically deceptive [14].

## Open questions

1. **Should partner identity remain in adult risk stratification?** Three adult cohorts
   (HARMONY n=205, MD Anderson n=172, TROPHY n=292) found no partner-specific OS difference once
   age, secondary disease and co-mutation were accounted for [3,30,33], yet ELN 2022 still splits
   t(9;11) from t(v;11q23.3) [4,15]. A prospective, co-mutation-adjusted reanalysis is needed.
2. **Where do *NUP98* fusions and *CBFA2T3::GLIS2* belong in ELN?** Both are WHO/ICC entities
   with dismal outcomes and neither appears in the ELN 2022 genetic risk table.
3. **Why the adult/pediatric transplant discordance?** Adult series show large allo-HSCT
   benefit in CR1 [3,33]; the 1,130-child I-BFM analysis shows relapse reduction without OS
   benefit [22]. Confounding by indication in the adult retrospective data is the obvious
   candidate and has not been excluded.
4. **Can menin inhibition move to front line and to *NUP98*r?** Triplet data are promising but
   phase 1-2 with short follow-up [39,40]; no randomised readout for revumenib exists as of
   9 Sep 2026, and the *NUP98*r indication is not approved anywhere.
5. **Is *KMT2A*-PTD a driver at all?** The most rigorous recent adult analysis finds no
   prognostic effect [5], it was excluded from the revumenib label [19], and its menin
   dependency is unestablished. Treating it as equivalent to *KMT2A*r is not supported.
6. **Who develops drugs for ~17 children a year?** The luveltamab withdrawal is a
   market-failure, not a science, problem [41,42].
7. **Evidence trail goes cold** on: partner-resolved MRD thresholds outside *MLLT3*/*MLLT10*;
   menin-inhibitor activity in *KAT6A::CREBBP* and *DEK::NUP214* (no clinical data retrieved);
   and any prospective validation of RNA-seq-driven risk reassignment on survival endpoints
   (the 10.4% reclassification figure [35] is analytic, not outcome-validated).

---

## References

1. HGNC gene records, retrieved 9 Sep 2026: *KMT2A* (lysine methyltransferase 2A), HGNC:7132, 11q23.3, NM_005933, OMIM 159555, UniProt Q03164 — https://rest.genenames.org/fetch/symbol/KMT2A ; *NUP98* (nucleoporin 98 and 96 precursor), HGNC:8068, 11p15.4, NM_016320, OMIM 601021, UniProt P52948 — https://rest.genenames.org/fetch/symbol/NUP98
2. Meyer C, Larghero P, Almeida Lopes B, et al. The KMT2A recombinome of acute leukemias in 2023. *Leukemia*. 2023;37(5):988–1005. PMID 37019990. doi:10.1038/s41375-023-01877-1
3. Issa GC, Zarka J, Sasaki K, et al. Predictors of outcomes in adults with acute myeloid leukemia and KMT2A rearrangements. *Blood Cancer J*. 2021;11(9):162. PMID 34588432. doi:10.1038/s41408-021-00557-6
4. Testa U, Pelosi E, Castelli G. Acute myeloid leukemias with alterations of lysine methyltransferase 2A (KMT2A): recent therapeutic developments. *Cancers (Basel)*. 2026;18(9):1341. PMID 42122138. doi:10.3390/cancers18091341 *(review; used for ELN assignment restatement, KMT2A-alteration frequencies as reported from a Cleveland Clinic series, agent/NCT list, and resistance taxonomy)*
5. Xie DH, Chen WM, Hao Y, et al. The characteristics and outcomes of adult acute myeloid leukemia patients with KMT2A-partial tandem duplication. *Int J Lab Hematol*. 2025;47(6):1119–1127. PMID 40662375. doi:10.1111/ijlh.14532
6. Kim N, et al. NUP98 is rearranged in 5.0% of adult East Asian patients with AML. *Blood Adv*. 2024;8(19):5122–5125. PMID 39158088. doi:10.1182/bloodadvances.2024012960
7. Yuen LD, Hasserjian RP, Fathi AT, et al. Strategies for identifying NUP98 rearrangements in adult myeloid neoplasms. *Haematologica*. 2026;111(2):518–534. PMID 40820841. doi:10.3324/haematol.2025.288080
8. Richard-Carpentier G, et al. Characteristics and clinical outcomes of patients with acute myeloid leukemia with inv(3)(q21q26.2) or t(3;3)(q21;q26.2). *Haematologica*. 2023;108(9):2331–2342. PMID 36951163. doi:10.3324/haematol.2022.282030
9. Potluri S, Kellaway SG, Coleman DJL, et al. Gene regulation in t(6;9) DEK::NUP214 acute myeloid leukemia resembles that of FLT3-ITD/NPM1 acute myeloid leukemia but with an altered HOX/MEIS axis. *Leukemia*. 2024;38(2):403–407. PMID 38172329. doi:10.1038/s41375-023-02118-1
10. Coenen EA, Zwaan CM, Reinhardt D, et al. Pediatric acute myeloid leukemia with t(8;16)(p11;p13), a distinct clinical and biological entity: a collaborative study by the International-Berlin-Frankfurt-Münster AML-study group. *Blood*. 2013;122(15):2704–2713. PMID 23974201. doi:10.1182/blood-2013-02-485524
11. Pollard JA, Guest E, Alonzo TA, et al. Gemtuzumab ozogamicin improves event-free survival and reduces relapse in pediatric KMT2A-rearranged AML: results from the phase III Children's Oncology Group trial AAML0531. *J Clin Oncol*. 2021;39(28):3149–3160. PMID 34048275. doi:10.1200/JCO.20.03048
12. Egan G, Tasian SK. Precision medicine for high-risk gene fusions in pediatric AML: a focus on KMT2A, NUP98, and GLIS2 rearrangements. *Blood*. 2025;145(22):2574–2586. PMID 39808803. doi:10.1182/blood.2024026598
13. Bertrums EJM, Smith JL, Harmon L, et al. Comprehensive molecular and clinical characterization of NUP98 fusions in pediatric acute myeloid leukemia. *Haematologica*. 2023;108(8):2044–2058. PMID 36815378. doi:10.3324/haematol.2022.281653
14. Masetti R, Bertuccio SN, Pession A, Locatelli F. CBFA2T3-GLIS2-positive acute myeloid leukaemia. A peculiar paediatric entity. *Br J Haematol*. 2019;184(3):337–347. PMID 30592296. doi:10.1111/bjh.15725
15. Döhner H, Wei AH, Appelbaum FR, et al. Diagnosis and management of AML in adults: 2022 recommendations from an international expert panel on behalf of the ELN. *Blood*. 2022;140(12):1345–1377. PMID 35797463. doi:10.1182/blood.2022016867
16. Aqil B. What's new in hematopathology 2025: myeloid neoplasms in the WHO 5th edition and ICC. *J Pathol Transl Med*. 2025;59:472–475. PMID 41266100. doi:10.4132/jptm.2025.09.24
17. Khoury JD, Solary E, Abla O, et al. The 5th edition of the World Health Organization Classification of Haematolymphoid Tumours: Myeloid and Histiocytic/Dendritic Neoplasms. *Leukemia*. 2022;36(7):1703–1719. PMID 35732831. doi:10.1038/s41375-022-01613-1
18. Arber DA, Orazi A, Hasserjian RP, et al. International Consensus Classification of Myeloid Neoplasms and Acute Leukemias: integrating morphologic, clinical, and genomic data. *Blood*. 2022;140(11):1200–1228. PMID 35767897. doi:10.1182/blood.2022015850
19. REVUFORJ (revumenib) US prescribing information, NDA 218944 (label effective 4 Feb 2026; original approval 15 Nov 2024; supplemental NPM1 indication 24 Oct 2025). Retrieved via openFDA drug label API and FDA Drugs@FDA. https://api.fda.gov/drug/label.json?search=openfda.brand_name:%22REVUFORJ%22 ; FDA approval announcement (15 Nov 2024): https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-revumenib-relapsed-or-refractory-acute-leukemia-kmt2a-translocation
20. KOMZIFTI (ziftomenib) US prescribing information (label effective 9 Dec 2025) and Drugs@FDA record NDA 220305, sponsor Kura, original approval **13 Nov 2025**. Retrieved via openFDA drug label and drugsfda APIs. https://api.fda.gov/drug/label.json?search=openfda.brand_name:%22KOMZIFTI%22 ; https://api.fda.gov/drug/drugsfda.json?search=openfda.brand_name:%22KOMZIFTI%22
21. Loo S, Potter N, Ivey A, et al. Pretransplant MRD detection of fusion transcripts is strongly prognostic in KMT2A-rearranged acute myeloid leukemia. *Blood*. 2024;144(24):2554–2557. PMID 39316646. doi:10.1182/blood.2024026605
22. van Weelderen RE, Klein K, Harrison CJ, et al. Measurable residual disease and fusion partner independently predict survival and relapse risk in childhood KMT2A-rearranged acute myeloid leukemia: a study by the International Berlin-Frankfurt-Münster Study Group. *J Clin Oncol*. 2023;41(16):2963–2974. PMID 36996387. doi:10.1200/JCO.22.02120
23. Heuser M, Freeman SD, Ossenkoppele GJ, et al. 2021 Update on MRD in acute myeloid leukemia: a consensus document from the European LeukemiaNet MRD Working Party. *Blood*. 2021;138(26):2753–2767. PMID 34724563. doi:10.1182/blood.2021013626
24. Syndrome of the month: radioulnar synostosis with amegakaryocytic thrombocytopenia type 2 (germline *MECOM*/RUSAT-2). *Am J Med Genet A*. 2026;200:1239–1244. PMID 41635268. doi:10.1002/ajmga.70077
25. Issa GC, Aldoss I, DiPersio J, et al. The menin inhibitor revumenib in KMT2A-rearranged or NPM1-mutant leukaemia. *Nature*. 2023;615(7954):920–924. PMID 36922593. doi:10.1038/s41586-023-05812-3
26. The MLL–menin interaction is a therapeutic vulnerability in NUP98-rearranged AML. *HemaSphere*. 2023;7(8):e935. PMID 37520776. doi:10.1097/HS9.0000000000000935
27. Le Q, Hadland B, Smith JL, et al. CBFA2T3-GLIS2 model of pediatric acute megakaryoblastic leukemia identifies FOLR1 as a CAR T cell target. *J Clin Invest*. 2022;132(22):e157101. PMID 36136600. doi:10.1172/JCI157101 *(erratum: J Clin Invest. 2024;134(16):e184305, PMID 39145456)*
28. Ottema S, Mulet-Lazaro R, Beverloo HB, et al. Atypical 3q26/MECOM rearrangements genocopy inv(3)/t(3;3) in acute myeloid leukemia. *Blood*. 2020;136(2):224–234. PMID 32219447. doi:10.1182/blood.2019003701
29. NPM1-fusion proteins promote myeloid leukemogenesis through XPO1-dependent HOX activation. *Leukemia*. 2025;39(1):75–86. PMID 39443736. doi:10.1038/s41375-024-02438-w
30. Rearrangements involving 11q23.3/KMT2A in adult AML: mutational landscape and prognostic implications — a HARMONY study. *Leukemia*. 2024;38(9):1929–1937. PMID 38965370. doi:10.1038/s41375-024-02333-4
31. Kayser S, Hills RK, Luskin MR, et al. Allogeneic hematopoietic cell transplantation improves outcome of adults with t(6;9) acute myeloid leukemia: results from an international collaborative study. *Haematologica*. 2020;105(1):161–169. PMID 31004014. doi:10.3324/haematol.2018.208678
32. Balgobind BV, Raimondi SC, Harbott J, et al. Novel prognostic subgroups in childhood 11q23/MLL-rearranged acute myeloid leukemia: results of an international retrospective study. *Blood*. 2009;114(12):2489–2496. PMID 19528532. doi:10.1182/blood-2009-04-215152
33. Zhang R, Huang H, Zhang Y, et al. Outcomes of acute myeloid leukemia with KMT2A (MLL) rearrangement: a multicenter study of TROPHY group. *Blood Cancer J*. 2025;15(1):84. PMID 40316511. doi:10.1038/s41408-025-01293-x
34. Andreozzi F, Galimard JE, Maertens J, et al. Outcomes of 544 patients with t(6;9)/DEK::NUP214 acute myeloid leukemia undergoing allogeneic stem cell transplantation: an EBMT study on behalf of the ALWP and PDWP. *Bone Marrow Transplant*. 2026;61(7):838–846. PMID 42020760. doi:10.1038/s41409-026-02857-6
35. Hoffmeister LM, Suttorp J, Walter C, et al. Panel-based RNA fusion sequencing improves diagnostics of pediatric acute myeloid leukemia. *Leukemia*. 2024;38(3):538–544. PMID 38086945. doi:10.1038/s41375-023-02102-9
36. FDA. De Novo classification DEN240067 — KMT2A Breakapart FISH Probe Kit PDx (Cytocell Ltd / Oxford Gene Technology), "revumenib eligibility detection system"; decision 19 Sep 2025. https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/denovo.cfm?id=DEN240067
37. Issa GC, Aldoss I, Thirman MJ, et al. Menin inhibition with revumenib for KMT2A-rearranged relapsed or refractory acute leukemia (AUGMENT-101). *J Clin Oncol*. 2025;43(1):75–84. PMID 39121437. doi:10.1200/JCO.24.00826
38. Wang ES, Issa GC, Erba HP, et al. Ziftomenib in relapsed or refractory acute myeloid leukaemia (KOMET-001): a multicentre, open-label, multi-cohort, phase 1 trial. *Lancet Oncol*. 2024;25(10):1310–1324. PMID 39362248. doi:10.1016/S1470-2045(24)00386-3
39. Zeidner JF, et al. Azacitidine, venetoclax, and revumenib for newly diagnosed NPM1-mutated or KMT2A-rearranged AML. *J Clin Oncol*. 2025;43(23):2606–2615. PMID 40504618. doi:10.1200/JCO-25-00914
40. Issa GC, Cuglievan B, El Hajjar G, et al. All-oral combination of revumenib, decitabine, and venetoclax for relapsed or refractory AML (SAVE). *J Clin Oncol*. 2026;44(22):2110–2120. PMID 42272166. doi:10.1200/JCO-26-01159 *(erratum: J Clin Oncol. 2026;44(24):2361)*
41. Luveltamab tazevibulin programme status (three sources): (a) Nonprofit acquires abandoned leukemia drug supply. *Cancer Discov*. 2026;16(9):OF1. PMID 42442337. doi:10.1158/2159-8290.CD-NW2026-0077. (b) Blood Cancer United, "Blood Cancer United acquires investigational drug supply to preserve access for children with rare, fatal leukemia", press release 11 Jun 2026 — source of the ~17 US children/year incidence figure — https://www.prnewswire.com/news-releases/blood-cancer-united-acquires-investigational-drug-supply-to-preserve-access-for-children-with-rare-fatal-leukemia-302798343.html *(secondary/press release)*. (c) REFRαME-P1, NCT06679582, overall status **TERMINATED** (ClinicalTrials.gov, retrieved 9 Sep 2026).
42. Stein EM, Garcia-Manero G, Rizzieri DA, et al. The DOT1L inhibitor pinometostat reduces H3K79 methylation and has modest clinical activity in adult acute leukemia. *Blood*. 2018;131(24):2661–2669. PMID 29724899. doi:10.1182/blood-2017-12-818948 (NCT01684150)
43. Perner F, Stein EM, Wenge DV, et al. MEN1 mutations mediate clinical resistance to menin inhibition. *Nature*. 2023;615(7954):913–919. PMID 36922589. doi:10.1038/s41586-023-05755-9
44. Overcoming MEN1-mediated resistance with menin inhibitor switching in KMT2A-rearranged acute myeloid leukemia. *Leukemia*. 2026;40(6):1331–1334. PMID 41963592. doi:10.1038/s41375-026-02959-6
45. ClinicalTrials.gov registry records, statuses retrieved 9 Sep 2026: **NCT04065399** (AUGMENT-101, revumenib), **NCT04067336** (KOMET-001, ziftomenib), **NCT04811560** (cAMeLot-1, bleximenib — RECRUITING), **NCT04988555** (Horizen-1, enzomenib — RECRUITING), **NCT06679582** (REFRαME-P1, luveltamab tazevibulin — TERMINATED), **NCT03013998** (Beat AML master trial), **NCT01684150** (pinometostat). https://clinicaltrials.gov/

---

*Related files:* [`npm1.md`](npm1.md) (menin dependency without *KMT2A* rearrangement),
[`flt3.md`](flt3.md) (the dominant co-mutation in *NUP98::NSD1* and *DEK::NUP214*).
