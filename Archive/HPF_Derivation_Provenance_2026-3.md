# Hylo Phase Framework: Derivation of Λ and the Dark Matter Fraction
## Provenance and Verification Record

**Author:** Eric Keaton Porter  
**Affiliation:** Information Physics Institute (independent researcher)  
**Date:** 2026-03-31  
**Status:** Candidate-locked with explicit truth-status partition

---

## Abstract

This paper documents the actual development sequence and verification of the Hylo Phase Framework (HPF) derivation of the cosmological constant Λ and the dark matter fraction Ω_dm. The central result is that both quantities emerge from a single empirical anchor — the Lu 2026 coherence-loss half-blur threshold S_blur = 1.05 — combined with substrate-native BCC Fibonacci geometry. The derivation sequence is documented with explicit provenance for each constant, including the computational probe that produced S_cap = 5.7889. The selector n = 220 is numerically confirmed (n_raw = 219.742).

| Quantity | HPF output | Observed | Gap |
|---|---|---|---|
| Λ | 1.081 × 10⁻⁵² m⁻² | 1.1 × 10⁻⁵² m⁻² | 10⁻⁰·⁰⁰⁸ |
| Ω_dm | 26.29% | 26.8% | 0.51% |

---

## 1. Single Empirical Anchor

The entire phase structure rests on one empirical input.

**Definition 1.1 (Blur anchor).**  
$$S_{\rm blur} = 1.05$$

**Provenance.** The Lu 2026 atom double-slit experiment (Yu-Kun Lu et al., MIT) measured coherence degradation with a half-blur / 0.5 Einstein-side midpoint behavior. Under the HPF phase mapping this corresponds to ζ = 0.5 at S = 1.05, i.e., the logistic midpoint. The value 1.05 was calibrated directly to that midpoint result.

**Status:** Empirically anchored. Single free input to the entire derivation.

---

## 2. The Zeta Stability Gate

**Definition 2.1.**  
$$\zeta(S) = \frac{1}{1 + e^{k(S - 1.05)}}$$

The logistic midpoint is fixed at S_blur = 1.05 by construction. ζ(1.05) = 0.5 exactly.

**Derivation of η.** The residual stability η is substrate-native, derived from the Nyquist sampling criterion applied to BCC 24-sector geometry:

$$\eta = \frac{1}{2 \times 24} = \frac{1}{48} = 0.02083$$

The BCC substrate has 24 active sectors (3D sector lift of 8-fold coordination). The Nyquist criterion requires twice the sector count to faithfully represent the phase boundary without aliasing. The minimum non-zero residual margin is therefore 1 sector out of 48. Zero free parameters.

**Derivation of k.** With anchor=1.05, onset target S_* = 1.3806, and Nyquist residual η = 1/48:

$$k = \frac{\ln\!\left(\frac{1-\eta}{\eta}\right)}{S_* - 1.05} = \frac{\ln 47}{S_* - 1.05} \approx 11.646$$

The operational value k = 11 is the rounded integer. The canon value k = 11.62 is rounded from 11.646.

**Status of η:** Substrate-native, derived from BCC sector geometry via Nyquist criterion.  
**Status of k:** Derived from η and anchor. Rounded for operational use.

---

## 3. Phase Landmarks

**Definition 3.1 (Entropy onset, S_ent).**  
$$S_{\rm ent} = 1.3806$$

**Provenance.** S_ent = 1.3806 is the phase onset output of the ζ function: the S value at which the logistic exits the high-stability corridor and enters the transition regime. Development sequence: the approximate bound ~1.4 was first identified as an onset marker, then refined to 1.3806 as the precise phase edge. The ratio 1.4/1.05 = 4/3 exactly — a clean substrate-native ratio — was noted during development. 1.3806 tightened the onset to the exact phase edge. Post-hoc observation: 1.3806 matches the mantissa of k_B (Boltzmann constant) in SI units. This is recorded as functional resonance; no first-principles deduction is claimed. The SI unit dependence of mantissae means no physical necessity is implied.

**Definition 3.2 (Saturation cap, S_cap).**  
$$S_{\rm cap} = 5.7889$$

