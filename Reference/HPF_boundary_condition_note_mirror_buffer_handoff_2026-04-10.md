# HPF Boundary Condition Note - Mirror Buffer Closure Ends at Geometric Prose; QPRCA Handoff Required

**Document Class:** HPF boundary-condition / handoff note  
**Status:** Candidate freeze for execution-layer handoff. Not canon-closing by itself.  
**Author:** Eric Keaton Porter  
**Date:** 2026-04-10

---

## 1. Purpose

This note freezes the exact point at which the passive mirror-buffer candidate stops being legally extendable by geometric prose alone and must hand off to QPRCA update algebra.

The goal is not to close the remaining residuals by arithmetic. The goal is to define:

1. what the geometric layer has actually established,
2. what it has ruled out,
3. what corrections are illegal from this point forward, and
4. what exact mechanical questions QPRCA must now answer.

---

## 2. What the geometric layer has established

### 2.1 Bipartite mirror path motivates the passive correction family

On the BCC bipartite substrate, the candidate geometric picture remains:

- forward leg = 1 node length,
- mirror return = 1/2 node length,
- effective path = 1 + 1/2 = 3/2 node lengths.

Combined with the active Nyquist residual

$$\eta = \frac{1}{2 \times 24} = \frac{1}{48},$$

the passive mirror construction yields

$$\eta_{\rm passive} = \frac{1}{(3/2) \times 48} = \frac{1}{72}$$

and therefore the candidate correction family

$$\delta_{\rm mirror} = \frac{b}{72}.$$

This remains a geometrically motivated, substrate-native candidate family using only already-locked package objects.

### 2.2 Cross-branch effectiveness is real at the geometric layer

Applied without introducing new free parameters, the $b/72$ family removes the bulk of two independent residuals:

- the dark-matter residual,
- the neutrino mass-squared ratio residual.

This is enough to justify continued consideration of $b/72$ as a real candidate correction family for sublattice-sensitive observables.

### 2.3 The mirror family is not yet formally derived

The geometric layer has motivated the $3/2$ effective path. It has **not** yet derived it in QPRCA update language. The family is therefore candidate-supported, not execution-locked.

---

## 3. What has been ruled out at this layer

### 3.1 Phase-corridor corrections cannot be imported into immune branches

The dark-matter branch and the neutrino BCC-indexing branch are immune to the $\zeta(S)$ selector machinery, including the hard-step limit $k \to \infty$.

Therefore finite-$k$ selector leakage is **not** a legal explanation for the remaining dark-matter or neutrino residuals.

### 3.2 The coarse term $b/360$ is not universal grammar

The cycle-level blur term

$$\frac{b}{360}$$

provides a good candidate closure for the dark-matter remainder when paired with the local mirror term, but it does **not** transfer cleanly to the neutrino vertex branch.

Therefore $b/360$ may be retained only as a **dark-matter branch-specific candidate coarse correction**. It may not be promoted to a universal correction rule.

### 3.3 $b/120$ and $b/72$ are different local families

The FSC local term

$$\frac{b}{120}$$

and the mirror-buffer term

$$\frac{b}{72}$$

must not be conflated.

Their triggers are different:

- **Family A - choice-space resolution:**
  $$\frac{b}{N_{\rm hop}} = \frac{b}{120}$$
  Triggered only when the derivation includes one-hop enumeration of available local path-state configurations.

- **Family B - mirror-path elongation:**
  $$\frac{b}{72}$$
  Triggered only when the derivation is sublattice-sensitive and samples transport across the bipartite boundary.

The governing legality rule is:

> **If an observable is corrected by a term whose trigger mechanism is absent from its derivation, that correction is illegal.**

This rule replaces label-based reasoning such as "rotation vs translation" with trigger-based grammar discipline.

---

## 4. Boundary condition reached by the neutrino audit

The neutrino branch begins from the vertex construction

$$n = 8 + 1,$$

with the +1 shared-face term representing a real executional crossing event, not mere topological bookkeeping.

Applying the legal mirror-family correction removes most of the neutrino residual, but not all of it. The remaining discrepancy is too small to be honestly assigned by scheduler-averaging prose or by introducing a second ad hoc denominator.

