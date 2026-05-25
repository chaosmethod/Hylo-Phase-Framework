# HPF Candidate Note — Measurement Interaction Trigger Rule

**Document Class:** HPF phenomenology candidate note — Obligation Q2 closure (boundary condition note, 2026-04-10)
**Date:** 2026-05-25
**Author:** Eric Keaton Porter
**Status:** Candidate. Closes Obligation Q2 at the algebraic sketch level. Execution lock pending 256/256 existence-sensor run on bifurcated-state subspace under r_RESOLVE.
**Compatibility:** Repo-consistent. Extends boundary condition note (2026-04-10), Entanglement Candidate Note (2026-04-11), Entanglement Obligation Closure (2026-04-12), and Mirror-Buffer Entanglement Closure (2026-04-30). Adds r_RESOLVE to the RULES registry and a third rule_choice mode to HPF_QPRCA_BCC_v0_3_0.py.

---

## Abstract

The boundary condition note (2026-04-10) froze the passive mirror-buffer candidate at the geometric prose limit and demanded that QPRCA update algebra answer Obligation Q2: which observable classes legally sample the directional-resolution operation, derived as a trigger rule rather than assigned by pattern-matching. The Entanglement Candidate Note carried "measurement as grammar operation" as candidate-unchanged through the April 2026 closure cycle. This note closes both obligations substrate-natively.

The trigger criterion is derived from three objects already present in the active package: the continuation-ambiguity channel (Volume II, v0.2.7), the sublattice-sensitivity test (boundary condition note §3.3), and the bifurcated address structure (Entanglement Candidate Note §§4–6). No new machinery is introduced. No effective-theory input (QM, GR) is used as a source; effective theories may be checked for consistency after the fact but do not determine the criterion.

The criterion identifies a measurement-class interaction as one that imposes a sublattice-selective A/B boundary constraint sufficient to collapse the continuation ambiguity of the (nL=1, nR=1) bifurcated state to zero under the full rule family — making r_RESOLVE the unique legal minimum-F operation. A new bijective rule r_RESOLVE is specified and added to the RULES registry. A third rule_choice mode "measurement_class" is defined for HPF_QPRCA_BCC_v0_3_0.py.

---

## 1. Locked Inputs From Active Package

| Input | Value | Status |
|---|---|---|
| 4-bit site grammar (nL, nR, b, q) | 16 configs, 15 active | Candidate-locked |
| Bifurcated address state | (nL=1, nR=1) — both directional bits live | Candidate |
| S_ent = 1.3806 | Lower phase wall / entanglement threshold | Locked |
| S_cap = 5.7889 | Saturation ceiling | Locked |
| Continuation ambiguity P_cont | Normalized over reversible RULES family | Active (v0.2.7) |
| Sublattice-sensitivity trigger criterion | Collapsing A/B distinction changes derivation output | Candidate-locked (boundary condition note) |
| b/72 trigger discipline | No cross-branch import without trigger presence | Active |
| "Measurement as grammar operation" | (nL=1,nR=1) → single resolved bit | Candidate-unchanged |

---

## 2. The Gap Being Closed

The executable (HPF_QPRCA_BCC_v0_3_0.py) selects rules as follows:

```python
rule = (self.rng.choice(list(RULES.keys()))
        if self.rule_choice == "random" else self.rule_choice)
```

Two modes exist: random selection over the full RULES family, or an externally fixed rule name. Neither mode contains a mapping from physical interaction class to a legally permitted rule subset. The RULES family (ID, SWAP, TQ, SB, BOUNCE, EXCH, TQ0, BQ0, SWEQ) has no entry that implements directional resolution — the operation (nL=1,nR=1) → (nL=1,nR=0) or (nL=0,nR=1) described in Entanglement Candidate Note §6. The slot for the trigger rule exists in rule_choice. The trigger rule and the rule it licenses are both absent.

This note supplies both.

---

## 3. Derivation of the Trigger Criterion

### 3.1 Continuation ambiguity of the bifurcated state

Fix the local input pair (inA, inB) where site A is in the bifurcated address state (nL=1, nR=1, b, q). The continuation ambiguity P_cont is computed over the full reversible RULES family per v0.2.7:

P_cont(inA, inB) = log(N_eff_cont) / log(N_eff_cont_max)

where N_eff_cont = 1 / sum_kappa(p_kappa^2) and p_kappa is the probability mass on each continuation class kappa = Sigma(output pair).

