# HPF Phenomenology — Index and Dependency Map

**Maintainer:** Eric Keaton Porter  
**Last updated:** 2026-04-12  
**Scope:** All candidate and support notes in the `/Phenomenology` folder. Canon volumes are in `/Docs`. Reference documents are in `/Reference`.

---

## Status Key

| Symbol | Meaning |
| :--- | :--- |
| ✅ | Closed at candidate note level |
| 🔶 | Partially closed |
| ⬜ | Open |

---

## Dependency Chains

Three independent derivation threads run through this folder. They share substrate objects but no derivation steps.

```
ENTANGLEMENT / BELL THREAD
──────────────────────────
HPF_Entanglement_Candidate_Note_2026-04-11
        ↓
HPF_Entanglement_Obligation_Closure_2026-04-12
        ↓
HPF_Bell_Tsirelson_Candidate_Note_2026-04-12

NEUTRINO THREAD
───────────────
HPF_Neutrino_Mass_Hierarchy_Candidate_Note_2026-04-11_final
        (standalone — no internal phenomenology dependencies)

PHOTON RING THREAD
──────────────────
HPF_Photon_Ring_Candidate_Note
        ↓
HPF_Photon_Ring_Obligation_Update_2026-04-12

SUPPORTING / INTERPRETIVE
─────────────────────────
Lattice_Mirror_Symmetry_updated
The_Cosmological_Boot_Sequence_updated
candidate_substrate_hpf
hpf_phenomenology_subject_dimensional_closure_and_3_d_forging
HPF_Fine_Structure_Constant_Candidate_Note_2026-04-10_final
HPF_Stochastic_Jitter_Falsifier_Candidate_Note
HPF_Vacuum_Catastrophe_Candidate_Note
```

All threads draw from the same live package objects:
- BCC bipartite geometry and 24-sector ring (`/Docs/Volume_I_Foundations.md`)
- QPRCA update algebra (`/Docs/Volume_II_Microscopic_Derivation.md`)
- Active entropy band $1.3806 < S_f < 5.7889$
- $\eta = 1/48$, $S_{\rm blur} = 1.05$, $b = \ln\varphi/(\pi/2)$
- $b/72$ passive mirror correction (`/Reference/HPF_Mirror_Buffer_Obligation_Closure_2026-04-12.md`)

---

## Document Registry

---

### `HPF_Entanglement_Candidate_Note_2026-04-11.md`
**Subject:** Quantum entanglement as bifurcated lattice address in the active entropy band  
**Date:** 2026-04-11  
**Status:** Candidate — one obligation open

| Obligation | Status |
| :--- | :--- |
| $S_{\rm ent}$ as constitutive entanglement threshold | ✅ closed by Obligation Closure |
| Equal bit-weight from bijectivity | ✅ closed by Obligation Closure |
| Grammar uniqueness | ⬜ separate open problem; does not gate 3/2 derivation |
| SPDC creation event bridge | ⬜ path identified, not constructed |

**Key result:** Entanglement is a single QPRCA node in the bifurcated address state $(n_L=1, n_R=1)$. The 3/2 update path cost = $1.0$ (propagation) $+ 1/4 + 1/4$ ($n_{Lh}$ and $n_{Rh}$ disambiguation). Measurement zeros one directional bit — local resolution, no signaling.

---

### `HPF_Entanglement_Obligation_Closure_2026-04-12.md`
**Subject:** Lower-wall constitutive derivation, equal bit-weight, SPDC bridge status  
**Date:** 2026-04-12  
**Status:** Closes Obligation 1; partially closes Obligation 2; tightens Obligation 3  
**Upstream:** `HPF_Entanglement_Candidate_Note_2026-04-11.md`

| Obligation | Status |
| :--- | :--- |
| $S_{\rm ent}$ as single-sublattice Nyquist floor ($1/24$) | ✅ |
| Equal bit-weight ($1/4$ per bit) from bijectivity | ✅ |
| Grammar uniqueness | ⬜ |
| SPDC creation event bridge | ⬜ |

**Key result:** Equal bit-weight is forced by bijectivity of the QPRCA update rule on the full 4-bit state space — not assumed. $S_{\rm ent}$ is constitutively the single-sublattice resolution failure point on the BCC 24-sector ring.

---

### `HPF_Bell_Tsirelson_Candidate_Note_2026-04-12.md`
**Subject:** Tsirelson bound $2\sqrt{2}$ as substrate output; mirror-buffer Obligation 3 closure  
**Date:** 2026-04-12  
**Status:** Candidate — closes mirror-buffer Obligation 3  
**Upstream:** `HPF_Entanglement_Candidate_Note_2026-04-11.md`, `HPF_Entanglement_Obligation_Closure_2026-04-12.md`

| Obligation | Status |
| :--- | :--- |
| Derive $2\sqrt{2}$ from substrate geometry | ✅ |
| $b/72$ correction as third independent sublattice-sensitive observable | ✅ |

**Key result:** Substrate bidirectional peak $(3/2)(\pi/12) = \pi/8$. CHSH measurement resolves both $n_{Lh}$ and $n_{Rh}$ simultaneously (one-way probe), doubling to $\pi/4$ — the optimal CHSH gap. $S_{\rm max} = 2\sqrt{2}$ is substrate geometry, not a quantum-mechanical axiom. Predicted deviation $\Delta S \approx -7.02 \times 10^{-6}$ from $b/72$ correction — not yet experimentally testable (~2.5 ppm).

**Closes:** mirror-buffer Obligation 3. Three independent sublattice-sensitive observables (dark matter fraction, neutrino mass-squared ratio, Tsirelson bound) now receive the same $b/72$ correction from the same substrate mechanism.

