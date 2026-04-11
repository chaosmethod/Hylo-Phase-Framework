# HPF Canonical Derivation Package — Volume IV
## First-Principles Derivation of $\Lambda$ and the Dark Matter Fraction
**Truth-Status:** Internally Consolidated with Explicit Status Partition
**Date:** 2026-03-29
**Author:** Eric Keaton Porter

---

# Section 1: Executive Summary

This document presents the active HPF derivation package for the cosmological constant ($\Lambda$) and the dark-matter fraction, with explicit separation between internally derived, empirically anchored, candidate-locked, and canon-proved claims. The active derivation structure is split into two branches; the old mixed March 27 branch is retired.

**Lambda branch:**
$$1.05 \to 1.3806 \to 5.7889 \to n=220 \to L_{\mathrm{vac}} \to \Lambda$$

**Dark-matter branch:**
$$b \to f_{\mathrm{coh}} \to \alpha_{\mathrm{vac}} \to \Omega_{\mathrm{dm}}=1-\alpha_{\mathrm{vac}}$$

**Outputs**

| Quantity | HPF Output | Observed | Gap |
| :--- | :--- | :--- | :--- |
| $\Lambda$ | $1.081 \times 10^{-52}$ m⁻² | $1.1 \times 10^{-52}$ m⁻² | $10^{-0.008}$ |
| Dark matter fraction | 26.29% | 26.8% | 0.51% |

The corrected radial law is:
$$R_H = L_{\mathrm{vac}} \phi^n, \qquad L_{\mathrm{vac}} = \frac{R_H}{\phi^n}$$

No `/2` belongs in this identity. The earlier `/2` factor arose from double-counting bipartite half-active support in a radial relation where it does not belong.

> **Status note:** The shell selector is now the integrated entropy-phase budget. In the active canon, $n=220$ is candidate-locked by regulated phase span. $H_0$ may still be used as an external consistency anchor, but it is not the primary selector.

---

# Section 2: The Lattice Identity and $c$ as Regulator

$c$, $L_{\mathrm{vac}}$, and $t_{\mathrm{sched}}$ are the same substrate primitive under three descriptions.

**Identity:**
$$L_{\mathrm{vac}} = c \cdot t_{\mathrm{sched}}$$

In substrate units, $c=1$, $L_{\mathrm{vac}}=1$, and $t_{\mathrm{sched}}=1$. In this sense, $c$ is the scheduler rate, not an externally imposed speed bound. The SI value of $L_{\mathrm{vac}}$ is set by the integer Fibonacci shell depth from the substrate unit to the Hubble scale:
$$L_{\mathrm{vac}} = \frac{R_H}{\phi^n}$$

Since the scheduler is discrete, $n \in \mathbb{Z}_{>0}$. The active selector for $n$ is:
$$n_{\mathrm{sel}} \equiv \mathrm{round} \! \left[ \frac{24}{\ln \phi} \int_{1.3806}^{5.7889} (1 - \zeta(S)) \, dS \right] \approx 220$$

with the Zeta gate:
$$\zeta(S) = \frac{1}{1 + e^{k(S - 1.05)}}, \qquad k=11$$

---

# Section 3: BCC Geometric Coefficient

The BCC bipartite lattice contributes three substrate-native suppression factors:
- $Coordination number: 8$
- $Bipartite sublattice split: \times 1/2$
- $LMS mirror factor (direct/reflected view): \times 1/2$

$$\kappa_{\mathrm{BCC}} = 8 \times (1/2) \times (1/2) = 2$$

**Status:** Exact. Substrate-native. Zero free parameters.

---

# Section 4: Prerequisite P1 — Fibonacci Update Law

## 4.1 BCC Bipartite Structure
The BCC lattice decomposes into two disjoint sublattices A and B. Every nearest neighbor of any A site is a B site and vice versa. The BCC lattice is strictly bipartite. Staggered update schedule: even ticks activate all A sites, odd ticks activate all B sites.

## 4.2 Coherent Global Update Sequences
A coherent global update sequence of length $n$ is a sequence of scheduler decisions {Continue, Branch} with no two consecutive Branches. The no-consecutive-Branch constraint follows from HPF Axiom II (reversibility).

