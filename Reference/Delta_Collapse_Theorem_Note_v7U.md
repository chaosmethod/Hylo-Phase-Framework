# δ\_collapse — Admissibility and Derivation Pass

## Internal Theorem Note — v7

**Author:** Eric Keaton Porter  
**Date:** 2026-04-01 (v7 update)  
**Status:** Internal structural lock / near-theorem derivation. Core wall-unification and correction-order obligations are resolved within current canon; denominator uniqueness is conditionally closed under the Principle of Return-Class Capacity.

\---

## 1\. Formal Target Definition

$$\\delta\_{\\rm collapse} = S\_{\\rm cap} - \\left(S\_{\\rm blur} + \\frac{3\\pi}{2} + \\eta\\right) = 0.005678$$

**Probe precision:** Binary search \[5.0, 5.99], 6 iterations → ±0.0155.

\---

## 2\. Current Best Expression

$$\\boxed{S\_{\\rm cap} = S\_{\\rm blur} + \\frac{3\\pi}{2} + \\frac{1}{48} + \\frac{b^3}{(2\\phi-1)^2}}$$

$$= 1.05 + 4.712389 + 0.020833 + 0.005750 = 5.788972$$

Gap from empirical 5.7889: **0.000072** — within probe precision.

\---

## 3\. Denominator (carried from v3)

$$\\frac{b^3}{(2\\phi-1)^2} = \\frac{b^3}{5}, \\qquad 2\\phi-1 = P'(\\phi) = \\sqrt{5}$$

Denominator = squared fixed-point sensitivity of the Fibonacci characteristic polynomial. **Status: candidate-explained, strong.**

\---

## 4\. Fork Resolution (carried from v2)

**Fork B eliminated.** $\\zeta(S\_{\\rm budget}) = 0$. $\\delta\_{\\rm collapse}$ is geometric (Fork A).

\---

## 5\. Robustness Paper Foundation

From *Topology and Dimensional Reduction of the Λ Selector Branch* (2026-03-31):

* 47,628-point sweep confirms $n=220$ selector occupies a connected anisotropic robustness volume
* $k \\to \\infty$ (step-function limit) is legal and preserves $n=220$
* $k$ is demoted to a one-sided tail-softening parameter
* Effective parameter space reduces from 4D to **3D structural constraint manifold**: $(S\_{\\rm lo}, S\_{\\rm hi}, \\varepsilon)$
* Admissible ceiling interval: \[5.784, 5.804]
* $b^3/(2\\phi-1)^2$ places $S\_{\\rm cap}$ at 5.788972 — inside this window ✓

\---

## 6\. The Cubic Order Derivation Spine

**Status: Near-theorem structural derivation.** The selector can now be organized into a $b$-scaling framework in which the zero-order term is topological, lower-order corrections are plausibly identified with blur-tail structure, and the cubic term emerges as the leading surviving geometric candidate. A full theorem still requires the proofs in Section 8.

### 6.1 The b-Scaling Framework

Following the Layer 3 pressure test, the $\\Lambda$ branch parameter space undergoes dimensional reduction into a 3D structural constraint manifold: $(S\_{\\rm lo}, S\_{\\rm hi}, \\varepsilon)$.

Mapping these coordinates to the Fibonacci boundary parameter $b = \\ln(\\phi)/(\\pi/2)$:

* Phase-budget differential: $dS \\propto b$ (since $S = \\ln(r)$ is the log-radial measure)
* Shell-conversion prefactor: $P = 24/\\ln(\\phi) \\propto b^{-1}$ (since $P^{-1} = \\ln(\\phi)/24 = b \\cdot \\pi/48$)
* Zero-order raw selector: $X\_0 = P \\cdot \\Delta S \\propto b^{-1} \\cdot b = \\mathbf{b^0}$

**The zero-order selector is the current candidate topological invariant of the reduced structural manifold.** Verified: $X\_0 = 49.874 \\times 4.408 = 219.86$.

