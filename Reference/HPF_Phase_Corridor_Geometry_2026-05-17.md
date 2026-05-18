# HPF Phase Corridor Geometry — Reference

**Document Class:** HPF reference note
**Status:** Compiled from existing canon. Consolidates corridor-geometry facts that live implicitly across Volume I § 23, the $S_{\rm cap}$ derivation note, the $b/72$ mirror correction note, and the neutrino mass hierarchy note. Promotes nothing into canon; alters no truth-status partition.
**Author:** Eric Keaton Porter
**Date:** 2026-05-17

---

## 1. Scope

One-page geometric reference for the **Phase Corridor**. Purpose: make explicit what the formulas in canon imply by construction — the relative position of $S_{\rm blur}$, $S_{\rm ent}$, $S_{\rm cap}$, the **Hylo Forwarding Gate** transition between them, and the shadow correspondences pinned at each named point.

---

## 2. The three named points

The corridor has three named points: **Phase Blur** ($S_{\rm blur}$), **Phase Entropy** ($S_{\rm ent}$), and **Phase Cap** ($S_{\rm cap}$).

| Symbol | Value | Status | Shadow correspondence |
|---|---|---|---|
| $S_{\rm blur}$ | $1.05$ | Empirically anchored under HPF mapping (Lin 2026 single-atom double-slit half-blur midpoint) | $\hbar$ mantissa $= 1.054571$ |
| $S_{\rm ent}$ | $1.3806$ | Derived from corridor closure | $k_B$ mantissa $= 1.380649$ |
| $S_{\rm cap}$ | $5.7889$ | Substrate-native / derived (Jan 2026 autoencoder phase transition) | $\mu_B$ mantissa $= 5.788382$ |

Numerical ordering by construction:

$$S_{\rm blur} \;<\; S_{\rm ent} \;<\; S_{\rm cap}$$

$S_{\rm blur}$ sits **below** the **Phase Corridor** $[S_{\rm ent}, S_{\rm cap}]$. It is not the corridor midpoint. The geometric midpoint of the corridor is $\sqrt{S_{\rm ent} \cdot S_{\rm cap}} \approx 2.83$; the linear midpoint is $\approx 3.58$. Neither is $S_{\rm blur}$.

---

## 3. The Hylo Forwarding Gate

The **Phase Corridor** is structured by the logistic coherence gate

$$\zeta(S) \;=\; \frac{1}{1 + \exp\!\big(k(S - S_{\rm blur})\big)}$$

with steepness determined by the **Phase Residual** $\eta = 1/48$ (BCC 24-sector Nyquist residual):

$$k_{\rm exact} \;=\; \frac{\ln\big((1-\eta)/\eta\big)}{S^{*} - S_{\rm blur}} \;=\; \frac{\ln 47}{S^{*} - 1.05} \;\approx\; 11.646$$

operationally rounded to $k_{\rm op} = 11$.

Gate behavior:

- $S \ll S_{\rm blur}$: $\zeta(S) \approx 1$ — coherent regime
- $S = S_{\rm blur}$: $\zeta(S) = 1/2$ — half-blur (decoherence midpoint, where Lin 2026 anchors)
- $S \gg S_{\rm blur}$: $\zeta(S) \approx 0$ — decohered regime

By the time $S$ reaches $S_{\rm ent} = 1.3806$, the **Hylo Forwarding Gate** has essentially completed its transition. The **Phase Corridor** $[S_{\rm ent}, S_{\rm cap}]$ is post-gate territory.

---

## 4. The Hylo Selector

The integral over the decohered region produces the shell selector:

$$n_{\rm sel} \;=\; \mathrm{round}\!\left[\frac{24}{\ln\varphi} \int_{S_{\rm ent}}^{S_{\rm cap}} \big(1 - \zeta(S)\big)\, dS\right] \;=\; 220$$

Equivalent static form (load-bearing closure since 2026-05-09; cell-counting premise closed 2026-05-17 via the bipartite-squaring mechanism in `Reference/HPF_Cell_Counting_Premise_Closure_2026-05-17.md`):

$$n \;=\; \mathrm{round}\!\left(\frac{N_s^{\,2}}{\varphi^{\,2}}\right) \;=\; \mathrm{round}\!\left(\frac{576}{2.618}\right) \;=\; 220$$

with $N_s = 24$ active spatial sectors from BCC 8-fold coordination lifted to 3D. Both forms yield the substrate-native shell count $n=220$. Rounding margin $\approx 0.5$.

---

## 5. Physical interpretation (structural argument)

The **Phase Corridor** $[S_{\rm ent}, S_{\rm cap}]$ admits a natural physical interpretation as the **wave function collapse phase**: the region between coherence-loss completion and classical-observable emergence. The three named points label three physical transitions:

| Point | Physical role | Constant shadowing |
|---|---|---|
| $S_{\rm blur}$ | Coherence-loss midpoint | $\hbar$ — action quantum, scale of quantum dynamics |
| $S_{\rm ent}$ | Entropy onset, lower wall | $k_B$ — entropy in physical units |
| $S_{\rm cap}$ | Spin / EM emergence, upper wall | $\mu_B = e\hbar/(2m_e)$ — bridge between angular momentum, charge, mass |

Reading by region:

- $S < S_{\rm blur}$: quantum-coherent regime
- $S_{\rm blur} \le S < S_{\rm ent}$: **Hylo Forwarding Gate** transition, coherence being lost
- $S_{\rm ent} \le S \le S_{\rm cap}$: collapse-phase corridor where survival-weighted representation lives
- $S > S_{\rm cap}$: classical states with definite EM observables

The constants $\hbar$, $k_B$, $\mu_B$ are the constants physics has independently used to label exactly these transitions. Substrate landing within mantissa tolerance of those three specific constants out of all possible constants is consistent with the corridor representing the wave function collapse phase.

---

## 6. Shadow-correspondence chronology

For provenance and against the "tuning" reading of the **HPF Shadow Rule**:

1. **January 2026** — Autoencoder phase-transition experiments locate $S_{\rm cap} = 5.7889$ as the hard-collapse threshold. Predates the formal framework.
2. **~February 2026** — Corridor closure derives $S_{\rm ent} = 1.3806$ from $S_{\rm blur} + \eta + k$.
3. **~March 2026** — Numerical proximity to $\hbar$, $k_B$, $\mu_B$ mantissas noticed. Shadow identifications hypothesized as candidate correspondences.
4. **Tested for consistency** — Predictions computed with $\hbar$, $k_B$, $\mu_B$ used as bridges at $S_{\rm blur}$, $S_{\rm ent}$, $S_{\rm cap}$. Identifications passed.
5. **Adopted as working shadows** — Used in the $\nu$ base-mass derivation and other downstream computations.

The shadow correspondences are tested candidate identifications, not fits. Substrate values came first; the constants were noticed second; the identifications were verified by consistency rather than calibrated to match. GitHub commit timestamps make this auditable.

---

## 7. Open frontier

The structural argument in § 5 supplies a candidate answer to *why* the substrate values fall within mantissa tolerance of $\hbar$, $k_B$, $\mu_B$: they label the same physical transitions the constants label. This is the Route 2 shadow-closure argument (structural role match).

What remains open:

1. Closing $S_{\rm ent}$'s first-principles derivation in a single consolidated document (currently distributed across notes).
2. Developing the substrate-native unit chain (Route 1) that would make the SI value-correspondence derivable rather than tested.
3. Item (2) of Vacuum Sector Bipartite Closure § 6 — bipartite A/B invariance audit on $\zeta(S)$, $S_{\rm ent}$, $S_{\rm cap}$ in the **Hylo Selector** integral.

These remain frontier items under the **HPF Truth Discipline**.

---

## 8. Summary

$$S_{\rm blur}\,(\hbar) \;\;<\;\; S_{\rm ent}\,(k_B) \;\;<\;\; S_{\rm cap}\,(\mu_B)$$

| Region | $S$ range | Regime |
|---|---|---|
| Below $S_{\rm blur}$ | $S < 1.05$ | Quantum-coherent |
| **Hylo Forwarding Gate** transition | $1.05 \le S < 1.3806$ | Coherence being lost |
| **Phase Corridor** | $1.3806 \le S \le 5.7889$ | **Wave function collapse phase** |
| Above $S_{\rm cap}$ | $S > 5.7889$ | Classical / hard collapse |

---

## Cross-references

- `Docs/Volume_I_Foundations.md` § 22–23 — active phase landmarks and statuses
- `Reference/HPF_Scap_SubstrateNative_Derivation.md` — $S_{\rm cap}$ derivation, including the $N_s^2/\varphi^2$ static form
- `Reference/HPF_Cell_Counting_Premise_Closure_2026-05-17.md` — bipartite-squaring closure of the $N_s^2$ and $\varphi^2$ cell-counting premise underlying $n=220$
- `Reference/HPF_b72_Passive_Mirror_Correction_Reference_2026-04-15.md` — $\eta = 1/48$ and $b/72$ derivation
- `Reference/HPF_Correction_Note_LowerWall_Nyquist_2026-04-12.md` — $S_{\rm ent}$ Nyquist relation
- `Phenomenology/HPF_Neutrino_Mass_Hierarchy_Candidate_Note_2026-04-11_final.md` — $\nu$ base-mass derivation using the $k_B$ shadow at $S_{\rm ent}$
- `Reference/HPF_2_5_0_release_notes_2026-05-16.md` — current vocabulary lock

---

*Compiled 2026-05-17. Reference document only — geometric explication of existing HPF canon. Promotes nothing into canon and alters no truth-status partition.*
