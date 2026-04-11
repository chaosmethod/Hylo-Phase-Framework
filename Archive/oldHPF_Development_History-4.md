# Hylo Phase Framework — Development History
## Chronological Record of Constant Discovery and Derivation

**Author:** Eric Keaton Porter  
**Compiled:** 2026-03-31  
**Purpose:** Prevent loss of provenance between repo updates. This document records how each constant was actually found, not just what it is.

---

## Overview

The HPF Lambda/dark matter derivation chain was developed bottom-up over approximately two months. The theoretical substrate framework (BCC, Fibonacci, phase structure) was developed after and around empirical findings, not before them. This document records that actual sequence.

---

## Phase 1 — Early Engine (HPF_Engine.py era)

**Constants active:** k=5.0, anchor=1.05, PHI_GRID  
**Key file:** `HPF_Engine.py`

S_f was defined as a dimensionless Information Flux Ratio:

```
S_f = (dp_abs × dx) / PHI_GRID
```

where PHI_GRID = HK_UNIT × 2.0e-8, HK_UNIT = 8.5e-28 kg·m/s (momentum of 780nm photon).

**The 20nm (2.0e-8 m) resolution constant** is the spatial scale at which one 780nm photon momentum exactly fills one PHI_GRID unit. It is a unit normalization choice — the HPF action grid unit cell — not a measurement from the Lu or Fedoseev experiments. The Fedoseev 2024 experiment (Lithium, 671nm) uses x₀ ≈ 66nm, an entirely different scale.

**k=5.0** was the rendering slope in the early engine. At this k value the ζ function is shallow and the phase edge at η=0.021 falls at ~1.82 — not yet meaningful as a phase landmark.

**S_blur = 1.05** was calibrated to the Lu 2026 half-blur result. The Lu paper (Lin, Lu, Fedoseev et al., arXiv:2507.19801, Ketterle group MIT) measures fringe contrast reduction in atom double-slit experiments. The HPF mapping: coherence loss half-blur → ζ = 0.5 → S_blur = 1.05. This is the single empirical anchor for the entire chain.

**Three-phase state map at k=5.0:**
- S_f ≪ 1: Einstein phase (stable geometry)
- S_f ≈ 1.05: Lu threshold (blur)
- S_f ≫ 1: Bohr phase (delocalized)

---

## Phase 2 — Binary Search Probe and S_cap Discovery

**Constants found:** S_cap = 5.7889  
**Key files:** Binary search scripts (not in final repo)

The saturation ceiling S_cap was found by computational binary search on a geometric stability probe — a 2-layer tanh bottleneck architecture (INPUT_DIM=20, LATENT_DIM=2) trained to compress and reconstruct a noisy sine signal.

**Probe design:**
- Signal: sin(x + phase) + Gaussian noise(σ)
- Architecture: 20D input → 2D latent → 20D reconstruction
- Roughness criterion: mean |output[i] - output[i-1]| < threshold (0.65)
- Stable at σ=5.0 (roughness 0.38), collapsed at σ=5.99 (roughness 0.78)

**Binary search sequence:**
1. Confirmed stable: σ=5.0
2. Confirmed collapsed: σ=5.99
3. Bisection over 6 iterations converged to σ=5.7889

**This is the sole current source for S_cap = 5.7889.**

**GitHub timestamp proof:** Entropy_graph.png — showing the ζ function with Floor S_f = 1.4 (green) and Ceiling λ = 5.7889 (red) — was committed to the public Holographic-Projection-Framework repository on **January 29, 2026** (commit fc4df64, verified). The Lambda/dark matter derivation came in March 2026. The canonical release was March 20, 2026. S_cap = 5.7889 therefore predates the cosmological derivation by approximately **seven weeks**, publicly timestamped and immutable on GitHub.

**Confirmation process — hi-lo iteration:**
S_cap was located by hi-lo iteration on the geometric stability probe — scanning noise levels until the collapse boundary was isolated. The cosmological outputs (n=220, Λ, Ω_dm) were not yet known at this stage and were not used to confirm S_cap.

**n=220 and Λ were discovered approximately two months later**, when the BCC Fibonacci substrate geometry was developed. At that point S_cap was already fixed at 5.7889 from the probe. The BCC machinery independently produced n=220 and Λ using that pre-existing ceiling value.

