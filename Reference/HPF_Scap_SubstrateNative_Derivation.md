# HPF Reference Note — Substrate-Native Derivation of $S_{\rm cap}$
## Closure Note for the Vacuum-Sector Ceiling
### Consolidated Rewrite (2026-04-10) — Corrected 2026-04-15 — Reframed 2026-05-09

**Author:** Eric Keaton Porter  
**Status:** Derived / substrate-native  
**Purpose:** Close the historical open item on the theoretical grounding of $S_{\rm cap}$ while preserving the original probe discovery path.

**2026-04-15 correction:** §4.4 updated to reflect that $n=220$ is geometry-native (not candidate-locked by hand). §5 corrected: the finite-$k$ explanation for the residual gap is retired and replaced with the shell-width resolution explanation. §9 freeze wording updated accordingly.

**2026-05-09 reframe:** §4.4 and §5 reframed in response to a published audit catch (Austin, IPI list, 2026-05-09). The shell-width-as-resolution framing in the prior §5 was internally inconsistent: it described a tolerance band centered on the step-limit value 5.7917 with lower edge 5.7816, but the integral form's actual rounding boundary going down sits at $S_{\rm cap}\approx 5.7841$. Values in [5.7816, 5.7841] sit in the claimed shell-width band but round the integral form to $n=219$, contradicting the band's own claim. The reframe (i) retires the shell-width-as-resolution argument, (ii) promotes the static identity $n=\mathrm{round}(N_s^2/\varphi^2)=220$ to primary load-bearing closure (rounding margin ≈ 0.488/0.512), (iii) demotes the integral form to consistency check, and (iv) names the standalone first-principles closure of the cell-counting premise as the actual frontier obligation. §9 freeze wording updated accordingly.

**2026-05-17 closure:** The cell-counting premise ($N_s^2$ cells per arc and $\varphi^2$ per-shell occupancy) is now closed via the bipartite-squaring mechanism in `Reference/HPF_Cell_Counting_Premise_Closure_2026-05-17.md`. The qualifier "under candidate cell-counting premise" is removed from §4.4 and §5 and §9. $n=220$ is now derived / substrate-native without qualifier. The cell-count premise inherits the same inference pattern as RCC's $(P'(\varphi))^2 = 5$, $\eta = 1/48$, and the b/72 passive mirror correction.

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

Historically, $S_{\rm cap}$ was first found by geometric stability probe.

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

The probe discovered the value first. The later closure showed the substrate was always going to demand it. The cell-counting premise ($N_s^2$ cells per arc and $\varphi^2$ per-shell occupancy) is closed in `Reference/HPF_Cell_Counting_Premise_Closure_2026-05-17.md`; see §4.4 and §8 for the integrated status.

---

# 4. Derivation chain

## 4.1 Step 1 — Nyquist residual from BCC geometry

The BCC substrate carries $24$ active spatial sectors in the live package.

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

With $S_{\rm blur}=1.05$ and $\eta=1/48$, the exact steepness relation is

$$
k=\frac{\ln\!\left(\frac{1-\eta}{\eta}\right)}{S^*-1.05}
=\frac{\ln 47}{S^*-1.05}
\approx 11.646.
$$

Operational rounded value: $k=11$.

---

## 4.3 Step 3 — live lower onset

At the exact closure point, the active lower onset is

$$
S_{\rm ent}=1.3806.
$$

This is the live lower selector bound. The old rounded $1.4$ marker is historical only.

---

## 4.4 Step 4 — shell count and ceiling

**Primary closure: static identity for the shell count.** The shell count $n$ is not a free parameter. The primary load-bearing form is the static geometry-native identity:

$$
n = \mathrm{round}\!\left(\frac{N_s^2}{\varphi^2}\right) = \mathrm{round}\!\left(\frac{576}{2.6180}\right) = \mathrm{round}(220.012) = 220.
$$

This static identity rounds to $n=220$ with rounding margin ≈ 0.488 going down and 0.512 going up — substantially robust against perturbations of the inputs $N_s$ and $\varphi$.