Under random rule selection with the current nine-rule family, the bifurcated state (nL=1,nR=1) maps to multiple distinct output classes. P_cont > 0. The state is genuinely ambiguous — the substrate has not selected a canonical directional address.

### 3.2 What a measurement-class interaction does to the continuation landscape

A measurement-class interaction imposes an external constraint on the A/B boundary crossing. Specifically: it differentially weights A-origin and B-origin information in the bipartite crossing — it is not symmetric across the sublattice boundary.

The substrate-native expression of this constraint is: the interaction reduces the legal rule subset to those operations that are sublattice-selective at the directional-occupancy layer. A rule is sublattice-selective at the directional-occupancy layer if and only if it maps (nL=1,nR=1) to distinct outputs on A-sites and B-sites respectively, with the A-site output preserving nL and zeroing nR, and the B-site output preserving nR and zeroing nL.

This is the A/B distinction collapse criterion from the boundary condition note: the interaction "collapses the A/B distinction" not globally but at the directional-occupancy level. The b/72 trigger fires when collapsing the A/B distinction changes a derivation output. The measurement trigger fires when imposing an A/B constraint at the directional-occupancy layer collapses P_cont to zero.

### 3.3 The formal criterion

**Measurement-class trigger rule:**

An interaction I is measurement-class — legally licensed to constrain rule selection to the directional-resolving subset — if and only if all three conditions hold:

**Condition 1 — Bifurcated input:** The local site is in the bifurcated address state (nL=1, nR=1), i.e., S_f is in the active entropy band (S_ent, S_cap).

**Condition 2 — Sublattice-selective A/B constraint:** The interaction imposes an asymmetric weight on the A/B boundary crossing at the directional-occupancy layer. Operationally: under I's constraint, the legal successor states of (nL=1,nR=1) on an A-site exclude (nL=0,nR=1), and the legal successor states on a B-site exclude (nL=1,nR=0).

**Condition 3 — Continuation ambiguity collapse:** The three conditions jointly reduce P_cont of the (nL=1,nR=1) state to zero under the constrained rule subset. Only one continuation class survives: the directional-resolving class implemented by r_RESOLVE.

Condition 3 is the closure condition. When P_cont = 0, r_RESOLVE is not selected arbitrarily — it is the unique legal operator. The measurement interaction does not choose which rule fires. It eliminates all other continuation classes, leaving one.

### 3.4 Why this is substrate-native

The criterion uses only: the bifurcated address state (already in the entanglement note), the P_cont continuation ambiguity channel (already in v0.2.7), and the sublattice-selective A/B constraint structure (already in the boundary condition note §3.3). No effective-theory input determines any step. QM's spin-resolving interactions are consistent with Condition 2 — they break rotational symmetry in a specific direction, which is the physical expression of asymmetric A/B boundary weighting at the directional-occupancy layer — but QM does not supply the criterion. The criterion is derived first; QM is checked against it afterward.

---

## 4. The r_RESOLVE Rule

### 4.1 Specification

r_RESOLVE acts on a pair (l, r) where l is the A-site and r is the B-site:

```python
def r_RESOLVE(l, r):
    nLl, nRl, bl, ql = unpack(l)
    nLr, nRr, br, qr = unpack(r)

    # A-site: bifurcated <-> left-canonical (involution)
    if   nLl == 1 and nRl == 1:
        l_out = pack(1, 0, bl, ql)   # bifurcated -> A-canonical (nL survives)
    elif nLl == 1 and nRl == 0:
        l_out = pack(1, 1, bl, ql)   # A-canonical -> bifurcated (inverse)
    else:
        l_out = l                     # all other states: identity

    # B-site: bifurcated <-> right-canonical (involution)
    if   nLr == 1 and nRr == 1:
        r_out = pack(0, 1, br, qr)   # bifurcated -> B-canonical (nR survives)
    elif nLr == 0 and nRr == 1:
        r_out = pack(1, 1, br, qr)   # B-canonical -> bifurcated (inverse)
    else:
        r_out = r                     # all other states: identity

    return l_out, r_out
```

### 4.2 Bijectivity verification

r_RESOLVE is a product of two independent involutions — one on the A-site state space, one on the B-site state space. Each involution swaps exactly two states (for each (b,q) value: the bifurcated and the sublattice-canonical state) and leaves all others fixed. A product of two involutions on independent state spaces is bijective. The pair-level operation on {0..15} x {0..15} is therefore bijective.

Specifically, on the A-site:
- (nL=1,nR=1,b,q) <-> (nL=1,nR=0,b,q)  for each of the 4 (b,q) combinations: 4 swapped pairs
- All 12 remaining states: fixed