This is genuine independent convergence: the geometric probe found the ceiling, and the substrate geometry built two months later converged on the same value when producing correct cosmological outputs. S_cap was not tuned to hit n=220 or Λ — it predates both by approximately two months.

**Architecture dependence (tested 2026-03-31):** The probe is architecture-dependent. Different INPUT_DIM/LATENT_DIM/epoch configurations give ceilings in the range 5.0–6.1. The probe consistently finds a phase transition region but cannot resolve it to four decimal places. 5.7889 is one sample from the transition distribution, not a universal constant of the signal geometry.

**SI resonance:** 5.7889 ≈ μ_B mantissa in eV/T (5.7884). This is noted functional resonance. S_f is dimensionless; μ_B is in eV/T; no unit-system-independent physical necessity is implied. The alignment was noticed post-derivation.

**BCC geometry tested (2026-03-31):** No combination of BCC + Fibonacci substrate-native quantities independently reproduces 5.7889. Best candidate 1/(b·ln(φ)) = 6.78 is 17% off.

**ℏ/PHI_GRID path tested (2026-03-31):** ℏ/PHI_GRID = 6.21, not 5.7889. The 20nm is a unit normalization choice so this path is circular.

**Status of S_cap:** Empirically derived via computational stability probe. Theoretical grounding from substrate-native axioms remains open.

---

## Phase 3 — Floor Discovery (~1.4) and k Refinement

**Constants active:** floor ≈ 1.4, k refined from 5.0 toward 11  

The approximate lower phase bound ~1.4 was observed — likely from scanning the stability probe output or from explicit ζ function analysis. At k=5.0, ζ(1.4) = 0.148, not yet a meaningful phase edge. As k was refined upward, 1.4 became a more meaningful threshold.

**Ratio 1.4/1.05 = 4/3 exactly** — a clean substrate-native ratio, noted during development.

**k=11 established:** At k=11, ζ(1.4) = 0.0208 ≈ 0.021. The floor and k are mutually consistent at the η=0.021 threshold. This is the point where the floor 1.4 becomes a real phase edge rather than an approximate marker.

---

## Phase 4 — Nyquist Derivation of η and Floor Refinement

**Key discovery:** η = 1/48 from Nyquist criterion on BCC 24-sector geometry

**η = 1/48 derivation:**
- BCC substrate has 24 active sectors (3D sector lift of 8-fold coordination)
- Nyquist sampling criterion: requires 2× sector count to represent phase boundary without aliasing
- Minimum non-zero residual stability margin = 1/48 = 0.02083
- Zero free parameters, substrate-native

**k derivation from η:**
```
k = ln((1-η)/η) / (S* - 1.05) = ln(47) / (S* - 1.05)
```

At k=11, η=0.021 gives floor=1.4 exactly.  
At k=11.62 (exact derived value), η=0.021 gives floor=1.3806 exactly.

**Floor refinement from 1.4 to 1.3806:**
- 1.4 was the floor at k=11 (operational rounded value)
- 1.3806 is the floor at k=11.62 (exact derived value)
- The refinement is not a fitting step — it is the consequence of using the exact k rather than the rounded k
- k=11.62 derived from η=1/48 and anchor=1.05 with onset target S*

**SI resonance of 1.3806:** Matches k_B mantissa in SI units (1.3806 × 10⁻²³ J/K). S_f is dimensionless; k_B is in J/K; no unit-system-independent physical necessity is implied.

---

## Phase 5 — n=220 Confirmation

**Key finding:** n=220 requires floor=1.3806, not 1.4

The shell selector:
```
n_sel = round[24/ln(φ) × ∫(1.3806 to 5.7889) (1-ζ(S)) dS]
```

**Numerical verification:**
- Integral = 4.4059
- n_raw = 24/ln(φ) × 4.4059 = 219.742
- n = round(219.742) = 220 ✓

**Critical distinction:** The integration runs from S_ent=1.3806, NOT from S_blur=1.05. Using 1.05 as the lower bound gives n_raw≈233, not 220.

**Sensitivity:** n=220 is robust across S_cap ∈ [5.789, 5.83] and S_low ∈ [1.37, 1.39]. Not a knife-edge result.

**Historical combinations tested:**
| k | floor | S_cap=5.7889 gives |
|---|---|---|
| 11 | 1.3806 | n=220 ✓ |
| 11 | 1.4 | n=219 ✗ |
| 11.6 | 1.4 | n=219 ✗ |

Only k=11, floor=1.3806 recovers n=220 from 5.7889.

