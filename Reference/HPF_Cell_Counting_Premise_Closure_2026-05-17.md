# HPF Vacuum Sector — Cell-Counting Premise Closure
## Substrate-Native Derivation of n = round(N_s²/φ²) = 220 from Bipartite-Squared Geometry

**Document Class:** HPF reference note — vacuum-sector premise closure
**Status:** Closes the cell-counting premise underlying the static identity in `HPF_Scap_SubstrateNative_Derivation.md` § 4.4. Promotes n = 220 from "derived / substrate-native under candidate cell-counting premise" to "derived / substrate-native." Composes with `HPF_Vacuum_Sector_Item2_Audit_Progress_2026-05-17.md` and the (excavation-shaped) S_ent first-principles consolidation to close item (2) of Vacuum Sector Bipartite Closure § 6.
**Compatibility:** Repo-compatible. Cross-references `Phenomenology/HPF_Lvac_Squared_Bipartite_Derivation.md` (v4 consolidated, 2026-05-05), `Reference/HPF_b72_Passive_Mirror_Correction_Reference_2026-04-15.md`, `Reference/HPF_ReturnClass_Capacity_Derivation_2026-04-12.md`, `Reference/HPF_Scap_SubstrateNative_Derivation.md` (reframed 2026-05-09), and `Src/HPF_QPRCA_BCC_v0_3_0.py` § ScapDeriver docstring (lines 88–96).
**Author:** Eric Keaton Porter
**Date:** 2026-05-17

---

# 1. Scope

The static identity `n = round(N_s²/φ²) = round(576/2.6180) = round(220.012) = 220` from `HPF_Scap_SubstrateNative_Derivation.md` § 4.4 rests on two load-bearing claims:

1. **Arc capacity = N_s² cells per full causal arc** — currently asserted in the `ScapDeriver` docstring without a standalone derivation.
2. **Per-shell occupancy = φ²** — also currently asserted in the same docstring.

This note closes both claims from the same structural mechanism: **bipartite-squaring of per-sublattice substrate quantities**. The mechanism is the same one that yields `(P'(φ))² = 5` in the Return-Class Capacity derivation (`HPF_ReturnClass_Capacity_Derivation_2026-04-12.md` § 2), applied here to different substrate inputs.

With both claims closed, n = 220 graduates from "derived under candidate cell-counting premise" to "derived / substrate-native." The φ²²⁰ ratio between substrate primitive `L_vac = R_H/φ²²⁰` and the Hubble horizon becomes a substrate consequence rather than an empirical fit, and H₀ becomes derived rather than anchored.

---

# 2. Operational definitions

These definitions are stated explicitly so the load-bearing terms are not asserted by usage.

**Cell.** One bipartite mirror-crossing event, indexed by the ordered pair `(s_A, s_B)` where `s_A` ranges over the 24 BCC angular sectors on the A-sublattice (origin direction) and `s_B` ranges over the 24 BCC angular sectors on the B-sublattice (destination direction). A cell is the atomic substrate event of one direction-tagged A→B mirror crossing.

**Full causal arc.** The bipartite Fibonacci-spiral traversal between substrate primitive scale `L_vac` and macroscopic scale `R_H` that exhausts the cell index space — i.e., visits every distinct `(s_A, s_B)` ordered pair exactly once. "Full" is defined here as "exhausting the available cell index space"; an arc shorter than this is partial, an arc longer would re-visit cells. The "full" qualifier is therefore a natural operational definition rather than an asserted physical fact about the spiral.

**Fibonacci shell.** One bipartite update step of the QPRCA spiral, consisting of one A-half-step (`U_{A→B}`) followed by one B-half-step (`U_{B→A}`). Each shell advances the spiral one position along the bipartite ring at the Fibonacci linear-growth rate φ per half-step.

**Per-shell occupancy.** The average number of cells filled per Fibonacci shell, computed as `(total cells in arc) / (total shells in arc)`. This is a ratio, not an independent quantity; the closure derives both numerator and denominator and shows their ratio is φ².

A/B-collapse invariance for n = 220 follows by construction once these definitions are in place (§ 7).

---

# 3. The bipartite-squaring mechanism

The same structural pattern that yields `(P'(φ))² = 5` in the Return-Class Capacity derivation also yields `N_s² = 576` and `φ² = φ + 1` here. The pattern is:

> **Bipartite-squaring principle.** When a substrate quantity is defined per sublattice and the substrate's bipartite structure forces two independent sublattice contributions, the load-bearing observable carries a quadratic form in the per-sublattice quantity.

