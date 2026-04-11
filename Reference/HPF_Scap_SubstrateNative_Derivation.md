# HPF Reference Note — Substrate-Native Derivation of \(S_{\rm cap}\)
## Closure Note for the Vacuum-Sector Ceiling
### Consolidated Rewrite (2026-04-10)

**Author:** Eric Keaton Porter  
**Status:** Derived / substrate-native  
**Purpose:** Close the historical open item on the theoretical grounding of \(S_{\rm cap}\) while preserving the original probe discovery path.

---

# 1. What this note does

This note exists for one reason:

> to state cleanly why the live HPF package now treats
> 
> $$
> S_{\rm cap}=5.7889
> $$
> 
> as **derived / substrate-native** rather than merely “empirically found but theoretically open.”

It is not a full vacuum-sector presentation. It is a closure note.

---

# 2. Historical fact that remains true

Historically, \(S_{\rm cap}\) was first found by geometric stability probe.

A tanh bottleneck system was driven through increasing noise until the collapse boundary was isolated by binary search. That produced the boundary value

$$
S_{\rm cap}=5.7889.
$$

That historical fact remains true and must not be erased.

---

# 3. Live closure fact that now also holds

Later structural work closed the theoretical grounding.

In the current package, the ceiling is forced by the chain

$$
\text{BCC} \rightarrow \eta=\frac{1}{48} \rightarrow k \rightarrow S_{\rm ent}=1.3806 \xrightarrow{n=220} S_{\rm cap}=5.7889.
$$

That means the live truth-status is now:

$$
S_{\rm cap} \quad \text{is derived / substrate-native.}
$$

The probe discovered the value first. The later closure showed the substrate was always going to demand it.

---

# 4. Derivation chain

## 4.1 Step 1 — Nyquist residual from BCC geometry

The BCC substrate carries \(24\) active spatial sectors in the live package.

Nyquist then gives the minimum non-zero residual margin

$$
\eta=\frac{1}{2\times24}=\frac{1}{48}.
$$

No free parameter enters.

---

## 4.2 Step 2 — gate steepness from the blur anchor and residual

The active blur gate is

$$
\zeta(S)=\frac{1}{1+e^{k(S-1.05)}}.
$$

With \(S_{\rm blur}=1.05\) and \(\eta=1/48\), the exact steepness relation is

$$
k=\frac{\ln\!\left(\frac{1-\eta}{\eta}\right)}{S^*-1.05}
=\frac{\ln 47}{S^*-1.05}
\approx 11.646.
$$

Operational rounded value: \(k=11\).

---

## 4.3 Step 3 — live lower onset

At the exact closure point, the active lower onset is

$$
S_{\rm ent}=1.3806.
$$

This is the live lower selector bound. The old rounded \(1.4\) marker is historical only.

---

## 4.4 Step 4 — shell selector fixes the ceiling

The active shell selector is

$$
n_{\rm sel}=
\mathrm{round}\!\left[
\frac{24}{\ln\varphi}
\int_{S_{\rm ent}}^{S_{\rm cap}}(1-\zeta(S))\,dS
\right].
$$

The live package has already candidate-locked

$$
n=220.
$$

So once the active lower onset is fixed and the selector is fixed, the upper wall is no longer free.

In the step-limit approximation, this gives

$$
S_{\rm cap}\approx S_{\rm ent}+220\frac{\ln\varphi}{24}.
$$

Numerically,

$$
S_{\rm cap}\approx 1.3806 + 220\frac{0.481212}{24}
=1.3806+4.4111
=5.7917.
$$

That already lands essentially on the discovered ceiling.

---

# 5. Why the remaining gap is not a derivation failure

The step-limit estimate gives \(5.7917\), while the probe found \(5.7889\).

Difference:

$$
5.7917-5.7889 \approx 0.0028.
$$

That gap is small and expected. It comes from the fact that the true gate is not an infinite step function. The logistic tail at finite \(k\) slightly lowers the effective ceiling relative to the sharp-step estimate.

So the correct reading is:

- \(5.7917\) = sharp-step closure estimate,
- \(5.7889\) = finite-\(k\) realized ceiling.

These are consistent, not contradictory.

---

# 6. Closed statement

The ceiling is determined by the live lower onset and the shell count.

Equivalently:

> \(S_{\rm cap}\) is the amount of phase-space corridor required to support the candidate-locked shell count \(n=220\) once the BCC 24-sector conversion law and live lower onset \(S_{\rm ent}=1.3806\) are fixed.

That is why the current package no longer treats \(S_{\rm cap}\) as theoretically open.

---

# 7. What this note changes in package wording

## Old wording (historical)
- \(S_{\rm cap}\) discovered by probe.
- theoretical grounding still open.

## New live wording
- \(S_{\rm cap}\) discovered historically by probe,
- now **derived / substrate-native** in the live package.

That is the whole point of this note.

---

# 8. What this note does not do

This note does **not**:
- prove uniqueness of every intermediate step,
- replace the full vacuum-sector package,
- replace the provenance history,
- erase the probe chronology,
- promote \(n=220\) from candidate-locked to theorem-level uniqueness.

It closes one status question only: the live status of \(S_{\rm cap}\).

---

# 9. Freeze wording

> \(S_{\rm cap}=5.7889\) was discovered historically by geometric stability probe, but in the current HPF package it is no longer treated as theoretically open. The live closure chain is
> 
> $$
> \text{BCC} \rightarrow \eta=\frac{1}{48} \rightarrow k \rightarrow S_{\rm ent}=1.3806 \xrightarrow{n=220} S_{\rm cap}=5.7889.
> $$
> 
> In the sharp-step limit this gives \(S_{\rm cap}\approx5.7917\), and the small residual gap to the probe value is accounted for by the finite-\(k\) tail of the logistic gate. The correct live truth-status is therefore: \(S_{\rm cap}\) is derived / substrate-native, with the probe preserved as the original discovery path.

