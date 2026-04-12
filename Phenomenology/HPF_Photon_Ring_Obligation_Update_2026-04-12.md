# HPF Photon Ring — Obligation Status Update
## Forwarding Identification Closed; Displacement Law Obstruction Identified; Amplitude Unaffected by Nyquist Correction

**Document Class:** HPF candidate support note — photon ring obligation update  
**Status:** Closes Obligation 1 to bridge-axiom level. Reports honest obstruction on Obligation 2. Confirms Obligation 3 unaffected by lower-wall Nyquist correction. Notes one new candidate observation.  
**Author:** Eric Keaton Porter  
**Date:** 2026-04-12

---

# 1. Scope

| Obligation | Previous status | Updated status |
|---|---|---|
| 1 — Forwarding-identification lemma | Open | **Closed** to bridge-axiom level (§2) |
| 2 — Radial blur displacement law | Open | **Open** with honest obstruction identified (§3) |
| 3 — Mode-indexing and reflection bridge | Open | **Open** (unchanged); amplitude claim confirmed unaffected by Nyquist correction (§4) |

---

# 2. Obligation 1 — Forwarding Identification: Closed

## 2.1 Bridge axiom

> **Bridge Axiom (Photon-Ring Forwarding).** In the Schwarzschild GR expert regime, the HPF forwarding gate $\zeta$ is realized by the null escape fraction $f_{\rm forward}(r) = 1 - f_{\rm capture}(r)$.

## 2.2 Justification

The identification is justified by the five-property match (all verified in the original note) and by the elimination argument against all low-complexity GR competitors:

| GR candidate | Midpoint value at $r_{\rm photon}$ | HPF $\zeta$ requires $1/2$ | Result |
|---|---|---|---|
| $f_{\rm forward}$ | $1/2$ (exact) | ✓ | **Matches** |
| Redshift $\sqrt{1-2M/r}$ | $1/\sqrt{3} \approx 0.577$ | ✗ | Eliminated |
| Compactness $2M/r$ | $2/3$ | ✗ | Eliminated |
| $V_{\rm eff}$ | Maximum (unbounded) | ✗ | Eliminated |
| $\lambda_L$ | Instability rate | ✗ | Eliminated |

$f_{\rm forward}(3M) = 1/2$ is a hard mathematical fact of Schwarzschild geometry. No competing low-complexity GR scalar achieves the required midpoint value.

This is an elimination argument, not a uniqueness theorem over all possible GR constructions. But the elimination is strong: any competing object must be dimensionless, local, monotone, bounded in $[0,1]$, and equal to $1/2$ at the photon sphere. The null escape fraction is the unique natural GR object satisfying all five.

**Status: closed to bridge-axiom level.** The identification is the unique survivor of the elimination, justified by five-property match. Not claimed as a uniqueness theorem.

---

# 3. Obligation 2 — Radial Blur Displacement Law: Open (Obstruction Identified)

## 3.1 The linearized GR bridge fails to recover 1.05×

Under the forwarding identification $\zeta = f_{\rm forward}$, the candidate derivation maps the blur margin $\Delta S = 0.05$ to a radial displacement via the linearized GR derivative near the photon sphere.

Near $r = 3M$:

$$\cos\psi_c \approx \frac{r - 3M}{\sqrt{3}\,M}, \qquad f_{\rm forward} \approx \frac{1}{2} + \frac{r - 3M}{2\sqrt{3}\,M}$$

The linearized HPF-to-GR bridge:

$$\frac{\Delta r}{r_{\rm photon}} = \frac{k \sqrt{3}\,\Delta S}{6}$$

| $\eta$ at lower wall | $k$ | Predicted $r_{\rm echo}/r_{\rm photon}$ | Target |
|---|---|---|---|
| $1/24$ | $9.484$ | $1.137$ | $1.05$ |
| $1/48$ | $11.646$ | $1.168$ | $1.05$ |

Both values overshoot the target by a factor of $\sim 2.5$–$3\times$. The linearized bridge maps a 5% substrate margin to a $\sim 14$–$17\%$ radial displacement, not 5%.

## 3.2 The $\Delta S$ needed for 1.05× is not 0.05

Inverting the linearized bridge: the blur margin that would produce a 5% radial displacement is $\Delta S \approx 0.015$–$0.018$, not $0.05$.

## 3.3 Assessment

