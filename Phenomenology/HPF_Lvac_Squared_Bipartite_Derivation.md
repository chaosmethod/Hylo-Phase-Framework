# HPF Derivation — L_vac² Bipartite Multiplicity on the BCC Lattice (3+1 Structure, b_bit-Grounded)

**Document Class:** HPF phenomenology derivation note (formal closure, v4 consolidated)  
**Date:** 2026-05-03 (v4 derivation); 2026-05-05 (consolidation)  
**Author:** Eric Keaton Porter  
**Status:** Formal substrate-native derivation. Closes pending item (1) from Vacuum Sector Bipartite Closure (2026-04-30) § 6. Grounded in the canonical 4-bit grammar $(n_L, n_R, b_{\text{bit}}, q)$ — the +1 grammar event is identified with the dedicated b_bit letter of the substrate alphabet.  
**Compatibility:** Refines V § 5.1 (BCC geometric inputs) and Vacuum Sector Bipartite Closure § 2.4 (Λ application). Imports trigger criterion from Mirror Buffer Entanglement Closure (2026-04-30). Aligns with neutrino F(9) = 8+1 (Neutrino Mass Hierarchy Candidate Note explicitly identifying the +1 as the b_bit bridge commitment), Bell-Tsirelson chiral doubling on the (n_L, n_R) sector (Bell-Tsirelson Candidate Note), 4-bit grammar lock (Fine Structure Constant Candidate Note), and 3+1 spacetime fusion (Dimensional Closure and 3D Forging).

**Consolidation note (2026-05-05):** This is the consolidated single-canonical version of the L_vac² Bipartite Multiplicity derivation, replacing prior standalone v1, v2, and v3 documents. The body (§§ 1–12) is the v4 derivation. Appendix B has been expanded from v4's original short summary to preserve the concrete mathematical content of v1, v2, v3 — including their formulas and the specific structural arguments that were superseded — so that the derivation history is auditable rather than only summarized.

---

## Abstract

The cosmological constant scales as $\Lambda \propto 1/L_{\mathrm{vac}}^{2}$ on the HPF substrate. This note derives formally that $L_{\mathrm{vac}}^{2}$ inherits a **3+1 bipartite correction** of the form $(1 - 4\,b/72)$ from:

1. **3 spatial bipartite events** — one per spatial dimension that L_vac² spans in the 3D-closure-stable substrate, contributed through the directional address bits $(n_L, n_R)$ of the canonical 4-bit grammar
2. **+1 grammar event** — the dedicated **b_bit** letter of the substrate alphabet $(n_L, n_R, b_{\text{bit}}, q)$, encoding the sublattice-crossing commitment as its own structural contribution

The +1 is **not** an abstract "grammar event" — it is literally the b_bit letter of the canonical 4-bit grammar doing its dedicated job. This is the same b_bit that contributes the +1 in:

- Neutrino F(9) = **8** (BCC neighbors via $n_L, n_R, q$ projections) **+1** (b_bit bridge commitment) — explicitly identified in Neutrino Mass Hierarchy Candidate Note
- Mirror buffer **3/2** = **1** (forward) **+1/2** (return half via b_bit-mediated bipartite return)
- Tsirelson chiral doubling on the $(n_L, n_R)$ sector

The correction is applied linearly per the universal HPF pattern. Numerical closure: $\Lambda_{\mathrm{corrected}} = 1.0997 \times 10^{-52}$ m⁻², gap to observation 0.027%.

---

## 1. Substrate Foundation

### 1.1 BCC bipartite structure

The HPF substrate is a body-centered cubic (BCC) lattice partitioned into two disjoint sublattices A and B, with all nearest-neighbor edges connecting A↔B (Volume IV § 1).

### 1.2 Bipartite update rule

The global reversible update is $U = U_B \circ U_A$ — strictly sequential and reversible.

### 1.3 The 3+1 spacetime structure (canonical phenomenology)

From Dimensional Closure and 3D Forging (Phenomenology/, non-canonical exploratory but repo-consistent):

> *3D did not lose time. It kept both space and time by forcing them into one regulated relation.*  
> *4D lost an independent freedom; 3D retained both space and time in fused regulated form.*

Time is **fused into the substrate** at the L_vac scale, not added as a primitive coordination direction. The 8-fold BCC coordination already encodes this fusion through the U_B ∘ U_A update sequence (the alternation IS the temporal flow).

**Consequence:** The substrate operates in a 3+1 structure where:
- **3 spatial dimensions** are independently bipartite-resolvable
- **+1 temporal fold** is fused into the update sequence as a single grammar event

### 1.4 Trigger criterion (imported)

From Mirror Buffer Entanglement Closure:

> An observable receives the $b/72$ correction if and only if collapsing the $A/B$ distinction changes its derivation output. Each independent $A/B$ collapse contributes one $b/72$.

---

## 2. The Canonical 4-Bit Grammar — Substrate Alphabet

### 2.1 The 4-letter alphabet

The HPF substrate has a canonical-locked 4-bit grammar (Fine Structure Constant Candidate Note, 2026-04-10):

$$\mathcal{A} = (n_L,\ n_R,\ b_{\text{bit}},\ q)$$

The four letters of the BCC substrate alphabet:

| Letter | Role | Function |
|---|---|---|
| $n_L$ | Left occupancy bit | Directional address, left chirality |
| $n_R$ | Right occupancy bit | Directional address, right chirality |
| $b_{\text{bit}}$ | Bipartite bridge bit | Sublattice-crossing grammar event |
| $q$ | Internal indicator | Charge/internal state |

This gives $2^4 = 16$ states total, with the (0,0,0,0) vacuum state excluded → **15 active non-vacuum microstates** (Fine Structure Constant Note, line 67).

### 2.2 The b_bit as the dedicated grammar-event letter

The b_bit is **not** a redundant directional bit. It is the canonical letter that encodes **the act of crossing the bipartite sublattice boundary as its own grammar event**, independent of the directional or internal bits.

This is explicit in the Neutrino Mass Hierarchy Candidate Note (line 401):

> *The BCC lattice has 8 nearest neighbors, and the bipartite shared-face traversal contributes +1 through the **b-bit bridge commitment** — the act of crossing the sublattice boundary is its own grammar event, independent of the 8 neighbor relationships — yielding Fibonacci index 9.*

The b_bit is the substrate's dedicated letter for marking sublattice transitions. It is to the BCC substrate what a delimiter is to a written language — its own signal, separate from the content letters.

### 2.3 The chirality components n_Lh and n_Rh

The chirality decompositions $n_{Lh}$ and $n_{Rh}$ (Bell-Tsirelson Candidate Note) are *helicity refinements within* the directional bits $n_L$ and $n_R$. They are not separate letters of the alphabet. The 4-bit grammar lock is fixed at $(n_L, n_R, b_{\text{bit}}, q)$.

### 2.4 Why this matters for L_vac²

The L_vac² correction must be expressible in terms of operations on the canonical 4-letter alphabet. If the +1 grammar event in the 3+1 structure has any meaning, it must correspond to a specific letter or operation in $\mathcal{A}$.

**Claim (developed in § 5):** The +1 in 3+1 = the b_bit letter, doing exactly the same job it does in neutrino F(9) and mirror buffer 3/2.

---

## 3. The Universal "Base + Grammar Event" Pattern in HPF

Before deriving the L_vac² correction, we establish that the repo handles bipartite contributions through a consistent pattern of **linear addition of grammar events to base coordination**, NOT through multiplicative independence. The grammar event in every case corresponds to the b_bit letter of the canonical alphabet.

### 3.1 Neutrino F(9) = 8 + 1 — explicit b_bit identification

From Neutrino Mass Hierarchy Candidate Note (2026-04-11):

> *The BCC lattice has 8 nearest neighbors, and the bipartite shared-face traversal contributes +1 through the **b-bit bridge commitment** — the act of crossing the sublattice boundary is its own grammar event, independent of the 8 neighbor relationships — yielding Fibonacci index 9.*

Structure: **8 (base, via $n_L, n_R, q$ projections across BCC neighbors) + 1 (b_bit) = 9**, applied linearly.

### 3.2 Mirror buffer 3/2 = 1 + 1/2

From Mirror Buffer Obligation Closure (2026-04-12):

> *Total effective sampling path: 1 + 1/2 = 3/2.*

Structure: **1 (forward) + 1/2 (return half) = 3/2**, applied linearly. The return-half is the b_bit-mediated bipartite-return contribution at half-weight (forced by bipartite symmetry, $|A|=|B|$).

### 3.3 Bell-Tsirelson chiral doubling

From Bell-Tsirelson Candidate Note (2026-04-12):

> *A CHSH measurement is a one-way probe resolving both chiral components $n_{Lh}$ and $n_{Rh}$ simultaneously, doubling the effective angular span to π/4*

Structure: operates on the $(n_L, n_R)$ directional sector of the alphabet, doubling angular span linearly (not squared).

### 3.4 The pattern with letter assignments

| Observable | Base (alphabet projection) | + Grammar event | = Total |
|---|---|---|---|
| Neutrino F(9) | 8 (BCC neighbors via $n_L, n_R, q$) | +1 (**b_bit**) | 9 |
| Mirror sampling | 1 (forward) | +1/2 (**b_bit**-mediated return) | 3/2 |
| Tsirelson | 3/2 (one chirality of $n_L, n_R$) | +3/2 (other chirality of $n_L, n_R$) | π/4 |

**HPF universally treats bipartite-plus-grammar contributions as linear addition, with the b_bit letter providing the grammar event.** This is the pattern L_vac² must follow.

---

## 4. $L_{\mathrm{vac}}$ as a Bipartite Substrate Length

### 4.1 The radial law

From Volume IV § 3:
$$L_{\mathrm{vac}} = \frac{R_H}{\phi^n}, \qquad n = 220$$

$L_{\mathrm{vac}} \approx 1.45 \times 10^{-20}$ m is the universal substrate resolution scale.

### 4.2 $L_{\mathrm{vac}}$ as a primitive bipartite segment

In the BCC graph, the smallest substrate distance corresponds to a nearest-neighbor edge — which **always** connects an A-site to a B-site. Every L_vac measurement is bipartite at its origin, with the b_bit letter active during the crossing.

### 4.3 The internal round-trip structure (from LMS)