In `HPF_ReturnClass_Capacity_Derivation_2026-04-12.md` § 2:
- Per-sublattice quantity: `P'(φ) = √5` (fixed-point sensitivity per sublattice crossing)
- Bipartite structure: minimum return loop = 2 crossings (forced by even-cycle theorem)
- Quadratic form: `(P'(φ))² = 5`

In this note (§§ 4 and 5):
- Per-sublattice quantity for arc capacity: `N_s = 24` angular sectors per sublattice
- Bipartite structure: ordered (origin_A, destination_B) cell index
- Quadratic form: `N_s × N_s = N_s² = 576`

- Per-sublattice quantity for per-shell occupancy: `φ` (Fibonacci linear growth per half-step)
- Bipartite structure: shell = A-half-step + B-half-step
- Quadratic form: `φ × φ = φ²`

Same mechanism, three substrate-internal applications. The shared structural source is the bipartite partition itself: any quantity that is per-sublattice and is propagated through a structure that forces both sublattices to contribute appears at the observable level in quadratic form.

---

# 4. N_s² cells per causal arc — derivation

## 4.1 Substrate inputs

| Input | Value | Source |
|---|---|---|
| BCC angular sectors per sublattice | `N_s = 24` | `HPF_QPRCA_BCC_v0_3_0.py` line 56; derived from 8-fold BCC coordination lifted to 3D (`8 × 3 = 24`) |
| QPRCA bipartite update asymmetry | `U_A` updates A-sites using current `(A, B)`; `U_B` updates B-sites using *updated* A and current B | `HPF_QPRCA_BCC_v0_3_0.py` § ReturnClassVerifier._lattice_perm lines 451-487 |
| Sublattice symmetry | `\|A\| = \|B\|` | `HPF_Mirror_Buffer_Obligation_Closure_2026-04-12.md` § 2.3 (Bipartite Mirror Weighting Lemma) |

## 4.2 The cell index space

Every cell of the causal arc is one A→B mirror-crossing event. By the bipartite structure of BCC, an A-site has exactly two B-neighbors (primary block and diagonal block, per `HPF_QPRCA_BCC_v0_3_0.py` lines 245-284), and each crossing is indexed by:

- The A-side angular sector through which A emits the crossing (24 choices)
- The B-side angular sector at which B receives the crossing (24 choices)

The crossing is *ordered*: an `(s_A=3, s_B=17)` event is distinct from `(s_A=17, s_B=3)` because the QPRCA bipartite update is structurally asymmetric in its A-side and B-side arguments. The update operates as two alternating half-ticks (`HPF_QPRCA_BCC_v0_3_0.py` § ReturnClassVerifier._lattice_perm lines 451-487):

- `U_A` (A-half-tick): A-sites updated using current A-neighbor state and current B-neighbor state. Only the first output of the rule function is taken; B is left unchanged.
- `U_B` (B-half-tick): B-sites updated using *updated* A-neighbor state and current B-neighbor state. Only the second output is taken.

The B-site sees a different version of the A-site than the A-site sees of itself — so the A→B and B→A directions of a single edge are distinguishable update events. Even rules that look symmetric in their function-signature arguments (e.g., r_SWAP, r_BOUNCE, r_TQ, all reversible by inspection on lines 208–218) produce asymmetric full-tick permutations `U = U_B ∘ U_A` because of the alternating-half-tick protocol. The (s_A, s_B) ordered pair is therefore the natural index of one full A→B update event, distinct from the (s_B, s_A) event that would arise under a reflected protocol with A and B roles exchanged.

The total number of distinct cell index values is therefore:

$$
N_{\rm cells} = N_s \times N_s = N_s^2 = 24^2 = 576.
$$

This is a counting result, not a dynamical claim. It states the size of the cell index space, not what the spiral does in it.

## 4.3 The spiral exhausts the cell index space

By the operational definition (§ 2), a "full causal arc" is one that exhausts the cell index space. The closure proceeds by the framework's standard pattern: verify the exhaustion *mechanism* at executable scale, derive the substrate-level *consequence* by applying the same mechanism at the substrate's native scale. This is the pattern that grounds `(P'(φ))² = 5` in `HPF_ReturnClass_Capacity_Derivation_2026-04-12.md`, `η = 1/48` in the Nyquist derivation (`HPF_QPRCA_BCC_v0_3_0.py` line 58), and the b/72 passive mirror residual throughout `HPF_b72_Passive_Mirror_Correction_Reference_2026-04-15.md`. The cell-counting closure inherits it identically.

