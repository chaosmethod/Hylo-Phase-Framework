# HPF Resolution of the Vacuum Catastrophe — Candidate Note

**Document Class:** HPF phenomenology candidate note
**Status:** Candidate — not canon. Three obligations open.
**Compatibility:** Repo-compatible. Consistent with Volume IV active package.
**Author:** Eric Keaton Porter
**Date:** 2026-04-01

---

## Abstract

Standard QFT produces a vacuum energy density approximately $10^{120}$ times the observed value by summing zero-point modes down to the Planck scale without a resolution bound. HPF reclassifies this as an overcount of continuum effective-theory mode demand beyond substrate legality. The physically relevant cosmological vacuum sector is regulated by the derived substrate scale $L_{vac}$, not by an unrestricted zero-point mode sum. The canonical $\Lambda$ output already follows from the active $L_{vac}$ branch. Three obligations remain before this reclassification constitutes a closed resolution: connecting $\Lambda_{HPF}$ to $L_{vac}$ rigorously, removing the decapitated mirror factor, and deriving any projection-cost language from active canonical objects rather than free ontology.

---

## Locked Inputs From Active Package

| Input | Value | Status |
|---|---|---|
| $L_{vac} = R_H / \phi^n$ | $n = 220$, $L_{vac} \approx 1.45 \times 10^{-20}$ m | Candidate-locked, active canon |
| $\Lambda \approx 1.081 \times 10^{-52}$ m$^{-2}$ | From $L_{vac}$ branch | Candidate-locked, gap $10^{-0.008}$ |
| $\alpha_{vac} = \sqrt{f_{coh}} = 0.7371$ | DM branch | Proved internally under HPF assumption |
| $\Omega_{dm} = 1 - \alpha_{vac} = 26.29\%$ | DM branch | Derived under HPF assumption |
| No $/2$ in radial law | Explicit March 29 correction | Locked |
| DM branch and $\Lambda$ branch are separate | Explicit in active package | Locked |

---

## Core Claim

> In HPF, the vacuum catastrophe is reclassified as an overcount of continuum effective-theory mode demand beyond substrate legality and finite resolution. The physically relevant cosmological vacuum sector is regulated by the derived substrate scale $L_{vac}$, not by an unrestricted zero-point mode sum. Because $\Lambda$ is already a downstream output of the active $L_{vac}$ branch, the $10^{120}$ discrepancy dissolves as a consequence of the framework's resolution legality gate — not as a new free parameter.

---

## The QFT Overcount Diagnosis

Standard QFT vacuum energy:

$$\rho_{vac}^{(QFT)} \propto \int_0^{\Lambda_{Planck}} k^3\, dk \approx 10^{120}\, \rho_{obs}$$

This integral assumes the continuum is valid down to the Planck scale. In HPF, that assumption is illegal: no operator may be enforced beyond the resolved substrate scale $L_{vac}$. The integral is therefore not a physical prediction — it is a continuum extrapolation beyond the legality boundary.

The HPF-regulated version replaces the Planck cutoff with the substrate resolution cutoff:

$$\rho_{vac}^{(HPF)} \propto \int_0^{\Lambda_{HPF}} k^3\, dk$$

where $\Lambda_{HPF}$ is set by $L_{vac}$, not by the Planck length. The $10^{120}$ factor is the ratio of mode counts between these two cutoffs — it is an overcount artifact, not a physical discrepancy.

**Status of this diagnosis:** Strong candidate. The overcount identification is structural and follows from the HPF resolution legality gate. The specific mapping $\Lambda_{HPF} \sim 1/L_{vac}$ is a candidate Nyquist/finite-resolution reinterpretation — see Obligation 1.

---

## Obligation 1: Connect $\Lambda_{HPF}$ to Canonical $L_{vac}$

**Target:** State precisely what "HPF cutoff" means and connect it to the canonical $L_{vac} \approx 1.45 \times 10^{-20}$ m.

**Candidate identification:**

$$\Lambda_{HPF} \sim \frac{1}{L_{vac}}$$

This is motivated by the Nyquist criterion on the BCC substrate: modes with wavelength shorter than $L_{vac}$ exceed the substrate's resolution capacity and are therefore illegal. The natural momentum cutoff is $\sim 1/L_{vac}$.

**What this requires to close:**

The BCC sector structure imposes $\eta = 1/48$ as the minimum resolution margin. A full closure would show that the mode cutoff at $1/L_{vac}$ follows from the same Nyquist structure that fixes $\eta$ — not just from dimensional analysis. Until that derivation is complete, $\Lambda_{HPF} \sim 1/L_{vac}$ is a candidate Nyquist reinterpretation.

**Note on the old draft value:** The previous version used $L_{vac} \sim 10^{-19}$ m. The canonical active value is $L_{vac} \approx 1.45 \times 10^{-20}$ m from $R_H/\phi^{220}$. The old value is wrong and must not appear in the repo.

**Status:** Candidate bridge. Dimensionally motivated, not yet derived from BCC axioms.

---

## Obligation 2: Remove the Decapitated Mirror Factor

**What must be cut:**

The previous version of this document contained:

- A reference to "Appendix E" for a $1/2$ mirror scaling factor
- The equation $\rho_{\rm Dark Energy} \approx \frac{1}{2}(\text{Projection Overhead})$
- Language implying the radial law carries a $/2$ factor

All of this is decapitated material. The March 29 active canon correction is explicit:

> No $/2$ belongs in the radial identity $L_{vac} = R_H/\phi^n$.