From Lattice Mirror Symmetry (2026-04-04) and Mirror Buffer Obligation Closure (2026-04-12), an L_vac measurement involves:
- Forward leg: object warps substrate (1 unit, b_bit set on outbound crossing)
- Return leg: substrate returns warp to observer (1/2 unit, via bipartite weighting; b_bit set on return crossing)

Total effective path: **3/2** per L_vac measurement.

This is one bipartite event (one b_bit grammar event) per L_vac. The round-trip is itself the single bipartite-grammar contribution at the L_vac scale.

---

## 5. Counting Collapses for $L_{\mathrm{vac}}^{2}$ in the 3+1 Structure

### 5.1 What L_vac² actually is in the substrate

$\Lambda$ has dimension (length)$^{-2}$, so $\Lambda \propto 1/L_{\mathrm{vac}}^{2}$.

In a fused 3+1 spacetime substrate (per § 1.3), $L_{\mathrm{vac}}^{2}$ is **NOT** "two independent length factors that can be multiplied multiplicatively." It is **one fused area-like observable** spanning 3 spatial dimensions and 1 temporal fold.

### 5.2 The 3+1 collapse count — letter by letter

For $L_{\mathrm{vac}}^{2}$ as a fused spacetime observable:

| Source | Letter / Operation | Collapses |
|---|---|---|
| 1st spatial bipartite event | $(n_L, n_R)$ projection on x-axis | 1 |
| 2nd spatial bipartite event | $(n_L, n_R)$ projection on y-axis | 1 |
| 3rd spatial bipartite event | $(n_L, n_R)$ projection on z-axis | 1 |
| Temporal fold grammar event | **b_bit** commitment | 1 |
| **Total** | | **4 = 3 + 1** |

The structure is **3 spatial + 1 b_bit = 4**, applied linearly per the universal HPF pattern.

### 5.3 The +1 IS the b_bit letter

This is the critical identification. The +1 grammar event in 3+1 is **not abstract** — it is specifically the b_bit letter of the canonical 4-bit alphabet, performing exactly the function defined in the Neutrino Mass Hierarchy Candidate Note:

> *"the b-bit bridge commitment — the act of crossing the sublattice boundary is its own grammar event"*

The b_bit is the single dedicated letter for marking sublattice transitions. In the 3+1 structure for L_vac²:
- The 3 spatial events are projections through the directional sector $(n_L, n_R)$
- The +1 is the b_bit letter committing the temporal-fold/sublattice-crossing as its own grammar event

This grounds the +1 in the canonical alphabet — it is not added by hand. It is what the b_bit letter is FOR.

### 5.4 Why 3 spatial events (not 2)

In a 3D-closure-stable substrate, the area-like quantity $L_{\mathrm{vac}}^{2}$ spans the volumetric/areal substrate. The vacuum-sector observable $\Lambda$ couples to the FULL spatial substrate, not just to a 2D plane.

This matches the canonical phenomenology: $a_3$ is "**volumetric** regulator availability, stable renormalizing capacity, lawful closure under load" (Dimensional Closure, § 4.3).

The vacuum-sector observable inherits all 3 spatial directions because the regulator availability $a_{\mathrm{vac}}$ is the **3D closure output**, not a planar projection. Each spatial direction contributes one $(n_L, n_R)$ projection event.

### 5.5 Why exactly +1 b_bit (not 0 or 2)

The 4-bit grammar has **exactly one** b_bit. There is no "second b_bit" in the canonical alphabet — the bipartite-crossing grammar is encoded by a single dedicated letter.

This is forced by the substrate alphabet itself:
1. The grammar lock $(n_L, n_R, b_{\text{bit}}, q)$ has one and only one b_bit
2. The b_bit is dedicated to sublattice-crossing commitment (not directional, not internal)
3. A sublattice-crossing is one grammar event regardless of how many spatial directions are involved
4. Therefore L_vac² has +1 (one b_bit), not +2 or +3

This is the same reason neutrino F(9) has +1 and not more: there's only one b_bit in the alphabet, and it can only commit once per grammar event.

---

## 6. Linear Application of the Correction

### 6.1 The substrate-native form

Each of the 4 collapses (3 spatial $(n_L, n_R)$ events + 1 b_bit) contributes one $b/72$ correction. They add linearly per the universal HPF pattern:

$$L_{\mathrm{vac}}^{2} \;\longrightarrow\; L_{\mathrm{vac}}^{2}\,\bigl(1 - 4\,\tfrac{b}{72}\bigr)$$

NOT:
$$L_{\mathrm{vac}}^{2} \;\longrightarrow\; L_{\mathrm{vac}}^{2}\,\bigl(1 - 2\,\tfrac{b}{72}\bigr)^{2}$$

The squared form would imply two **independent** length factors with multiplicative independence — which contradicts both the canonical fused-spacetime substrate phenomenology AND the 4-bit grammar (which has one dedicated b_bit, not two).

### 6.2 Decomposition

$$1 - 4\,\tfrac{b}{72} \;=\; 1 - \underbrace{3\,\tfrac{b}{72}}_{\text{3 spatial }(n_L, n_R)\text{ events}} - \underbrace{\tfrac{b}{72}}_{\text{+1 b\_bit grammar event}}$$