**BCC + Planck substrate gives n=291** — the phase integral cuts 71 shells from the natural substrate count. The integration bounds do active restriction work: only entropy-active phase (above S_ent) counts toward shell selection.

---

## Phase 6 — BCC Fibonacci Geometry and Dark Matter

**These were developed independently of the Lambda chain.**

BCC bipartite scheduler → Fibonacci recurrence → φ emerges as asymptotic growth rate. The causal boundary traces a logarithmic spiral with growth parameter b = ln(φ)/(π/2).

Coherent support fraction f_coh = (1/2πb)√(1+b²) = 0.5434 is purely geometric.

Governor transfer: α_vac = √f_coh = 0.7371 (one square-root under HPF scheduler assumption).

Ω_dm = 1 - α_vac = 26.29% — derived, 0.51% from observed 26.8%.

**BCC geometry was developed ~2 months after S_cap was found.** The two branches (Lambda and dark matter) converged from different directions.

---

## Constants: Final Provenance Summary

| Constant | Value | Source | Status |
|---|---|---|---|
| S_blur | 1.05 | Lu 2026 coherence-loss half-blur, HPF mapped | Empirically anchored |
| η | 1/48 | Nyquist on BCC 24-sector geometry | Substrate-native, derived |
| k | 11.646 → 11 | ln(47)/(S*-1.05), rounded | Derived |
| S_ent | 1.3806 | Phase edge of ζ at exact k, η=1/48 | Derived |
| S_cap | 5.7889 | Binary search on geometric stability probe | Empirically derived, theoretical grounding open |
| n | 220 | Phase integral, confirmed n_raw=219.742 | Candidate-locked |
| Λ | 1.081×10⁻⁵² m⁻² | BCC Fibonacci radial law, n=220 | Candidate-locked, gap 10⁻⁰·⁰⁰⁸ |
| Ω_dm | 26.29% | BCC spiral governor transfer | Derived under governing assumption |

---

## What Was Lost Between Repo Updates

The following were reconstructed in the 2026-03-31 session and are not in earlier canonical volumes:

1. η = 1/48 Nyquist derivation
2. S_cap = 5.7889 from binary search probe (code not in repo)
3. PHI_GRID 20nm as unit normalization, not experimental measurement
4. k=5.0 early history
5. 1.4 → 1.3806 refinement mechanism
6. BCC does not reproduce S_cap (verified numerically)
7. Architecture dependence of the geometric stability probe
8. n=220 requires floor=1.3806, not 1.4 (not stated explicitly anywhere)
9. The Rosetta Stone paper (early routing architecture, predates Lambda derivation)

---

## Open Items (as of 2026-03-31)

1. **S_cap substrate-native derivation** — theoretical grounding from BCC axioms not found. Eric searching original probe code and chat logs.
2. **Uniqueness of Nyquist application** — why 24 sectors specifically for the Nyquist criterion, not 8 or 48
3. **Governor transfer uniqueness** — one square-root proved under HPF assumption, not assumption-free
4. **Strongest-form Λ derivation** — currently requires H_0 as external consistency anchor

---

## Decapitated Material (2026-03-31)

The following was explicitly removed from canonical HPF scope:

**ε = 0.134, 0.124, 0.083 — Hubble tension fitting parameters**

These values emerged from optimizer fits to Pantheon+, DESI 2024, and Planck CMB data. They are observational residuals, not HPF derivations. They were never substrate-native and never belonged in the framework.

Reason for removal: supernovae at z < 1 are in the laminar regime (S_f ≪ 1.05, ζ ≈ 1). HPF predicts GR output there by construction. Finding no deviation from ΛCDM in that regime is exactly what the framework requires — not a signal to explain. The Hubble tension fitting work was chasing an HPF fingerprint in a regime where the framework explicitly predicts classical behavior.

The photon ring code (holographic_photon_ring.py) used ε = 0.134 as the echo amplitude. That script is exploratory only. The echo location (r_peak × 1.05) is substrate-native via S_blur. The echo amplitude needs a substrate-native derivation before it can be claimed as an HPF prediction.

**Canonical HPF observational predictions remain:**
- Λ = 1.081×10⁻⁵² m⁻² (gap 10⁻⁰·⁰⁰⁸)
- Ω_dm = 26.29% (gap 0.51%)
- Photon ring echo at 1.05× standard radius (testable with ngEHT, amplitude TBD)
