# HPF Photon-Ring Echo: Candidate Note
## Three Isolated Obligations

**Document Class:** HPF phenomenology candidate note
**Status:** Candidate — not canon. Three obligations open.
**Compatibility:** Repo-compatible. Fills the admitted amplitude gap in active package.
**Author:** Eric Keaton Porter
**Date:** 2026-04-01

---

## Abstract

The active HPF package retains the photon-ring echo location at $1.05 \times r_{\rm photon}$ as substrate-native via $S_{\rm blur}$, while explicitly removing the old amplitude fit $\varepsilon = 0.134$ and leaving amplitude open. This note fills that gap with a substrate-native amplitude candidate $A_{\rm echo} = \eta = 1/48 \approx 2.08\%$, derived from the BCC Nyquist residual. Three obligations remain before this becomes candidate-locked. They are isolated and stated explicitly below.

---

## Locked Inputs From Active Package

| Input | Value | Status in active package |
|---|---|---|
| $S_{\rm blur}$ | 1.05 | Locked empirical anchor |
| $\zeta(S_{\rm blur})$ | 0.5 | Locked by construction |
| $\eta = 1/(2N_s) = 1/48$ | 0.02083 | Candidate-strong, BCC Nyquist |
| Echo location | $1.05 \times r_{\rm photon}$ | Candidate retained in active package; derivational closure still open |
| Old amplitude $\varepsilon = 0.134$ | — | Explicitly removed, not substrate-native |

---

## Universality Assumption (UA)

Before the three obligations, one explicit assumption must be stated.

> **Universality Assumption (UA).** The entropic flux variable $S_f$ is a substrate-native, dimensionless load measure defined at the HPF layer prior to expert routing. The value $S_{\rm blur} = 1.05$ is the unique half-saturation blur boundary of the BCC 24-sector phase-representation law. Because this boundary is substrate-intrinsic rather than expert-defined, any physical process whose substrate load reaches $S_{\rm blur}$ encounters the same sector-resolution limit and the same minimum unresolved Nyquist remainder $\eta = 1/48$, while the observable downstream consequence remains domain-dependent.

**Canon support for UA:** $S_f$ lives at the HPF layer upstream of all expert routing. $S_{\rm blur}$ cannot be owned by QM or GR because both are downstream experts. The dimensionlessness of $S_f$ is a necessary condition for UA coherence — satisfied by construction.

**What UA does not claim:**
- That $S_{\rm blur}$ is the only substrate boundary
- That every system reaches $S_{\rm blur}$
- That downstream observables are identical across domains
- That Lu and M87* are the same physical system

UA is an explicit assumption, well-motivated but not yet a derived consequence of canon.

---

## Obligation 1: Forwarding-Identification Lemma

**Target:** Show that in the Schwarzschild GR expert regime, the local null escape fraction $f_{\rm forward}(r)$ is the natural candidate realization of the HPF forwarding efficiency $\zeta$.

**Current derivation:**

Five required properties of $\zeta$ in HPF canon:

1. Dimensionless
2. Local boundary-processing measure
3. Monotonically degrading as trapping load increases
4. Equal to 1/2 at the marginal forwarding boundary
5. Governs whether coherent propagation continues or fails

**Check against $f_{\rm forward}(r) = 1 - f_{\rm capture}(r)$ in Schwarzschild:**

*Property 1:* $f_{\rm forward}$ is a ratio of solid angles. Dimensionless by construction. ✓

*Property 2:* Computed for a local static observer at $r$. Local — depends only on $r$, not global integration. ✓

*Property 3:* $f_{\rm capture}$ increases monotonically as $r \to 3M$, so $f_{\rm forward}$ decreases monotonically as trapping load increases. ✓

*Property 4:* For a local static observer at $r = 3M$, the critical escape cone satisfies $\theta_c = \pi/2$. Therefore:

$$f_{\rm forward}(3M) = \frac{1}{2}$$

exactly — not an approximation, a hard GR result. ✓

*Property 5:* Above photon sphere: $f_{\rm forward} > 1/2$, coherent outward propagation dominant, GR routes normally. Below: $f_{\rm forward} < 1/2$, trapping dominant, GR validity degrades. At photon sphere: exactly marginal. Under the HPF routing interpretation this makes the photon sphere the handoff boundary — but this step layers HPF routing logic onto the GR object and is therefore a candidate bridge, not a pure Schwarzschild theorem. **Bridge, not proved.**