The failed oversized scheduler-average argument shows that the remaining softening is **not** captured by naive geometric averaging of $1$ and $1/2$ crossing weights.

Therefore the live remainder must be treated as one of only two possibilities:

1. the mirror-path family is only formally legal if QPRCA derives the exact crossing mechanism that produces it, including any tiny bridge renormalization as a byproduct, or
2. the mirror-buffer candidate fails when exposed to execution-layer algebra.

This is the boundary condition.

---

## 5. What is illegal from this point forward

From this point on, the following moves are not allowed:

1. **No denominator hunting.**
   No new fraction may be introduced merely because it is numerically close to a leftover residual.

2. **No cross-branch import without trigger presence.**
   A correction family cannot be borrowed from another observable class unless its trigger mechanism is present in the derivation under inspection.

3. **No promotion of $\epsilon_{\rm sf}$ from numerics alone.**
   Any tiny shared-face softening must come out of the update algebra or remain unassigned.

4. **No universal promotion of $b/360$.**
   Until a branch-native trigger rule is derived, $b/360$ stays a dark-matter-only candidate.

---

## 6. QPRCA handoff requirements

QPRCA must now decide the candidate mechanically, not rhetorically.

The first target is the single bipartite crossing event:

$$\mathcal{U}_{A \to B}$$

or, if needed, the full two-half-cycle crossing pair

$$\mathcal{U}_{A \to B} \circ \mathcal{U}_{B \to A}.$$

From that derivation, QPRCA must answer exactly four questions:

### Obligation Q1 - Effective path legality

Does the update algebra produce an effective path length

$$\ell_{\rm eff} = \frac{3}{2}$$

for the relevant class of sublattice-sensitive transport observables?

### Obligation Q2 - Observable-class trigger rule

Which observable classes legally sample the mirror-path correction family?

This must be derived as a trigger rule, not assigned by pattern-matching.

### Obligation Q3 - Shared-face bridge renormalization

Does the same crossing algebra produce a small softening of the shared-face bridge term

$$n_{\rm eff} = 8 + 1 - \epsilon_{\rm sf}?$$

If yes, the value must emerge as a byproduct of the same mechanism. If no, the neutrino remainder remains a clean falsifier for mirror-family overreach.

### Obligation Q4 - Branch separation

Does QPRCA preserve the distinction between:

- local choice-space resolution corrections,
- local mirror-path corrections,
- branch-specific coarse averaging corrections?

If not, the family map is wrong and must be revised.

---

## 7. Falsification / decision rule at the handoff boundary

The passive mirror-buffer candidate is falsified at the execution layer if any of the following occur:

1. QPRCA produces an effective crossing law other than $3/2$ for the claimed observable class.
2. The observable-class trigger rule excludes either dark matter or the neutrino ratio from legal membership in the mirror family.
3. The same crossing algebra cannot support the claimed mirror correction while remaining consistent with the rest of the bipartite scheduler.
4. A third independent sublattice-sensitive observable rejects the $b/72$ family when the trigger mechanism is genuinely present.

Conversely, the candidate survives handoff only if the update algebra produces the crossing law and the trigger rule without importing unlicensed corrections.

---

## 8. Freeze wording

> The passive mirror-buffer candidate has reached its legal geometric limit. The $b/72$ family is still live because it is substrate-native, cross-branch effective, and triggered by the bipartite mirror-path picture, but it is not yet execution-locked. The dark-matter branch may additionally admit a branch-specific coarse term, but that term is not universal grammar and may not be imported elsewhere without a derived trigger. The remaining neutrino shared-face discrepancy is now below the honest resolution of geometric prose. No further closure is legal at the geometric layer. The framework must hand off to QPRCA update algebra to decide whether a single bipartite crossing event generates the $3/2$ effective path, whether the observable-class trigger rule is real, and whether any tiny shared-face softening emerges from the same operation. If QPRCA derives these, the mirror family survives. If not, the candidate is falsified cleanly.

---

## 9. Operational status

This note does **not** close the passive mirror candidate.

It closes the **geometric-prose phase of the inquiry** and defines the exact entry conditions for execution-layer adjudication.