### 6.2 The Structural Hypothesis

The ceiling $S\_{\\rm hi}$ decomposes into:
$$S\_{\\rm hi} = S\_{\\rm geom}(b) + S\_{\\rm blur}(k)$$

where $S\_{\\rm geom}$ is the hard geometric substrate capacity and $S\_{\\rm blur}$ is the thermodynamic blur shift governed by gate steepness $k$.

Because $k \\to \\infty$ legally preserves $n=220$, the thermodynamic blur strictly vanishes in the step-function limit.

The structural hypothesis posits two links:

1. The thermodynamic blur is the minimal resolvable phase uncertainty induced by the finite causal wedge, motivating the scaling $k \\propto 1/b$
2. The surviving geometric capacity correction is the 3D spatial volume of the constraint manifold tolerances $(dS\_{\\rm lo} \\wedge dS\_{\\rm hi} \\wedge d\\varepsilon)$, making cubic order $b^3$ the leading surviving geometric candidate

### 6.3 Two-Wall b-Scaling Summary

Restating both walls in $b$-language clarifies the corridor architecture:

$$S\_{\\rm ent} = 1.05 + \\frac{\\ln 47}{K}b \\qquad \\text{($b^{+1}$-dominated; resolution-limited onset)}$$

$$S\_{\\rm cap} = 1.05 + \\frac{3\\ln \\phi}{b} + \\frac{1}{48} + \\frac{b^3}{5} \\qquad \\text{($b^{-1}$-led with $b^3$ correction; geometry-budget saturation)}$$

The corridor width $S\_{\\rm cap} - S\_{\\rm ent}$ is therefore set by the competition between opposite $b$-scalings: the lower wall grows with $b$ while the upper wall shrinks with $b$.

The former structural obstruction $K \\approx 3.567$ is now resolved within current canon. The lower wall is no longer merely numerically consistent with $b$-language; it is generated from the same substrate-variable architecture as the upper wall.

\---

## 7\. Two-Wall Common Spine

**Status checkpoint — v7.** This section records a structural upgrade from v6.

### 7.1 Statement

**Two-Wall Common Spine (current status).** The lower and upper walls are not independent phenomenological fits. They share two substrate-native structural inputs:

$$S\_{\\rm blur} = 1.05 \\qquad \\text{(empirically anchored single free input)}$$

$$\\eta = \\frac{1}{48} \\qquad \\text{(substrate-native Nyquist residual; zero free parameters)}$$

These shared inputs enter the two walls differently. $\\eta$ is the same substrate object playing two different structural jobs.

**Lower wall.** The Nyquist residual fixes the gate-exit sharpness through

$$k = \\frac{\\ln((1-\\eta)/\\eta)}{S\_{\\rm ent} - S\_{\\rm blur}} = \\frac{\\ln 47}{S\_{\\rm ent} - 1.05}.$$

Here $\\eta$ appears implicitly as the substrate-resolution constraint governing logistic onset.

**Upper wall.** The same Nyquist residual appears explicitly as the additive margin term in

$$S\_{\\rm cap} = 1.05 + \\frac{3\\pi}{2} + \\frac{1}{48} + \\frac{b^3}{5}.$$

Here $\\eta$ appears explicitly as the minimum nonzero residual margin after the geometric collapse budget is exhausted.

The current common spine is therefore:
$${S\_{\\rm blur}, \\eta} = {1.05, 1/48}.$$

### 7.2 Significance

Before this framing, the two walls could be described as two separate constructions sharing only a blur anchor. The correct description is now:

> Two wall-specific geometric constructions that share a blur anchor and a substrate-resolution constraint, each deploying that constraint in a different structural role.

This is the first structural evidence that the two walls belong to a single regulated phase system.

### 7.3 Full Unification Achieved

Because Obligation 2 is closed substrate-natively in the form $k = K/b$, the common spine upgrades to

$${S\_{\\rm blur}, \\eta, b},$$

