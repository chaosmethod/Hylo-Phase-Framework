# Hylo Phase Framework (HPF)

## Canonical Presentation Package
### Repository Front Page and Reading Guide — Milestone Lock State (2026-04-25)

**Version:** v2.3.0 — QPRCA BCC Bipartite Build & S_cap Derivation Closure

**Previously:** *Holographic Projection Framework (HPF)*

**Role of this file:** This README is the front door to the repository. It states what HPF is, what it is not, how the package is organized, which files are authoritative, what the current milestone locks are, and what order to read the material in.

**What this README does not do by itself:** It does not replace the canon volumes, the microscopic executable record, the provenance/status map, or the dedicated vacuum-sector derivation package. Those remain the job of the individual files listed below.

---

# 1. What HPF is

The **Hylo Phase Framework (HPF)** is a **regulatory execution framework** for bounded physical evolution on a finite-capacity substrate.

In operating language:

> **HPF is the physics OS.**

HPF does not attempt to be a blanket Theory of Everything. Its role is narrower and stricter:

1. enforce hard execution constraints,
2. track bounded substrate load,
3. distinguish **legality** from **validity**,
4. govern expert routing and lawful handoff,
5. determine when effective theories remain trustworthy,
6. route execution to deeper substrate-side authority when effective descriptions cease to remain valid or legal.

The framework is implemented architecturally as a layered stack rather than a single monolithic theory claim.

---

# 2. Fixed architecture

The dependency order is fixed:

1. **HPF** — regulator / legality framework
2. **MDEA** — routing kernel / model-of-expertise execution layer
3. **GR / QM / effective theories** — downstream expert regimes
4. **QPRCA** — deeper substrate expert / handoff destination

This order must not be inverted.

## 2.1 Non-negotiable framework rules

- HPF is **not** an object-level gravity theory.
- Geometry is **not** the regulator.
- QPRCA is **not** the regulator; it is a substrate-side expert governed by HPF.
- Legality and validity must not be collapsed.
- Candidate phenomenology must not be silently promoted into canon.
- Branches must not be mixed without an explicit bridge theorem.
- HPF forbids more than **three physical spatial dimensions** in emergent geometry. Higher-dimensional mode spaces, topological classifications, or state spaces are legal only as **descriptive structure inside a 3D forged substrate**, not as extra physical directions.

---

# 3. Core substrate picture

The current HPF package is built on a **BCC Fibonacci substrate** with finite execution capacity and discrete lawful update structure.

## 3.1 Live microscopic grammar

The local executable line uses the **candidate-locked 4-bit site alphabet**

$$(n_L,n_R,b,q).$$

This is no longer treated as provisional "toy" language. It is the current candidate-locked **fundamental operator grammar of the substrate**.

That gives:

- $2^4 = 16$ local configurations,
- $15$ active non-vacuum microstates,
- the active complete-cycle count

$$N_{\rm cycle} = 24 \times 15 = 360,$$

where the factor 24 is the active BCC spatial sector count.

This April 9, 2026 milestone closes Obligation 1 of the Fine Structure Constant candidate note and is part of the live package state.

---

# 4. Current active anchors

The following anchors are not to be blurred or generalized away in the package.

## 4.1 Single empirical blur anchor

The live blur anchor is

$$S_{\rm blur}=1.05.$$

Under HPF mapping this is tied to the coherence-loss midpoint behavior in the Lin et al. single-atom double-slit program and serves as the single empirical blur anchor for the current vacuum-sector derivation package.

## 4.2 Nyquist denominator

The live residual margin is

$$\eta=\frac{1}{48}.$$

This is derived from **BCC 24-sector Nyquist geometry** with zero free parameters:

$$\eta = \frac{1}{2N_s} = \frac{1}{48}.$$

This is a first-principles substrate count, not a fitted coefficient. As of v2.3.0, $\eta = 1/48$ is derived directly from BCC geometry inside the executable — it is no longer imported as an external value.

## 4.3 Live phase landmarks

The active phase landmarks are:

