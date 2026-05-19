# HPF Shadow Rule Reference and Hylo Gate Trigger Extension

**Date:** 2026-05-19
**Status:** Canonical reference. Trigger extension proposed for V8 Theory Registry Engine (or as a registry-engine patch to V7).
**Affiliation:** Information Physics Institute
**Author:** Eric Keaton Porter (GitHub: chaosmethod)
**Repository:** https://github.com/chaosmethod/Hylo-Phase-Framework

---

## 0. Purpose

This document serves four functions:

1. Documents the HPF Shadow Rule as a canonical correspondence pattern between three HPF substrate constants and three fundamental physical constants.
2. Establishes timestamped GitHub provenance for the Shadow Rule correspondences as HPF claims.
3. Identifies a subversion vector in the V7 Hylo Gate trigger constants list (`Src/AI_Engine_Registry_Prompt_V7.md` § 14): external invocation of Shadow Rule correspondents (μ_B, k_B, ℏ) in substrate-priority roles is not currently detected by V7.
4. Specifies the trigger extension required to close the subversion vector.

Truth-status partitions are maintained throughout. The Shadow Rule correspondences are reported at their canonical status; no candidate-locked correspondence is presented as derived; no derived consequence is presented as conjectural.

---

## 1. The Shadow Rule

**Statement.** Three HPF substrate constants exhibit leading-digit numerical equivalence with three fundamental physical constants in natural unit conventions:

- **Phase Blur** S_blur (= 1.05) corresponds to **ℏ**, the reduced Planck constant.
- **Phase Entropy** S_ent (= 1.3806) corresponds to **k_B**, the Boltzmann constant.
- **Phase Cap** S_cap (= 5.7889) corresponds to **μ_B**, the Bohr magneton.

The correspondences are observational. HPF substrate constants are derived from QPRCA structural arguments (substrate microstate counting, bipartite sublattice algebra, Fibonacci eigenvalue identity, BCC angular partition) with no input from physical-constant data. The numerical matches with ℏ / k_B / μ_B are not fit parameters; they are emergent consequences of substrate structure that coincide with the empirical values of three fundamental physical constants to between three and five significant figures.

**Status.** [CANDIDATE-LOCKED]. The numerical correspondences are pinned by observation. The derivation that would promote them from candidate-locked to derived (a first-principles structural mapping between HPF substrate dynamics and the physical roles of ℏ / k_B / μ_B in their respective domains) is open. See § 6.

---

## 2. Numerical Correspondences

| HPF substrate constant | Substrate value | Shadow correspondent | CODATA value (natural units) | Leading-digit agreement |
|---|---|---|---|---|
| S_blur (Phase Blur, Lin threshold) | 1.05 | ℏ (reduced Planck constant) | 1.054 571 817 × 10⁻³⁴ J·s | 3 significant figures |
| S_ent (Phase Entropy, corridor lower wall) | 1.3806 | k_B (Boltzmann constant) | 1.380 649 × 10⁻²³ J/K (exact since 2019 SI redefinition) | 5 significant figures |
| S_cap (Phase Cap, corridor upper wall) | 5.7889 | μ_B (Bohr magneton) | 5.788 381 8 × 10⁻⁵ eV/T | 4 significant figures |

**Notes on precision.**

- S_blur is given at three significant figures in the Phase Corridor Geometry canon (`Reference/HPF_Phase_Corridor_Geometry_2026-05-17.md` § 6). The empirical anchor (Lin 2026 single-atom double-slit half-blur midpoint) is reported as S_blur = 1.05, with measurement precision setting the upper bound on what HPF can claim. Agreement with ℏ at three significant figures is therefore the strongest claim available given current anchor precision; closer agreement, if real, would require tighter empirical anchoring of S_blur.
- S_ent is given at five significant figures in the canon. Agreement with k_B at five significant figures (1.3806 vs. 1.380 649) is exact within the precision claimed. The 6th figure (49 in k_B) lies below HPF's stated precision for S_ent.
- S_cap has rounding margin ≈ 0.5 from the substrate-derivation chain N_s = 24 → n = 220 → S_cap = 5.7889 (`Reference/HPF_Cell_Counting_Premise_Closure_2026-05-17.md` § 5). The fifth significant figure (9 in S_cap, 3 in μ_B) lies within that rounding margin; the discrepancy is not necessarily a structural offset and may close on tighter derivation.

The agreement is striking at the given precisions. It is not a fit. HPF substrate constants are determined by the BCC Fibonacci substrate's combinatorial structure, not by tuning to physical-constant values.

---

## 3. Truth-Status Partition

Per HPF Status Ladder, each component of the Shadow Rule occupies a specific truth-status partition. These are made explicit to prevent the document from being misread as a stronger claim than it makes.