On the B-site:
- (nL=1,nR=1,b,q) <-> (nL=0,nR=1,b,q)  for each of the 4 (b,q) combinations: 4 swapped pairs
- All 12 remaining states: fixed

No state is mapped to two outputs. No output is reached from two inputs. Bijection confirmed algebraically. Execution-level verification (ReturnClassVerifier) is Obligation 1 of this note.

### 4.3 Sublattice logic of the rule

The A-site preserves nL (the forward-direction occupancy) and zeros nR. This is substrate-native: A-sites initiate the forward half-step U_A→B; their canonical directional address is left-origin. The B-site preserves nR (the return-direction occupancy) and zeros nL. B-sites receive the return half-step U_B→A; their canonical directional address is right-origin.

r_RESOLVE therefore encodes the bipartite handoff structure directly in the directional-bit resolution. It is not an arbitrary assignment. The sublattice logic follows from the same A/B asymmetry that grounds the 3/2 effective path length and the b/72 correction family.

---

## 5. The Third rule_choice Mode

### 5.1 Code patch

Add r_RESOLVE to the RULES registry:

```python
RULES: Dict[str, callable] = {
    "ID": r_ID, "SWAP": r_SWAP, "TQ": r_TQ,
    "SB": r_SB, "BOUNCE": r_BOUNCE, "EXCH": r_EXCH,
    "TQ0": r_TQ0, "BQ0": r_BQ0, "SWEQ": r_SWEQ,
    "RESOLVE": r_RESOLVE,   # measurement-class directional resolution
}
```

Add the third rule_choice mode to _block_step:

```python
def _select_rule(self, inA: int, inB: int) -> str:
    if self.rule_choice == "random":
        return self.rng.choice(list(RULES.keys()))
    elif self.rule_choice == "measurement_class":
        return self._measurement_class_select(inA, inB)
    else:
        return self.rule_choice

def _measurement_class_select(self, inA: int, inB: int) -> str:
    """
    Measurement-class rule selection.

    Applies the trigger criterion: if the A-site is in the bifurcated
    address state (nL=1,nR=1), filter RULES to the directional-resolving
    subset {RESOLVE} and select minimum-F within that subset.

    If the site is not bifurcated, the measurement-class mode falls
    through to random selection — no constraint is imposed on
    non-bifurcated states.
    """
    nLa, nRa, _, _ = unpack(inA)
    if nLa == 1 and nRa == 1:
        # Bifurcated state under measurement-class constraint:
        # RESOLVE is the unique legal continuation class.
        return "RESOLVE"
    else:
        # Non-bifurcated state: no directional ambiguity to resolve.
        return self.rng.choice(list(RULES.keys()))
```

### 5.2 What this achieves

The third mode implements the trigger criterion in the executable. When rule_choice = "measurement_class" and the local A-site is bifurcated, RESOLVE is selected — not randomly but as the unique continuation class surviving the ambiguity collapse. For non-bifurcated sites, the mode falls through to random selection because no measurement-class constraint is active on an already-resolved directional address.

This makes the gap architecturally closed at the code level. The physical coupling → rule subset mapping now exists. It is not arbitrary: it is forced by the trigger criterion and the bijectivity of r_RESOLVE.

---

## 6. Relation to Existing Closures

| Prior closure | Connection |
|---|---|
| Boundary condition note (2026-04-10) Obligation Q2 | Closed at algebraic sketch level by this note. Execution lock is Obligation 1 here. |
| Entanglement Candidate Note §6 | "Measurement as grammar operation" now has the rule that implements it (r_RESOLVE) and the criterion that licenses it. Status upgrades from candidate-unchanged to candidate-strengthened. |
| Entanglement Obligation Closure — SPDC bridge | Orthogonal. The SPDC bridge identifies which physical interactions drive S_f > S_ent; this note identifies which rule subset is licensed once S_f is in the active band. Both are needed for full closure. Neither gates the other. |
| b/72 trigger discipline | Same structure. b/72 fires when collapsing A/B distinction changes derivation output. Measurement trigger fires when imposing A/B constraint at directional-occupancy layer collapses P_cont to zero. Two trigger classes, same governing rule: trigger mechanism must be present in the derivation for the correction to be legal. |
| Mirror-Buffer Entanglement Closure | Entanglement as bijective self-accounting across A/B boundary. r_RESOLVE is the rule that makes that accounting visible from one sublattice only — it is the executable expression of "measurement reveals the bijective accounting." |
| Volume I §32 open items | Physical coupling → grammar operation bridge is not currently listed. This note supplies the missing item. It should be added as item 7: "derivation of measurement-class trigger rule from QPRCA update algebra." |

