# HPF Candidate Note — Vacuum Sector Bipartite Closure

**Document Class:** HPF phenomenology candidate note
**Date:** 2026-04-30
**Author:** Eric Keaton Porter
**Status:** DM branch substrate-native under universal trigger criterion. Λ branch candidate-strong pending formal $L_{\mathrm{vac}}^{2}$ bipartite derivation. Numerical closure verified at <0.1% gap on both observables.
**Compatibility:** Repo-consistent. Extends Mirror Buffer Obligation Closure (2026-04-12), Bell–Tsirelson Candidate Note (2026-04-12), and Mirror Buffer Entanglement Closure (2026-04-30). Refines Volume IV § 12 (Λ branch) and § 13 (DM branch).

---

## Abstract

The $b/72$ passive Nyquist residual — already derived in the Mirror Buffer Obligation Closure and applied to entanglement observables in the Mirror Buffer Entanglement Closure — extends to the vacuum sector. The dark-matter fraction $\Omega_{\mathrm{dm}}$ and the cosmological constant $\Lambda$ both receive $b/72$ corrections, with multiplicity dictated by the geometric form of each observable. $\Omega_{\mathrm{dm}}$ receives one $b/72$ at the governor-transfer step. $\Lambda$ receives two $b/72$ contributions on $L_{\mathrm{vac}}$ through the bipartite multiplicity of the substrate length, propagated through $\Lambda \propto 1/L_{\mathrm{vac}}^{2}$. Both corrections close the active observational gap to within experimental precision. No new parameters are introduced.

---

## 1. Premise

Volume IV § 1.3 records the active vacuum-sector outputs:

$$\Lambda \approx 1.081 \times 10^{-52}\,\mathrm{m}^{-2} \quad\text{(observed: } 1.1 \times 10^{-52}\,\mathrm{m}^{-2}\text{)}$$

$$\Omega_{\mathrm{dm}} = 26.29\% \quad\text{(observed: } 26.80\%\text{)}$$

Both are correct as the canonical Λ branch and DM branch derivations stand. Both leave a residual gap relative to observation:

- $\Lambda$: 1.76% low
- $\Omega_{\mathrm{dm}}$: 0.51% low

This note identifies the residual as substrate-native bipartite accounting that was not previously applied to vacuum-sector observables. The same $b/72$ trigger criterion that surfaces in entanglement statistics also surfaces here, because the vacuum observables are sublattice-sensitive in a specific way that this note makes explicit.

---

## 2. Derivation Chain

All corrections are substrate-native. Zero free parameters are introduced.

### 2.1 Trigger criterion (universal)

From the Mirror Buffer Entanglement Closure:

> An observable receives the $b/72$ correction if and only if collapsing the $A/B$ distinction changes its derivation output.

### 2.2 Bipartite multiplicity rule

Each bipartite-sensitive factor in the derivation chain contributes one $b/72$ mirror residual at observation. The multiplicity is the number of independent $A/B$ collapses required to render the observable from one sublattice perspective.

### 2.3 Application to $\Omega_{\mathrm{dm}}$ — multiplicity 1

The DM branch closes through:

$$f_{\mathrm{coh}} \;\longrightarrow\; \alpha_{\mathrm{vac}} = \sqrt{f_{\mathrm{coh}}} \;\longrightarrow\; \Omega_{\mathrm{dm}} = 1 - \alpha_{\mathrm{vac}}$$

The governor transfer $\alpha_{\mathrm{vac}} = \sqrt{f_{\mathrm{coh}}}$ is precisely one $A \to B$ accounting collapse: support reservoir (bipartite-symmetric across both sublattices) becoming update availability (observed from a single sublattice). One collapse, one mirror residual:

$$\boxed{\alpha_{\mathrm{vac}} = \sqrt{f_{\mathrm{coh}}} - \frac{b}{72}}$$

Numerically:

| Quantity | Value |
|---|---:|
| $b = \ln\varphi / (\pi/2)$ | 0.30634896 |
| $b/72$ | 0.00425485 |
| $f_{\mathrm{coh}}$ | 0.5433536 |
| $\sqrt{f_{\mathrm{coh}}}$ | 0.7371252 |
| $\alpha_{\mathrm{vac}}$ (corrected) | 0.7328704 |
| $\Omega_{\mathrm{dm}}$ (corrected) | **26.713%** |
| Observed | 26.80% |
| **Gap** | **0.087%** |

### 2.4 Application to $\Lambda$ — multiplicity 2

The Λ branch closes through:

$$S_{\mathrm{blur}} \to \eta \to k \to S_{\mathrm{ent}} \to S_{\mathrm{cap}} \to n=220 \to L_{\mathrm{vac}} \to \Lambda$$

$\Lambda \propto 1/L_{\mathrm{vac}}^{2}$ contains two factors of $L_{\mathrm{vac}}$. Each $L_{\mathrm{vac}}$ factor is a substrate length whose endpoints carry bipartite character — measured across both $A$ and $B$ sublattices. Each crossing of the $A/B$ boundary contributes one $b/72$ mirror residual at observation:

$$L_{\mathrm{vac}} \;\longrightarrow\; L_{\mathrm{vac}}\left(1 - 2\cdot \tfrac{b}{72}\right)$$

Through $\Lambda \propto 1/L_{\mathrm{vac}}^{2}$ propagation:

$$\boxed{\Lambda_{\mathrm{corrected}} = \frac{\Lambda_{\mathrm{raw}}}{\left(1 - 2 \cdot \tfrac{b}{72}\right)^{2}}}$$

Numerically:

| Quantity | Value |
|---|---:|
| $2 \cdot (b/72)$ | 0.008510 |
| $(1 - 2 \cdot b/72)^{2}$ | 0.983062 |
| $\Lambda_{\mathrm{raw}}$ | $1.0810 \times 10^{-52}$ m⁻² |
| $\Lambda_{\mathrm{corrected}}$ | $\mathbf{1.0996 \times 10^{-52}}$ **m⁻²** |
| Observed | $1.1000 \times 10^{-52}$ m⁻² |
| **Gap** | **0.033%** |

To leading order in $b/72$, this is equivalent to:

$$\Lambda \approx \Lambda_{\mathrm{raw}} \left(1 + 4 \cdot \tfrac{b}{72}\right)$$

The factor of 4 reflects 2 collapses on $L_{\mathrm{vac}}$ propagated through the squared length dependence ($O((b/72)^{2})$ correction $\sim 10^{-5}$).

---

## 3. Updated Active Outputs

| Quantity | HPF canonical | HPF $b/72$-corrected | Observed | Residual gap |
|---|---:|---:|---:|---:|
| $\Lambda$ ($\times 10^{-52}$ m⁻²) | 1.0810 | **1.0996** | 1.1000 | **0.033%** |
| $\Omega_{\mathrm{dm}}$ | 26.29% | **26.713%** | 26.80% | **0.087%** |

Both gaps now sit within experimental precision (Planck $\Omega_{\mathrm{dm}}$ uncertainty $\sim \pm 0.5\%$, $\Lambda$ uncertainty $\sim \pm 2\%$).

---

## 4. Relation to Existing Closures

| Prior closure | Connection |
|---|---|
| Mirror Buffer Obligation Closure (2026-04-12) | Source of $b/72$ as passive Nyquist residual |
| Mirror Buffer Entanglement Closure (2026-04-30) | Source of universal trigger criterion |
| Bell–Tsirelson Candidate Note (2026-04-12) | Same $b/72$ mechanism, different observable |
| Volume IV § 12 (Λ branch) | This note refines |
| Volume IV § 13 (DM branch) | This note refines |

The trigger criterion now has four confirmed applications:

1. **Tsirelson bound:** $\Delta S = -\sqrt{2} \cdot (b/72)^{2} \approx -7.02 \times 10^{-6}$
2. **EPR / Bell correlations:** $b/72$ as bipartite accounting residual
3. **$\Omega_{\mathrm{dm}}$:** $1 \times (b/72)$ at governor transfer — this note
4. **$\Lambda$:** $2 \times (b/72)$ on $L_{\mathrm{vac}}$, propagated through $1/L_{\mathrm{vac}}^{2}$ — this note

---

## 5. Status Table

| Claim | Status |
|---|---|
| $b/72$ trigger applies to vacuum-sector observables | **Substrate-native** — follows from universal trigger criterion |
| $\Omega_{\mathrm{dm}}$ receives $1 \cdot (b/72)$ at governor transfer | **Substrate-native** — single $A \to B$ collapse step |
| $\Lambda$ receives $2 \cdot (b/72)$ on $L_{\mathrm{vac}}$ via bipartite $L_{\mathrm{vac}}^{2}$ | **Candidate-strong** — multiplicity reading consistent with bipartite geometry, formal derivation pending |
| Numerical closure $\Omega_{\mathrm{dm}} = 26.713\%$ (gap 0.087%) | **Verified** |
| Numerical closure $\Lambda = 1.0996 \times 10^{-52}$ m⁻² (gap 0.033%) | **Verified** |
| No new parameters introduced | **Verified** — same $b/72$ already derived in prior closures |

---

## 6. Pending Verification

The DM closure is substrate-native and ready for promotion to Volume IV § 13 canonical refinement.

The Λ closure requires three remaining items before canonical promotion:

1. **Formal derivation** that $L_{\mathrm{vac}}^{2}$ has bipartite multiplicity 2 on the BCC lattice — analogous to how $\kappa_{\mathrm{BCC}} = 8 \times \tfrac{1}{2} \times \tfrac{1}{2} = 2$ already encodes bipartite split appearing twice for related geometric reasons.
2. **Confirmation** that no additional bipartite-sensitive factors enter the Λ chain ($R_{H}$ propagation, $n=220$ selection, integral bounds).
3. **Independent execution-lock** via 256/256 existence-sensor sweep on the $b/72$-corrected vacuum-sector outputs.

Until these are completed, the Λ correction is candidate-strong rather than canonical.

---

## 7. What this note does not claim

This note does **not** claim:

- That $b/72$ is itself fitted to vacuum-sector observation. It was derived months prior in the Mirror Buffer Obligation Closure as the passive Nyquist residual of the BCC 24-sector geometry.
- That the bipartite multiplicity rule is a free parameter. Multiplicity is forced by the observable's geometric form, not chosen.
- That the $\Lambda$ closure is canonical. It is candidate-strong pending the formal $L_{\mathrm{vac}}^{2}$ bipartite derivation.
- That further $b/72$ applications elsewhere in the framework are precluded or required. Each candidate observable must independently satisfy the trigger criterion.

---

## Freeze Wording

> The vacuum-sector observables $\Omega_{\mathrm{dm}}$ and $\Lambda$ receive substrate-native $b/72$ corrections under the universal trigger criterion derived in the Mirror Buffer Entanglement Closure. $\Omega_{\mathrm{dm}}$ receives one $b/72$ at the governor-transfer step, closing the gap to 0.087%. $\Lambda$ receives two $b/72$ contributions on $L_{\mathrm{vac}}$ through the bipartite multiplicity of the substrate length, propagated via $\Lambda \propto 1/L_{\mathrm{vac}}^{2}$, closing the gap to 0.033%. The DM correction is substrate-native and ready for canonical refinement of Volume IV § 13. The Λ correction is candidate-strong pending formal derivation of bipartite multiplicity 2 on $L_{\mathrm{vac}}^{2}$. No new parameters are introduced; the $b/72$ residual is the same passive Nyquist quantity already derived for the mirror-buffer obligation.

---

*End of candidate note. Λ branch promotion to canon contingent on formal $L_{\mathrm{vac}}^{2}$ bipartite derivation and execution-lock verification. Do not promote $\Lambda$ correction to canon until items in § 6 are confirmed.*