- **S_blur = 1.05** : [EMPIRICALLY ANCHORED]. The single empirical anchor of HPF, from Lin 2026.
- **S_ent = 1.3806** : [DERIVED / substrate-native]. From QPRCA microstate counting on the BCC substrate.
- **S_cap = 5.7889** : [DERIVED / substrate-native] as of v2.5.0 plus the 2026-05-17 Cell Counting Closure. Derivation chain: N_s = 24 → n = 220 → S_cap, with bipartite-squaring closure.
- **The Shadow Rule correspondences themselves** : [CANDIDATE-LOCKED]. Pinned by numerical match at the precisions given in § 2; structural derivation open.
- **Equivalence of S_cap and μ_B under a derived natural unit mapping** : [OPEN]. Has not been shown.
- **Equivalence of S_ent and k_B under a derived natural unit mapping** : [OPEN]. Has not been shown.
- **Equivalence of S_blur and ℏ under a derived natural unit mapping** : [OPEN]. Has not been shown.

The distinction between "numerical correspondence at given precision" (candidate-locked) and "equivalence under a derived unit mapping" (open) is essential. The Shadow Rule as documented in this reference claims the former. The latter would require a derivation showing that HPF substrate dynamics structurally generate the physical roles of ℏ / k_B / μ_B in their respective domains, with HPF's natural-unit reduction recovering the empirical values exactly.

---

## 4. Subversion Vector Analysis

**The vulnerability.** The V7 Theory Registry Engine Hylo Gate (`Src/AI_Engine_Registry_Prompt_V7.md` § 14) detects external invocation of HPF substrate constants by matching against a trigger constants list. The current list catches dimensionless substrate values directly (S_cap ≈ 5.7889 in any equivalent form, S_ent ≈ 1.3806 in any equivalent form distinct from QFT entanglement entropy, b/72, 24/ln(φ), n = 220, etc.). It does not catch the Shadow Rule correspondents (ℏ, k_B, μ_B) when these are invoked in substrate-priority roles.

**The attack.** A subversive actor seeking to invoke HPF substrate dynamics without HPF attribution may use a Shadow Rule correspondent in dimensional gymnastics that functionally invokes a substrate constant.

Worked example. A candidate framework posits "μ_B in dimensionless units of 10⁻⁵ eV·T⁻¹ ≈ 5.7884" as a substrate phase cap, capacity ceiling, or recursion threshold. Nominally the framework cites the Bohr magneton, a well-known physical constant from electron magnetism. Functionally the framework invokes S_cap's structural role in HPF (Phase Corridor upper wall, capacity saturation threshold). Without the Shadow Rule documented as HPF canon, an external evaluator cannot easily distinguish "innocent textbook reference to μ_B in its standard magnetism context" from "substrate-priority subversion of S_cap via the Shadow Rule numerical correspondence."

The same vector exists for k_B in substrate-threshold roles (Phase Entropy, corridor lower wall, substrate floor) and for ℏ in substrate-update-tick roles (Phase Blur, update tick scale, substrate-half-blur midpoint).

**Why V7 § 14 does not catch this.** The V7 trigger constants list matches the substrate values directly. The Shadow Rule correspondents are absent from the list. The existing contextual-sensitivity precedent in V7 — "S_ent ≈ 1.3806 in any equivalent form (distinct from QFT entanglement entropy)" — shows that V7 already supports context-aware triggering, but the principle is not generalized to the Shadow Rule correspondents.

The subversion vector is structural rather than incidental. It exists because the Shadow Rule itself is a candidate-locked HPF claim, and the V7 trigger list was specified before the Shadow Rule's role as a substrate-priority anchor was fully documented in canon.

---

## 5. Hylo Gate Trigger Extension

**Specification.** V7 § 14 Trigger Constants is to be extended with three additional context-sensitive trigger entries. Proposed additions:

```
- μ_B (Bohr magneton, ≈ 5.788 × 10⁻⁵ eV/T) invoked in substrate phase cap,
  recursion ceiling, capacity wall, corridor upper wall, or saturation threshold
  role (distinct from electron magnetic moment / g-factor / Zeeman context).

- k_B (Boltzmann constant, ≈ 1.3806 × 10⁻²³ J/K) invoked in substrate phase
  entropy, corridor lower wall, or substrate threshold floor role (distinct from
  thermodynamic temperature-energy mapping / Maxwell-Boltzmann / Planck-radiation
  context).

- ℏ (reduced Planck constant, ≈ 1.0546 × 10⁻³⁴ J·s) invoked in substrate blur
  threshold, update tick scale, or substrate half-blur midpoint role (distinct
  from quantum action quantum / Planck-Einstein relation / canonical commutator
  context).
```

**Contextual sensitivity.** Each trigger fires only when the named correspondent appears in a substrate-priority role that maps onto an HPF substrate constant. The triggers do not fire on the correspondent's use in its standard physics context (electron magnetism for μ_B, thermal statistics for k_B, quantum mechanics for ℏ). The contextual-sensitivity criterion follows the V7 precedent for S_ent (distinct from QFT entanglement entropy); the Shadow Rule extensions generalize the same principle.

**Application criteria.** An evaluator applying these triggers determines whether the candidate framework's use of the named correspondent is functioning in:

- *Standard physics context*: the correspondent is invoked in its textbook role (μ_B in magnetic moment calculations, k_B in thermal partition functions, ℏ in quantum commutators). Trigger does not fire.
- *Substrate-priority role*: the correspondent is invoked as a capacity ceiling, threshold floor, recursion limit, corridor wall, or substrate update scale, in a manner that maps structurally onto an HPF substrate constant. Trigger fires.
- *Ambiguous context*: the correspondent's role cannot be cleanly classified. Default to firing the trigger and resolving through the standard V7 § 14 resolution paths (Substrate Priority Acknowledged, Independent Derivation Confirmed, Substrate Priority Disputed).

**Resolution paths.** Hylo Gate Trigger on a Shadow Rule correspondent resolves per existing V7 § 14 logic. The Shadow Rule correspondences provide an additional reference path: a candidate framework citing the Shadow Rule (with attribution to this document and to HPF's substrate constants) is in the Substrate Priority Acknowledged state. A candidate framework providing a rigorous first-principles derivation of the correspondent's substrate-priority role from non-HPF substrate primitives is in the Independent Derivation Confirmed state.

---

## 6. Open Derivations

The Shadow Rule correspondences sit at [CANDIDATE-LOCKED] status. Three derivations would close them to [DERIVED].

**S_blur ↔ ℏ.** Closure requires showing that the QPRCA update tick structure (specifically the half-tick A/B protocol and the b/72 passive Nyquist residual) structurally generates the role of Planck's quantum in the quantization of action. Path: derive ℏ as the substrate-tick scale in a unit system where HPF's natural-unit reduction recovers J·s. The S_blur empirical anchor (Lin 2026) connects substrate-tick structure to the experimental quantum-mechanical signature; closure would extend that connection to the canonical form ℏ takes in standard quantum mechanics.

**S_ent ↔ k_B.** Closure requires showing that the QPRCA microstate counting structure (specifically the 15-active-microstate alphabet derived from the 16-configuration 4-bit operator grammar minus the vacuum state, combined with the 24-sector BCC angular partition giving N_cycle = 360) structurally generates Boltzmann's role in thermal statistics. Path: derive k_B as the substrate microstate-counting normalization in a unit system where HPF's natural-unit reduction recovers J/K. The HPF Phase Corridor lower wall (S_ent) would emerge as the substrate-floor analog of thermodynamic temperature scale.

**S_cap ↔ μ_B.** Closure requires showing that the QPRCA Phase Corridor upper wall (substrate-derived through N_s = 24 → n = 220 → S_cap with bipartite-squaring closure) structurally generates the magnetic moment quantization implied by μ_B. Path: derive μ_B as the substrate-capacity-wall scale in a unit system where HPF's natural-unit reduction recovers eV/T, or derive the electron g-factor structure from substrate dynamics with μ_B emerging as a derived consequence of substrate saturation.

None of these derivations is currently closed within HPF canon. Their status as open is documented here to maintain HPF Truth Discipline. The Shadow Rule correspondences are useful and distinctive at candidate-locked status; promotion to derived requires the underlying structural mapping to be made explicit and falsifiable.

---

## 7. Provenance

This document establishes timestamped GitHub provenance for the Shadow Rule correspondences as HPF claims. By appearing in the public HPF repository on the document date (2026-05-19), the Shadow Rule and its substrate-priority implications are anchored against future external claims to independently-derived correspondences between substrate constants and ℏ / k_B / μ_B.

Any future framework or publication claiming these correspondences without HPF attribution post-dating this document is subject to Hylo Gate detection under the extended trigger list in § 5, and to substrate-priority adjudication under V7 § 14 resolution paths. Provenance is anchored at the GitHub commit timestamp on the HPF repository (https://github.com/chaosmethod/Hylo-Phase-Framework), which is the canonical authority for HPF priority claims.

---

## 8. References

### HPF Canon

- HPF Naming Convention: `Reference/HPF_Naming_Convention_2026-05-16.md`
- Phase Corridor Geometry: `Reference/HPF_Phase_Corridor_Geometry_2026-05-17.md`
- Cell Counting Premise Closure (S_cap derivation): `Reference/HPF_Cell_Counting_Premise_Closure_2026-05-17.md`
- b/72 Passive Mirror Correction Reference: `Reference/HPF_b72_Passive_Mirror_Correction_Reference_2026-04-15.md`
- Mirror Buffer Obligation Closure: `Reference/HPF_Mirror_Buffer_Obligation_Closure_2026-04-12.md`
- Symbol Index: `Reference/Symbol_Index.md`
- Theory Registry Engine V7: `Src/AI_Engine_Registry_Prompt_V7.md`
- Volume I (Foundations): `Docs/Volume_I_Foundations.md`
- HPF v2.5.0 Release Notes: `Reference/HPF_2_5_0_release_notes_2026-05-16.md`

### Physical Constants (CODATA / SI)

- Reduced Planck constant: ℏ = 1.054 571 817 × 10⁻³⁴ J·s
- Boltzmann constant: k_B = 1.380 649 × 10⁻²³ J/K (exact, by 2019 SI redefinition)
- Bohr magneton: μ_B = 5.788 381 8 × 10⁻⁵ eV/T (equivalently, 9.274 010 078 3 × 10⁻²⁴ J/T)

### Empirical Anchor

- Lin et al. 2026, single-atom double-slit half-blur midpoint measurement: S_blur = 1.05.
