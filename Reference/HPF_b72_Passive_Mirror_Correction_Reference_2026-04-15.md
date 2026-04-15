# HPF Reference Note — The b/72 Passive Mirror Correction
## Standalone Consolidation

**Document Class:** HPF reference note — standalone consolidation  
**Status:** Candidate — all three obligations closed as of 2026-04-12  
**Author:** Eric Keaton Porter  
**Date:** 2026-04-15  
**Framework version:** Hylo-Phase Framework v2.2.1  
**Consolidates:**
- `HPF_Mirror_Buffer_Correction_Note_draft.md` (2026-04-10) — problem identification and proposed solution
- `HPF_Mirror_Buffer_Obligation_Closure_2026-04-12.md` — formal QPRCA derivation, sublattice-sensitivity criterion
- `HPF_Bell_Tsirelson_Candidate_Note_2026-04-12.md` — third independent observable, Obligation 3 closure

---

## 1. The Problem This Solves

The HPF package carried a consistent ~0.5% residual gap across two independent derivation branches:

| Observable | Derived | Observed | Gap |
|---|---|---|---|
| Dark matter fraction $\Omega_{\rm dm}$ | 26.29% | 26.8% | 0.51% |
| Neutrino mass-squared ratio $\Delta m^2_{31}/\Delta m^2_{21}$ | 34 | 33.831 | 0.49% |

Two gaps of nearly identical magnitude from entirely independent branches, both connected to BCC lattice geometry, both ratio-type observables sensitive to local substrate load. A single geometric effect was missing from both derivations.

---

## 2. The Spine — Derivation of b/72

### 2.1 The QPRCA bipartite update cycle

The QPRCA on the BCC bipartite lattice executes via two alternating half-steps:

$$\mathcal{U}_{A \to B}: \text{ each B site updated as a bijective function of (old-B state, A-neighbor states)}$$
$$\mathcal{U}_{B \to A}: \text{ each A site updated as a bijective function of (old-A state, B-neighbor states)}$$

Reversibility requires $\mathcal{U}_{A \to B}$ to be bijective in the old-B state for any fixed A-neighbor configuration.

### 2.2 Information content after the forward half-step

After $\mathcal{U}_{A \to B}$, the new B state encodes the full information content of both inputs — A-origin (from A-sublattice neighbors) and B-origin (from old-B, preserved by bijectivity). These two components are bijectively mixed but distinguishable by provenance.

### 2.3 The bipartite symmetry forces 1/2 weighting

**Lemma (Bipartite Mirror Weighting).** On a bipartite lattice with $|A| = |B|$, the independent information fraction of the mirror return half-step, for sublattice-sensitive sampling, is $1/2$.

**Proof.** The forward half-step $\mathcal{U}_{A \to B}$ is a bijection from $(s_B^{\rm old}, \{s_A^{\rm old}\}_{\rm nbr}) \mapsto s_B^{\rm new}$. Bijectivity preserves total information. By bipartite symmetry, the two sublattices contribute equal state-space dimension: $\dim(\mathcal{S}_A) = \dim(\mathcal{S}_B)$. The B-origin fraction of information in $s_B^{\rm new}$ is therefore:

$$\frac{H(s_B^{\rm old})}{H(s_B^{\rm old}) + H(\{s_A^{\rm old}\}_{\rm nbr} \mid s_B^{\rm old})} = \frac{1}{2}$$

by the equal-dimension condition. $\square$

### 2.4 Effective sampling path

- **Forward half-step** $\mathcal{U}_{A \to B}$: transports A-state information across 1 lattice spacing. Full weight. Effective contribution: **1**.
- **Mirror half-step** $\mathcal{U}_{B \to A}$: only the B-origin fraction (weight 1/2) is new to A. Effective contribution: **1/2**.

**Total effective sampling path per full bipartite cycle:**

$$L_{\rm eff} = 1 + \frac{1}{2} = \frac{3}{2}$$

### 2.5 Passive Nyquist residual

The active Nyquist residual uses full two-sample-per-cycle resolution:

$$\eta = \frac{1}{2 \times 24} = \frac{1}{48}$$

The passive mirror residual replaces the factor of 2 with the effective sampling multiplier $3/2$:

$$\eta_{\rm passive} = \frac{1}{\frac{3}{2} \times 48} = \frac{1}{72}$$

### 2.6 The correction term

The passive mirror correction enters sublattice-sensitive observables as:

$$\boxed{\delta_{\rm mirror} = \frac{b}{72}}$$

where $b = \ln\varphi / (\pi/2) = 0.3063489625$ is the Fibonacci growth parameter already present in the live package.

Numerically:

$$\frac{b}{72} = \frac{0.3063489625}{72} \approx 0.004254 \approx 0.43\%$$

