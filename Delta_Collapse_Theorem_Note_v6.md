# δ_collapse — Admissibility and Derivation Pass
## Internal Theorem Note — v6

**Author:** Eric Keaton Porter  
**Date:** 2026-03-31 (v6 update same session)  
**Status:** Near-theorem structural derivation. One constitutive bridge and one uniqueness step remain open.

---

## 1. Formal Target Definition

$$\delta_{\rm collapse} = S_{\rm cap} - \left(S_{\rm blur} + \frac{3\pi}{2} + \eta\right) = 0.005678$$

**Probe precision:** Binary search [5.0, 5.99], 6 iterations → ±0.0155.

---

## 2. Current Best Expression

$$\boxed{S_{\rm cap} = S_{\rm blur} + \frac{3\pi}{2} + \frac{1}{48} + \frac{b^3}{(2\phi-1)^2}}$$

$$= 1.05 + 4.712389 + 0.020833 + 0.005750 = 5.788972$$

Gap from empirical 5.7889: **0.000072** — within probe precision.

---

## 3. Denominator (carried from v3)

$$\frac{b^3}{(2\phi-1)^2} = \frac{b^3}{5}, \qquad 2\phi-1 = P'(\phi) = \sqrt{5}$$

Denominator = squared fixed-point sensitivity of the Fibonacci characteristic polynomial. **Status: candidate-explained, strong.**

---

## 4. Fork Resolution (carried from v2)

**Fork B eliminated.** ζ(S_budget) = 0. δ_collapse is geometric (Fork A).

---

## 5. Robustness Paper Foundation

From *Topology and Dimensional Reduction of the Λ Selector Branch* (2026-03-31):

- 47,628-point sweep confirms n=220 selector occupies a connected anisotropic robustness volume
- k→∞ (step-function limit) is legal and preserves n=220
- k is demoted to a one-sided tail-softening parameter
- Effective parameter space reduces from 4D to **3D structural constraint manifold**: (S_lo, S_hi, ε)
- Admissible ceiling interval: [5.784, 5.804]
- b³/(2φ-1)² places S_cap at 5.788972 — inside this window ✓

---

## 6. The Cubic Order Derivation Spine

**Status: Near-theorem structural derivation.** The selector can now be organized into a b-scaling framework in which the zero-order term is topological, lower-order corrections are plausibly identified with blur-tail structure, and the cubic term emerges as the leading surviving geometric candidate. A full theorem still requires the proofs in Section 7.

### 6.1 The b-Scaling Framework

Following the Layer 3 pressure test, the Λ branch parameter space undergoes dimensional reduction into a 3D structural constraint manifold: (S_lo, S_hi, ε).

Mapping these coordinates to the Fibonacci boundary parameter b = ln(φ)/(π/2):

- Phase-budget differential: dS ∝ b (since S = ln(r) is the log-radial measure)
- Shell-conversion prefactor: P = 24/ln(φ) ∝ b⁻¹ (since P⁻¹ = ln(φ)/24 = b·π/48)
- Zero-order raw selector: X₀ = P·ΔS ∝ b⁻¹·b = **b⁰**

**The zero-order selector is a b-independent topological invariant.** Verified: X₀ = 49.874 × 4.408 = 219.86.

### 6.2 The Structural Hypothesis

The ceiling S_hi decomposes into:
$$S_{\rm hi} = S_{\rm geom}(b) + S_{\rm blur}(k)$$

where S_geom is the hard geometric substrate capacity and S_blur is the thermodynamic blur shift governed by gate steepness k.

Because k→∞ legally preserves n=220, the thermodynamic blur strictly vanishes in the step-function limit.

The structural hypothesis posits two links:
1. The thermodynamic blur is the minimal resolvable phase uncertainty induced by the finite causal wedge, forcing the scaling k ∝ 1/b
2. The surviving geometric capacity correction is the 3D spatial volume of the constraint manifold tolerances (dS_lo ∧ dS_hi ∧ dε), making cubic order b³ the leading surviving geometric candidate

---

## 7. Remaining Theorem Obligations

To upgrade this derivation spine into a formal uniqueness theorem, three explicit proofs must be secured:

### Obligation 1 — Constitutive Linearity and Separability
A proof that the finite structural correction factors through the 3-manifold coordinates with exactly one linear power of b per independent coordinate, excluding arbitrary nonlinear maps.

*Current status:* **Step 3 (linearity) closed in the sharp-gate active-sector regime.** Lemma proved: for fully active sectors with $S_{\rm lo} > S_{\rm blur} = 1.05$, the sector-capacity integral is strictly linear in $(S_{\rm hi} - S_{\rm lo})$ in the limit $k \to \infty$. The finite-$k$ nonlinearity is exponentially suppressed in the boundary tail and vanishes in the structural limit. Straddling sectors ($S_{\rm lo} < 1.05 < S_{\rm hi}$) remain outside proved scope. Step 1 (P factoring) is canon-consistent but uniqueness not proved; QPRCA substrate no-overlap lemma still missing. Step 2 (translational invariance) is strong.

### Obligation 2 — The k ∝ 1/b Bridge
A formal derivation proving the gate steepness is inversely proportional to the Fibonacci causal wedge parameter b.

*Current status:* k = ln(47)/(S_ent - S_blur) is derived. k·b = 3.567 — not a pure constant, because (S_ent - S_blur) contains the canonical onset target, not a pure b-expression. The proportionality k ∝ 1/b is a physically motivated ansatz, not a derived result.

### Obligation 3 — Uniqueness of the Cubic Correction Order

The numerical value of $S_{\rm cap}$ is locked, and the four-term structural form is the active candidate explanation. The remaining open obligation is a uniqueness proof: a formal argument that any $b^1$ or $b^2$ geometric correction to $S_{\rm cap}$ is forbidden by HPF substrate symmetry or topological cancellation, independently of the current derivation path. Until that proof is in hand, the cubic form is the unique surviving candidate, but not the uniquely admissible form.

*Current status:* The b-expansion of the capacity integral confirms that b¹ and b² terms are structurally absent given the current four-term form of $S_{\rm cap}$ and the b-independence of $S_{\rm ent}$. This is a consequence of the derived form, not an independent exclusion. The likely attack path runs through the b-scaling framework: if $X_0 = P \cdot \Delta S$ as a topological invariant constrains admissible correction structure, that may supply the selection rule on ceiling deformations — but the bridge from leading-order invariant to general exclusion principle is not yet proved.

---

## 8. Locked Summary (v5)

The cubic-order argument is no longer a loose dimensional intuition. The selector is organized into a b-scaling framework where:
- The zero-order term is a topological invariant (b⁰)
- Lower-order corrections are absent in the current canonized expansion, but not yet independently excluded by theorem
- The cubic term b³/(2φ-1)² emerges as the leading surviving geometric candidate

A full theorem requires Obligations 1, 2, and 3. Until then: **near-theorem structural derivation**.

---

## 9. Candidate Registry Summary

| Candidate | δ value | Status |
|---|---|---|
| C9: b³/(2φ-1)² | 0.005750 | Leading — near-theorem |
| C8: η·b·(1-b²) | 0.005783 | Secondary candidate |
| C5: ζ tail lag | — | Eliminated (Fork B) |
| C1: η·b | 0.006382 | Demoted |

---

## 10. Admissibility Guardrails (unchanged)

1. Independence from 5.7889
2. Drift-free across canon
3. k-robust with S_ent fixed
4. Interpretable in substrate operations
5. Geometric (Fork A)

---

## 11. μ_B Status (unchanged)

Functional resonance only. Revisit after Obligations 1–3 are resolved.

---

## 12. Full Canon Chain (current best)

$$S_{\rm cap} = \underbrace{1.05}_{\rm Lu\ anchor} + \underbrace{\frac{3\pi}{2}}_{\rm 3\ BCC\ channels} + \underbrace{\frac{1}{48}}_{\rm Nyquist} + \underbrace{\frac{b^3}{(P'(\phi))^2}}_{\rm cubic\ Fibonacci\ correction}$$

$$= 5.788972 \approx 5.7889$$

**Status:** Near-theorem structural derivation. Three obligations remain for full theorem status.