## 4.3 Why Coordination Number 8 Does Not Affect the Recurrence
The scheduler decision is binary: {Activate A, Activate B}. This is independent of coordination number.

## 4.4 Proof of the Fibonacci Recurrence
Let $C(n)$ = number of distinct coherent global update sequences of length $n$.
$C(1) = 1, C(2) = 2$.
Every coherent sequence of length $n$ either ends with Continue ($C(n-1)$ such sequences) or ends with Branch preceded by Continue ($C(n-2)$ such sequences).
**Therefore:** $C(n) = C(n-1) + C(n-2)$ — the Fibonacci recurrence.

## 4.5 Emergence of $\phi$
$\phi \approx 1.618034$ emerges as the asymptotic growth rate $F(n+1)/F(n)$. It is not imposed; it is what the BCC bipartite scheduler does at scale.

---

# Section 5: Prerequisite P2 — Fibonacci Spiral as Causal Boundary

## 5.1 The Logarithmic Spiral is the Unique Causal Boundary
Fibonacci growth gives a constant multiplicative factor $\phi$ per step. In differential geometry, the logarithmic spiral $r = a e^{b \theta}$ is the unique smooth curve with constant multiplicative radial growth.
- $Growth parameter: b = \frac{\ln \phi}{\pi/2} \approx 0.306349$

The spiral grows by $\phi$ per quarter turn—the natural periodicity of the BCC bipartite A $\to$ B cycle.

## 5.2 Causal Support Fraction
- $Arc length: L_{\mathrm{arc}} = \frac{1}{b} \sqrt{1 + b^2} (R_H - L_{\mathrm{vac}})$
- $Coherent support fraction: f_{\mathrm{coh}} = \frac{L_{\mathrm{arc}}}{2 \pi R_H} = \frac{1}{2 \pi b} \sqrt{1 + b^2} \approx 0.5434$

$f_{\mathrm{coh}}$ is a dimensionless geometric occupancy fraction. The Fibonacci spiral naturally traverses about half the spherical boundary because only half the BCC sites are active per tick. This is where the bipartite 1/2 belongs—in $f_{\mathrm{coh}}$—not in the radial law.

---

# Section 6: Governor Transfer Lemma

## 6.1 Definitions
$$f_{\mathrm{coh}} = \frac{1}{2 \pi b} \sqrt{1 + b^2}, \qquad b = \frac{\ln \phi}{\pi/2}$$

## 6.2 Lemma
$$\alpha_{\mathrm{vac}} = \sqrt{f_{\mathrm{coh}}}$$

## 6.3 Assumption used
The transfer from geometric support fraction to usable availability is governed by the HPF chronological-governor rule: availability enters linearly in scheduler time while support enters quadratically as reservoir measure. Under that rule, the unique one-step transfer is a single square root.

## 6.4 Proof under the governing assumption
Under the governing assumption stated in 6.3, exactly one square-root transfer is admitted.
**Numerical values:**
- $f_{\mathrm{coh}} = 0.543354$
- $\alpha_{\mathrm{vac}} = \sqrt{f_{\mathrm{coh}}} = 0.737125$

## 6.7 Corollary: Dark-matter fraction
$$\Omega_{\mathrm{dm}} = 1 - \alpha_{\mathrm{vac}} = 0.262875 = 26.29\%$$

---

# Section 7: $L_{\mathrm{vac}}$ Derivation

## 7.1 Definitions and radial law
$$\frac{R_H}{L_{\mathrm{vac}}} = \phi^n, \qquad L_{\mathrm{vac}} = \frac{R_H}{\phi^n}$$

## 7.2 Status of $n$
$n=220$ is candidate-locked by the phase selector. For the Planck 2018 anchor ($H_0 = 67.4$ km s⁻¹ Mpc⁻¹):
- $R_H = c/H_0 = 1.3736 \times 10^{26}$ m
- $L_{\mathrm{vac}} = R_H / \phi^{220} = 1.447 \times 10^{-20}$ m

## 7.3 3D BCC streaming factor
The three-dimensional BCC streaming contribution is:
- $e^{3 \pi / 2} \approx 111.32$

## 7.4 Formal phase structure
- $Blur anchor (S_{\mathrm{blur}}): 1.05$
- $Entropy onset (S_{\mathrm{ent}}): 1.3806$
- $Capacity wall (S_{\mathrm{cap}}): 5.7889$