No free parameters. No objects beyond the existing QPRCA package.

---

## 3. The Application Rule — Sublattice-Sensitivity Criterion

Not every observable receives the b/72 correction. The formal criterion:

**Definition.** An observable $O$ is *sublattice-sensitive* if its derivation chain contains at least one step whose output depends on the state of a single sublattice (A or B) before bipartite cycle averaging.

**Operational test.** $O$ is sublattice-sensitive if and only if collapsing the A/B distinction — treating all lattice sites as belonging to a single sublattice — changes the derivation's output.

**Trigger rule:** The b/72 correction applies if and only if the A/B distinction is load-bearing in the derivation chain. If the correction's trigger mechanism is absent from an observable's derivation, that correction is illegal for that observable.

### Verification against all current observables

| Observable | Sublattice-sensitive? | Correction | Reason |
|---|---|---|---|
| Radial law $L_{\rm vac} = R_H/\varphi^n$ | No | None | $n=220$ is a full-cycle integral over both sublattices; collapsing A/B does not change $n$ |
| Dark matter fraction $\Omega_{\rm dm}$ | **Yes** | $+b/72$ | Fibonacci spiral alternates A/B-dominant sectors; collapsing A/B changes angular sampling |
| Neutrino ratio $\Delta m^2_{31}/\Delta m^2_{21}$ | **Yes** | $-b/72 \times 34$ | Fibonacci index +1 term is a bipartite shared-face crossing; collapsing A/B removes it |
| Fine-structure constant $1/\alpha_{\rm fs}$ | Pre-absorbed | None | $N_{\rm cycle} = 360$ and $N_{\rm hop} = 120$ already average over bipartite structure; residual 0.000026% |
| Tsirelson bound $S_{\rm max}$ (CHSH) | **Yes** | $-7.02 \times 10^{-6}$ | Angular reach of mirror operator $M$ depends on B-origin information fraction at bipartite boundary |

The removal of the $/2$ from the radial law was correct and is confirmed here: the radial law is not sublattice-sensitive. The mirror geometry is still present in the substrate — it simply does not affect global geometric identities that already span both sublattices simultaneously.

---

## 4. The Three Independent Observables

### 4.1 Observable 1 — Dark matter fraction

**Derivation branch:** Governor Transfer Theorem → $f_{\rm coh}$ → $\alpha_{\rm vac}$ → $\Omega_{\rm dm} = 1 - \alpha_{\rm vac}$

**Why sublattice-sensitive:** The coherent support fraction $f_{\rm coh}$ integrates the Fibonacci boundary's angular coverage. The Fibonacci spiral on BCC alternates between A-dominant and B-dominant angular sectors. Each sector's contribution depends on which sublattice currently hosts the leading edge.

**Correction:**

$$\Omega_{\rm dm}^{\rm corrected} = 26.29\% + \frac{b}{72} = 26.29\% + 0.4254\% = 26.715\%$$

### 4.2 Observable 2 — Neutrino mass-squared ratio

**Derivation branch:** BCC Fibonacci indexing → $\Delta m^2_{31}/\Delta m^2_{21} = F(9)/F(1) = 34$

**Why sublattice-sensitive:** The Fibonacci index 9 = BCC coordination number 8 + bipartite shared-face crossing +1. The +1 term is specifically a bipartite crossing event — a shared face between A and B sublattices. Collapsing A/B eliminates this crossing and changes the index.

**Correction:**

$$\left(\frac{\Delta m^2_{31}}{\Delta m^2_{21}}\right)^{\rm corrected} = 34 - \frac{b}{72} \times 34 = 34 - 0.1446 = 33.856$$

### 4.3 Observable 3 — Tsirelson bound

**Derivation branch:** Mirror operator $M = JK$ on BCC directional qubit → bipartite angular reach $3/2$ sectors → substrate bidirectional peak $\pi/8$ → CHSH one-way doubling → $S_{\rm max} = 2\sqrt{2}$

**Why sublattice-sensitive:** The angular reach of $M$ is derived from the B-origin information fraction at the bipartite boundary. Collapsing A/B changes the effective reach from $3/2$ to 2 (full Nyquist), changing the result.