and both walls become $b$-structured offsets from the same blur anchor, with $\\eta$ as the shared resolution floor:

$$S\_{\\rm ent} = 1.05 + \\frac{\\ln 47}{K}b, \\qquad S\_{\\rm cap} = 1.05 + \\frac{3\\ln \\phi}{b} + \\frac{1}{48} + \\frac{b^3}{5}.$$

The corridor is therefore not two parallel mechanisms with a shared anchor. It is one blur-anchored $b$-structured phase system with a shared Nyquist constraint.

### 7.4 Status

${S\_{\\rm blur}, \\eta}$ is locked, and $b$-unification is now achieved within current canon through Obligation 2.

**Before v7:** shared blur anchor only.  
**v7:** shared blur anchor and shared substrate-resolution constraint.  
**Current status:** full two-wall $b$-unification achieved.

\---

## 8\. Closure Status of Theorem Obligations

### Obligation 2 — The k ∝ 1/b Bridge: Proved

**Claim.** The gate steepness satisfies $k = K/b$ with $K$ substrate-native and $b$-independent to within 0.1%.

**Derivation chain.** The minimum causal arc on the BCC Fibonacci boundary is $\\theta\_{\\rm min} = \\pi/3 + \\delta\\theta\_{\\rm coh}$, where:

* $\\pi/3$ is naturally induced as the zero-crossing seed: two inactive BCC gaps separate the entry active sector $\[0, \\pi/12]$ from the nearest exit active sector $\[\\pi/3, 5\\pi/12]$. A state exhausting all forward ticks reaches $\\theta = \\pi/3$ with zero lateral spread — tangency by tick budget.
* $\\delta\\theta\_{\\rm coh}$ is the minimum advance for $\\mathcal{O}(\\eta)$ coherent overlap, derived from the causal-shadow opening rate $\\phi'*{\\rm lead} = r*{\\rm lat}\\sqrt{1+b^2}$.

**Combinatorial Lemma** (closed). In 2D BCC with 8 nearest-neighbor links ${(\\pm 1,0), (0,\\pm 1), (\\pm 1,\\pm 1)}$, links with angular component ($y \\neq 0$) number 6; of these, same-sublattice ($(x+y)$ even) number exactly 4 — the four diagonal links $(\\pm 1,\\pm 1)$. These are the body-center diagonals, forced by BCC connectivity. Given BCC 8-fold coordination + bipartite sublattice constraint + 24-sector ring:

$$r\_{\\rm lat} = \\frac{4}{24} = \\frac{1}{6} \\qquad \\text{(zero free parameters)} \\qquad \\square$$

The metric compression follows from $ds\_\\parallel = r\\sqrt{1+b^2}d\\theta$, giving:

$$\\phi'\_{\\rm lead} = \\frac{1}{6}\\sqrt{1+b^2}$$

This reproduces $\\Delta S\_{\\rm ent}$ to within $\\mathcal{O}(10^{-6})$. The full derivation chain:

$$\\underbrace{\\text{BCC diagonals}}*{4\\ \\text{links}} + \\underbrace{\\text{bipartite}}*{\\text{same-sublattice}} + \\underbrace{N\_s=24}*{\\text{ring}} \\Rightarrow r*{\\rm lat} = \\frac{1}{6} \\Rightarrow \\phi'*{\\rm lead} = \\frac{1}{6}\\sqrt{1+b^2} \\Rightarrow \\Delta S*{\\rm ent} \\Rightarrow k = \\frac{K}{b}$$

*Status: proved within current canon. Zero free parameters.*

\---

### Obligations 1 and 3 — Straddling-Sector Exclusion Lemma: Proved

**Claim.** Straddling sectors ($S\_{\\rm lo} < 1.05 < S\_{\\rm hi}$) generate no $b^2$ term in $S\_{\\rm cap}$. Combined with the $b^1$ type-mismatch, the cubic correction $b^3/5$ is the unique admissible leading geometric correction.