**Elimination of main competitors:**

| GR scalar | Value at $r_{photon}$ | Problem |
|---|---|---|
| Redshift $\sqrt{1-2M/r}$ | $1/\sqrt{3} \neq 1/2$ | Wrong midpoint locus |
| Effective potential $V_{eff}$ | Maximum, not in $[0,1]$ | Wrong object type |
| Lyapunov exponent $\lambda_L$ | Instability rate, not bounded | Wrong object type |
| Compactness $2M/r$ | $2/3 \neq 1/2$ | Wrong midpoint value |

These are the obvious low-complexity competitors. This is an elimination argument, not a classification theorem over all admissible GR scalars.

**Lemma statement:**

> **Forwarding-Identification Lemma (Schwarzschild, candidate form).** In the Schwarzschild GR expert regime, the local null escape fraction $f_{\rm forward}(r)$ is the strongest natural low-complexity candidate realization of the HPF forwarding efficiency $\zeta$. It is dimensionless, local, monotonically degrading under trapping load, and equals $1/2$ at the marginal forwarding boundary $r = 3M$. Under the HPF routing interpretation, this makes the photon sphere the candidate GR locus of $S_f = S_{\rm blur}$.

**Status:** Candidate form. Properties 1–4 proved in Schwarzschild. Property 5 is a candidate bridge under HPF routing interpretation. Uniqueness is elimination of main low-complexity competitors, not a classification theorem.

**Scope:** Schwarzschild only. Kerr requires separate treatment.

---

## Obligation 2: Radial Blur Displacement Law

**Target:** Derive $r_{\rm echo} = 1.05 \times r_{\rm photon}$ from GR-side dynamics rather than asserting it from the $S_{\rm blur}$ label.

**Current state:** The echo location is repo-retained as substrate-native via $S_{\rm blur}$. The identification in Obligation 1, if accepted, places $S_f = S_{\rm blur}$ at $r_{\rm photon}$. But the multiplicative radial offset $\times 1.05$ still requires a displacement law.

**Candidate attack path:**

The blur boundary $S_{\rm blur} = 1.05$ is the logistic midpoint — the flux level at which the substrate transitions from coherence-dominated to decoherence-dominated processing. In the GR regime, the radial displacement corresponding to a flux change of $\Delta S_f = S_{\rm blur} - 1 = 0.05$ from the clean baseline maps to a physical radius shift.

Under the forwarding identification $\zeta_{\rm GR}(r) = f_{\rm forward}(r)$, the radial profile of $f_{\rm forward}$ near the photon sphere determines the displacement scale. Near $r = 3M$:

$$\frac{df_{\rm forward}}{dr}\Bigg|_{r=3M}$$

is finite and computable from the Schwarzschild capture cross-section. The blur displacement $\Delta r$ satisfies:

$$\Delta r \sim \frac{\Delta f_{\rm forward}}{|df_{\rm forward}/dr|_{3M}}$$

If the forwarding-identification map is locally linear near the midpoint, the blur margin can be translated into a corresponding $\Delta f_{\rm forward}$ and hence into a radial displacement.

**This calculation is not yet completed.** The candidate claim is that this approach yields $\Delta r / r_{\rm photon} = 0.05$, reproducing the $1.05\times$ factor. If it does, the echo location becomes derivationally closed. If it misses, the location claim must be weakened.

**Status:** Open. Candidate attack path identified. Calculation needed.

---

## Obligation 3: Mode-Indexing and Reflection Bridge

**Target:** Prove that the Nyquist residual $\eta = 1/48$ at the blur boundary projects dominantly into the outgoing null mode family, making the intrinsic echo fraction exactly $\eta$.

**Current derivation:**

*BCC Nyquist remainder:* At $S_{\rm blur}$, the 24-sector BCC substrate imposes a minimum unresolved phase fraction:

$$\eta = \frac{1}{2N_s} = \frac{1}{48}$$

This is the smallest irreducible sector-resolution remainder. It does **not** require a literal 47+1 mode decomposition — it identifies the minimum nonzero unresolved fraction.

*Reversibility constraint:* HPF substrate evolution is reversible. The unresolved fraction $\eta$ cannot be destroyed by absorption — that would be information loss, which is illegal under HPF substrate constraints. Therefore $\eta$ survives as a reversible residual.

*What is proved:*