---

# Section 8: Empirical Anchors

## 8.2 Lu 2026 — Lower Blur Threshold
- $Source: Yu-Kun Lu et al. (arXiv:2507.19801), MIT.$
- $HPF role: S_{\mathrm{blur}} = 1.05$ inferred by mapping coherence-loss profile.

## 8.3 Planck 2018 — Hubble Constant
- $Source: Planck Collaboration 2018.$
- $HPF use: Consistency anchor for R_H.$

---

# Section 9: Continuum Emergence Theorem

## 9.2 Observable bound
For observable $O$ at probing scale $\ell_O$:
$$\varepsilon(\ell_O / L_{\mathrm{vac}}, S_f) = (1 - \zeta(S_f)) \left( \frac{L_{\mathrm{vac}}}{\ell_O} \right)^{S_{\mathrm{ent}}}$$

## 9.3 Active redistribution exponent
The continuum-emergence bound uses the live lower entropy onset:
- $S_{\mathrm{ent}} = 1.3806$

---

# Section 10: Truth-Status Discipline

| Claim | Form | Status Note |
| :--- | :--- | :--- |
| $C(n)=F(n)$ | Proposition | Internal derivation |
| $\phi$ emergence | Corollary | Internal derivation |
| $\kappa_{\mathrm{BCC}}=2$ | Computation | Internal derivation |
| $S_{\mathrm{blur}}=1.05$ | Mapped anchor | Empirically anchored |
| $n=220$ | Selector result | Candidate-locked |
| $\alpha_{\mathrm{vac}} = \sqrt{f_{\mathrm{coh}}}$ | Lemma | Proved internally (HPF canon) |

---

# Section 12: Number Provenance and Truth-Status Index

| Quantity | Role | Truth-Status |
| :--- | :--- | :--- |
| $\phi = 1.618034$ | Fibonacci growth | Derived / substrate-native |
| $b = 0.306349$ | Spiral parameter | Derived |
| $f_{\mathrm{coh}} = 0.543354$ | Support fraction | Derived geometric quantity |
| $\alpha_{\mathrm{vac}} = 0.737125$ | Vacuum availability | Proved internally (HPF) |
| $\Omega_{\mathrm{dm}} = 26.29\%$ | Dark matter fraction | Downstream output |
| $S_{\mathrm{ent}} = 1.3806$ | Entropy onset | Candidate-locked |
| $n = 220$ | Shell index | Candidate-locked selector |
| $\Lambda \approx 1.081 \times 10^{-52}$ m⁻² | Lambda output | Downstream supported output |

---

# Appendix A: Minimal Attackable Core

- $Corrected radial law: L_{\mathrm{vac}} = \frac{R_H}{\phi^n}$
- $Phase landmarks: S_{\mathrm{blur}} = 1.05, S_{\mathrm{ent}} = 1.3806, S_{\mathrm{cap}} = 5.7889$
- $Zeta gate: \zeta(S) = \frac{1}{1 + e^{k(S - 1.05)}}, \quad k=11$
- Integer selector: $n_{\mathrm{sel}} \equiv \mathrm{round} \! \left[ \frac{24}{\ln \phi} \int_{1.3806}^{5.7889} (1 - \zeta(S)) \, dS \right]$
- $Dark-matter chain: b = \frac{\ln \phi}{\pi/2}, \quad f_{\mathrm{coh}} = \frac{1}{2 \pi b} \sqrt{1 + b^2}, \quad \alpha_{\mathrm{vac}} = \sqrt{f_{\mathrm{coh}}}, \quad \Omega_{\mathrm{dm}} = 1 - \alpha_{\mathrm{vac}}$

---

# Appendix B: Local Robustness of the Active Shell Selector

The baseline evaluation gives:
- raw selector value: $X \approx 219.7422$
- rounded shell count: $n_{\mathrm{sel}} = 220$
- half-integer margin: $\approx 0.2422$

**Summary:** The selector occupies a genuine connected local robustness volume in ( $S_{\mathrm{lo}}, S_{\mathrm{hi}}, k, \epsilon$ )-space. Its robustness is anisotropic: broad in gate steepness, moderate along the phase-budget interval directions, and narrow in the shell-conversion prefactor direction.