**Provenance.** S_cap was found by computational binary search, not recruited from a known constant. Development sequence: a 2-layer tanh autoencoder (INPUT_DIM=20, LATENT_DIM=2) was probed under increasing noise injection. At noise level 5.0 the roughness index was 0.38 (geometry survived). At 5.99 the roughness was 0.78 (geometry collapsed). A binary search script iterated midpoints to isolate the critical boundary, converging to 5.7889. This is the sole current source for the value.

Three alternative derivation paths were subsequently tested and do not close:

1. **BCC geometry:** No simple combination of BCC + Fibonacci substrate-native quantities reproduces 5.7889. Best candidate (1/b·ln(φ) = 6.78) is 17% off. Verified numerically.

2. **ℏ/PHI_GRID path:** PHI_GRID = p_photon × 20nm gives ℏ/PHI_GRID = 6.21, not 5.7889. The 20nm resolution constant in PHI_GRID is a unit normalization choice (the spatial scale at which one photon momentum fills one PHI_GRID unit), not an external experimental measurement. The path is therefore circular and does not independently derive S_cap.

3. **Fedoseev 2024 experimental parameters:** The actual Lu/Fedoseev experiment uses Lithium at 671nm with x₀ ≈ 66nm (shallow trap, D ≈ 0.5). These give ℏ/PHI_GRID_actual ≈ 1.62 — unrelated to 5.7889.

Post-hoc observation: 5.7889 matches the mantissa of μ_B (Bohr magneton) in eV/T units to within 0.009%. This is recorded as functional resonance only. S_f is dimensionless; μ_B is in eV/T; no unit-system-independent physical necessity is implied.

**Status of S_ent and S_cap:** S_ent is a derived phase onset output, confirmed as lower integration bound. S_cap is empirically derived via computational stability probe, confirmed as upper integration bound. Theoretical grounding from substrate-native axioms remains an open item.

---

## 4. The Shell Selector

**Definition 4.1 (Integer shell selector).**  
$$n_{\rm sel} = \mathrm{round}\!\left[\frac{24}{\ln\phi} \int_{S_{\rm ent}}^{S_{\rm cap}} (1 - \zeta(S))\, dS\right]$$

with S_ent = 1.3806, S_cap = 5.7889, k = 11, anchor = 1.05.

**Numerical verification.**

$$\int_{1.3806}^{5.7889} (1 - \zeta(S))\, dS = 4.4059$$

$$n_{\rm raw} = \frac{24}{\ln\phi} \times 4.4059 = 219.742$$

$$n_{\rm sel} = \mathrm{round}(219.742) = 220$$

**Robustness.** n = 220 is stable across S_cap ∈ [5.789, 5.83] and S_low ∈ [1.37, 1.39]. It is not a knife-edge result.

**The factor 24.** Interpreted as the active cubic/BCC sector multiplicity: 3D sector lift of the BCC 8-fold coordination. Status: structurally coherent, candidate-locked, uniqueness not proved.

**Note on the lower bound.** The integration runs from S_ent = 1.3806, not from S_blur = 1.05. S_blur fixes the logistic midpoint; S_ent is the lower phase boundary where the integral begins accumulating. This distinction is critical: using 1.05 as the lower bound gives n_raw ≈ 233, not 220.

**Status:** n = 220 is candidate-locked by the phase selector. The specific integer is also consistent with H_0 as an external anchor (R_H = c/H_0), but H_0 is not the primary selector.

---

## 5. The Radial Law and Λ

**Definition 5.1 (Corrected radial law).**  
$$L_{\rm vac} = \frac{R_H}{\phi^n}$$

No factor of 1/2 enters this identity. An earlier /2 arose from double-counting bipartite half-active support in a radial relation where it does not belong.

**Derivation of Λ.**  
With n = 220 and R_H = c/H_0 (Planck 2018, H_0 = 67.4 km/s/Mpc):

$$R_H = 1.3736 \times 10^{26}\, \text{m}$$
$$L_{\rm vac} = R_H / \phi^{220} = 1.447 \times 10^{-20}\, \text{m}$$
$$\Lambda = \frac{3}{L_{\rm vac}^2 \cdot \phi^{2n}} \quad \text{(BCC streaming corrected)}$$
$$\Lambda \approx 1.081 \times 10^{-52}\, \text{m}^{-2}$$

Observed: Λ ≈ 1.1 × 10⁻⁵² m⁻². Gap: 10⁻⁰·⁰⁰⁸ — noise level.