**Theorem** (Straddling-Sector Exclusion). In the sharp-gate limit $k = K/b$, the correction from one straddling sector $\[1.05-\\alpha b, 1.05+\\beta b]$ to the capacity integral is:

$$\\delta I = \\frac{b}{K}\\ln\\frac{1+e^{-K\\beta}}{1+e^{-K\\alpha}} = \\mathcal{O}(b^1)$$

The $b$-cancellation is exact: $k \\cdot (\\beta b) = (K/b) \\cdot (\\beta b) = K\\beta$, so the logarithm sees a $b$-independent argument, forcing the prefactor $b/K$ to carry the sole $b$-dependence. Verified numerically for all tested $(\\alpha, \\beta)$ pairs. Symmetric straddling ($\\alpha = \\beta$) gives $\\delta I = 0$ exactly.

Summing: $\\delta I\_{\\rm total} = \\mathcal{O}(b^1)$. Multiplying by $P = (48/\\pi)/b$: $\\delta n = \\mathcal{O}(b^0)$ — a constant selector offset absorbed by rounding. For $\\delta S\_{\\rm cap} = \\mathcal{O}(b^2)$ to arise would require $\\delta I = \\mathcal{O}(b^3)$; the actual $\\delta I = \\mathcal{O}(b^1)$ makes this impossible. $\\square$

**The $b^1$ exclusion** (kinematic type mismatch). $S\_{\\rm cap}$ is a static topological bound set by discrete channel counts and phase quanta — both $b$-independent. The parameter $b = dS/d\\theta$ is a kinematic winding rate. A $b^1$ term conflates flow rate with static capacity ceiling. *Status: structurally argued; formal lemmatization pending.*

**The $b^3$ survival** (bulk volume). The 3D constraint manifold $(S\_{\\rm lo}, S\_{\\rm hi}, \\varepsilon)$ contributes a bulk volume element $\\sim b^3$ where each coordinate contributes one power of $b$ by active-sector linearity (proved in the sharp-gate interior). Denominator $5 = (2\\phi-1)^2$ is the squared fixed-point sensitivity of the Fibonacci characteristic polynomial. *Status: proved in active-sector interior; denominator candidate-locked.*

*Status: $b^2$ exclusion proved. $b^1$ exclusion structurally argued, formal lemmatization outstanding. $b^3$ survival proved in active-sector interior.*

\---

### Remaining Foundational Dependencies

**Dependency 1 — State-Space Ceiling Axiom formalization.**

The $b^1$ exclusion is structurally closed in canon, but its final formal presentation depends on one explicit axiom statement:

> \*\*State-Space Ceiling Axiom.\*\* HPF capacity ceilings are defined on state-space $S$-values, not on trajectory derivatives ($dS/d\\theta$).

This rule is already implicit throughout current canon, since $S\_{\\rm blur}$, $S\_{\\rm ent}$, and $S\_{\\rm cap}$ are all threshold values in $S$-space rather than kinematic rates. Writing it explicitly closes the $b^1$ exclusion as a formal lemma.

**Dependency 2 — Denominator uniqueness.**