- $S_{\rm blur}=1.05$
- $S_{\rm ent}=1.3806$
- $S_{\rm cap}=5.7889$

The old rounded `1.4` marker is retained only as historical development context. The live lower onset is $S_{\rm ent}=1.3806$.

## 4.4 Active vacuum-branch outputs

The active vacuum branch uses the corrected radial law

$$L_{\rm vac} = \frac{R_H}{\varphi^n}$$

with no `/2` factor in the radial identity.

Current live vacuum-branch state:

- $n=220$ is geometry-native: $n = \mathrm{round}(N_s^2/\varphi^2) = \mathrm{round}(220.012) = 220$,
- $\Lambda \approx 1.081 \times 10^{-52}\ \mathrm{m^{-2}}$ in the current package,
- $\Omega_{\rm dm} \approx 26.29\%$ through the governor-transfer branch,
- `S_cap` is treated as **substrate-native / derived**, not as theoretically open.

## 4.5 v2.3.0 milestone: S_cap derivation closure

As of v2.3.0, $S_{\rm cap} = 5.7889$ is **fully derived** with no free parameters anywhere in the chain:

$$N_s = 24 \rightarrow n = \mathrm{round}(N_s^2/\varphi^2) = 220 \rightarrow S_{\rm cap} = S_{\rm ent} + n \cdot \frac{\ln\varphi}{N_s} \approx 5.7889.$$

$n = 220$ is geometry-native, not candidate-locked by hand. The finite-$k$ explanation for the legacy 0.003 residual gap is retired; the correct explanation is shell-width resolution $\delta S = \ln(\varphi)/N_s \approx 0.020$, placing both values inside the same $n=220$ bin.

## 4.6 b/72 passive mirror correction

A single correction term $b/72 \approx 0.43\%$ (where $b = \ln\varphi/(\pi/2)$) is derived from QPRCA bipartite update algebra and applies to sublattice-sensitive observables. Three independent derivation branches confirm the same mechanism:

| Observable | Uncorrected | Corrected | Observed | Residual |
|---|---|---|---|---|
| Dark matter $\Omega_{\rm dm}$ | $26.29\%$ | $26.715\%$ | $26.8\%$ | $0.085\%$ |
| Neutrino ratio $\Delta m^2_{31}/\Delta m^2_{21}$ | $34$ | $33.856$ | $33.831$ | $0.07\%$ |
| Tsirelson bound $S_{\rm max}$ | $2\sqrt{2}$ | $2\sqrt{2} - 7.02\times10^{-6}$ | $2\sqrt{2}$ ($<10^{-3}$) | Not yet testable |

---

# 5. Repository structure

This repository is organized into four main lanes:

- `Docs/` — core canon volumes
- `Reference/` — theorem notes, correction notes, provenance, and symbol support
- `Phenomenology/` — candidate and exploratory phenomenology lanes
- `Src/` — executable and operational artifacts
- `Archive/` — superseded material retained for provenance

This split is intentional. It prevents active canon, support infrastructure, candidate tracks, and executable artifacts from being conflated.

---

# 6. Repository contents

## 6.1 Core canon volumes (`Docs/`)

- `Docs/Volume_I_Foundations.md`
  Top-level canonical framework statement and fixed architectural commitments.

- `Docs/Volume_II_Microscopic_Derivation.md`
  Microscopic executable-development line, legality theorem spine, registry repair, continuation-ambiguity line, and bridge/existence-sensor material.

- `Docs/Volume_III_Provenance_and_Status.md`
  Authority ladder, truth-status partition, supersession rules, contamination exclusion, and live-reference map.

- `Docs/Volume_IV_Lambda_and_Dark_Matter.md`
  Active vacuum-sector derivation package for the cosmological constant and dark-matter fraction, including the current handling of the blur anchor, Nyquist denominator, and selector chain.

## 6.2 Reference support (`Reference/`)

- `Reference/Symbol_Index.md`
  Live symbol and notation reference for the current canon set.

- `Reference/HPF_Derivation_Provenance_2026-3.md`
  2026 research-paper-state provenance support for the current $\Lambda$/dark-matter derivation chain.