---

## 7. What This Note Does Not Claim

This note does not claim that all physical measurement interactions are measurement-class under this criterion. It derives the substrate-native criterion and shows that the criterion is non-empty — that r_RESOLVE is the unique operation satisfying it for bifurcated states. Mapping specific physical coupling types (magnetic, optical, gravitational) to the criterion is a consistency check, not a derivation input. That check belongs in a separate phenomenology note.

This note does not close the Born rule gap. The trigger criterion determines which rule fires under measurement-class interactions. It does not determine which basin the system routes to when both (nL=1,nR=0) and (nL=0,nR=1) are legal outputs of r_RESOLVE on different sites. That routing probability — the HPF analog of |psi|^2 — remains open and is the correct next target after this note's obligations are closed.

This note does not prove r_RESOLVE is the unique admissible directional-resolution rule. It is the unique rule satisfying the sublattice-canonical logic derived here. Whether other bijective rules could satisfy the trigger criterion under a different derivation is not addressed.

---

## 8. Open Obligations

### Obligation 1 — r_RESOLVE execution lock

Run the ReturnClassVerifier on r_RESOLVE: confirm even-cycle structure at the lattice level (N=4, state space 16^4 = 65536) under the alternating bipartite sweep. Confirm the bijection holds in the executable, not just algebraically.

**Target:** All non-degenerate lattice cycles even. Empirical return-class capacity 1/mean_len consistent with 1/5 theoretical target.

**Status:** Open.

### Obligation 2 — Continuation ambiguity collapse verification

Confirm numerically that under the measurement_class rule_choice mode, P_cont of the (nL=1,nR=1) state collapses to zero — that only the RESOLVE continuation class survives. This is the executable verification of Condition 3 in §3.3.

**Target:** P_cont(inA=(nL=1,nR=1), measurement_class mode) = 0.0 across all (b,q) variants.

**Status:** Open.

### Obligation 3 — Volume I §32 update

Add "derivation of measurement-class trigger rule from QPRCA update algebra" as item 7 to the open-items list in Volume I §32. The self-audit currently does not see this gap; this note closes it at the candidate level and the canonical volume must reflect the item.

**Status:** Open — editorial.

---

## 9. Status Table

| Claim | Status |
|---|---|
| Trigger criterion substrate-native (no QM/GR input) | **Candidate** — derived from continuation ambiguity + sublattice-sensitivity + bifurcated address |
| r_RESOLVE bijective (algebraic) | **Candidate-strong** — involution product proof complete |
| r_RESOLVE bijective (execution) | **Open** — Obligation 1 |
| "measurement_class" rule_choice mode defined | **Candidate** — code specified, not yet run |
| P_cont collapse to zero under mode (Condition 3) | **Open** — Obligation 2 |
| "Measurement as grammar operation" status | **Candidate-strengthened** — rule and trigger criterion now present |
| Obligation Q2 (boundary condition note) | **Closed at algebraic sketch level** — execution lock pending |
| Born rule gap | **Open** — explicitly out of scope; correct next target |
| Volume I §32 updated | **Open** — Obligation 3 |

---

## 10. Freeze Wording

> The measurement-class trigger rule is derived substrate-natively from three existing package objects: the continuation-ambiguity channel, the sublattice-sensitivity criterion, and the bifurcated address structure. An interaction is measurement-class — legally licensed to constrain rule selection to the directional-resolving subset — if and only if it is in the bifurcated address state (nL=1,nR=1), it imposes a sublattice-selective A/B boundary constraint at the directional-occupancy layer, and that constraint collapses the continuation ambiguity P_cont of the bifurcated state to zero. The unique surviving operation is r_RESOLVE: a bijective involution that maps (nL=1,nR=1) to (nL=1,nR=0) on A-sites and to (nL=0,nR=1) on B-sites, with the inverse defined by the same involution. r_RESOLVE is added to the RULES registry and licensed by a third rule_choice mode "measurement_class" in HPF_QPRCA_BCC_v0_3_0.py. No effective-theory input determines any step; QM is a consistency check, not a source. Obligation Q2 of the boundary condition note is closed at the algebraic sketch level. Two execution locks remain open. The Born rule gap is explicitly out of scope and is the correct next target.

---

*End of candidate note. Do not promote to canon until Obligations 1 and 2 are closed.*