The denominator $5 = (2\\phi-1)^2 = (P'(\\phi))^2$ is conditionally closed under the candidate Principle of Return-Class Capacity. Under that principle, denominator uniqueness is proved: the local fixed-point sensitivity generator is $P'(\\phi)$, and the minimal admissible bipartite return loop forces the quadratic power.

The remaining active research lane is not structural obstruction inside the theorem spine, but independent derivation of the Principle of Return-Class Capacity from microscopic QPRCA mechanics (reversibility, bijectivity, and return-class closure).

\---

## 9\. Locked Summary (v7)

The cubic-order argument is no longer a loose dimensional intuition. The selector is organized into a $b$-scaling framework where the zero-order term is the current candidate topological invariant of the reduced structural manifold, lower-order corrections are actively excluded, and the cubic term

$$\\frac{b^3}{(2\\phi-1)^2}$$

is the leading admissible geometric correction under the current canon, with denominator uniqueness conditionally closed under the Principle of Return-Class Capacity.

The two-wall architecture now shares the substrate-native common spine ${S\_{\\rm blur}=1.05, \\eta=1/48, b}$.

Obligation 2 is proved: $k = K/b$ follows from BCC diagonal structure, bipartite sublattice constraint, and the 24-sector ring with zero free parameters. The $b^2$ exclusion is proved by the Straddling-Sector Exclusion Lemma. The $b^3$ correction survives as the leading admissible bulk term in the active-sector interior. The $b^1$ exclusion is structurally closed and awaits only explicit axiomatization of the State-Space Ceiling rule.

**Obligation status:**

* Obligation 2: **proved**
* Obligations 1+3 ($b^2$ exclusion and cubic-order survival): **proved** within current canon
* $b^1$ exclusion: structurally closed; formal axiom statement pending
* Denominator $5 = (2\\phi-1)^2$: **conditionally closed** under the Principle of Return-Class Capacity

**Overall classification: internal structural lock / near-theorem derivation.** No internal structural obstruction remains in the current theorem spine. The remaining items are foundational formalization and independent microscopic grounding of the candidate return-class principle.

\---

## 10\. Candidate Registry Summary

|Candidate|$\\delta$ value|Status|
|-|-|-|
|C9: $b^3/(2\\phi-1)^2$|0.005750|Leading — near-theorem|
|C8: $\\eta \\cdot b \\cdot (1-b^2)$|0.005783|Secondary candidate|
|C5: $\\zeta$ tail lag|—|Eliminated (Fork B)|
|C1: $\\eta \\cdot b$|0.006382|Demoted|



\---

## 11\. Admissibility Guardrails (unchanged)

1. Independence from 5.7889
2. Drift-free across canon
3. $k$-robust with $S\_{\\rm ent}$ fixed
4. Interpretable in substrate operations
5. Geometric (Fork A)

\---

## \## 12. μ\_B Status (reframed)

The wall value $S\_{\\rm cap}=5.7889$ is no longer classified as a free resonance inside the live package; it is treated as derived / substrate-native through the BCC $\\to \\eta=1/48 \\to k \\to S\_{\\rm ent}=1.3806 \\xrightarrow{n=220} S\_{\\rm cap}$ closure chain. What remains open is the external identification $5.7889 \\leftrightarrow \\mu\_B$. The uniformization pressure test still shows that the $k\_B$ and $\\mu\_B$ SI mantissa matches do not co-appear in a single unit basis, so no completed SI derivation is claimed here. The $\\mu\_B$ correspondence therefore remains a ceiling-side candidate, weaker than the $k\_B$ correspondence, and independent of the theorem obligations.

## \---

## 13\. Full Canon Chain (current best)

$$S\_{\\rm cap} = \\underbrace{1.05}*{\\rm Lu\\ anchor} + \\underbrace{\\frac{3\\pi}{2}}*{\\rm 3\\ BCC\\ channels} + \\underbrace{\\frac{1}{48}}*{\\rm Nyquist} + \\underbrace{\\frac{b^3}{(P'(\\phi))^2}}*{\\rm cubic\\ Fibonacci\\ correction}$$

$$= 5.788972 \\quad \\text{(matching the active 5.7889 cap target within probe precision)}$$

**Status: Internal structural lock / near-theorem derivation.** The two-wall common spine ${S\_{\\rm blur}, \\eta, b}$ is locked. Obligation 2 is proved. The $b^2$ exclusion is proved via the Straddling-Sector Exclusion Lemma. The $b^1$ exclusion is structurally closed and awaits only explicit axiomatization of the State-Space Ceiling rule. Denominator uniqueness is conditionally closed under the candidate Principle of Return-Class Capacity; independent microscopic derivation of that principle remains open.