- `Reference/HPF_Development_History-4.md`
  Development-path record preserving discovery order, constant provenance, and upgrade history.

- `Reference/HPF_Scap_SubstrateNative_Derivation.md`
  Closure note establishing the live substrate-native status of `S_cap`.

- `Reference/Delta_Collapse_Theorem_Note_v7U.md`
  Theorem-track support note for the active $S_{\rm cap}$ / $\delta_{\rm collapse}$ spine.

- `Reference/HPF_Correction_Note_Bcap_and_ChiGeom.md`
  Closure/provenance correction note including the live $B_{\rm cap}$ and $\chi_{\rm geom}^{*}$ starter language.

- `Reference/Governor_Transfer_Theorem.md`
  Support theorem for the dark-matter branch transfer $f_{\rm coh}\rightarrow \alpha_{\rm vac}\rightarrow \Omega_{\rm dm}$.

- `Reference/Existence_Sensor_Protocol.md`
  Protocol note for the existence-sensor line used with the executable stack.

- `Reference/HPF_Repo_Status_Memo.md`
  Package-status memo and live correction/status tracker.

- `Reference/HPF_Mirror_Buffer_Correction_Note_draft.md`
  Candidate passive mirror buffer correction for sublattice-sensitive observables.

- `Reference/HPF_Mirror_Buffer_Obligation_Closure_2026-04-12.md`
  Closes all three mirror-buffer obligations. Canonical closure reference for the $b/72$ correction.

- `Reference/HPF_boundary_condition_note_mirror_buffer_handoff_2026-04-10.md`
  Boundary condition note closing the geometric-prose phase of the mirror buffer inquiry and defining the QPRCA handoff obligations.

- `Reference/HPF_b72_Passive_Mirror_Correction_Reference_2026-04-15.md`
  Standalone consolidation of the $b/72$ passive mirror correction. Unifies the mirror-buffer draft, obligation closure, and Bell-Tsirelson candidate note. All three obligations closed.

- `Reference/HPF_QPRCA_Hard_Execution_Protocol_2026-04-15.md`
  Protocol note for the $k=11\rightarrow\infty$ transition, frozen boundary states, and mandatory continuation under QPRCA hard-gate execution. Executable-confirmed 2026-04-15. **256/256 strong pass — zero false positives, zero false negatives.**

- `Reference/HPF_Regulator_Availability_Bridge_Note_2026-04-10.md`
  Bridge note mapping the portable regulator object $\alpha(x)$ across the dimensional ladder from local availability to vacuum closure $\alpha_{\rm vac}$.

- `Reference/HPF_ReturnClass_Capacity_Derivation_2026-04-12.md`
  DCT Return-Class Capacity theorem: all non-degenerate lattice cycles have even length under $U = U_B \circ U_A$. Verifies the BCC bipartite update structure.

- `Reference/HPF_Correction_Note_LowerWall_Nyquist_2026-04-12.md`
  Correction note for the lower-wall Nyquist closure, fixing the single-sublattice resolution floor at $S_{\rm ent} = 1.3806$.

- `Reference/HPF_2_1_repo_patch_notes_2026-04-11.md`
  Patch notes for the v2.1 repo reorganization pass.

## 6.3 Candidate and exploratory phenomenology (`Phenomenology/`)

Four independent derivation threads plus supporting/interpretive notes. All are explicitly candidate — not canon.

### Entanglement / Bell thread

- `Phenomenology/HPF_Entanglement_Candidate_Note_2026-04-11.md`
  Entanglement as bifurcated lattice address in the active entropy band. Key result: entanglement is a single QPRCA node in the bifurcated address state $(n_L=1, n_R=1)$. Measurement zeros one directional bit — local resolution, no signaling.

- `Phenomenology/HPF_Entanglement_Obligation_Closure_2026-04-12.md`
  Closes lower-wall constitutive derivation and equal bit-weight obligations. $S_{\rm ent}$ constitutively the single-sublattice Nyquist floor. Equal bit-weight ($1/4$ per bit) forced by bijectivity — not assumed.