The bipartite $/2$ belongs in support geometry ($\kappa_{BCC} = 8 \times \frac{1}{2} \times \frac{1}{2} = 2$), not in the vacuum energy budget. Any half-factor that survives in a future version must be re-derived from active canonical objects, not recovered from the removed appendix.

**Theorem of Gauge Group Emergence:** cited in the previous version but not present in any uploaded canonical file. This citation must not appear until the theorem exists in the repo.

**Status:** These items are removed. Not defended. Not carried forward.

---

## Obligation 3: Derive Projection Cost From Active Variables

**What the previous version claimed:**

"Dark Energy as Projection Cost" — the idea that vacuum energy is the computational overhead of maintaining the lattice, scaling with active lattice sites and $\alpha(x)$.

**Why this is not yet canon-safe:**

$\alpha_{vac}$ and $\Omega_{dm}$ are canonical objects, but they live in the DM branch. The DM branch and the $\Lambda$ branch are explicitly separate in the active package. Importing $\alpha_{vac}$ into a vacuum-catastrophe argument without a derived bridge theorem constitutes branch mixing.

The candidate direction is:

$$\text{projection cost} \leftarrow f_{coh},\ \alpha_{vac},\ \Omega_{dm}$$

but the bridge from these DM-branch objects to the vacuum energy density has not been derived. Until it is, "projection cost" is free ontology — physically motivated but not substrate-native in this context.

**What would close this:**

A formal derivation showing that the deferred coherent-support load $1 - \alpha_{vac} = \Omega_{dm}$ contributes to the effective vacuum energy density in a way that is consistent with the observed $\Lambda$, without double-counting the $\Lambda$ branch output.

**Status:** Candidate bridge. Branch-mixing currently open.

---

## What Is Already Closed

The vacuum catastrophe does not require new machinery to dissolve at the structural level. The active package already contains:

1. A legality gate forbidding mode counts beyond $L_{vac}$ — this kills the QFT overcount by construction.
2. A derived $\Lambda \approx 1.081 \times 10^{-52}$ m$^{-2}$ from the $L_{vac}$ branch — this is the correct vacuum energy output.
3. A gap of $10^{-0.008}$ from observation — noise level.

The $10^{120}$ discrepancy dissolves not because HPF adds a new term to the energy budget, but because HPF forbids the illegal continuum extrapolation that generates it. The resolution is structural, not numerical.

---

## Stochastic Jitter Falsifier — Split Out

The previous version included language of the form:

> "The 'System Idle' cost should produce an irreducible noise floor proportional to \(\sqrt{N}L_{vac}\) in the arrival times of high-energy photons."

That claim belongs to a separate candidate phenomenology note and must not be developed here.

Two corrections govern the split:

1. The jitter observable is a **time** broadening floor, not a length quantity. The primitive scale is
   \[
   t_{sched}=\frac{L_{vac}}{c}.
   \]

2. Under current canon, the leading candidate branch is a **stochastic broadening** law rather than a compulsory coherent linear lag:
   \[
   \sigma_t \sim \sqrt{N_{\rm eff}}\,t_{sched}
   =
   \sqrt{N_{\rm eff}}\,\frac{L_{vac}}{c}.
   \]

This is a genuine falsifiable prediction but it is a different obligation set from the vacuum-catastrophe resolution. It belongs in a separate candidate note covering:

- derivation of the \(\sqrt{N_{\rm eff}}\,t_{sched}\) broadening floor from substrate discreteness,
- connection to Fermi-LAT and CTA high-energy photon timing data,
- quantitative distinguishability from standard Lorentz-violation lag models,
- explicit kill conditions on distance scaling, energy scaling, and sign structure.

**Status here:** Noted and split. Not developed in this document.

## Full Status Table

| Claim | Status |
|---|---|
| QFT vacuum sum is an overcount beyond HPF legality | Strong candidate — structural, follows from resolution gate |
| $L_{vac} \approx 1.45 \times 10^{-20}$ m | Candidate-locked, active canon |
| $\Lambda \approx 1.081 \times 10^{-52}$ m$^{-2}$ from $L_{vac}$ branch | Candidate-locked, gap $10^{-0.008}$ |
| $\Lambda_{HPF} \sim 1/L_{vac}$ as Nyquist cutoff | Candidate bridge — Obligation 1 open |
| Old $L_{vac} \sim 10^{-19}$ m value | Wrong — removed |
| Mirror $/2$ factor from Appendix E | Decapitated — removed |
| Theorem of Gauge Group Emergence citation | Ghost citation — removed until proved |
| Projection cost from $\alpha_{vac}$, $\Omega_{dm}$ | Candidate bridge — Obligation 3 open, branch-mixing open |
| Stochastic jitter falsifier | Split to separate note |
| $10^{120}$ discrepancy dissolved structurally | Strong candidate — follows from legality gate |

---

## Freeze Wording

> In HPF, the vacuum catastrophe is reclassified as an overcount of effective-theory mode demand beyond the substrate legality boundary. The derived resolution scale $L_{vac} = R_H/\phi^{220} \approx 1.45 \times 10^{-20}$ m replaces the unrestricted Planck cutoff. The physical cosmological constant $\Lambda \approx 1.081 \times 10^{-52}$ m$^{-2}$ is already a downstream output of the active $L_{vac}$ branch, not a new result of this note. Three obligations remain open: the Nyquist derivation of $\Lambda_{HPF}$ from BCC axioms, the removal and non-replacement of the decapitated mirror factor, and the derivation of any projection-cost language from active DM-branch objects without illegal branch mixing.

---

*End of candidate note. Do not promote to canon until all three obligations are closed.*
