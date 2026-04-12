# HPF Entanglement Candidate Note — Obligation Closure
## Lower-Wall Constitutive Derivation, Equal Bit-Weight, and Creation Event Status

**Document Class:** HPF candidate support note — entanglement obligation closure  
**Status:** Closes Obligation 1. Partially closes Obligation 2. Tightens Obligation 3.  
**Compatibility:** Repo-compatible. Extends the entanglement candidate note (2026-04-11) without modifying canon volumes.  
**Author:** Eric Keaton Porter  
**Date:** 2026-04-12

---

# 1. Scope

This note addresses the three open obligations in the Entanglement Candidate Note:

| Obligation | Previous status | Updated status |
|---|---|---|
| 1 — Lower wall constitutive derivation | Open | **Closed** (§2) |
| 2 — Grammar uniqueness / equal bit-weight | Open | **Partially closed**: equal bit-weight derived; grammar uniqueness remains separate problem (§3) |
| 3 — Creation event formalization | Open | **Tightened** to specific bridge path (§4) |

---

# 2. Obligation 1 — Lower Wall Constitutive Derivation: Closed

## 2.1 The obligation

The entanglement note claimed that $S_{\rm ent} = 1.3806$ is the minimum threshold for sustaining a bifurcated address state $(n_L = 1, n_R = 1)$. The obligation was to derive *why* this specific value constitutively marks the entanglement onset, not just that it is derived/substrate-native in the vacuum-sector package.

## 2.2 Resolution

The lower-wall Nyquist correction (HPF Correction Note, 2026-04-12) identifies $S_{\rm ent}$ as the **single-sublattice resolution failure point**:

$$\zeta(S_{\rm ent}) = \frac{1}{N_s} = \frac{1}{24}$$

At $S_{\rm ent}$, the coherence gate drops to $1/24$ — the point at which one sublattice of the BCC 24-sector ring can no longer resolve adjacent angular sectors.

This is constitutively the entanglement threshold because:

1. **Below $S_{\rm ent}$:** coherent fraction $\zeta > 1/24$. The single sublattice can resolve adjacent sectors. The directional address is unique — the lattice knows whether the node's canonical direction is "left" or "right." The $(n_L, n_R)$ bits carry unambiguous values.

2. **At $S_{\rm ent}$:** coherent fraction $\zeta = 1/24$. Single-sublattice angular resolution reaches the Nyquist limit. Adjacent sectors are no longer independently resolvable by one sublattice alone.

3. **Above $S_{\rm ent}$:** coherent fraction $\zeta < 1/24$. The single sublattice cannot distinguish left-sector from right-sector. Both directional occupancy bits become simultaneously valid: $(n_L = 1, n_R = 1)$. The bifurcated address state is entered.

The entanglement threshold is therefore not an independently asserted value. It is the geometrically determined point at which single-sublattice directional resolution fails — the same $S_{\rm ent} = 1.3806$ derived from the Obligation 2 causal-arc chain, now with a constitutive physical reading from the particle side.

## 2.3 The two readings of $S_{\rm ent}$

| Reading | Physical content |
|---|---|
| Vacuum-sector (existing) | Lower integration bound for the shell selector; onset of the active entropy band |
| Particle-side (this closure) | Single-sublattice resolution failure; onset of bifurcated address / entanglement-capable regime |

These are two readings of the same geometrically determined threshold. Neither contradicts the other.

## 2.4 Status

**Obligation 1: closed.** The constitutive derivation is: $S_{\rm ent}$ is the single-sublattice Nyquist floor ($1/24$) of the BCC 24-sector ring, the point at which directional address resolution fails on one sublattice and both $(n_L, n_R)$ go live.

---

# 3. Obligation 2 — Grammar Uniqueness / Equal Bit-Weight: Partially Closed

## 3.1 The obligation

The entanglement note derived the 3/2 update path cost using equal bit-weight: cost per bit = 1/4 across the 4-bit alphabet $(n_L, n_R, b_{\rm bit}, q)$. The obligation noted that this depends on the equal-weight assumption, which in turn depends on the grammar being the unique admissible substrate grammar.

## 3.2 Equal bit-weight is forced by bijectivity

The equal-weight assumption does not require grammar uniqueness. It requires only that the QPRCA update rule is bijective on the full 4-bit state.

**Lemma (Equal Bit-Weight).** If the QPRCA update rule $\mathcal{U}$ is a bijection on the full 4-bit state space, and no mechanism in $\mathcal{U}$ explicitly breaks the symmetry between bit positions, then the information-theoretic cost per bit is uniform: $1/4$.

**Argument.** A bijection on a $2^4$-element state space is a permutation of 16 states. The 4-bit representation assigns each state a unique binary address. A permutation acting on the full state space treats all bit positions symmetrically in the information-theoretic sense — each bit contributes equally to distinguishing states — unless the permutation's cycle structure explicitly correlates with specific bit positions.

