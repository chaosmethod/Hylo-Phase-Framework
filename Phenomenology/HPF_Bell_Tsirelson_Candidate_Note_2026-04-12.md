# HPF Candidate Note — Tsirelson Bound as Substrate Output

## Mirror-Buffer Obligation 3 Closure and Third Independent Observable

**Document Class:** HPF phenomenology candidate note — mirror-buffer Obligation 3 closure  
**Status:** Candidate — closes mirror-buffer Obligation 3. Derives the Tsirelson bound $2\sqrt{2}$ from substrate objects already present in the live package.  
**Compatibility:** Repo-compatible. Extends the mirror-buffer obligation closure (2026-04-12) and the Bell-State Constraints document without modifying canon volumes.  
**Author:** Eric Keaton Porter  
**Date:** 2026-04-12

---

# 1. Scope

This note closes mirror-buffer Obligation 3 by:

1. Identifying the mirror operator $M = JK$ as the substrate-level generator of Bell correlations on the BCC lattice.
2. Showing that the bipartite propagation reach of $M$ peaks at $3/2$ sectors on the 24-sector ring.
3. Deriving the optimal CHSH measurement gap $\pi/4$ from substrate geometry.
4. Recovering the Tsirelson bound $2\sqrt{2}$ as a substrate output.
5. Computing the $b/72$ passive mirror correction to the predicted bound as the third independent sublattice-sensitive observable.

No new objects are introduced. Every element of the derivation is already present in the live package across three existing documents:

* **Bell-State Constraints and Substrate Architecture** (mirror operator $M = JK$, $M^2 = -I$)
* **Mirror Buffer Obligation Closure** (bipartite propagation reach $3/2$, passive Nyquist residual $b/72$)
* **Entanglement Candidate Note** (bifurcated address state $(n_L=1, n_R=1)$ in the active entropy band)

---

# 2. The mirror operator on the directional qubit

## 2.1 The entanglement-active subspace

The candidate-locked 4-bit grammar $(n_L, n_R, b_{\text{bit}}, q)$ contains a directional qubit in the $(n_L, n_R)$ sector. The two resolved address states are:

$$
|L\rangle \equiv (n_L=1,\ n_R=0), \qquad |R\rangle \equiv (n_L=0,\ n_R=1).
$$

The bifurcated address state $(n_L=1, n_R=1)$ is the superposition that lives in the active entropy band $S_{\text{ent}} < S_f < S_{\text{cap}}$. The vacuum state $(0,0)$ is null. The entanglement-active subspace is $\{|L\rangle, |R\rangle\}$ — a qubit embedded in the 4-state directional space.

## 2.2 Operator definitions

**$K$** is complex conjugation. In the computational basis $\{|L\rangle, |R\rangle\}$, which is real, $K$ acts as identity on basis vectors and conjugates amplitudes. On the lattice: $K$ is time reversal of the bipartite update schedule — it reverses $\mathcal{U}_{A \to B}$ into $\mathcal{U}_{B \to A}$.

**$J$** is the antisymmetric swap on the directional qubit:

$$
J = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}
$$

So $J|L\rangle = |R\rangle$ and $J|R\rangle = -|L\rangle$. This is $i\sigma_y$, the standard symplectic form on a qubit. On the lattice: $J$ swaps the directional address with an antisymmetric sign — the sign that distinguishes the singlet $|\Psi^-\rangle$ from the triplet $|\Psi^+\rangle$.

**$M = JK$** is the combined mirror operator:

$$
M|L\rangle = |R\rangle, \qquad M|R\rangle = -|L\rangle.
$$

## 2.3 Verification of $M^2 = -I$

$$
M^2|L\rangle = M|R\rangle = -|L\rangle, \qquad M^2|R\rangle = M(-|L\rangle) = -|R\rangle.
$$

$M^2 = -I$ is confirmed. This is the spin-$1/2$ time-reversal structure — the algebraic engine behind Kramers degeneracy and the non-factorizability of the Bell singlet. The $M^2 = -I$ property forces the entangled pair to be non-factorizable: the bifurcated state cannot be smoothly deformed into a product state without breaking the antisymmetry.

---

# 3. Angular reach of the mirror operator on the 24-sector ring

## 3.1 Setup

The BCC 24-sector ring assigns angular sectors $j = 0, 1, \ldots, 23$, each subtending

$$
\Delta\theta_{\text{sector}} = \frac{2\pi}{24} = \frac{\pi}{12}.
$$

At each sector $j$, the directional qubit $\{|L_j\rangle, |R_j\rangle\}$ has "left" and "right" defined relative to sector $j$'s neighbors on the ring.

## 3.2 The mirror operator acts through the bipartite update

$M = JK$ is not a static operator — it acts by propagating through the bipartite update cycle $\mathcal{U}_{B \to A} \circ \mathcal{U}_{A \to B}$. The time-reversal component $K$ reverses the update direction; the symplectic swap $J$ exchanges the directional labels with antisymmetric sign.

The physical reach of $M$ across the ring is therefore set by the bipartite propagation kernel — the same kernel whose effective path length was derived in the mirror-buffer obligation closure.