---

### `HPF_Neutrino_Mass_Hierarchy_Candidate_Note_2026-04-11_final.md`
**Subject:** BCC Fibonacci derivation of neutrino mass-squared splittings  
**Date:** 2026-04-11  
**Status:** Candidate — two obligations closed; one open  
**Upstream:** Live package only (no internal phenomenology dependencies)

| Obligation | Status |
| :--- | :--- |
| Derive $\mu$ from canonical HPF objects | ✅ (0.000015% error) |
| Derive shared-face index ($+1$) in QPRCA algebra | ✅ |
| PMNS mixing matrix from axis-pair precession | ⬜ |

**Key result:** $\Delta m^2_{31}/\Delta m^2_{21} = F(9)/F(1) = 34$. Observed ratio $33.831$ — $0.49\%$ error at zero free parameters. After $b/72$ correction residual drops to $0.07\%$. Base unit $\mu$ derived from substrate-native objects with zero free parameters, $0.000015\%$ error. BCC coordination number $8$ + shared-face $b$-bit traversal $+1$ = Fibonacci index $9$.

---

### `HPF_Photon_Ring_Candidate_Note.md`
**Subject:** Photon-ring echo location and amplitude from BCC Nyquist residual  
**Date:** 2026-04-10  
**Status:** Candidate — Obligation 1 closed by update note; Obligations 2 and 3 open

| Obligation | Status |
| :--- | :--- |
| Forwarding-identification lemma ($\zeta = f_{\rm forward}$) | ✅ closed by update note |
| Radial blur displacement law ($1.05\times$) | ⬜ obstruction identified |
| Mode-indexing and reflection bridge | ⬜ |

**Key result:** Echo location candidate $r_{\rm echo} = 1.05 \times r_{\rm photon}$. Echo amplitude candidate $A_{\rm echo} = \eta = 1/48 \approx 2.08\%$. Old fitted amplitude $\varepsilon = 0.134$ excluded from HPF scope.

---

### `HPF_Photon_Ring_Obligation_Update_2026-04-12.md`
**Subject:** Forwarding identification closed; displacement law obstruction identified; amplitude confirmed  
**Date:** 2026-04-12  
**Status:** Closes Obligation 1; Obligation 2 open with honest obstruction; Obligation 3 unaffected  
**Upstream:** `HPF_Photon_Ring_Candidate_Note.md`

| Obligation | Status |
| :--- | :--- |
| Forwarding identification ($\zeta = f_{\rm forward}$) | ✅ bridge axiom + elimination |
| Radial displacement law | ⬜ linearized bridge overshoots by ~2.5–3× |
| Echo amplitude $A_{\rm echo} = 1/48$ | Confirmed unaffected by Nyquist correction |

**Key result:** $f_{\rm forward}$ is the unique survivor of five-property elimination against all low-complexity GR candidates. Hard midpoint fact: $f_{\rm forward}(3M) = 1/2$. Linearized displacement bridge fails — $1.05\times$ retained as direct substrate transfer, not GR-derived. New candidate observation: $f_{\rm forward}(1.05 \times 3M) = 0.5406$ within $0.5\%$ of $f_{\rm coh} = 0.5434$ from the dark matter branch.

---

### `HPF_Fine_Structure_Constant_Candidate_Note_2026-04-10_final.md`
**Subject:** Fine-structure constant derivation from BCC substrate  
**Date:** 2026-04-10  
**Status:** Candidate  
**Upstream:** Live package only

---

### `HPF_Stochastic_Jitter_Falsifier_Candidate_Note.md`
**Subject:** Stochastic jitter as falsifier for substrate discreteness  
**Status:** Candidate  
**Upstream:** Live package only

---

### `HPF_Vacuum_Catastrophe_Candidate_Note.md`
**Subject:** Vacuum catastrophe resolution from substrate saturation ceiling  
**Status:** Candidate  
**Upstream:** Live package only

---

### `Lattice_Mirror_Symmetry_updated.md`
**Subject:** Entanglement as substrate unity; $1/2$ factor substrate-native derivation  
**Status:** Candidate — one obligation open (formal metric derivation from $L_{\rm vac}$ round-trip)  
**Upstream:** Live package only

---

### `The_Cosmological_Boot_Sequence_updated.md`
**Subject:** Phase sequence from substrate initialization to emergent spacetime  
**Status:** Candidate  
**Upstream:** Live package only

---

### `candidate_substrate_hpf.md`
**Subject:** Candidate substrate architecture overview  
**Status:** Candidate  
**Upstream:** Live package only

---

### `hpf_phenomenology_subject_dimensional_closure_and_3_d_forging.md`
**Subject:** Dimensional closure and 3D forging from substrate geometry  
**Status:** Candidate  
**Upstream:** Live package only

---

## Cross-Thread Connections

The $b/72$ passive mirror correction threads through three independent derivation branches, each arriving at the same correction from the same substrate mechanism:

| Observable | Thread | Uncorrected | Corrected | Observed | Residual |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Dark matter fraction $\Omega_{\rm dm}$ | `/Docs/Volume_IV` | $26.29\%$ | $26.715\%$ | $26.8\%$ | $0.085\%$ |
| Neutrino ratio $\Delta m^2_{31}/\Delta m^2_{21}$ | Neutrino thread | $34$ | $33.856$ | $33.831$ | $0.07\%$ |
| Tsirelson bound $S_{\rm max}$ | Bell thread | $2\sqrt{2}$ | $2\sqrt{2} - 7.02\times10^{-6}$ | $2\sqrt{2}$ (within $10^{-3}$) | Not yet testable |
