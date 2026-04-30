# HPF Candidate Note — Mirror Buffer Entanglement Closure

**Document Class:** HPF phenomenology candidate note   
**Date:** 2026-04-30  
**Author:** Eric Keaton Porter  
**Status:** Substrate-native derivation; $b/72$ as bijective accounting across the single bipartite boundary. Pending third independent Bell-test execution lock.  
**Compatibility:** Repo-consistent. Extends Mirror Buffer Obligation Closure (2026-04-12) and Bell–Tsirelson Candidate Note (2026-04-12).

---

## Abstract

In the Hylo-Phase Framework, quantum entanglement is the geometric enforcement of bijectivity in the single reversible substrate $U = U_B \circ U_A$ on the BCC lattice. There are not two entangled substrates connected by some non-local link. There is only *one* substrate whose state is accounted for across the bipartite $A/B$ boundary. The mirror-buffer obligation ($b/72$ residual) is the exact capacity accounting that keeps the single substrate self-consistent when the $A/B$ distinction is collapsed from either side.

---

## 1. Premise

Standard treatments of entanglement describe two particles sharing a connection. This note reframes entanglement entirely within the HPF substrate grammar:

> Entanglement is not a link between two objects. It is the single substrate's bijective self-accounting across the $A/B$ bipartite boundary — one lattice viewed from two angles of the same mirror.

No additional postulates are required beyond the reversibility axiom already present in the live package.

---

## 2. Derivation Chain

All steps are substrate-native. Zero free parameters are introduced.

**Step 1 — Reversibility**

The global update

$$U = U_B \circ U_A$$

is strictly reversible on the 24-sector BCC lattice. Every update can be exactly undone.

**Step 2 — Bijectivity of $U_{A \to B}$**

Reversibility forces bijectivity. A single $B$-state must encode *both* its own $B$-origin information and the complete information required to reconstruct the paired $A$-state. The entire substrate is one bijective object.

**Step 3 — Bipartite Symmetry**

The $A$ and $B$ sublattices are symmetric views of the *same* lattice:

$$|A| = |B| \implies \text{B-origin fraction} = \frac{1}{2}$$

This is a theorem, not an assumption.

**Step 4 — Sublattice-Sensitive Sampling**

At mirror return, the effective path length is

$$L_{\mathrm{eff}} = 1 + \frac{1}{2} = \frac{3}{2}$$

Only the $B$-origin fraction carries *new* accounting relative to the local observer. The $A$-origin information was already fixed in the forward step of the single substrate.

**Step 5 — Passive Nyquist Residual**

The finite capacity floor ($N_s = 24$ active sectors $\to$ $2N_s = 48$ total update capacity) leaves a residual margin:

$$\eta_{\mathrm{passive}} = \frac{1}{\tfrac{3}{2} \times 48} = \frac{1}{72}$$

This residual lives in the mirror buffer as the passive obligation of the single substrate.

**Step 6 — $b/72$ Correction**

The Fibonacci boundary parameter

$$b = \frac{\ln \varphi}{\pi/2} \approx 0.3063$$

modulates the residual geometrically:

$$\delta_{\mathrm{mirror}} = \frac{b}{72} \approx 0.00425$$

**Trigger criterion:** An observable receives the $b/72$ correction *if and only if* collapsing the $A/B$ distinction changes its derivation output — i.e., when the observer forces the single substrate to reveal its full bijective accounting from one side only.

---

## 3. Entanglement Interpretation

Measurement is the collapse of the $A/B$ distinction on the *single* substrate.

When one side collapses the distinction, the mirror-buffer obligation makes the full accounting visible from the opposite side. The $b/72$ fraction is the precise correlation that appears in the statistics because the substrate was always one bijective object whose internal accounting already spanned the boundary.

There is no "action at a distance," no rebalancing, and no update propagating across space. Distance is an emergent 3D coordinate label after $\Delta$-collapse. Inside the substrate the buffer is capacity-local to the single lattice. The correlation was encoded in the bijective state from the start; the mirror simply refuses to let the accounting become inconsistent when viewed from one sublattice only.

Consequently:

- **EPR correlations** — substrate bijective accounting enforced at mirror return
- **Bell inequality violations** — the $A/B$ boundary accounting exceeds classical local limits by the exact geometric margin of the single bipartite update
- **Tsirelson bound** — the substrate derivation (Bell–Tsirelson Candidate Note, 2026-04-12) gives

$$S_{\max} = 2\sqrt{2}$$

with passive mirror correction:

$$\Delta S = -\sqrt{2} \times (b/72)^2 \approx -7.02 \times 10^{-6}$$

yielding the predicted bound:

$$S_{\max}^{\mathrm{corrected}} = 2\sqrt{2} - \sqrt{2} \left( \frac{b}{72} \right)^2 \approx 2.8284201$$

No hidden variables. No retrocausality. No dual substrates. Just the unavoidable residual of bijective accounting on a finite-capacity BCC lattice.

---

## 4. Relation to Existing Closures

| Prior closure | Connection |
|---|---|
| Mirror Buffer Obligation Closure (2026-04-12) | Identical derivation spine; this note extends the interpretation to entanglement |
| Bell–Tsirelson Candidate Note (2026-04-12) | Tsirelson bound and $\Delta S$ value imported directly |
| Volume IV — $\Omega_{\mathrm{dm}}$ branch | Same $b/72$ trigger criterion; same passive Nyquist residual |
| Neutrino Mass Hierarchy Candidate Note | Same sublattice-sensitivity trigger |
| Dimensional Closure / Boot Sequence | Single substrate forges 3D geometry; bijective accounting ($b/72$ entanglement) persists through the fold |

**Trigger criterion (universal):**

> An observable receives $b/72$ if and only if collapsing the $A/B$ distinction changes its derivation output.

This note adds entanglement observables to the verified trigger class.

---

## 5. Status Table

| Claim | Status |
|---|---|
| Entanglement as single-substrate bijective accounting | **Substrate-native** — follows from reversibility axiom |
| $b/72$ as the correlation residual | **Derived** — identical spine to existing closures |
| Tsirelson bound $2\sqrt{2}$ as substrate output | **Candidate-strong** — see Bell–Tsirelson note |
| Predicted deviation $\Delta S = -7.02 \times 10^{-6}$ | **Candidate** — below current experimental resolution |
| Third independent Bell-test execution lock | **Pending** — 256/256 existence-sensor run on entangled-pair statistics |

---

## 6. Pending Verification

The third independent Bell-test execution lock requires a full 256/256 existence-sensor run on entangled-pair statistics under `HPF_QPRCA_BCC_v0_3_0.py`. All analytic closures are complete. The execution lock is the remaining open item.

---

## Freeze Wording

> Quantum entanglement in HPF is the geometric enforcement of bijectivity in the single reversible BCC substrate. There are no two entangled objects — only one substrate accounted for across its $A/B$ bipartite boundary. The mirror-buffer passive residual $b/72$ is the exact capacity accounting that produces EPR correlations, Bell violations, and the Tsirelson bound tweak $\Delta S \approx -7.02 \times 10^{-6}$. The accounting was complete at preparation; measurement reveals it. No action propagates. No duality exists. One lattice, one mirror, one bijective accounting.

---

*End of candidate note. Do not promote to canon until Bell-test execution lock is confirmed.*
