# HPF Reference Note — Substrate-Native Derivation of \(S_{\rm cap}\)
## Closure Note for the Vacuum-Sector Ceiling
### Consolidated Rewrite (2026-04-10) — Corrected 2026-04-15

**Author:** Eric Keaton Porter  
**Status:** Derived / substrate-native  
**Purpose:** Close the historical open item on the theoretical grounding of \(S_{\rm cap}\) while preserving the original probe discovery path.

**2026-04-15 correction:** §4.4 updated to reflect that \(n=220\) is geometry-native (not candidate-locked by hand). §5 corrected: the finite-\(k\) explanation for the residual gap is retired and replaced with the shell-width resolution explanation. §9 freeze wording updated accordingly.

---

# 1. What this note does

This note exists for one reason:

> to state cleanly why the live HPF package now treats
> 
> $$
> S_{\rm cap}=5.7889
> $$
> 
> as **derived / substrate-native** rather than merely "empirically found but theoretically open."

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
\text{BCC} \rightarrow N_s=24 \rightarrow n=\mathrm{round}\!\left(\frac{N_s^2}{\varphi^2}\right)=220 \xrightarrow{} S_{\rm cap}=5.7889.
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

## 4.4 Step 4 — shell count and ceiling

**Shell count (geometry-native).** The shell count \(n\) is not a free parameter. It is derived from the BCC sector count and the golden ratio:

$$
n = \mathrm{round}\!\left(\frac{N_s^2}{\varphi^2}\right) = \mathrm{round}\!\left(\frac{576}{2.6180}\right) = \mathrm{round}(220.012) = 220.
$$

No free parameter enters. \(n=220\) is geometry-forced.

**Ceiling from shell count (step-limit).** The shell selector in the step-function limit gives

$$
S_{\rm cap} = S_{\rm ent} + n\cdot\frac{\ln\varphi}{N_s}.
$$

Numerically,

$$
S_{\rm cap} = 1.3806 + 220\cdot\frac{0.481212}{24}
= 1.3806 + 4.4111
= 5.7917.
$$

That lands essentially on the discovered ceiling. The full derivation chain collapses to a single formula with no free parameters:

$$
S_{\rm cap} = S_{\rm ent} + \frac{N_s^2}{\varphi^2}\cdot\frac{\ln\varphi}{N_s} = S_{\rm ent} + \frac{N_s\ln\varphi}{\varphi^2}.
$$

---

# 5. Why the remaining gap is not a derivation failure

The step-limit formula gives \(5.7917\), while the probe found \(5.7889\).

Difference:

$$
5.7917-5.7889 = 0.0028.
$$

This gap is not a derivation failure. The correct explanation is **shell-width resolution**.

The formula resolves \(S_{\rm cap}\) to one shell-width:

$$
\delta S = \frac{\ln\varphi}{N_s} = \frac{0.48121}{24} \approx 0.020.
$$

The valid range for \(S_{\rm cap}\) at \(n=220\) is therefore:

$$
S_{\rm cap} \in \left[S_{\rm ent} + 219.5\cdot\frac{\ln\varphi}{N_s},\; S_{\rm ent} + 220.5\cdot\frac{\ln\varphi}{N_s}\right] = [5.7816,\; 5.8016].
$$

Both the step-limit value \(5.7917\) and the probe value \(5.7889\) sit inside this bin. Their difference \(0.003\) is smaller than the resolution \(0.020\). The derivation cannot and does not need to distinguish them.

**Note on the finite-\(k\) explanation (retired).** An earlier version of this note attributed the gap to the logistic tail at finite \(k\) lowering the effective ceiling. This is incorrect. Numerical sweep of the integral formula across \(k \in [0.5, 10000]\) shows that the formula has a floor at the step-limit value \(5.7917\) (reached by \(k \approx 50\)), and lower \(k\) raises \(S_{\rm cap}\) further above the probe value, not toward it. No value of \(k\) reaches \(5.7889\) through the integral. The finite-\(k\) explanation is retired. The shell-width resolution explanation replaces it.

---

# 6. Closed statement

The ceiling is determined by the BCC sector count and the golden ratio alone.

Equivalently:

> \(S_{\rm cap}\) is the amount of phase-space corridor required to support \(n = \mathrm{round}(N_s^2/\varphi^2)\) Fibonacci shells once the BCC 24-sector geometry and live lower onset \(S_{\rm ent}=1.3806\) are fixed. No free parameters enter anywhere in the chain.

That is why the current package no longer treats \(S_{\rm cap}\) as theoretically open.

---

# 7. What this note changes in package wording

## Old wording (historical)
- \(S_{\rm cap}\) discovered by probe.
- Theoretical grounding still open.
- \(n=220\) candidate-locked by hand.

## New live wording
- \(S_{\rm cap}\) discovered historically by probe,
- now **derived / substrate-native** in the live package,
- \(n=220\) is geometry-native: \(\mathrm{round}(N_s^2/\varphi^2)\).

---

# 8. What this note does not do

This note does **not**:
- prove uniqueness of every intermediate step,
- replace the full vacuum-sector package,
- replace the provenance history,
- erase the probe chronology,
- promote \(n=220\) from geometry-native to theorem-level uniqueness of the rounding.

It closes one status question only: the live status of \(S_{\rm cap}\).

---

# 9. Freeze wording

> \(S_{\rm cap}=5.7889\) was discovered historically by geometric stability probe, but in the current HPF package it is no longer treated as theoretically open. The live closure chain is
> 
> $$
> N_s=24 \;\rightarrow\; n=\mathrm{round}(N_s^2/\varphi^2)=220 \;\rightarrow\; S_{\rm cap} = S_{\rm ent} + n\cdot\frac{\ln\varphi}{N_s} = 5.7917 \approx 5.7889.
> $$
> 
> The step-limit formula gives \(5.7917\). The probe gave \(5.7889\). The gap of \(0.003\) is sub-resolution: the formula resolves \(S_{\rm cap}\) to one shell-width \(\delta S = \ln\varphi/N_s \approx 0.020\), and both values sit inside the same \(n=220\) bin. No value of \(k\) in the logistic gate explains the gap — the integral formula has a floor at \(5.7917\) and lower \(k\) raises \(S_{\rm cap}\) further from the probe, not toward it. The correct explanation is shell-width resolution. The correct live truth-status is: \(S_{\rm cap}\) is derived / substrate-native, with no free parameters, and the probe is preserved as the original discovery path.

---

*Original: 2026-04-10. Corrected: 2026-04-15 (§4.4 n=220 geometry-native; §5 finite-k explanation retired, shell-width resolution substituted; §9 freeze wording updated). Numerical verification from WarStationAlpha QPRCA BCC v0.3.0 session.*