## 3.3 The reach is $3/2$ sectors

From the mirror-buffer obligation closure (2026-04-12):

* **Forward half-step** $\mathcal{U}_{A \to B}$: transports information across 1 sector. Full weight — all information is new to $B$. Effective contribution: **$1$**.
* **Mirror half-step** $\mathcal{U}_{B \to A}$: transports mixed $B$ state across 1 sector, but only the $B$-origin fraction (weight $1/2$, forced by bipartite symmetry) is new to $A$. Effective contribution: **$1/2$**.
* **Total effective reach:** $1 + 1/2 = 3/2$ sectors.

This reach is derived from:
1. Reversibility $\to$ bijectivity of $\mathcal{U}_{A \to B}$ in old-$B$ state.
2. Bijectivity $\to$ both $A$-origin and $B$-origin components encoded in new $B$ state.
3. Bipartite symmetry ($|A| = |B|$) $\to$ $B$-origin fraction is exactly $1/2$.
4. Sublattice-sensitive sampling $\to$ only $B$-origin fraction counts as new information in mirror return.

## 3.4 The angular correlation of $M$ peaks at $3/2$ sectors

The mirror operator $M$ generates correlations between directional qubits at sectors separated by the bipartite propagation reach. Because the effective reach is $3/2$ sectors, the two-point angular correlation function

$$
C(\Delta j) = \langle \Psi | M_j^\dagger M_{j+\Delta j} | \Psi \rangle
$$

peaks at $\Delta j = 3/2$.

---

# 4. From angular reach to the Tsirelson bound

## 4.1 The optimal CHSH angle is $\pi/4$

The peak correlation separation on the 24-sector ring is $3/2$ sectors. In radians:

$$
\theta_{\text{peak}} = \frac{3}{2} \times \frac{\pi}{12} = \frac{\pi}{8}.
$$

This is the angular separation at which the mirror operator $M$ produces maximum correlation between directional qubits. 

**Formal justification for the one-way doubling:**
A CHSH measurement is a projection onto a definite spin axis in the $\{|L\rangle, |R\rangle\}$ subspace. This projection necessarily engages both chiral components $n_{Lh}$ and $n_{Rh}$ simultaneously for two reasons:

1. **Bijectivity:** The QPRCA update rule is bijective on the full 4-bit state $(n_L, n_R, b_{\text{bit}}, q)$. In the bifurcated address state $(n_L=1, n_R=1)$, the two directional occupancy bits are jointly load-bearing. A projection that resolved $n_{Lh}$ without engaging $n_{Rh}$ would break bijectivity on the full state. 
2. **Symplectic Generator:** $J$ has no block-diagonal form in the $\{|L\rangle, |R\rangle\}$ basis. Every rotation $\theta$ is generated by the full action of $J$.

The substrate correlation peak $\pi/8$ is the bidirectional figure. A CHSH measurement is a one-way probe: it resolves both $n_{Lh}$ and $n_{Rh}$ simultaneously, doubling the effective angular span. The optimal CHSH measurement gap is therefore $2 \times \pi/8 = \pi/4$.

## 4.2 CHSH optimization at $\pi/4$

The CHSH correlator is:

$$
S = E(a,b) - E(a,b') + E(a',b) + E(a',b').
$$

For the Bell singlet state generated by $M$ with $M^2 = -I$, the correlation function is:

$$
E(\mathbf{a}, \mathbf{b}) = -\cos(\theta_a - \theta_b).
$$

The standard optimal settings are:

$$
a = 0, \quad a' = \frac{\pi}{2}, \quad b = \frac{\pi}{4}, \quad b' = \frac{3\pi}{4}.
$$

The adjacent measurement gaps are all $\pi/4$ — the one-way CHSH span derived from the substrate peak.

## 4.3 The Tsirelson bound

With $E(\mathbf{a}, \mathbf{b}) = -\cos(\theta_a - \theta_b)$ and these settings:

$$
|S_{\text{max}}| = \left|-\frac{4}{\sqrt{2}}\right| = 2\sqrt{2}.
$$

In this derivation, the Tsirelson bound is a **substrate output**: the maximum CHSH value achievable on a BCC bipartite lattice whose mirror operator has effective angular reach $3/2$ sectors across a 24-sector ring.

## 4.4 Derivation chain (single line)

$$
M = JK \xrightarrow{M^2=-I} \text{Bell singlet structure} \xrightarrow{\text{bipartite reach } 3/2} \theta_{\text{peak}} = \frac{\pi}{8} \xrightarrow{\text{CHSH at } \pi/4} S_{\text{max}} = 2\sqrt{2}
$$

---

# 5. The $b/72$ correction as third independent observable

## 5.1 The passive mirror residual shifts the peak

The mirror-buffer correction note establishes that sublattice-sensitive observables carry a passive correction of $b/72$, where $b = \ln\varphi / (\pi/2) \approx 0.3063$. The angular reach of $M$ is a sublattice-sensitive quantity.

The corrected effective reach is:

$$
L_{\text{eff}}^{\text{corrected}} = \frac{3}{2} + \frac{b}{72}.
$$

## 5.2 Corrected peak angle

The substrate bidirectional peak shifts to $\pi/8 + b\pi/864$. Applying the one-way doubling:

> $$
> \theta_{\text{CHSH}}^{\text{corrected}} = 2\left(\frac{\pi}{8} + \frac{b\pi}{864}\right) = \frac{\pi}{4} + \frac{b\pi}{432}
> $$

## 5.3 Corrected Tsirelson bound

The one-way CHSH gap $\pi/4$ is the stationary point. The leading correction is second order:

$$
\Delta S = -\sqrt{2}\left(\frac{b\pi}{432}\right)^2
$$

Numerically:
$$
\frac{b\pi}{432} \approx 0.002228
$$
$$
\Delta S = -\sqrt{2} \times (0.002228)^2 \approx -7.02 \times 10^{-6}
$$

## 5.4 Predicted corrected bound

$$
S_{\text{max}}^{\text{corrected}} = 2\sqrt{2} - 7.02 \times 10^{-6} \approx 2.8284201
$$

> The predicted deviation is $\sim 7.0 \times 10^{-6}$ — approximately $2.5$ parts per million below the standard Tsirelson bound.

---

# 6. Experimental status

* **6.1 Leading-order prediction:** $2\sqrt{2}$ is experimentally confirmed. The substrate derivation reproduces this as output.
* **6.2 The $b/72$ correction:** Current uncertainty in loophole-free Bell tests is $10^{-2}$ to $10^{-3}$, roughly three orders of magnitude above this predicted correction.
* **6.3 Falsifiability:** The prediction is falsified if future precision tests measure a deviation of a different sign/magnitude, or if the sublattice-sensitivity test for angular reach fails.

---

# 7. Status of mirror-buffer Obligation 3

## 7.1 The three-observable verification

| Observable | Uncorrected | Corrected | Observed | Residual |
| :--- | :--- | :--- | :--- | :--- |
| Dark matter fraction $\Omega_{\text{dm}}$ | $26.29\%$ | $26.715\%$ | $26.8\%$ | $0.085\%$ |
| Neutrino mass-squared ratio $\Delta m^2_{31}/\Delta m^2_{21}$ | $34$ | $33.856$ | $33.831$ | $0.07\%$ |
| Tsirelson bound $S_{\text{max}}$ (CHSH) | $2\sqrt{2}$ | $2\sqrt{2} - 7.02\times10^{-6}$ | $2\sqrt{2} (\pm 10^{-3})$ | Not yet testable |

## 7.2 Assessment

**Obligation 3: closed.** Three independent sublattice-sensitive observables are identified. The first two are confirmed against observation; the third produces a precision prediction.

---

# 8. Cross-document dependency map

| Input | Source document | Status |
| :--- | :--- | :--- |
| $M = JK$, $M^2 = -I$ | Bell-State Constraints | Substrate-native |
| Bipartite reach $3/2$ | Mirror Buffer Obligation Closure | Derived from QPRCA |
| 24-sector ring, $\pi/12$ per sector | BCC geometry (Volume IV) | Derived / substrate-native |
| Bifurcated address $(n_L=1, n_R=1)$ | Entanglement Candidate Note | Candidate |
| $b/72$ passive correction | Mirror Buffer Correction Note | Candidate |
| $b = \ln\varphi/(\pi/2)$ | Live package | Derived / substrate-native |

---

# 9. Updated mirror-buffer status

| Component | Status |
| :--- | :--- |
| Geometric $3/2$ path factor | Derived from QPRCA update algebra |
| Passive Nyquist residual $\eta_{\text{passive}} = 1/72$ | Derived |
| Correction magnitude $b/72 \approx 0.43\%$ | Derived |
| Sublattice-sensitivity criterion | Verified against 3 observables |
| **Third independent observable** | **Closed** — $\Delta S = -7.02 \times 10^{-6}$ predicted |

---

# 10. Freeze wording

> The Tsirelson bound $2\sqrt{2}$ is derived as a substrate output of the BCC bipartite lattice. The mirror operator $M = JK$ with $M^2 = -I$ generates Bell-singlet structure on the directional qubit $\{|L\rangle, |R\rangle\}$ embedded in the 4-bit grammar. $M$ acts through the bipartite update with effective angular reach $3/2$ sectors on the 24-sector ring. The substrate bidirectional peak is $(3/2)(\pi/12) = \pi/8$. A CHSH measurement is a one-way probe resolving both chiral components $n_{Lh}$ and $n_{Rh}$ simultaneously, doubling the effective angular span to $\pi/4$ — yielding $S_{\text{max}} = 2\sqrt{2}$ as substrate geometry, not quantum-mechanical axiom. The passive mirror correction $b/72$ shifts the effective reach, producing a predicted deviation $\Delta S \approx -7.02 \times 10^{-6}$ below $2\sqrt{2}$ — a precision prediction not yet within experimental reach. This closes mirror-buffer Obligation 3.