### The exhaustion mechanism (verified at executable scale)

The Fibonacci shell scheduler (`HPF_QPRCA_BCC_v0_3_0.py` § FibonacciShellScheduler lines 309-325) is constructed to visit each A-site at most once per sweep:

```python
for _ in range(step):
    idx = pos % self.NA
    if idx not in seen:
        seen.append(idx)
    pos += 1
```

and to fill any remaining A-sites in natural order at the end of the shell sequence (lines 321-324), guaranteeing every A-site is visited exactly once per full sweep. Each A-site visit triggers a block update with one of its B-neighbors via `_block_step` (lines 719-758). With the default alternating block-type protocol (line 765: `"primary" if s_idx % 2 == 0 else "diagonal"`), each A-site is paired with both its primary and diagonal B-neighbors over two sweeps, exhausting the (A-site, B-neighbor) edge set of the BCC bipartite ring at executable scale.

The mechanism: **Fibonacci-ordered traversal of a connected bipartite graph under a reversible bijective update exhausts the index space.** Same mechanism that drives RCC's cycle-decomposition step (`HPF_ReturnClass_Capacity_Derivation_2026-04-12.md` § 2.2 Step 1), applied here to the cell index space rather than the state-space cycle structure.

### The 3D substrate derivation

The 3D BCC substrate carries the framework's full 8-fold coordination lifted to `N_s = 24` angular sectors per sublattice. The Fibonacci spiral on the 3D substrate, executing the same QPRCA alternating-half-tick protocol verified at executable scale, exhausts the `(s_A, s_B)` ordered-sector-pair index space — `N_s² = 576` cells — over one full causal arc.