The 1.05× factor appears to be a **direct numerical transfer** of $S_{\rm blur} = 1.05$ to the radial ratio, not a quantity derivable from the linearized GR-side dynamics. The Universality Assumption (UA) permits this transfer — the blur anchor is substrate-intrinsic and can manifest at different scales — but the GR-side derivation that would independently produce the 1.05× factor does not close under linearization.

Possible resolutions (not explored here):

1. A non-perturbative bridge that replaces the linearized approximation.
2. A different GR-side mapping that does not go through $df_{\rm forward}/dr$.
3. The 1.05× is genuinely a direct substrate-level transfer with no independent GR derivation — the echo location is set by the substrate, not derived from GR.

**Obligation 2: open.** The obstruction is identified. The linearized derivation path fails quantitatively. The 1.05× factor is retained as a candidate but is not derivationally closed.

---

# 4. Obligation 3 — Amplitude Claim Unaffected by Nyquist Correction

## 4.1 The lower-wall Nyquist correction does not affect the echo amplitude

The lower-wall Nyquist correction (HPF Correction Note, 2026-04-12) changes the Nyquist assignment at $S_{\rm ent}$ from $1/48$ to $1/24$. This does **not** affect the echo amplitude claim $A_{\rm echo} = 1/48$ because:

- The echo is at $S_{\rm blur} = 1.05$, which is **below** $S_{\rm ent} = 1.3806$.
- At $S_{\rm blur}$, both sublattices are fully operational — single-sublattice resolution has not yet failed.
- The minimum unresolved fraction at $S_{\rm blur}$ is therefore the full two-sublattice Nyquist: $\eta = 1/(2N_s) = 1/48$.

The single-sublattice Nyquist $1/24$ governs the onset of resolution failure at $S_{\rm ent}$. The echo occurs below that threshold, where the tighter two-sublattice bound applies.

**The echo amplitude claim $A_{\rm echo} = 1/48 \approx 2.08\%$ is unchanged.**

## 4.2 The three sub-bridges remain open

The three missing steps identified in the original note — exact partition, outward projection, and image-plane translation — are unchanged by this update. All three remain open.

**Obligation 3: open (unchanged). Amplitude claim confirmed consistent with Nyquist correction.**

---

# 5. New Candidate Observation: $f_{\rm forward}$ at echo radius

A numerical near-match is noted without claiming it as a closure:

$$f_{\rm forward}(1.05 \times 3M) = 0.5406$$

$$f_{\rm coh} = 0.5434 \quad \text{(from the dark-matter branch)}$$

These differ by $0.5\%$ — within the mirror-buffer correction scale. They are produced by entirely independent derivation branches: $f_{\rm forward}$ is a Schwarzschild GR quantity, $f_{\rm coh}$ is a BCC Fibonacci boundary fraction.

If this near-match is not coincidental, it would connect the photon-ring echo to the dark-matter branch through a single substrate object (the coherent support fraction) evaluated at two different scales. This is noted as a candidate observation, not a claimed result.

---

# 6. Updated Photon Ring Status

| Component | Status |
|---|---|
| Echo location $1.05 \times r_{\rm photon}$ | Retained candidate; not derivationally closed from GR side |
| Forwarding identification $\zeta = f_{\rm forward}$ | **Closed** (bridge axiom with elimination) |
| Radial displacement law | **Open** (linearized bridge fails; obstruction identified) |
| Echo amplitude $A_{\rm echo} = 1/48$ | Retained candidate; three sub-bridges open; unaffected by Nyquist correction |
| $f_{\rm forward}$ / $f_{\rm coh}$ near-match | New candidate observation (0.5% difference) |

---

# 7. Freeze wording

> The forwarding identification $\zeta = f_{\rm forward}$ is closed to bridge-axiom level: the null escape fraction is the unique survivor of the five-property elimination against all low-complexity GR candidates, with the hard midpoint fact $f_{\rm forward}(3M) = 1/2$. The radial displacement law remains open: the linearized GR bridge maps a 5% substrate margin to a ~14–17% radial displacement, not 5%. The 1.05× factor is a retained candidate via direct substrate transfer, not a GR-derived displacement. The echo amplitude $A_{\rm echo} = 1/48$ is unaffected by the lower-wall Nyquist correction because the echo occurs at $S_{\rm blur} < S_{\rm ent}$, where both sublattices are operational and the two-sublattice Nyquist applies. A new candidate observation is noted: $f_{\rm forward}(1.05 \times 3M) = 0.5406$ is within 0.5% of $f_{\rm coh} = 0.5434$ from the dark-matter branch.