This makes the 3+1 structure explicit in the formula, with each contribution traced back to a specific letter or operation in the canonical alphabet.

### 6.3 Comparison: linear (3+1) vs squared (independent multiplication)

At leading order in $b/72$:

| Form | Leading order | Numerical coefficient |
|---|---|---|
| Linear (3+1) | $1 + 4(b/72)$ | 4 |
| Squared | $1 + 4(b/72) + 4(b/72)^2$ | 4 + ε |

The leading-order coefficient is the same (4). The difference appears at second order:
- Linear: no second-order term
- Squared: second-order term of $4(b/72)^2 \approx 7.2 \times 10^{-5}$

The squared form's spurious second-order term is the artifact of treating L_vac² as two independent factors — which would require two independent b_bit letters. The canonical alphabet has only one. The squared form is therefore alphabetically inconsistent.

---

## 7. Propagation Through $\Lambda \propto 1/L_{\mathrm{vac}}^{2}$

### 7.1 Direct substitution

$$\Lambda_{\mathrm{corrected}} \;=\; \frac{\Lambda_{\mathrm{raw}}}{1 - 4\,b/72}$$

### 7.2 Numerical verification

| Quantity | Value |
|---|---:|
| $b = \ln\varphi/(\pi/2)$ | $0.30634896$ |
| $b/72$ | $0.00425485$ |
| $4\,(b/72)$ | $0.01701942$ |
| $1 - 4\,b/72$ | $0.98298058$ |
| $\Lambda_{\mathrm{raw}}$ | $1.0810 \times 10^{-52}$ m⁻² |
| $\Lambda_{\mathrm{corrected}}$ | $\mathbf{1.0997 \times 10^{-52}}$ **m⁻²** |
| Observed | $1.1000 \times 10^{-52}$ m⁻² |
| **Gap** | **0.027%** |

This is marginally closer to observation than the squared form (0.027% vs 0.036%) and structurally consistent with the universal HPF pattern AND the 4-bit grammar lock.

---

## 8. Cross-Check Against the Repo's Universal Pattern

### 8.1 Pattern table (extended with letter assignments)

| Observable | Base (alphabet projection) | + Grammar event | = Total | Application |
|---|---|---|---|---|
| Neutrino F(9) | 8 ($n_L, n_R, q$ across BCC neighbors) | +1 (**b_bit**) | 9 | Linear |
| Mirror sampling | 1 (forward) | +1/2 (**b_bit**-mediated return) | 3/2 | Linear |
| Tsirelson | 3/2 (one chirality of $(n_L, n_R)$) | +3/2 (other chirality of $(n_L, n_R)$) | π/4 | Linear |
| **L_vac² for Λ** | **3 (three $(n_L, n_R)$ spatial events)** | **+1 (b_bit)** | **4** | **Linear** |

The L_vac² correction follows exactly the same pattern as everything else in the repo, with the +1 traced to the canonical b_bit letter in every case.

### 8.2 Why this matters

The squared form would have made L_vac² the **only** observable in the repo handled multiplicatively across "independent factors." That would have required:

1. Two independent b_bit letters (the canonical alphabet has only one)
2. Treating spacetime as un-fused at the L_vac scale (canonical phenomenology says it's fused)
3. Special pleading for L_vac² alone (no other observable does this)

The 3+1 linear form preserves the substrate's regulatory fusion, respects the 4-bit grammar lock, and matches the universal HPF pattern. It is the only form structurally consistent with the rest of the framework.

---

## 9. Status Summary

| Claim | Status | Justification |
|---|---|---|
| BCC substrate is bipartite | **Substrate-native** | Volume IV § 1 |
| Substrate is 3+1 fused (not 4D un-fused) | **Phenomenology-canonical** | Dimensional Closure note |
| 4-bit grammar lock $(n_L, n_R, b_{\text{bit}}, q)$ | **Canon-locked** | Fine Structure Constant Candidate Note |
| b_bit is the dedicated grammar-event letter | **Substrate-native** | Neutrino Note line 401 (explicit) |
| L_vac is a bipartite segment | **Derived** | BCC nearest-neighbor edges |
| L_vac has internal round-trip 3/2 | **Derived** | LMS round-trip + bipartite weighting |
| L_vac² in fused spacetime is one observable | **Derived** | 3+1 fusion at L_vac scale |
| 3 spatial collapse events from $(n_L, n_R)$ | **Derived** | Volumetric coupling × 3 dimensions |
| +1 b_bit grammar event | **Derived** | Universal pattern (neutrino, mirror, etc.); explicit alphabet identification |
| Linear addition of 4 collapses | **Derived** | Universal HPF pattern (§ 3) |
| $\Lambda_{\mathrm{corrected}} = 1.0997 \times 10^{-52}$ m⁻² | **Verified** | Numerical (§ 7.2) |
| Gap to observation: 0.027% | **Verified** | Empirical match |
| Consistent with repo's universal pattern | **Verified** | Cross-check table (§ 8.1) |
| Consistent with 4-bit grammar lock | **Verified** | One b_bit per alphabet, one b_bit per L_vac² |

---

## 10. What This Closure Accomplishes

Closes pending item **(1)** from Vacuum Sector Bipartite Closure (2026-04-30) § 6.

✅ **Closed with substrate-correct 3+1 form, grounded in the canonical 4-bit grammar.**

The derivation establishes:
1. Why L_vac² is one fused observable (not two independent factors): 3+1 spacetime fusion + one b_bit per alphabet
2. Why the collapse count is 4 = 3+1 (spatial $(n_L, n_R)$ + one b_bit)
3. Why the application is linear (universal HPF pattern + alphabet structure)
4. Why the squared form was an error (imports un-fused independence + would require two b_bits)

### 10.1 Remaining items for canonical promotion

| Item | Status |
|---|---|
| (1) Formal $L_{\mathrm{vac}}^{2}$ bipartite derivation | ✅ **Closed by this note (3+1 b_bit-grounded form)** |
| (2) Confirmation that no additional bipartite-sensitive factors enter elsewhere in the Λ chain | ⏳ Pending |
| (3) Independent execution-lock via 256/256 existence-sensor sweep | ✅ **Closed — see Appendix D (sweep run 2026-05-05, Strong Pass on all six aggregate × model combinations)** |

---

## 11. Reconciliation with Vacuum Sector Bipartite Closure § 2.4

The Vacuum Sector Bipartite Closure note writes:

$$\Lambda_{\mathrm{corrected}} = \frac{\Lambda_{\mathrm{raw}}}{(1 - 2\,b/72)^{2}}$$

This formula was a first attempt at the structural derivation. Numerically it gives **1.0996 × 10⁻⁵² m⁻²**, gap 0.036%.

The 3+1 substrate-correct form gives:

$$\Lambda_{\mathrm{corrected}} = \frac{\Lambda_{\mathrm{raw}}}{1 - 4\,b/72}$$

Numerically: **1.0997 × 10⁻⁵² m⁻²**, gap 0.027%.

**The two forms agree to 4 significant figures** because $(1-2x)^2 \approx 1 - 4x + O(x^2)$ for small x.

But **structurally they say different things**:
- Squared form: implies 2 independent length factors with two independent b_bit commitments (alphabetically inconsistent)
- Linear 3+1 form: implies 4 collapse events in fused spacetime, applied linearly with one b_bit (alphabet-consistent)

**Recommendation:** Update Vacuum Sector Bipartite Closure § 2.4 to use the linear 3+1 form, with this note as the formal derivation closure.

---

## 12. Freeze Wording

> $L_{\mathrm{vac}}^{2}$ in $\Lambda \propto 1/L_{\mathrm{vac}}^{2}$ inherits a $(1 - 4b/72)$ correction in the BCC bipartite substrate, decomposing as 3 spatial bipartite events (projections through the directional sector $(n_L, n_R)$ of the canonical 4-bit grammar) + 1 b_bit grammar event (the dedicated bipartite-crossing letter of the substrate alphabet $(n_L, n_R, b_{\text{bit}}, q)$). The +1 is not abstract — it is literally the b_bit letter performing the same function it performs in the neutrino F(9) = 8 + 1 derivation, the mirror buffer 3/2 = 1 + 1/2 derivation, and elsewhere. The correction is applied linearly per the universal HPF pattern of "base coordination + grammar event" addition. The squared form $(1-2b/72)^2$ would require two independent b_bit letters (the canonical alphabet has only one) and import multiplicative independence between two L_vac factors (contradicts the fused-spacetime phenomenology). Numerically, $\Lambda_{\mathrm{corrected}} = \Lambda_{\mathrm{raw}}/(1 - 4b/72) = 1.0997 \times 10^{-52}$ m⁻², closing the gap to observation at 0.027%. No new parameters are introduced; b/72 is the same passive Nyquist residual derived in the Mirror Buffer Obligation Closure (2026-04-12), and the b_bit is the same canonical alphabet letter locked in the 4-bit grammar.

---

## Appendix A — Why This Is Not Circular

Five independent inputs, none tuned to observation:

1. **Dimensional analysis** forces $\Lambda \sim 1/(\text{length})^{2}$
2. **BCC bipartite structure** + **3+1 fused spacetime** (canonical phenomenology) forces L_vac² to be a fused observable, not two independent factors
3. **4-bit grammar lock** $(n_L, n_R, b_{\text{bit}}, q)$ with exactly one b_bit forbids treating L_vac² as having two independent grammar events
4. **Universal HPF "base + grammar event" pattern** (verified across neutrino, mirror, Tsirelson) forces linear addition with b_bit as the +1 contributor
5. **Trigger criterion** (Mirror Buffer Entanglement Closure) provides b/72 per collapse

The 3+1 collapse count and linear application both follow from these inputs without tuning. The 0.027% match to observation is therefore a **prediction**, not a fit.

---

## Appendix B — Derivation History (v1 → v4 Progression)

This appendix preserves the concrete mathematical content of each prior version, not only a summary. The derivation passed through three superseded forms before reaching the current alphabet-grounded linear form. Each prior form is reproduced below with the formulas it actually used and the structural argument it made, so the corrections can be audited rather than taken on faith.

### B.1 — v1 (original): two-leg round-trip, multiplicity-2 framing

**Structural framing.** A measurement of L_vac was treated as a round trip:
- Outbound leg: A-sublattice → B-sublattice (one A/B crossing)
- Return leg: B-sublattice → A-sublattice (one B/A crossing)

Two crossings per single L_vac measurement.

**κ_BCC analogy as motivation.** v1 motivated the squared form by direct analogy with:

$$\kappa_{\mathrm{BCC}} = 8 \times \tfrac{1}{2} \times \tfrac{1}{2} = 2$$

The two 1/2 factors (bipartite split + LMS mirror) were taken as a structural template for L_vac² having "two bipartite boundaries" — one per length factor.

**Resulting form.** v1 carried the correction at multiplicity 2:

$$L_{\mathrm{vac}}^{2} \to L_{\mathrm{vac}}^{2}\bigl(1 - 2\,\tfrac{b}{72}\bigr)$$

**What v1 lacked.** Explicit trigger criterion (the b/72 firing rule was implicit), explicit alphabet grounding, and explicit treatment of fused 3+1 spacetime structure. The κ_BCC analogy was carried as motivation but not stress-tested against the repo's universal "base + grammar event" pattern.

### B.2 — v2 (refined squared): explicit trigger criterion, squared propagation

**What v2 added over v1.**
- §1.3 imported the explicit trigger criterion from Mirror Buffer Entanglement Closure: "An observable receives the b/72 correction if and only if collapsing the A/B distinction changes its derivation output. Each independent A/B collapse contributes one b/72."
- §7 stated the κ_BCC analogy honestly — not as proof, but as an example of bipartite factor structure with two distinct mechanisms.
- Appendix A ("Why This Is Not Circular") and Appendix C-equivalent ("Comparison with Ω_dm Multiplicity 1") were introduced. These survive into v3 and v4 unchanged in structure.

**The squared form, made explicit.**

Per-factor correction (each L_vac independently):

$$L_{\mathrm{vac}} \to L_{\mathrm{vac}}\bigl(1 - 2\,\tfrac{b}{72}\bigr)$$

Squared propagation through L_vac²:

$$L_{\mathrm{vac}}^{2} \to L_{\mathrm{vac}}^{2}\bigl(1 - 2\,\tfrac{b}{72}\bigr)^{2}$$

Λ correction:

$$\Lambda_{\mathrm{corrected}} = \frac{\Lambda_{\mathrm{raw}}}{(1 - 2b/72)^{2}} = 1.0996 \times 10^{-52}\ \text{m}^{-2}$$

**Gap to observation: 0.036%.**

**Where v2 was structurally wrong.** Caught in v3 and v4:
- §4.2 invoked "two independent length factors" with "2D integration with orthogonal directions." But in fused 3+1 substrate, no truly independent length directions exist at the L_vac scale. This was the load-bearing error.
- The squared form would require two independent b_bit grammar events. The canonical 4-bit alphabet (n_L, n_R, b_bit, q) has exactly one b_bit letter. The squared form is therefore alphabet-inadmissible. (This particular failure mode was not named until v4; v3 recognized the spacetime-fusion problem first.)
- L_vac² was treated as multiplicatively independent, making it unique among repo observables. No other observable in the repo uses multiplicative independence between sublattice-sensitive factors; the universal HPF pattern is linear addition of grammar events to base coordination.

### B.3 — v3 (3+1 linear): fused spacetime, linear application

**Structural correction.** L_vac² is one fused area-like observable spanning 3 spatial dimensions and 1 temporal fold — not two independent length factors. In 3D-closure-stable spacetime (per Dimensional Closure and 3D Forging), time is fused into the substrate at the L_vac scale; the substrate processes spatial extent and temporal evolution as one regulated relation. Treating L_vac² as multiplicatively independent imports un-fused 4D structure that the substrate explicitly does not have.

**The 3+1 collapse count.**
- 3 spatial bipartite events (one per spatial dimension that L_vac² spans)
- +1 temporal grammar event (the U_A → U_B alternation as a single sublattice transition per cycle)
- **Total: 4 = 3+1**, applied linearly per the universal HPF pattern

**The new form:**

$$L_{\mathrm{vac}}^{2} \to L_{\mathrm{vac}}^{2}\bigl(1 - 4\,\tfrac{b}{72}\bigr)$$

Decomposition with the 3+1 structure visible:

$$1 - 4\,\tfrac{b}{72} = 1 - \underbrace{3\,\tfrac{b}{72}}_{\text{3 spatial}} - \underbrace{\tfrac{b}{72}}_{\text{+1 temporal}}$$

**Λ correction:**

$$\Lambda_{\mathrm{corrected}} = \frac{\Lambda_{\mathrm{raw}}}{1 - 4b/72} = 1.0997 \times 10^{-52}\ \text{m}^{-2}$$

**Gap to observation: 0.027%.**

**Why the numerical agreement masked the v2 structural error.** The leading-order Taylor expansion of the squared form is $(1 - 2x)^{2} = 1 - 4x + 4x^{2} \approx 1 - 4x$ for small x. So the linear and squared forms agree numerically to four significant figures. The difference appears at second order — the squared form has a spurious $4(b/72)^{2} \approx 7.2 \times 10^{-5}$ correction that the linear form correctly does not produce. The numerical proximity is what allowed the v1/v2 squared form to look acceptable for as long as it did; only the structural argument (3+1 fusion) forced the form change. Numerical fit alone would not have caught the error.

**What v3 still lacked** (caught in v4): the +1 grammar event was identified as "temporal" without being pinned to a specific letter of the canonical alphabet. The cross-references to neutrino F(9) = 8 + 1 and mirror buffer 3/2 = 1 + 1/2 were noted as instances of "the universal pattern" but not yet tied to the same b_bit letter performing the +1 role in each lane.

### B.4 — v4 (b_bit-grounded, current): alphabet consistency lock

**What v4 added over v3.**
- The +1 grammar event is identified specifically as the b_bit letter of the canonical 4-bit grammar (n_L, n_R, b_bit, q).
- The same b_bit letter is shown to contribute the +1 in three independent derivations: neutrino F(9) = 8 (BCC neighbors via n_L, n_R, q) + 1 (b_bit), mirror buffer 3/2 = 1 (forward) + 1/2 (b_bit-mediated return), and Λ multiplicity 4 = 3 (spatial via n_L, n_R) + 1 (b_bit).
- The squared form is now ruled out by **alphabet consistency**: it would require two independent b_bit letters; the canonical alphabet has exactly one. This is a structural constraint, not a numerical preference.
- The 3 spatial events are made concrete as projections through the directional sector (n_L, n_R) per dimension.

**Numerical result unchanged from v3:** $\Lambda_{\mathrm{corrected}} = 1.0997 \times 10^{-52}$ m⁻², gap 0.027%.

**Why v4's contribution is structural rather than numerical.** The form of the bipartite correction is now constrained at three independent levels — dimensional analysis (Λ ∝ 1/length²), substrate phenomenology (3+1 fusion), and alphabet structure (one b_bit per derivation chain). Any future challenge to the linear form must contest one of these three constraints or accept the form as fixed. The alphabet constraint is the strongest: it forbids any squared-form revival regardless of whether the spacetime fusion argument is contested, because the alphabet has only the letters it has.

### B.5 — Numerical progression summary

| Version | Form | Λ (×10⁻⁵² m⁻²) | Gap to observation |
|---------|------|---------------|--------------------|
| v1 | Two-leg, multiplicity-2 framing | (not numerically computed in v1) | — |
| v2 | $(1-2b/72)^{2}$ squared | 1.0996 | 0.036% |
| v3 | $(1-4b/72)$ linear, 3+1 | 1.0997 | 0.027% |
| v4 | $(1-4b/72)$ linear, b_bit-grounded | 1.0997 | 0.027% |

The numerical gap closed by ~25% from v2 to v3 (0.036% → 0.027%) by switching to the linear form. v4 produces the same number as v3 — the v4 contribution is structural rigor, not numerical refinement.

### B.6 — Discipline note

The v1 → v4 progression was driven by internal recognition of inconsistencies, not by external pressure. Specifically:

- The v2 → v3 walk-back was caught when the 3+1 fused-spacetime phenomenology was applied to the squared form's "two independent length factors" assumption. The author recognized that fused 3+1 substrate forbids treating L_vac² as multiplicatively independent.
- The v3 → v4 strengthening was caught when the universal "base + grammar event" pattern was checked against the canonical 4-bit grammar lock. The +1 in the pattern had to correspond to a specific letter, and only b_bit qualified — this was not an external suggestion but an internal consistency requirement.

The original v1/v2 numerical match (0.036% gap) was already striking enough that conflating numerical fit with derivational closure would have been tempting. The framework instead caught its own structural errors and refined to the alphabet-grounded form, which is the substrate-correct one. This pattern of self-correction prior to release is the discipline that distinguishes a derivation chain from a numerical fit dressed in derivational language.

---

## Appendix C — Comparison with Ω_dm Multiplicity 1

For $\Omega_{\mathrm{dm}}$ (Vacuum Sector Bipartite Closure § 2.3), the multiplicity is 1, not 4. The reason:

- The DM chain involves a **single** bipartite operation: $\alpha_{\mathrm{vac}} = \sqrt{f_{\mathrm{coh}}}$ (governor transfer)
- This is one b_bit grammar event — one $A \to B$ accounting collapse, no spatial volumetric coupling, no temporal fold
- One collapse → one b/72 correction
- $\alpha_{\mathrm{vac}} \to \sqrt{f_{\mathrm{coh}}} - b/72$

The DM observable does not couple to spatial volume the way Λ does. It is a scalar fraction at the governor-transfer step (single b_bit commitment), not an area-like spacetime observable (3 spatial events + 1 b_bit).

This difference is now traceable to the alphabet level: DM activates the b_bit once (multiplicity 1), Λ activates the directional sector $(n_L, n_R)$ across 3 dimensions plus the b_bit once (multiplicity 4).

Both observables follow the universal "base + grammar event" pattern. They differ in how many bases their derivation chain involves, while the b_bit grammar event count remains tied to the alphabet's single b_bit letter.

---

## Appendix D — Item (3) Closure: Existence-Sensor Sweep (2026-05-05)

Item (3) of Vacuum Sector Bipartite Closure § 6 — "Independent execution-lock via 256/256 existence-sensor sweep" — is empirically closed by running the existing `qprca.py` executable in `/Src` against the protocol fixed in `Reference/Existence_Sensor_Protocol.md` (HPF v0.2.8, 2026-03-20).

### D.1 Protocol parameters

The Existence-Sensor Protocol locks the following before run:

- **Sanitized reversible subregistry** — extracted dynamically from the v0.2.7 file's bijection audit; no legacy non-bijective rules included.
- **Candidate minimal Sigma equivalence** — continuation signature $\Sigma=(T_{\rm out}, C_{\rm mode}, R_{\rm eng})$.
- **Threshold asymmetry** — false positives are the critical failure mode: $F_{\min}<1$ while no legal continuation exists overstates legality in the exact direction that would mislead the sufficiency program.

Pass criteria (Existence_Sensor_Protocol.md § "Pass / fail interpretation"):

- **Strong pass:** zero false positives, zero false negatives.
- **Conditional pass:** zero false positives, low false negatives with explainable structure.
- **Failure:** any persistent false positives, or substantial false negatives that cannot be localized cleanly.

### D.2 Sweep parameters

The sweep loops over all $16 \times 16 = 256$ input pairs $(\text{in}_L, \text{in}_R)$ in the 4-bit grammar state space, evaluates each rule in the sanitized reversible subregistry, and computes:

- $F_{\min} = \min_{\text{rules}} F_{\text{block}}$,
- `exists_legal_continuation` — whether any rule produces $F_{\text{block}} < 1$,

and assigns a confusion label per case.

The full grid is run across all six aggregate-mode × model-mode combinations:

- aggregate ∈ {`additive`, `max`, `grouped_l2`}
- model ∈ {`baseline`, `refined`}

### D.3 Results

| Aggregate | Model | TP | TN | FP | FN | Total | Verdict |
|---|---|---:|---:|---:|---:|---:|---|
| additive | baseline | 122 | 134 | 0 | 0 | 256 | **Strong Pass** |
| additive | refined | 127 | 129 | 0 | 0 | 256 | **Strong Pass** |
| max | baseline | 256 | 0 | 0 | 0 | 256 | **Strong Pass** (degenerate) |
| max | refined | 256 | 0 | 0 | 0 | 256 | **Strong Pass** (degenerate) |
| grouped_l2 | baseline | 204 | 52 | 0 | 0 | 256 | **Strong Pass** |
| grouped_l2 | refined | 210 | 46 | 0 | 0 | 256 | **Strong Pass** |

The two `max` rows are noted as "degenerate" because in `max` aggregation $F_{\min} < 1$ on every input pair, so the existence sensor never says "no continuation"; this still strict-aligns with the actual existence flag (no false positives, no false negatives) but the discriminative load is carried by `additive` and `grouped_l2`. The substantive discriminating rows show 122–134 TP and 46–52 TN — real partition between cases with and without legal continuations — and zero false signals in either direction.

### D.4 Reproducibility

The sweep is single-command from the repo root:

```
python3 Src/qprca.py --demo existence_sensor --aggregate-mode grouped_l2 --model-mode baseline --output sensor_out.json
```

(repeated for the six aggregate × model combinations). The script `Src/qprca.py` loads the canonical March 20 QPRCA executable (`HPF_QPRCA_MicroToy_v0_2_7_BridgedContinuationAmbiguity_2026-03-20.py`) and emits the confusion matrix and per-case continuation classes as JSON. No external data; deterministic; reproducible by any auditor with the repo.

### D.5 What this closes and what it does not

Closes: item (3) of Vacuum Sector Bipartite Closure § 6 — the execution-lock requirement on the b/72-corrected vacuum-sector outputs is satisfied at the substrate level. The QPRCA update grammar is bipartite-consistent across the full 4-bit state space; the existence sensor never overstates legality (zero FP) and never understates it (zero FN) under any of the six aggregation-model combinations.

Does not close: item (2). That item asks for confirmation that no additional bipartite-sensitive factors enter elsewhere in the Λ chain — specifically through the n=220 selector (24/ln(φ) prefactor, ζ(S) gate, S_ent and S_cap bounds). The existence-sensor sweep confirms substrate-level grammar consistency but does not by itself audit the higher-level Λ chain. Item (2) remains pending and requires direct verification that ζ(S), S_ent, S_cap are A/B-collapse invariant.

Numerical robustness margin worth flagging: 24/ln(φ) × 4.4059 = 219.742, which rounds to n=220. To flip to n=219 the integral would need to drop by approximately 0.084%. b/72 ≈ 0.43%. So the rounding gives roughly a 5× margin against b/72-scale perturbations — comfortable but not enormous, which is why item (2)'s explicit verification of ζ, S_ent, S_cap A/B-invariance is worth doing directly rather than by structural appeal.

---

*End of formal derivation, v4 consolidated. Item (1) of Vacuum Sector Bipartite Closure § 6 is closed by the substrate-correct 3+1 linear form, grounded in the canonical 4-bit grammar (§§ 1–12). Item (3) is closed by the existence-sensor sweep documented in Appendix D (256/256 strong pass across all six aggregate × model combinations). Item (2) remains open before canonical promotion to Volume IV § 12. Prior versions v1, v2, v3 are preserved in concrete detail in Appendix B; their standalone documents are superseded by this consolidation.*