- `Phenomenology/HPF_Bell_Tsirelson_Candidate_Note_2026-04-12.md`
  Derives Tsirelson bound $2\sqrt{2}$ from substrate geometry. Closes mirror-buffer Obligation 3. Predicted deviation $\Delta S \approx -7.02\times10^{-6}$ from $b/72$ correction — not yet experimentally testable (~2.5 ppm precision required).

### Neutrino thread

- `Phenomenology/HPF_Neutrino_Mass_Hierarchy_Candidate_Note_2026-04-11_final.md`
  BCC Fibonacci derivation of neutrino mass-squared splittings. $\Delta m^2_{31}/\Delta m^2_{21} = F(9)/F(1) = 34$. Observed $33.831$ — $0.49\%$ error at zero free parameters; $0.07\%$ after $b/72$ correction.

### Photon ring thread

- `Phenomenology/HPF_Photon_Ring_Candidate_Note.md`
  Photon-ring echo location and amplitude from BCC Nyquist residual. Echo location candidate $r_{\rm echo} = 1.05\times r_{\rm photon}$. Echo amplitude candidate $A_{\rm echo} = \eta = 1/48 \approx 2.08\%$.

- `Phenomenology/HPF_Photon_Ring_Obligation_Update_2026-04-12.md`
  Closes forwarding identification obligation. Identifies honest obstruction in radial displacement law. Candidate cross-connection: $f_{\rm forward}(1.05\times3M) = 0.5406$ within $0.5\%$ of $f_{\rm coh} = 0.5434$ from the dark matter branch.

### Geometry validity thread

- `Phenomenology/HPF_Geometry_Validity_Threshold_Candidate_Note_2026-04-12.md`
  Load tensor, microscopic saturation wall, geometry-validity threshold, and percolation measurement of $\Lambda_c^{\rm (geom)}$. $\Lambda_c^{\rm (sub)} = 1$ exact from locality + reversibility + finite capacity. Effective 2D percolation gives $\eta_c(\infty) \approx 0.300$, numerically consistent with hard gate $G_{\rm health} < 0.30$.

### Supporting / interpretive

- `Phenomenology/HPF_Fine_Structure_Constant_Candidate_Note_2026-04-10_final.md`
  Fine-structure constant candidate. Both derivational obligations closed at note level. Canon promotion requires independent predictive confirmation. Surviving residual $0.000026\%$ consistent with passive mirror-buffer correction.

- `Phenomenology/HPF_Stochastic_Jitter_Falsifier_Candidate_Note.md`
  External falsifier lane tied to scheduler discreteness and propagation-induced broadening. ngEHT shadow floor target: $\geq 0.008$. Not part of the active $\Lambda$/DM derivation chain.

- `Phenomenology/HPF_Vacuum_Catastrophe_Candidate_Note.md`
  Vacuum catastrophe resolution from substrate saturation ceiling. No DM branch mixing without explicit bridge theorem.

- `Phenomenology/Lattice_Mirror_Symmetry_updated.md`
  Entanglement as substrate unity; $1/2$ factor substrate-native derivation.

- `Phenomenology/The_Cosmological_Boot_Sequence_updated.md`
  Phase sequence from substrate initialization to emergent spacetime.

- `Phenomenology/candidate_substrate_hpf.md`
  Candidate substrate architecture overview.

- `Phenomenology/hpf_phenomenology_subject_dimensional_closure_and_3_d_forging.md`
  Dimensional closure and 3D forging from substrate geometry.

## 6.4 Executable and operational artifacts (`Src/`)

- `Src/qprca.py`
  Front active executable interface.

- `Src/HPF_QPRCA_BCC_v0_3_0.py`
  **Primary v2.3.0 executable.** BCC bipartite automaton. Closes four build gaps from the 2026-04-15 handoff: BCC A/B sublattice topology, Fibonacci shell propagation, full B/R/A/P channel activation, and DCT return-class capacity executable verification. Derives $\eta=1/48$ and $n=220$ from geometry — $S_{\rm cap}$ no longer imported. **256/256 existence sensor pass. Zero false positives. Zero false negatives.**