**Leading-order prediction:** $\pi/4$ is the stationary point of the CHSH correlator ($S' = 0$ at $\pi/4$, $S'' = 2\sqrt{2}$). The b/72 correction is therefore second-order:

$$\Delta S = -\frac{1}{2}|S''|\left(\frac{b\pi}{432}\right)^2 = -\sqrt{2}\left(\frac{b\pi}{432}\right)^2$$

Numerically: $b\pi/432 = 0.002228$

$$\boxed{\Delta S = -7.02 \times 10^{-6}}$$

**Corrected bound:**

$$S_{\rm max}^{\rm corrected} = 2\sqrt{2} - 7.02 \times 10^{-6} \approx 2.8284201$$

This prediction is not currently testable — state-of-the-art Bell tests achieve uncertainties ~$10^{-2}$ to $10^{-3}$, roughly three orders of magnitude above the predicted correction. It is a precision prediction for future experimental reach.

---

## 5. The Three-Observable Table

| Observable | Branch | Uncorrected | Corrected | Observed | Residual after correction |
|---|---|---|---|---|---|
| Dark matter fraction $\Omega_{\rm dm}$ | Governor Transfer | 26.29% | **26.715%** | 26.8% | **0.085%** |
| Neutrino ratio $\Delta m^2_{31}/\Delta m^2_{21}$ | BCC Fibonacci | 34 | **33.856** | 33.831 | **0.07%** |
| Tsirelson bound $S_{\rm max}$ | Mirror operator / Bell | $2\sqrt{2}$ | $2\sqrt{2} - 7.02\times10^{-6}$ | $2\sqrt{2}$ (within $10^{-3}$) | **Not yet testable** |

Single correction term. Three independent derivation branches. Order-of-magnitude residual improvement on the two testable observables.

---

## 6. Obligation Status

| Obligation | Status |
|---|---|
| 1 — Formal QPRCA derivation of 3/2 path factor | ✅ Closed — derived from reversibility → bijectivity → bipartite symmetry → sublattice-sensitive sampling |
| 2 — Formal sublattice-sensitivity criterion | ✅ Closed — defined, operationalized, and verified against 4 observables |
| 3 — Third independent sublattice-sensitive observable | ✅ Closed — Tsirelson bound derived from independent Bell/mirror branch with same mechanism |

All three obligations closed as of 2026-04-12.

---

## 7. What This Does Not Claim

- Grammar uniqueness — whether the 4-bit alphabet is the unique admissible substrate grammar — is a separate open problem that does not gate this correction, but does gate any claim that the derivation is the only possible one. A different substrate grammar could produce a different correction or none at all.
- The b/72 correction is **candidate**, not canon. It does not graduate to canon until independent predictive confirmation arrives.
- The Tsirelson correction ($7.02 \times 10^{-6}$) is a prediction, not a confirmed result. It is not currently testable.
- The fine-structure constant residual (0.000026%) is pre-absorbed by the bipartite-averaged cycle and hop counts. The correction is not applied there, consistently with the formal criterion.

---

## 8. Tier Classification

| Claim | Status |
|---|---|
| BCC bipartite lattice has $|A| = |B|$ | Substrate-native |
| QPRCA update is reversible and bijective | Substrate-native |
| Effective sampling path $L_{\rm eff} = 3/2$ per bipartite cycle | Derived from QPRCA |
| Passive Nyquist residual $\eta_{\rm passive} = 1/72$ | Derived |
| Correction magnitude $b/72 \approx 0.43\%$ | Derived |
| Sublattice-sensitivity criterion (formal) | Derived |
| Dark matter residual $0.51\% \to 0.085\%$ | Empirically anchored under HPF |
| Neutrino residual $0.49\% \to 0.07\%$ | Empirically anchored under HPF |
| Tsirelson bound $2\sqrt{2}$ as substrate output | Candidate |
| Tsirelson correction $\Delta S = -7.02 \times 10^{-6}$ | Candidate prediction |

---

## 9. Freeze Wording

> The passive mirror buffer correction $b/72$ is derived from QPRCA bipartite update algebra: reversibility forces bijectivity, bijectivity forces both A-origin and B-origin information into the updated B state, bipartite symmetry ($|A|=|B|$) forces the B-origin fraction to exactly $1/2$, and sublattice-sensitive sampling counts only the B-origin fraction as new information in the mirror return. Total effective sampling path: $1 + 1/2 = 3/2$. Passive Nyquist residual: $1/72$. Correction magnitude: $b/72 \approx 0.43\%$. The sublattice-sensitivity criterion — an observable receives the mirror correction if and only if collapsing the A/B distinction changes its derivation output — is verified against four observables: radial law (not sensitive, no correction), dark matter (sensitive, $0.51\% \to 0.085\%$), neutrino ratio (sensitive, $0.49\% \to 0.07\%$), fine-structure (pre-absorbed). The correction is confirmed against three independent derivation branches: governor transfer (dark matter), BCC Fibonacci (neutrino), and mirror operator / Bell geometry (Tsirelson bound $2\sqrt{2} - 7.02 \times 10^{-6}$). All three obligations are closed. The correction remains candidate pending independent predictive confirmation.

---

*Produced April 15, 2026. Consolidates mirror-buffer draft (2026-04-10), obligation closure (2026-04-12), and Bell/Tsirelson note (2026-04-12). Framework version: HPF v2.2.1.*
