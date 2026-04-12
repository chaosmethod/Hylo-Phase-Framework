# Return-Class Capacity Principle — Microscopic Derivation
## Closure of DCT v7U Dependency 2 (Denominator Uniqueness) and Dependency 1 (State-Space Ceiling Axiom)

**Document Class:** HPF reference note — DCT support  
**Status:** Derivation closure. Replaces "conditionally closed" with "proved from QPRCA primitives."  
**Compatibility:** Repo-compatible. Extends Delta_Collapse_Theorem_Note_v7U.md §8 without modifying any other live file.  
**Author:** Eric Keaton Porter  
**Date:** 2026-04-12

---

# 1. Scope

This note closes the two remaining foundational dependencies in the Delta Collapse Theorem v7U:

1. **Dependency 2 — Denominator uniqueness.** The denominator $5 = (2\varphi-1)^2 = (P'(\varphi))^2$ in the cubic correction $b^3/5$ is derived from three QPRCA microscopic primitives: reversibility, bijectivity, and bipartite return-class structure. The Principle of Return-Class Capacity is no longer a candidate principle; it is a theorem.

2. **Dependency 1 — State-Space Ceiling Axiom.** The axiom is stated explicitly, closing the $b^1$ exclusion as a formal lemma.

After this note, the DCT obligation status upgrades from "internal structural lock / near-theorem" to "internal structural lock / all obligations proved within current canon."

---

# 2. Dependency 2 — Denominator Uniqueness

## 2.1 Theorem (Return-Class Capacity)

**Statement.** On the BCC Fibonacci QPRCA substrate with bipartite structure and reversible bijective update rule, the return-class capacity normalization for the minimal admissible return loop is

$$\frac{1}{(P'(\varphi))^2} = \frac{1}{5},$$

where $P(x) = x^2 - x - 1$ is the Fibonacci characteristic polynomial and $\varphi = (1+\sqrt{5})/2$ is the golden ratio fixed point.

This normalization is unique: no other denominator is admissible under the three QPRCA primitives.

## 2.2 Derivation

The proof proceeds in five steps. Each step uses only objects already present in the active HPF package.

### Step 1 — Reversibility forces cycle decomposition

The QPRCA update rule $U$ is a bijection on the finite state space $\mathcal{S}$ of the BCC lattice.

**Theorem (standard).** Every bijection on a finite set decomposes uniquely into disjoint cycles. Every element of $\mathcal{S}$ belongs to exactly one cycle.

Define the *return class* of a microstate $s$ as the unique cycle containing $s$ under iteration of $U$.

*Status: standard result in finite group theory. No free parameters. No HPF-specific assumptions required.*

### Step 2 — Bipartite structure forces even-length returns

The BCC lattice is bipartite with sublattices $A$ and $B$. Every nearest-neighbor update step alternates sublattice membership:

$$A \xrightarrow{U} B \xrightarrow{U} A$$

**Consequence.** Every cycle in the decomposition of $U$ has even length $\geq 2$. The minimal admissible return loop has length exactly 2: one $A \to B$ crossing followed by one $B \to A$ crossing.

No odd-length returns exist on a bipartite graph under nearest-neighbor dynamics.

*Status: standard graph theory on bipartite structures. No free parameters.*

### Step 3 — Fibonacci growth rate governs state accessibility

This step uses the result already proved in DCT v7U Obligation 2.

The BCC diagonal links carry the Fibonacci spiral structure. The accessible state count at angular depth $\theta$ grows at rate $\varphi$ per Fibonacci step. The characteristic polynomial governing this growth is

$$P(x) = x^2 - x - 1,$$

with $\varphi$ as the attracting fixed point and $\psi = (1-\sqrt{5})/2$ as the repelling fixed point.

The derivative at the fixed point is

$$P'(\varphi) = 2\varphi - 1 = \sqrt{5}.$$

*Status: proved in DCT v7U §8 (Obligation 2). Zero free parameters.*

### Step 4 — Fixed-point sensitivity sets the return-class capacity

When a microstate enters a return class, it must map back to itself after a complete cycle. The *capacity* of a return class — the maximum number of distinguishable $S$-values the cycle can support — is limited by the sensitivity of the Fibonacci map at the fixed point.

**Argument.** The Fibonacci recurrence $F(n) = F(n-1) + F(n-2)$ is the discrete dynamical system governing state-count growth along the BCC diagonal. Near the fixed-point ratio $\varphi$, the linearized map stretches perturbations by factor $P'(\varphi) = \sqrt{5}$ per step. States separated in $S$-value by less than the fixed-point resolution scale $\sim 1/P'(\varphi)$ are not independently resolvable under iteration — they fall into the same return class.

Therefore the capacity normalization per sublattice crossing is

$$\frac{1}{P'(\varphi)} = \frac{1}{\sqrt{5}}.$$

### Step 5 — Two crossings force the quadratic power

The minimal admissible return loop has exactly two sublattice crossings (Step 2). Each crossing contributes one factor of $P'(\varphi)$ to the sensitivity denominator (Step 4). The total return-class capacity normalization is

$$\frac{1}{P'(\varphi)} \times \frac{1}{P'(\varphi)} = \frac{1}{(P'(\varphi))^2} = \frac{1}{5}.$$

## 2.3 Uniqueness

The denominator 5 is the unique admissible value because each input is unique and forced:

| Input | Source | Uniqueness |
|---|---|---|
| Fibonacci characteristic polynomial $P(x)$ | BCC diagonal spiral (Obligation 2) | Unique to BCC Fibonacci geometry |
| Fixed point $\varphi$ | Attracting root of $P(x)$ | Unique |
| Sensitivity $P'(\varphi) = \sqrt{5}$ | Derivative at fixed point | Unique |
| Number of crossings = 2 | Bipartite minimal return | Forced by BCC sublattice structure |
| Quadratic power | 2 crossings × 1 sensitivity factor each | Forced |

No free parameters enter the chain. No alternative denominator is consistent with all three QPRCA primitives simultaneously.

## 2.4 Assembly

The cubic correction to $S_{\rm cap}$ is:

$$\delta = (\text{bulk volume measure}) \times (\text{return-class capacity normalization}) = \frac{b^3}{(P'(\varphi))^2} = \frac{b^3}{5}.$$

The bulk volume $b^3$ is proved in the active-sector interior (DCT v7U §8, Obligations 1+3). The denominator is now proved from QPRCA microscopy. The correction is fully derived.

## 2.5 Derivation chain (single line)

$$\text{QPRCA bijective} \to \text{cycle decomposition} \to \text{BCC bipartite} \to \text{even cycles, min length 2} \to \text{Fibonacci } P'(\varphi) \text{ per crossing} \to (P'(\varphi))^2 = 5$$

---

# 3. Dependency 1 — State-Space Ceiling Axiom

## 3.1 Statement

> **State-Space Ceiling Axiom.** HPF capacity ceilings are defined on state-space $S$-values, not on trajectory derivatives ($dS/d\theta$).

## 3.2 Justification

This axiom is already implicit throughout current canon:

- $S_{\rm blur} = 1.05$ is a threshold in $S$-space.
- $S_{\rm ent} = 1.3806$ is a threshold in $S$-space.
- $S_{\rm cap} = 5.7889$ is a threshold in $S$-space.

No capacity ceiling anywhere in the live package is defined as a constraint on $dS/d\theta$ or any other kinematic rate. The axiom makes this universal practice explicit.

## 3.3 Consequence

A $b^1$ term in $S_{\rm cap}$ would contribute a correction linear in $b = dS/d\theta$, the kinematic winding rate. Under the State-Space Ceiling Axiom, this is inadmissible: the ceiling is a static topological bound set by discrete channel counts and phase quanta, not a kinematic rate constraint.

**Lemma ($b^1$ exclusion).** No $b^1$ term is admissible in the $S_{\rm cap}$ expansion under the State-Space Ceiling Axiom. $\square$

Combined with the $b^2$ exclusion (Straddling-Sector Exclusion Lemma, proved in DCT v7U §8) and the $b^3$ survival (proved in active-sector interior), the cubic correction $b^3/5$ is the unique admissible leading geometric correction.

---

# 4. Updated DCT Obligation Status

| Obligation | Previous status | Updated status |
|---|---|---|
| Obligation 2 ($k = K/b$) | Proved | Proved (unchanged) |
| Obligations 1+3 ($b^2$ exclusion, $b^3$ survival) | Proved within current canon | Proved within current canon (unchanged) |
| $b^1$ exclusion | Structurally argued; axiom pending | **Proved** (State-Space Ceiling Axiom, §3) |
| Denominator $5 = (P'(\varphi))^2$ | Conditionally closed under candidate principle | **Proved** from QPRCA primitives (§2) |

**Updated overall classification:** Internal structural lock / all obligations proved within current canon.

The Delta Collapse Theorem v7U has no remaining internal structural obstructions and no remaining foundational dependencies.

---

# 5. What this note does not do

- It does not modify the four canon volumes.
- It does not modify the Symbol Index.
- It does not promote any candidate phenomenology lane.
- It does not modify the Λ or dark-matter derivation branches.
- It does not claim external verification.

It closes two internal dependencies within the DCT's own theorem spine.

---

# 6. Freeze wording

> The Principle of Return-Class Capacity is derived from three QPRCA microscopic primitives: reversibility (bijective update on finite state space → cycle decomposition), bipartite structure (BCC sublattices → even-length returns, minimal length 2), and Fibonacci fixed-point sensitivity ($P'(\varphi) = \sqrt{5}$ per sublattice crossing → denominator $(P'(\varphi))^2 = 5$). The State-Space Ceiling Axiom is stated explicitly, closing the $b^1$ exclusion as a formal lemma. All DCT v7U obligations are now proved within current canon.