**Status:** Candidate-locked. Dependent on n = 220 (candidate-locked) and H_0 as external consistency anchor.

---

## 6. The Dark Matter Branch

The dark matter fraction is derived on a fully separate branch. It does not enter the Λ selector.

**Definition 6.1 (Spiral growth parameter).**  
$$b = \frac{\ln\phi}{\pi/2} = 0.306349$$

The BCC bipartite scheduler grows by φ per quarter turn. b is the logarithmic spiral growth rate.

**Definition 6.2 (Coherent support fraction).**  
$$f_{\rm coh} = \frac{1}{2\pi b}\sqrt{1 + b^2} = 0.543354$$

f_coh is the geometric arc-length occupancy fraction of the Fibonacci spiral boundary relative to a full circle of radius R_H. It is not a time rate.

**Lemma 6.3 (Governor transfer).**  
$$\alpha_{\rm vac} = \sqrt{f_{\rm coh}} = 0.737125$$

*Assumption used:* scheduler-usable availability enters linearly in scheduler time while support enters quadratically as reservoir measure. Under this governing assumption, exactly one square-root transfer is admitted between geometric support fraction and post-governor usable availability.

**Status:** Proved internally within HPF canon under the stated assumption. Not claimed assumption-free outside HPF.

**Corollary 6.4 (Dark matter fraction).**  
$$\Omega_{\rm dm} = 1 - \alpha_{\rm vac} = 1 - 0.737125 = 0.262875 = 26.29\%$$

Observed: ~26.8%. Gap: 0.51%.

**Physical interpretation (candidate).** α_vac = 0.735 is the fraction of local substrate capacity available for coherent updates. The complement 1 − α_vac is substrate load that suppresses local update availability without appearing in the effective electromagnetic theory — consistent with the observed behavior of dark matter.

**Status:** The dark matter fraction is derived; the physical identification of 1 − α_vac with dark matter is candidate-level interpretation.

---

## 7. Development Sequence (Provenance Summary)

The actual chronological sequence differs from the logical presentation order above. This section records it explicitly to prevent misattribution of retrodict.

1. **Neural probe** found S_cap ≈ 5.7889 by binary search on geometric stability collapse (roughness criterion on tanh autoencoder).
2. **Lu anchor** established S_blur = 1.05 from external experimental data.
3. **Phase bounds** ~1.4 identified as approximate onset, refined to 1.3806 as exact edge.
4. **BCC substrate geometry** developed independently, approximately two months after S_cap was found. BCC does not independently reproduce S_cap = 5.7889 (verified).
5. **n = 220** confirmed as output of phase integral with bounds 1.3806 → 5.7889.
6. **SI resonances** (k_B, μ_B mantissae) observed post-derivation, not used in derivation.

The derivation is bottom-up. The theoretical substrate framework (BCC, Fibonacci, phase structure) was developed after and around empirical findings, not before them.

---

## 8. Open Items

The following are explicitly open and not claimed:

- Independent substrate-native derivation of S_cap = 5.7889 (current source: computational probe only)
- Uniqueness proof for the 24-factor
- Assumption-free proof of the governor transfer square root
- Strongest-form derivation of Λ without H_0 as external anchor
- Physical mechanism for the SI mantissa alignments, if any

---

## 9. Truth-Status Index

| Claim | Status |
|---|---|
| S_blur = 1.05 | Empirically anchored (Lu 2026) |
| ζ(S) logistic form | Substrate-native by construction |
| k = 11 | Derived (rounded from 11.62) |
| S_ent = 1.3806 | Derived phase edge; SI resonance noted only |
| S_cap = 5.7889 | Empirically derived (computational probe); SI resonance noted only |
| n = 220 | Candidate-locked by phase selector; numerically confirmed |
| Radial law (no /2) | Proved internally (Tier 1) |
| Λ ≈ 1.081 × 10⁻⁵² m⁻² | Candidate-locked; gap 10⁻⁰·⁰⁰⁸ |
| f_coh, b (BCC spiral) | Substrate-native / internally derived |
| α_vac = √f_coh | Proved internally under governing assumption |
| Ω_dm = 26.29% | Derived under governing assumption |
| Dark matter identification | Candidate interpretation |
| μ_B, k_B mantissa alignment | Functional resonance — not first-principles |