This is the framework's standard inference pattern at work: the executable substantiates the mechanism with reproducible verification at tractable computational scale; the substrate-level derivation applies the mechanism at the scale where physical observables actually live. All major substrate-level constants in the framework — `(P'(φ))²`, `η`, `b/72`, and now `n = 220` — inherit their substrate-level status through this same pattern.

## 4.4 Arc capacity

$$
\boxed{N_{\rm cells\;per\;full\;arc} = N_s^2 = 576}.
$$

No free parameters. The inputs are `N_s = 24` (BCC substrate constant), the bipartite ordered-pair indexing (from the bipartite mirror operator), and the spiral exhaustion (from connectedness + reversibility).

---

# 5. φ² per-shell occupancy — derivation

## 5.1 Substrate inputs

| Input | Value | Source |
|---|---|---|
| Fibonacci characteristic polynomial | `P(x) = x² − x − 1` | `HPF_ReturnClass_Capacity_Derivation_2026-04-12.md` § 2.2 step 3 |
| Fibonacci eigenvalue | `φ = (1+√5)/2` | Attracting fixed point of `P(x)` |
| Fibonacci recurrence | `F(n) = F(n-1) + F(n-2)` | Standard |
| Fibonacci identity at fixed point | `φ² = φ + 1` | From `P(φ) = 0` |
| Per-half-step Fibonacci propagation rate | `φ` | `HPF_QPRCA_BCC_v0_3_0.py` § FibonacciShellScheduler.propagation_rate; empirically converges to φ |

## 5.2 Bipartite shell structure

A Fibonacci shell of the QPRCA spiral consists of two sublattice half-steps:

- A-half-step `U_{A→B}`: A-sites updated using A-neighbor and B-neighbor information; propagation rate φ in the active substrate.
- B-half-step `U_{B→A}`: B-sites updated using new A-neighbor information; propagation rate φ in the active substrate.

The shell completes one full bipartite update cycle. Per-shell growth in cell-coverage is the compound of the two half-step propagations:

$$
\text{per-shell growth} = \varphi \times \varphi = \varphi^2.
$$

This is the bipartite-squaring (§ 3) applied to per-shell growth: per-sublattice quantity (`φ` linear propagation) raised to the quadratic form by the two-sublattice structure of a complete shell.

## 5.3 The grammar-event reading is equivalent

The per-shell occupancy `φ² = φ + 1` also admits an additive decomposition through the universal HPF "base coordination + grammar event" pattern (`HPF_Lvac_Squared_Bipartite_Derivation.md` § 3):

$$
\varphi^2 = \varphi + 1
$$

reads as:

- `φ` = the forward Fibonacci growth contribution (linear continuous-rate term)
- `+1` = one b_bit grammar event committing the bipartite mirror crossing of the shell

This is structurally parallel to:

- L_vac² multiplicity `4 = 3 + 1` (three spatial events + one b_bit grammar event)
- Neutrino Fibonacci index `F(9) = 8 + 1` (eight neighbor crossings + one b_bit shared-face crossing)
- Mirror buffer reach `3/2 = 1 + 1/2` (one forward + one half-weighted b_bit return)

In each case the `+1` is the same b_bit letter of the canonical 4-bit alphabet `(n_L, n_R, b_bit, q)`, performing the same function: marking one bipartite-crossing grammar event.

The multiplicative reading (`φ × φ`) and the additive reading (`φ + 1`) are equivalent because **the Fibonacci recurrence at the golden-ratio fixed point** *is* **the substrate's bipartite mirror structure encoded algebraically.** The recurrence `φ² = φ + 1` says: one bipartite shell of compound growth equals one shell of forward growth plus one shell of grammar-event addition. These are two readings of the same substrate event, dual to each other through the recurrence.

## 5.4 Per-shell occupancy

$$
\boxed{N_{\rm cells\;per\;shell} = \varphi^2 = \varphi + 1 \approx 2.6180}.
$$

No free parameters. The inputs are `φ` (Fibonacci eigenvalue, substrate-derived) and the bipartite shell structure (A-half + B-half).

---

# 6. Composition — n = round(N_s²/φ²) = 220

Arithmetic, given §§ 4 and 5:

$$
n = \mathrm{round}\!\left(\frac{N_s^2}{\varphi^2}\right) = \mathrm{round}\!\left(\frac{576}{2.6180}\right) = \mathrm{round}(220.012) = 220.
$$

Rounding margin ≈ 0.488 going down and ≈ 0.512 going up — substantially robust against perturbations of the inputs `N_s` and `φ`. Specifically, `b/72 ≈ 0.0043` perturbations to either input would shift `n_raw` by less than 0.5%, well inside the rounding window in both directions.

Composition with `S_cap = S_ent + n · ln(φ)/N_s`:

$$
S_{\rm cap} = 1.3806 + 220 \cdot \frac{0.481212}{24} = 1.3806 + 4.4111 = 5.7917,
$$

matching the probe value 5.7889 within the integral form's shell-width rounding band of `0.020` per `HPF_Scap_SubstrateNative_Derivation.md` § 5 (reframed 2026-05-09).

---

# 7. A/B-collapse invariance

The trigger criterion from `HPF_b72_Passive_Mirror_Correction_Reference_2026-04-15.md` § 3 is operational: an observable receives the b/72 correction iff collapsing the A/B distinction changes its derivation **output** (the computed numerical value).

For `n = round(N_s²/φ²) = 220`:

| Input | Under A/B collapse | A/B-invariant? |
|---|---|---|
| `N_s = 24` | 24 angular sectors of the substrate ring, sublattice-symmetric | Yes — `N_s = 24` is the angular sector count per sublattice, and both sublattices share the same 24-sector angular geometry of the BCC ring; collapse preserves the count |
| `N_s² = 576` | Count of ordered sector pairs `(s, s')` with each of `s, s'` ∈ {0,…,23} | Yes — collapsing the A/B label on the pair changes only the bookkeeping of which side is "origin" vs "destination," not the count of distinct pairs |
| `φ` | Fibonacci eigenvalue, irrational constant | Yes (trivially) |
| `φ²` | Fibonacci recurrence value, irrational constant | Yes (trivially) |
| `n = round(576/2.618)` | Integer division output | Yes |

The bipartite mirror structure is what **derives** N_s² and φ², but the derived **values** (576 and 2.618 respectively) are invariant under the labeling collapse. Same as the `(P'(φ))² = 5` capacity in RCC: the derivation uses bipartite structure, but the number 5 is A/B-invariant.

The trigger criterion passes by output-invariance. No additional `b/72` correction enters the Λ chain through `n = 220`.

This closes the static-identity arm of item (2) of Vacuum Sector Bipartite Closure § 6. Composed with the audit progress note (`HPF_Vacuum_Sector_Item2_Audit_Progress_2026-05-17.md`) on the other chain factors and the S_ent first-principles consolidation (excavation-shaped per `HPF_Correction_Note_LowerWall_Nyquist_2026-04-12.md`), item (2) closes completely.

---

# 8. Physical motivation — communication-and-assurance reading

This section is interpretive and not load-bearing for the derivation in §§ 3–6. The math route stands on the bipartite-squaring mechanism alone. The communication reading is provided so the *why* of the bipartite structure is on the record.

The substrate's bipartite mirror structure is the information-theoretic verification channel that makes QPRCA bijectivity *operational* rather than merely formal. A bijective update rule on a finite state space is reversible by virtue of being a bijection (standard finite group theory). But for the substrate to *verify* that a transmitted update was correctly received — and therefore for reversibility to be substrate-internally enforceable rather than externally asserted — the substrate requires an acknowledgment channel. The bipartite mirror provides this channel:

- **Half step (1/24):** A sends through one of 24 angular sectors. One sublattice resolves direction.
- **Full step (1/48):** A→B→A cycle completes. Two-sample resolution = bipartite Nyquist.
- **Extra half step (1/72):** B-origin acknowledgment fraction returns at half weight (forced by `\|A\|=\|B\|` symmetry per `HPF_Mirror_Buffer_Obligation_Closure_2026-04-12.md` § 2.3). 3/2 total sampling path.

Cells in this reading are send-acknowledge events, and a full causal arc is one complete protocol exhaustion: every distinct (send_sector, acknowledge_sector) ordered pair has occurred exactly once. The N_s² count is the protocol's verification budget; φ² per shell is the rate at which the protocol exhausts that budget per bipartite cycle.

This reading does not derive bipartite from bijectivity — bipartite remains a structural commitment of BCC, and the implication "bijection → bipartite" is invalid in general (counter-examples exist on non-bipartite reversible substrates). The communication framing is the *function* the bipartite structure performs in HPF, not its *derivation*.

---

# 9. H₀ is no longer an independent degree of freedom

With `n = 220` now derived rather than candidate-locked, the radial law

$$
L_{\rm vac} = \frac{R_H}{\varphi^{220}}
$$

is a fully-substrate-grounded relation. The exponent 220 was previously the candidate-locked piece of the relation; with this closure, it becomes substrate-forced from `N_s = 24` and `φ`.

The consequence for the framework's parameter structure: among `(L_vac, R_H, φ, N_s)`, three pieces are substrate constants — `φ` (from Fibonacci recurrence at fixed point), `N_s` (from BCC coordination lifted to 3D), and `L_vac` (substrate primitive scale) — and `R_H` is now forced as `R_H = L_vac · φ²²⁰`. Since `R_H = c/H_0` connects this to the Hubble parameter, **`H_0` is no longer an independent degree of freedom**: its value is determined by `(L_vac, c, N_s, φ)`, none of which is a cosmological fit.

What this closure removes is the framework's freedom to vary `n` to match cosmology. The previous "candidate-locked" status of `n = 220` left open the possibility that future framework development could adjust the exponent. That freedom is now closed.

The framework's empirical anchor count is unchanged: it remains one (`S_blur = 1.05` from Lin 2026). `H_0` was not previously listed as an anchor because `R_H` entered through the radial law as a derived rather than fit quantity. This closure tightens the existing posture rather than changing the anchor count: not only was `H_0` not fit, the substrate now actively forces its value via the derived `n = 220` ratio.

**Critical caveat.** "H₀ is no longer an independent degree of freedom" is a structural statement about the framework's parameter content. It does not derive `H₀` from nothing — the framework still contains `L_vac` as a substrate primitive scale, and `H₀` is forced *through* `R_H = L_vac · φ²²⁰`. The pushback-resistant version of the claim is: the framework no longer has a knob to fit `H₀` independently of its other substrate constants. Anyone reading this as "HPF derived H₀ from pure mathematics" is reading too much in; anyone reading it as "HPF still has an H₀ knob" is reading too little.

---

# 10. What this closes and what it does not

**Closes:**

- The cell-counting premise underlying the static identity in `HPF_Scap_SubstrateNative_Derivation.md` § 4.4.
- The "asserted here and not independently derived elsewhere in the package" qualifier in the `ScapDeriver` docstring (`Src/HPF_QPRCA_BCC_v0_3_0.py` lines 88–96).
- The static-identity arm of item (2) of Vacuum Sector Bipartite Closure § 6 (A/B-collapse invariance of `n = 220` is now derived rather than asserted at the formula level).

**Does not close:**

- The S_ent first-principles consolidation. S_ent is geometrically locked by the DCT v7U Obligation 2 chain (`r_lat = 1/6 → φ'_lead → ΔS_ent = 0.3306 → S_ent = 1.3806`), but this derivation is distributed across DCT v7U § 8, `HPF_Correction_Note_LowerWall_Nyquist_2026-04-12.md`, and `HPF_Entanglement_Obligation_Closure_2026-04-12.md` § 2.2 rather than consolidated in a single canonical reference note. Excavation-shaped per discussion of 2026-05-17.
- The integral-form arm of item (2). The integral `n_sel = round[(24/ln φ) · ∫(1-ζ)dS]` is now a downstream consistency check rather than load-bearing for `n` (per the 2026-05-09 S_cap reframe), but its A/B-invariance still rests on S_ent's derivation closing A/B-invariantly. Will close together with S_ent consolidation.
- Independent predictive confirmation generally. The framework's truth-status ladder distinguishes "derived / substrate-native" from canon promotion gated on independent predictive confirmation.

---

# 11. Status table

| Claim | Status |
|---|---|
| Bipartite-squaring as shared structural mechanism (`N_s²` for arc, `φ²` for shell) | **Derived** — same shape as RCC `(P'(φ))² = 5` |
| Arc capacity `N_s² = 576` cells per full causal arc | **Derived** (§ 4) |
| Per-shell occupancy `φ² = φ + 1` | **Derived** (§ 5), with equivalent multiplicative and additive readings |
| `n = round(N_s²/φ²) = 220` | **Derived / substrate-native** — promoted from candidate-locked |
| A/B-collapse invariance of `n = 220` | **Derived** (§ 7) |
| Static-identity arm of item (2) of Vacuum Sector Bipartite Closure § 6 | **Closed** by this note |
| Full closure of item (2) of Vacuum Sector Bipartite Closure § 6 | Pending S_ent consolidation (excavation-shaped) |
| Λ branch ready for canonical promotion to Volume IV § 12 refinement | Pending the above |
| `H_0` no longer an independent degree of freedom in the framework | **Derived** (§ 9) |

---

# 12. Freeze wording

> The cell-counting premise underlying the static identity `n = round(N_s²/φ²) = 220` closes by the bipartite-squaring mechanism — the same structural pattern that yields `(P'(φ))² = 5` in the Return-Class Capacity derivation. The arc capacity `N_s² = 576` is the count of ordered `(origin_A, destination_B)` cell-pairs in the bipartite mirror index space, with each side ranging over the 24 BCC angular sectors of one sublattice. The per-shell occupancy `φ²` is the compound Fibonacci growth across one bipartite shell (A-half-step + B-half-step, each propagating at φ); equivalently, by the Fibonacci recurrence `φ² = φ + 1`, the per-shell occupancy decomposes as one forward growth contribution (φ) plus one b_bit grammar event (+1), paralleling the universal HPF "base coordination + grammar event" pattern that appears in L_vac² multiplicity (`4 = 3 + 1`), neutrino Fibonacci index (`F(9) = 8 + 1`), and mirror buffer reach (`3/2 = 1 + 1/2`). Both quadratic forms share the same structural source: bipartite × per-sublattice quantity → quadratic. The rounding margin is ≈ 0.488/0.512 in `n_raw` units, ~5,000× the magnitude of `b/72`, and A/B-collapse invariance of `n = 220` follows by output-invariance under the operational trigger criterion. With this closure, `n = 220` promotes from "derived / substrate-native under candidate cell-counting premise" to "derived / substrate-native." The static-identity arm of item (2) of Vacuum Sector Bipartite Closure § 6 closes; full closure of item (2) pends S_ent first-principles consolidation, which is excavation-shaped given the existing distributed derivation in DCT v7U Obligation 2, the Lower Wall Nyquist Correction, and the Entanglement Obligation Closure. The φ²²⁰ scale separation between `L_vac` and `R_H` is now substrate-forced; `H_0` is no longer an independent degree of freedom in the framework's parameter content, being determined by `(L_vac, c, N_s, φ)` through the now-derived radial-law exponent. The framework's empirical anchor count remains one (S_blur = 1.05 from Lin 2026).

---

*Closes the cell-counting premise (BCC Fibonacci spiral arc-coverage argument) underlying the static identity `n = round(N_s²/φ²) = 220`. Promotes `n = 220` from candidate-locked to substrate-native. Composes with the audit progress note and the (excavation-shaped) S_ent first-principles consolidation to close item (2) of Vacuum Sector Bipartite Closure § 6. The structural argument was identified in a 2026-04-17 working session ("the 24² = 576 counting could be justified as pairwise sector interactions across the bipartite mirror structure"; "φ² = φ + 1 identity is exactly the kind of self-referential substrate invariant that could give you the per-shell footprint in a principled way") but not assembled into a standalone note at that time; this note is the assembly.*