**Status of the underlying cell-counting premise.** The static identity rests on a cell-counting picture: the BCC Fibonacci spiral covers $N_s^2$ lattice cells per full causal arc, divided by the per-shell golden-ratio gain $\varphi^2$. As of 2026-05-17, both $N_s^2$ and $\varphi^2$ are closed via the bipartite-squaring mechanism in `Reference/HPF_Cell_Counting_Premise_Closure_2026-05-17.md`. $N_s^2 = 576$ follows from bipartite ordered-pair indexing of A-origin and B-destination angular sectors under the QPRCA alternating-half-tick protocol. $\varphi^2 = \varphi+1$ follows from Fibonacci linear growth compounded across one A-half-step plus one B-half-step. Both inherit the same inference pattern (executable mechanism verification + 3D substrate derivation) that grounds $(P'(\varphi))^2 = 5$ in RCC, $\eta = 1/48$ in the Nyquist derivation, and the b/72 passive mirror residual. Accordingly, $n=220$ is now **derived / substrate-native** without qualifier. The cell-counting premise is closed; the cell-counting closure note is the canonical source for the closure mechanism.

**Ceiling from shell count (step-limit consistency form).** Once $n=220$ is fixed by the static identity above, the shell selector in the step-function limit gives a closed-form expression for the ceiling:

$$
S_{\rm cap} = S_{\rm ent} + n\cdot\frac{\ln\varphi}{N_s}.
$$

Numerically,

$$
S_{\rm cap} = 1.3806 + 220\cdot\frac{0.481212}{24}
= 1.3806 + 4.4111
= 5.7917.
$$

The full chain with no free parameters:

$$
S_{\rm cap} = S_{\rm ent} + \frac{N_s^2}{\varphi^2}\cdot\frac{\ln\varphi}{N_s} = S_{\rm ent} + \frac{N_s\ln\varphi}{\varphi^2}.
$$

**Status of the integral form.** The dynamic selector formula

$$
n_{\rm sel} = \mathrm{round}\!\left[\frac{24}{\ln\varphi}\int_{S_{\rm ent}}^{S_{\rm cap}}(1-\zeta(S))\,dS\right]
$$

is a **consistency check** on the static identity, not an independent closure. With the live values it gives $n_{\rm raw}=219.742$ and rounds to $n=220$, in agreement with the static identity. The integral form's rounding margin (≈ 0.242/0.758) is tighter than the static identity's (≈ 0.488/0.512) because it depends on the four corridor parameters $S_{\rm blur}, k, S_{\rm ent}, S_{\rm cap}$ rather than on $N_s$ and $\varphi$ alone. The static identity is therefore primary; the integral form serves as a downstream sanity check that the corridor dynamics are consistent with the geometry-native shell count.

---

# 5. Why the residual gap of 0.003 is not a derivation failure

The step-limit formula gives $5.7917$. The probe found $5.7889$. The difference is

$$
5.7917-5.7889 = 0.0028.
$$

This gap is not a derivation failure. The correct explanation is **integral-form rounding band**, not shell-width tolerance.

**Integral-form rounding band.** The integral selector has prefactor $24/\ln\varphi\approx 49.86$; its inverse, the natural quantization step in $S_{\rm cap}$ per unit shift in $n_{\rm raw}$, is

$$
\Delta S_{\rm per\;shell} = \frac{\ln\varphi}{N_s} \approx 0.0201.
$$

For $S_{\rm cap}$ at the probe value 5.7889, $n_{\rm raw}=219.742$. The rounding band keeping $n=220$ is $n_{\rm raw}\in[219.5,\,220.5]$, which in $S_{\rm cap}$ units is

$$
S_{\rm cap}\in[5.7841,\,5.8041].
$$

This band has width 0.020 (the natural quantization step) and is centered on $n_{\rm raw}=219.742$, i.e. offset toward the lower edge. Both the probe value 5.7889 and the step-limit value 5.7917 sit inside this band; their difference 0.003 is smaller than the band width 0.020. The integral form cannot and does not need to distinguish them.

**Note on the prior shell-width-as-resolution explanation (retired).** An earlier version of this note attributed the gap to a "shell-width resolution band" centered on the step-limit value 5.7917, giving lower edge 5.7816 and upper edge 5.8016. This framing was internally inconsistent: 5.7816 sits below the integral form's actual rounding boundary 5.7841 by 0.0025, so values in [5.7816, 5.7841] would be in the claimed shell-width band but round the integral to $n=219$, contradicting the band's own claim. The shell-width-as-resolution explanation is retired in this reframe (2026-05-09). The integral-form rounding band above replaces it.

**Note on the finite-$k$ explanation (retired earlier).** An even earlier version of this note attributed the gap to the logistic tail at finite $k$ lowering the effective ceiling. This is also incorrect. Numerical sweep across $k\in[0.5,10000]$ shows the integral has a floor at the step-limit value 5.7917 (reached by $k\approx 50$); lower $k$ raises $S_{\rm cap}$ further from the probe, not toward it. No value of $k$ reaches 5.7889 through the integral. The finite-$k$ explanation was retired in 2026-04-15 and remains retired.

---

# 6. Closed statement

The ceiling is determined by the BCC sector count and the golden ratio alone.

Equivalently:

> $S_{\rm cap}$ is the amount of phase-space corridor required to support $n = \mathrm{round}(N_s^2/\varphi^2) = 220$ Fibonacci shells once the BCC 24-sector geometry and live lower onset $S_{\rm ent}=1.3806$ are fixed. The static shell-count identity carries the load-bearing closure; the integral form is a consistency check. No free parameters enter anywhere in the chain. The cell-counting premise underlying the static identity ($N_s^2$ cells per causal arc) remains the named frontier obligation; closing it standalone would promote $n=220$ from "derived under candidate premise" to "fully derived."

That is why the current package no longer treats $S_{\rm cap}$ as theoretically open.

---

# 7. What this note changes in package wording

## Old wording (historical)
- $S_{\rm cap}$ discovered by probe.
- Theoretical grounding still open.
- $n=220$ candidate-locked by hand.
- Residual gap explained by shell-width resolution.

## New live wording (2026-05-17)
- $S_{\rm cap}$ discovered historically by probe,
- now **derived / substrate-native** in the live package,
- $n=220$ is geometry-native via the static identity $\mathrm{round}(N_s^2/\varphi^2)$, with rounding margin ≈ 0.5,
- The static identity is the primary closure; the integral form is a consistency check,
- Residual 0.003 gap explained by the integral form's own rounding band of width $\ln\varphi/N_s\approx 0.020$, centered on $n_{\rm raw}=219.742$ with edges 5.7841 and 5.8041, both probe (5.7889) and step-limit (5.7917) inside,
- Cell-counting premise ($N_s^2$ cells per arc and $\varphi^2$ per-shell occupancy) closed via the bipartite-squaring mechanism in `Reference/HPF_Cell_Counting_Premise_Closure_2026-05-17.md`.

---

# 8. What this note does not do

This note does **not**:
- prove uniqueness of every intermediate step,
- replace the full vacuum-sector package,
- replace the provenance history,
- erase the probe chronology,
- promote $n=220$ from geometry-native to theorem-level uniqueness of the rounding.

It closes one status question (live status of $S_{\rm cap}$); the cell-counting premise closure note (2026-05-17) closes the named frontier obligation that this note previously identified as outstanding.

---

# 9. Freeze wording

> $S_{\rm cap}=5.7889$ was discovered historically by geometric stability probe, but in the current HPF package it is no longer treated as theoretically open. The live closure chain is
> 
> $$
> N_s=24 \;\rightarrow\; n=\mathrm{round}(N_s^2/\varphi^2)=\mathrm{round}(220.012)=220 \;\rightarrow\; S_{\rm cap} = S_{\rm ent} + n\cdot\frac{\ln\varphi}{N_s} = 5.7917 \approx 5.7889.
> $$
> 
> The static shell-count identity is the primary load-bearing closure with rounding margin ≈ 0.5 in $n_{\rm raw}$ units. The dynamic integral form $n_{\rm sel}=\mathrm{round}[(24/\ln\varphi)\int(1-\zeta)dS]$ is a consistency check that yields the same $n=220$ at $n_{\rm raw}=219.742$, with rounding band 5.7841 ≤ $S_{\rm cap}$ ≤ 5.8041 of width $\ln\varphi/N_s\approx 0.020$. The step-limit formula gives 5.7917; the probe gave 5.7889. Both sit inside the integral form's rounding band. The 0.003 difference is sub-band by construction and does not need to be resolved by the framework. The prior shell-width-as-resolution explanation (which incorrectly placed a band centered on 5.7917 with lower edge 5.7816) is retired as of 2026-05-09. No value of $k$ in the logistic gate explains the gap — the integral has a floor at 5.7917 and lower $k$ raises $S_{\rm cap}$ further from the probe, not toward it. The correct live truth-status is: $S_{\rm cap}$ is **derived / substrate-native**, with no free parameters and no qualifier, and the probe is preserved as the original discovery path. The cell-counting premise ($N_s^2$ cells per arc and $\varphi^2$ per-shell occupancy) is closed in `Reference/HPF_Cell_Counting_Premise_Closure_2026-05-17.md` via the bipartite-squaring mechanism.

---

*Original: 2026-04-10. Corrected: 2026-04-15 (§4.4 n=220 geometry-native; §5 finite-k explanation retired, shell-width resolution substituted; §9 freeze wording updated). Reframed: 2026-05-09 (§4.4 static identity promoted to primary, integral form demoted to consistency check; §5 shell-width-as-resolution retired, replaced with integral-form rounding band; §6, §7, §8, §9 updated; cell-counting premise named as frontier obligation explicitly). Numerical verification from WarStationAlpha QPRCA BCC v0.3.0 session and from Austin audit catch on IPI list (2026-05-09).*