$\eta$ sets the minimum surviving reversible residual scale.

**What is not yet proved:**

1. **Exact partition:** Reversibility kills absorption but does not kill phase scrambling, lateral redistribution, temporary trapping, or mode mixing. The claim $f_{\rm redirect} = \eta$ exactly requires excluding those alternatives at this boundary.

2. **Outward projection:** Even if residual redirects, it must project dominantly into the outgoing null mode family to appear as an image-plane echo ring rather than isotropic scatter.

3. **Flux ratio interpretation:** The substrate fraction $\eta$ must be shown to map to the image-plane flux ratio observed by a distant telescope — those are not automatically the same object.

**Mode-Indexing Lemma (target):**

> At $S_f = S_{\rm blur}$, the angular phase content of near-photon-sphere electromagnetic modes is sampled by the same 24-sector BCC substrate partition that governs coherence loss at the Lu boundary. Therefore $\eta$ is the natural unresolved fraction for photon-ring processing, and the reversible residual projects dominantly into the outgoing null mode family.

**Common-boundary argument:** Under UA, Lu coherence loss and photon-sphere echo are two manifestations of the same substrate event: $S_f = S_{\rm blur}$. The same BCC sector-resolution law therefore applies at both boundaries.

**Status:** Open. The common-boundary argument is physically motivated under UA. The outward projection step is the hardest remaining piece.

---

## Candidate Prediction (Contingent on All Three Obligations)

**Echo location:** $r_{\rm echo} = 1.05 \times r_{\rm photon}$ — retained candidate in the active package, with derivational closure still open.

**Echo amplitude:** $A_{\rm echo} = \eta = 1/48 \approx 2.08\%$ of photon ring flux — candidate, contingent on Obligations 1–3.

**Observable target:** M87* photon ring at ~20 μas angular diameter.

| Observable | Prediction | Current instrument | Note |
|---|---|---|---|
| Echo angular position | ~21 μas | ngEHT (15 μas resolution) | Spatially resolvable |
| Echo flux fraction | ~2.1% of ring flux | ngEHT 345 GHz deep integration | At sensitivity edge |

---

## Full Status Table

| Claim | Status |
|---|---|
| $S_{\rm blur} = 1.05$, $\zeta = 0.5$ midpoint | Locked in active package |
| $\eta = 1/48$ from BCC Nyquist | Candidate-strong, active package |
| UA: $S_f$ substrate-native, $S_{\rm blur}$ pre-theoretic | Explicit assumption, well-motivated |
| $f_{\rm capture} = 1/2$ at $r = 3M$ in Schwarzschild | Proved from GR |
| $f_{\rm forward}$ satisfies Properties 1–4 required of $\zeta$ | Proved in Schwarzschild |
| $f_{\rm forward}$ realizes Property 5 under HPF routing interpretation | Candidate bridge |
| $f_{\rm forward}$ is the strongest natural GR candidate for $\zeta$ | Strong candidate — elimination of main low-complexity competitors |
| Photon sphere is candidate GR locus of $S_{\rm blur}$ | Strong candidate contingent on identification |
| $r_{\rm echo} = 1.05 \times r_{\rm photon}$ | Separate candidate — Obligation 2 open |
| Reversibility preserves an $\eta$-scale minimum surviving residual | Proved under HPF axiom |
| Residual projects outward as echo | Candidate — Obligation 3 open |
| $A_{\rm echo} = 1/48$ | Separate candidate contingent on Obligations 1–3 |
| Image-plane flux ratio = $\eta$ | Not yet proved |

---

## Freeze Wording

> At $S_{\rm blur}$, the 24-sector BCC substrate imposes a minimum unresolved phase fraction $\eta = 1/48$. Reversibility forbids that residual from being destroyed, so $\eta$ survives as a reversible remainder. The GR null forwarding fraction provides a natural candidate realization of HPF $\zeta$, placing the photon sphere at the candidate GR locus of $S_{\rm blur}$. The remaining open bridges are: (1) formal identification of $f_{\rm forward}$ with $\zeta$ in the GR expert regime; (2) derivation of the $1.05\times$ radial displacement from GR-side dynamics; (3) proof that the Nyquist residual projects dominantly into the outgoing null mode family. Contingent on all three, the intrinsic echo fraction is $\eta = 1/48 \approx 2.08\%$.

---

*End of candidate note. Do not promote to canon until all three obligations are closed.*
