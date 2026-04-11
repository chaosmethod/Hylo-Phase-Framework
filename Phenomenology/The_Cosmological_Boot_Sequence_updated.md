# The Cosmological Boot Sequence — Candidate Note

**Document Class:** HPF phenomenology candidate note
**Status:** Candidate — not canon. One dependency open.
**Compatibility:** Repo-compatible. Consistent with Volume IV active package.
**Author:** Eric Keaton Porter
**Date:** 2026-04-04

---

## Abstract

The "Initial Singularity" is resolved as a saturation-limited initialization event of the QPRCA substrate. HPF axioms forbid infinite density, replacing the Big Bang with a Maximum Entropy Constrained State. The evolution of the early universe is governed by the transition of the Entropic Flux ($S_f$) through specific Stability Phases. Dark Energy is the constant computational overhead required to maintain the lattice address space as it expands — a structural consequence of the substrate, not a new field or free parameter.

---

## Locked Inputs From Active Package

| Input | Value | Status |
|---|---|---|
| $L_{vac} = R_H / \phi^n$ | $n = 220$, $L_{vac} \approx 1.45 \times 10^{-20}$ m | Candidate-locked, active canon |
| $\Lambda \approx 1.081 \times 10^{-52}$ m$^{-2}$ | From $L_{vac}$ branch | Candidate-locked, gap $10^{-0.008}$ |
| $S_{\rm blur} = 1.05$ | Phase boundary | Locked empirical anchor |
| $S_{\rm cap} = 5.7889$ | Saturation ceiling | Locked |
| $G_{\rm health}$ threshold | $0.3$ | Executor handoff condition |
| No $/2$ in radial law | Explicit March 29 correction | Locked |

---

## 1. The Saturation Limit ($\sigma \to 1$)

At $t_{sched} \approx 0$, the universe existed at the Axiom III density cap.

- **Density:** $\rho_{max} \approx L_{vac}^{-3}$
- **Executor:** Because $G_{\rm health}$ was below $0.3$, execution was handled by the QPRCA substrate rather than General Relativity. GR was not yet a legal executor.
- **Reversibility:** Every update was bijective, ensuring no information was lost during the high-density boot.

There was no singularity. The substrate enforced a hard density ceiling. The Big Bang was not an explosion from nothing — it was a Maximum Entropy Constrained State beginning to ring down through its saturation bands toward coherent geometry.

---

## 2. Phase Evolution of the Projection

The timeline of the universe is a gradient of Update Availability ($\alpha$), governed by the transition of $S_f$ through three execution regimes:

| Phase | $S_f$ range | Character |
|---|---|---|
| Saturation Phase | $S_f > 5.79$ | Raw information mixing. No stable geometry. QPRCA executor. |
| Quantum Phase | $1.4 < S_f < 5.79$ | Emerging complexity. Intermediate blur. Handoff corridor. |
| Einstein Phase | $S_f < 1.4$ | Laminar geometry. Stable matter. Classical expansion. GR legal. |

The universe did not begin in the Einstein phase. It rang down into it as saturation pressure decreased and Update Availability increased. GR became the legal executor only once $G_{\rm health}$ crossed the $0.3$ threshold — not before.

---

## 3. Dark Energy and the Expansion

**Projection Cost:** Dark Energy is the constant computational overhead required to maintain the lattice address space as it expands. This is Lemma 3 of the active package. The cost scales with the number of active lattice sites and appears as a constant density that does not dilute — because it is intrinsic to the substrate's update availability $\alpha(x)$, not to any specific matter configuration.

**The 1/2 Factor — Substrate-Native Derivation:**

The 1/2 factor that appears in the weak-field metric is not a mirror artifact. It is the substrate-native consequence of round-trip exchange accounting at the $L_{vac}$ resolution scale.

Every object sits on the substrate at $L_{vac} \approx 1.45 \times 10^{-20}$ m. There is no object closer to or further from the lattice than any other — the substrate is the universal medium. Any metric measurement is therefore one leg of a two-leg exchange:

1. The object warps the substrate outward at $L_{vac}$.
2. The substrate returns that warp to the observer at $L_{vac}$.

Because $L_{vac}$ is universal, both legs are always equal. The observer catches exactly half the total exchange. The BCC bipartite sublattice structure and this round-trip accounting are two descriptions of the same geometric fact — A measures B through the substrate and receives the return through the substrate. The bipartite handoff is the round trip.

The $\frac{1}{2}$ in $g_{tt} \approx 1 + \frac{1}{2}\frac{R_s}{r}$ is therefore not a GR assumption. It is the GR-phase expression of a substrate-native accounting rule.

**Dependency:** The formal metric derivation connecting $L_{vac}$ round-trip accounting to the weak-field coefficient as a substrate output rather than a GR input is upstream of this note. See the updated LMS candidate note.

---

## 4. Falsifiability

- **Stochastic Jitter:** The boot sequence predicts that the Arrow of Time should exhibit a microscopic noise floor proportional to $\sqrt{N} \cdot L_{vac}/c$ as the lattice updates grainily. See the Stochastic Jitter Falsifier candidate note.
- **Entropy Scaling:** In high-congestion regimes ($\sigma \to 1$), time should experience extreme dilation rather than reversal — confirming that time is a function of throughput, not a fundamental symmetry.
- **Phase Signatures:** The transition from Quantum Phase to Einstein Phase should leave observable signatures in early universe structure formation distinguishable from standard inflationary predictions.

---

## Full Status Table

| Claim | Status |
|---|---|
| Big Bang as Maximum Entropy Constrained State | Substrate-native — follows from Axiom III density cap |
| QPRCA executor below $G_{\rm health} = 0.3$ | Candidate-strong, consistent with active canon |
| Three-phase evolution via $S_f$ thresholds | Candidate-strong, consistent with active canon |
| Dark Energy as Projection Cost (Lemma 3) | Candidate, active package |
| $\frac{1}{2}$ factor as substrate-native round-trip accounting | Strong candidate — see LMS updated note |
| Formal metric derivation from $L_{vac}$ round-trip | Upstream dependency — not derived in this document |
| Old mirror-reflection justification of $\frac{1}{2}$ | Decapitated — removed |

---

## Freeze Wording

> The Big Bang is resolved as a saturation-limited initialization event of the QPRCA substrate — a Maximum Entropy Constrained State, not an explosion from nothing. The universe rang down through three execution phases governed by $S_f$: Saturation, Quantum, and Einstein. GR became the legal executor only after $G_{\rm health}$ crossed $0.3$. Dark Energy is the constant computational overhead of maintaining the expanding lattice address space. The $\frac{1}{2}$ factor in the weak-field metric is the GR-phase expression of symmetric round-trip substrate accounting at the $L_{vac}$ resolution scale — every object is equidistant from the substrate, both exchange legs are equal, the observer always catches exactly half. One upstream dependency remains: the formal metric derivation connecting $L_{vac}$ round-trip accounting to the weak-field coefficient.

---

*End of candidate note. Do not promote to canon until upstream metric derivation is confirmed.*