- `Src/HPF_QPRCA_MicroToy_v0_2_7_BridgedContinuationAmbiguity_2026-03-20.py`
  Canonical March 20 executable reference. The 4-bit alphabet documented here is now treated under the April 9 epistemic upgrade — no longer a toy harness.

- `Src/sigma_pressure_test.json`
- `Src/AI_Engine_Registry_Prompt.md`

---

# 7. What is active, what is candidate, what is historical

## 7.1 Active canon
- Volumes I–IV
- Symbol Index
- current correction / provenance / theorem support notes in `Reference/`

## 7.2 Candidate
- all files in `Phenomenology/` unless explicitly promoted
- no phenomenology file has been promoted to canon as of v2.3.0

## 7.3 Historical / archive only
- superseded files in `Archive/`
- older wording that predates the corrected no-`/2` radial law
- older wording that treats `1.4` as the live lower onset
- older wording that leaves `S_cap` theoretically open after the closure note
- older wording that treats the 4-bit alphabet as merely "toy"
- fit-artifact amplitudes ($\varepsilon = 0.134$, $0.124$, $0.083$)

---

# 8. Recommended reading order

For a serious first pass through the repository:

1. `README.md`
2. `Docs/Volume_I_Foundations.md`
3. `Docs/Volume_II_Microscopic_Derivation.md`
4. `Docs/Volume_III_Provenance_and_Status.md`
5. `Docs/Volume_IV_Lambda_and_Dark_Matter.md`
6. `Reference/Symbol_Index.md`
7. `Reference/HPF_Derivation_Provenance_2026-3.md`
8. `Reference/HPF_Development_History-4.md`
9. `Reference/HPF_Scap_SubstrateNative_Derivation.md`
10. `Reference/Delta_Collapse_Theorem_Note_v7U.md`
11. `Reference/Governor_Transfer_Theorem.md`
12. `Reference/HPF_Correction_Note_Bcap_and_ChiGeom.md`
13. `Reference/Existence_Sensor_Protocol.md`
14. `Reference/HPF_QPRCA_Hard_Execution_Protocol_2026-04-15.md`
15. `Reference/HPF_b72_Passive_Mirror_Correction_Reference_2026-04-15.md`
16. `Reference/HPF_ReturnClass_Capacity_Derivation_2026-04-12.md`
17. `Src/HPF_QPRCA_BCC_v0_3_0.py`

Candidate phenomenology notes should be read after the canon and reference stack, not before. The `Phenomenology/READme.md` provides a dependency map for the phenomenology lanes.

---

# 9. Short package freeze

> HPF is a regulatory physics OS, not a catch-all theory. It governs legality, validity, and handoff across bounded execution regimes on a BCC Fibonacci substrate. The active package is the four-volume canon plus the live reference stack. The corrected no-`/2` radial law is active. The live lower onset is $S_{\rm ent}=1.3806$. The residual denominator is $\eta=1/48$ from BCC 24-sector Nyquist geometry with zero free parameters — derived inside the executable as of v2.3.0. `S_cap = 5.7889` is substrate-native / derived with no free parameters anywhere in the chain: $N_s=24 \rightarrow n=220 \rightarrow S_{\rm cap}$. $n=220$ is geometry-native: $\mathrm{round}(N_s^2/\varphi^2)$. The 4-bit alphabet $(n_L,n_R,b,q)$ is the candidate-locked fundamental operator grammar with 15 active non-vacuum microstates and $N_{\rm cycle}=360$. The $b/72$ passive mirror correction closes three independent obligations across three independent derivation branches. Candidate phenomenology remains separated from canon, and excluded contamination remains excluded.

---

## References used by the live package

- Lin, H., Lu, Y.-K., Fedoseev, V., Lee, Y. K., Lyu, J., & Ketterle, W. *Fringe visibility and which-way information in Young's double slit experiments with light scattered from single atoms.* arXiv:2507.19801.
