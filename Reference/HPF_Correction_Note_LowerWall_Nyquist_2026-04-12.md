# HPF Correction Note — Lower-Wall Nyquist Assignment
## Single-Sublattice Resolution Floor at $S_{\rm ent}$, Common Spine Restatement

**Document Class:** HPF correction note  
**Status:** Canon correction. Affects Volume IV §9 and DCT v7U §7 (common spine). No downstream numerical outputs change.  
**Author:** Eric Keaton Porter  
**Date:** 2026-04-12

---

# 1. Correction

The lower wall $S_{\rm ent} = 1.3806$ uses the **single-sublattice Nyquist floor** $1/N_s = 1/24$, not the two-sublattice Nyquist residual $1/(2N_s) = 1/48$.

**Previous (Volume IV §9):**

$$k = \frac{\ln 47}{S_{\rm ent} - 1.05} \approx 11.646 \qquad (\eta = 1/48)$$

**Corrected:**

$$k = \frac{\ln 23}{S_{\rm ent} - 1.05} \approx 9.484 \qquad (\eta = 1/24)$$

---

# 2. Why $S_{\rm ent}$ is unchanged

$S_{\rm ent} = 1.3806$ is geometrically determined by the Obligation 2 derivation chain:

$$r_{\rm lat} = \frac{1}{6} \;\Rightarrow\; \varphi'_{\rm lead} = \frac{1}{6}\sqrt{1+b^2} \;\Rightarrow\; \Delta S_{\rm ent} = 0.3306 \;\Rightarrow\; S_{\rm ent} = 1.3806$$

This chain depends on the BCC causal-arc geometry and does not depend on which $\eta$ is assigned at the lower wall. The value $S_{\rm ent} = 1.3806$ is locked by the geometry, not by the Nyquist interpretation.

The Nyquist assignment enters only when interpreting $S_{\rm ent}$ as the point where the coherence gate reaches $\eta$:

$$\zeta(S_{\rm ent}) = \eta \qquad \Rightarrow \qquad k = \frac{\ln\!\left(\frac{1-\eta}{\eta}\right)}{S_{\rm ent} - S_{\rm blur}}$$

Both $(\eta, k)$ pairs reproduce the same $S_{\rm ent}$:

| Assignment | $\eta$ | $k$ | $S_{\rm ent}$ |
|---|---|---|---|
| Previous | $1/48$ | $11.646$ | $1.3806$ |
| Corrected | $1/24$ | $9.484$ | $1.3806$ |

---

# 3. What changes

Only two things change:

1. **Gate steepness $k$:** from $11.646$ to $9.484$. This affects the logistic gate shape between $S_{\rm blur}$ and $S_{\rm ent}$. The step-function limit $k \to \infty$ (which the DCT robustness sweep confirms preserves $n = 220$) is unaffected.

2. **Physical interpretation of $S_{\rm ent}$:** Previously, $S_{\rm ent}$ was where the two-sublattice Nyquist residual was reached. Now, $S_{\rm ent}$ is where a single sublattice loses angular resolution — the point at which one sublattice of the BCC lattice can no longer distinguish adjacent sectors in the 24-sector ring.

---

# 4. What does not change

| Quantity | Value | Depends on $\eta$ at lower wall? |
|---|---|---|
| $S_{\rm ent}$ | $1.3806$ | No (geometrically determined) |
| $S_{\rm cap}$ | $5.7889$ | No ($1/48$ enters as additive margin, separate role) |
| $n$ (shell selector) | $220$ | No (depends on $S_{\rm cap} - S_{\rm ent}$) |
| $\Lambda$ | $\approx 1.081 \times 10^{-52}\;\mathrm{m}^{-2}$ | No |
| $\Omega_{\rm dm}$ | $26.29\%$ | No (depends on $b$ and $f_{\rm coh}$) |
| $1/\alpha_{\rm fs}$ (candidate) | $137.035963$ | No |
| Neutrino ratio (candidate) | $34$ | No |

Every downstream numerical output of the framework is unchanged.

---

# 5. Common spine restatement

**Previous (DCT v7U §7):**

> The current common spine is $\{S_{\rm blur},\;\eta = 1/48\}$. $\eta$ is the same substrate object playing two different structural jobs.

**Corrected:**

> The common spine is $\{S_{\rm blur},\;N_s = 24,\;b\}$. The shared structural primitive is the 24-sector count $N_s$, which enters the two walls at different Nyquist scales:
>
> **Lower wall.** Single-sublattice Nyquist floor $1/N_s = 1/24$. At $S_{\rm ent}$, one sublattice can no longer resolve adjacent sectors. The coherence gate reaches $\zeta = 1/24$.
>
> **Upper wall.** Two-sublattice Nyquist margin $1/(2N_s) = 1/48$. The additive term $\eta = 1/48$ in $S_{\rm cap}$ is the minimum nonzero residual margin after the geometric collapse budget is exhausted, resolved by both sublattices together.

The shared primitive is the sector count, not the derived fraction. The two walls use the same geometry at different resolution scales — single-sublattice at the lower wall, bipartite at the upper wall.

---

# 6. Files requiring update

| File | Section | Change |
|---|---|---|
| `Docs/Volume_IV_Lambda_and_Dark_Matter.md` | §9 | $k = \ln 23 / (S_{\rm ent} - 1.05)$, $\eta = 1/24$ |
| `Reference/Delta_Collapse_Theorem_Note_v7U.md` | §7 (common spine) | Restate around $N_s = 24$ per §5 above |
| `Reference/HPF_Repo_Status_Memo.md` | §1.10 | Clarify that $\eta = 1/48$ is the upper-wall Nyquist; lower wall uses $1/24$ |

No changes required to: Volumes I–III, Symbol Index, any candidate phenomenology note, any reference note other than those listed.

---

# 7. Freeze wording

> The lower wall $S_{\rm ent} = 1.3806$ marks single-sublattice resolution failure: the coherence gate $\zeta$ reaches $1/N_s = 1/24$, the point at which one sublattice of the BCC 24-sector ring can no longer resolve adjacent sectors. Gate steepness corrects from $k \approx 11.646$ to $k \approx 9.484$. The upper wall $S_{\rm cap}$ retains $1/(2N_s) = 1/48$ as its additive Nyquist margin, representing the two-sublattice resolution limit. The common spine shared primitive is $N_s = 24$, not $\eta = 1/48$. All downstream framework outputs ($S_{\rm ent}$, $S_{\rm cap}$, $n = 220$, $\Lambda$, $\Omega_{\rm dm}$) are unchanged.