In the BCC QPRCA, the update rule $\mathcal{U}_{A \to B}$ is bijective in the full 4-bit state of the B site for fixed A-neighbor configuration (reversibility requirement). The bijectivity acts on the 16-element state space as a whole, not on subsets of bits. No mechanism in the current grammar assigns different update costs to $n_L$ vs $n_R$ vs $b_{\rm bit}$ vs $q$.

Therefore the default cost assignment — equal weight $1/4$ per bit — is the unique assignment consistent with bijectivity on the full state space without explicit symmetry-breaking.

## 3.3 Grammar uniqueness is a separate problem

The equal bit-weight closure does not prove that the 4-bit grammar is the unique admissible substrate grammar. It proves that *if* the grammar is 4-bit, *then* equal bit-weight is forced.

Grammar uniqueness — proving that no 3-bit, 5-bit, or other alphabet satisfies all HPF legality conditions — is a larger open problem. It is not required for the entanglement note's 3/2 path derivation, which depends only on equal bit-weight within the candidate-locked 4-bit grammar.

## 3.4 Status

**Equal bit-weight: closed.** Derived from bijectivity of the update rule on the full 4-bit state space.

**Grammar uniqueness: open.** Separate problem, does not gate the 3/2 path derivation.

**Obligation 2: partially closed.** The part that the entanglement note actually depends on (equal bit-weight) is derived. The part it doesn't depend on (grammar uniqueness) remains open.

---

# 4. Obligation 3 — Creation Event Formalization: Tightened

## 4.1 The obligation

The entanglement note claimed that SPDC drives $S_f$ past $S_{\rm ent}$. The obligation was to construct a formal bridge from the standard QED description of SPDC to the HPF phase-load variable $S_f$.

## 4.2 The bridge path (identified, not constructed)

The bridge requires identifying $S_f$ with a measurable optical quantity in the SPDC context. The candidate identification:

$$S_f \sim \frac{\text{accumulated phase per coherence length in the nonlinear medium}}{\text{blur anchor phase scale}}$$

The SPDC phase-matching condition ($\omega_p = \omega_s + \omega_i$, $\vec{k}_p = \vec{k}_s + \vec{k}_i$) constrains the phase accumulation geometry. The nonlinear susceptibility $\chi^{(2)}$ controls the coupling strength and therefore the rate of phase-load growth per unit path in the crystal.

The threshold claim — only interactions capable of driving $S_f > S_{\rm ent}$ produce entanglement — translates to: the crystal length $\times$ $\chi^{(2)}$ $\times$ pump intensity must exceed a minimum value set by $S_{\rm ent} = 1.3806$.

## 4.3 What remains

The formal bridge is not constructed. Specifically:

1. The quantitative identification of $S_f$ with optical observables (crystal length, $\chi^{(2)}$, pump parameters) is not derived.
2. The prediction that below-threshold SPDC configurations fail to produce entanglement has not been tested against experimental data.
3. The connection between $S_{\rm ent} = 1.3806$ and the minimum crystal/pump conditions for SPDC has not been computed.

## 4.4 Status

**Obligation 3: tightened, not closed.** The bridge path is identified. The formal construction and experimental test remain open.

---

# 5. Updated Entanglement Note Status

| Component | Status |
|---|---|
| Bifurcated address interpretation | Candidate (unchanged) |
| Active entropy band as entanglement regime | Candidate (unchanged) |
| $S_{\rm ent}$ as constitutive entanglement threshold | **Closed** — single-sublattice Nyquist floor |
| 3/2 update path cost | **Strengthened** — equal bit-weight derived from bijectivity |
| Measurement as grammar operation | Candidate (unchanged) |
| SPDC creation event bridge | Tightened, not closed |

The entanglement candidate note moves from "three obligations open" to "one obligation open (creation event bridge), one partially closed (grammar uniqueness as separate problem), one fully closed (lower-wall constitutive derivation)."

---

# 6. Freeze wording

> $S_{\rm ent} = 1.3806$ is constitutively the entanglement threshold because it is the single-sublattice resolution failure point: the coherence gate reaches $1/N_s = 1/24$, the Nyquist floor of the BCC 24-sector ring for one sublattice. Below $S_{\rm ent}$, a single sublattice resolves directional address; above $S_{\rm ent}$, it cannot, and both $(n_L, n_R)$ go live — the bifurcated address state is entered. Equal bit-weight (cost per bit = $1/4$) is forced by bijectivity of the QPRCA update rule on the full 4-bit state space, not assumed. Grammar uniqueness is a separate open problem that does not gate the 3/2 path derivation. The SPDC creation event bridge is tightened to a specific identification path ($S_f$ mapped to accumulated phase per coherence length in the nonlinear medium) but not formally constructed.
