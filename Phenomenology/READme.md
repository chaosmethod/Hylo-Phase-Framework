# HPF Phenomenology — Index and Dependency Map

**Maintainer:** Eric Keaton Porter  
**Last updated:** 2026-05-05  
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

Five independent derivation threads run through this folder. They share substrate objects but no derivation steps.

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

GEOMETRY VALIDITY THREAD
────────────────────────
HPF_Geometry_Validity_Threshold_Candidate_Note_2026-04-12
        (standalone — synthesizes archived 2026-03-17 geometry-failure work;
         candidate connection to mirror-buffer thread via frontier renormalization)

VACUUM SECTOR / Λ THREAD
────────────────────────
HPF_Vacuum_Catastrophe_Candidate_Note  (structural diagnosis, 2026-04-01)
        ↓
HPF_Vacuum_Sector_Bipartite_Closure_2026-04-30  (DM + Λ bipartite multiplicity, §2.4 superseded for Λ)
        ↓
HPF_Lvac_Squared_Bipartite_Derivation  (consolidated v4, 2026-05-05; closes items 1 + 3 of upstream § 6)

SUPPORTING / INTERPRETIVE
─────────────────────────
Lattice_Mirror_Symmetry_updated
The_Cosmological_Boot_Sequence_updated
candidate_substrate_hpf
hpf_phenomenology_subject_dimensional_closure_and_3_d_forging
HPF_Fine_Structure_Constant_Candidate_Note_2026-04-10_final
HPF_Stochastic_Jitter_Falsifier_Candidate_Note
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

### `HPF_Geometry_Validity_Threshold_Candidate_Note_2026-04-12.md`
**Subject:** Load tensor, microscopic saturation wall, geometry-validity threshold, and percolation measurement of $\Lambda_c^{\rm (geom)}$  
**Date:** 2026-04-12  
**Status:** Candidate — synthesizes archived geometry-failure work (2026-03-17) into HPF v2.2.0 language  
**Upstream:** Live package only; candidate connection to mirror-buffer thread via frontier renormalization

| Obligation | Status |
| :--- | :--- |
| $\Lambda_c^{\rm (sub)} = 1$ from finite-capacity axioms | ✅ |
| $\zeta(S_f)$ as geometry survival probability | ✅ |
| $\eta_c(\infty) \approx 0.30$ numerical measurement (effective 2D proxy) | ✅ |
| Formal derivation of $\Lambda_c^{\rm (geom)}$ from QPRCA dynamics | ⬜ |
| Full 3D BCC percolation measurement of $\Lambda_c^{\rm (geom)}$ | ⬜ |
| $\alpha_{\rm stat}$ from QPRCA load statistics | ⬜ |
| Frontier renormalization ↔ $b/72$ mirror-buffer identification | ⬜ |
| $\hbar$, $G$, $c$ from substrate axioms | ⬜ |

**Key result:** $\Lambda_c^{\rm (sub)} = 1$ is exact from locality + reversibility + finite capacity — no free parameters. The logistic forwarding gate $\zeta(S_f)$ is derived as the coarse-grained probability $P(\Lambda^{(b)} < \Lambda_c^{\rm (geom)})$, not an assumption. Effective 2D percolation gives $\eta_c(\infty) \approx 0.300$, $\nu \approx 1.36 \pm 0.04$, numerically consistent with the MDEA routing hard gate $G_{\rm health} < 0.30$. Metric response $g_{00} = -(1-\Lambda_0)^2$ and Einstein-like closure $\kappa = 8\pi G/c^4$ are candidate structural results with $\hbar$, $G$, $c$ external.

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
**Date:** 2026-04-01  
**Status:** Candidate — three obligations open. Numerics for the bipartite correction superseded by `HPF_Lvac_Squared_Bipartite_Derivation.md` (consolidated 2026-05-05); structural diagnosis (QFT overcount → resolution legality gate) unchanged.  
**Upstream:** Live package only

---

### `HPF_Vacuum_Sector_Bipartite_Closure_2026-04-30.md` *(in `/Reference`, cross-listed here as Λ-thread upstream)*
**Subject:** Universal trigger criterion applied to vacuum sector — DM and Λ bipartite multiplicities  
**Date:** 2026-04-30 (superseding update note added 2026-05-05)  
**Status:** DM closure (§2.3, multiplicity 1) substrate-native and ready for canon. Λ closure (§2.4) **superseded** for the bipartite multiplicity by the consolidated derivation; original squared-form numerics preserved for traceability.

| Obligation (§ 6) | Status |
| :--- | :--- |
| (1) Formal $L_{\rm vac}^{2}$ bipartite multiplicity | ✅ closed by consolidated derivation 2026-05-05 — substrate-native multiplicity is 4 (linear 3+1), not 2 (squared) |
| (2) No additional bipartite-sensitive factors elsewhere in Λ chain | ⬜ open — verification of $\zeta(S)$, $S_{\rm ent}$, $S_{\rm cap}$ A/B-collapse invariance pending |
| (3) Independent execution-lock via 256/256 existence-sensor sweep | ✅ closed 2026-05-05 — `Src/qprca.py` Strong Pass on all six aggregate × model combinations |

**Key result:** Λ_corrected (linear form) = $1.0997 \times 10^{-52}$ m⁻², gap 0.027%. DM_corrected = 26.715%, gap 0.085%.

---

### `HPF_Lvac_Squared_Bipartite_Derivation.md`
**Subject:** Formal substrate-native derivation of $L_{\rm vac}^{2}$ bipartite multiplicity in the 3+1 fused-spacetime substrate, grounded in the canonical 4-bit grammar $(n_L, n_R, b_{\rm bit}, q)$  
**Date:** 2026-05-03 (v4 derivation); 2026-05-05 (consolidated, supersedes standalone v1, v2, v3)  
**Status:** Candidate — closes items (1) and (3) of `HPF_Vacuum_Sector_Bipartite_Closure_2026-04-30.md` § 6; item (2) remains open.  
**Upstream:** `/Reference/HPF_Mirror_Buffer_Entanglement_Closure_2026-04-30.md` (trigger criterion); `/Reference/HPF_Mirror_Buffer_Obligation_Closure_2026-04-12.md` ($b/72$ residual); `Vacuum_Sector_Bipartite_Closure_2026-04-30` (DM/Λ pairing and items list); 4-bit grammar lock from `HPF_Fine_Structure_Constant_Candidate_Note_2026-04-10_final.md`.

| Obligation | Status |
| :--- | :--- |
| (1) Formal $L_{\rm vac}^{2}$ bipartite multiplicity | ✅ closed at note level — multiplicity 4 (linear 3+1), b_bit-grounded |
| (2) No additional bipartite-sensitive factors in Λ chain | ⬜ open — see Appendix D § D.5 audit-path note |
| (3) 256/256 existence-sensor sweep | ✅ closed — Appendix D documents Strong Pass across all six aggregate × model combinations |

**Key result:** $L_{\rm vac}^{2} \to L_{\rm vac}^{2}(1 - 4\,b/72)$ with the 4 = 3 + 1 decomposition (3 spatial bipartite events through $(n_L, n_R)$ + 1 b_bit grammar event). $\Lambda_{\rm corrected} = 1.0997 \times 10^{-52}$ m⁻², gap 0.027%. The squared form $(1-2b/72)^{2}$ is structurally inadmissible because it would require two independent b_bit letters (the canonical alphabet has exactly one). Internal v1 → v4 progression preserved in Appendix B with full mathematical content.

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

### $b/72$ Correction — Four Independent Branches

The $b/72$ passive mirror correction threads through four independent derivation branches, each arriving at the same correction from the same substrate mechanism:

| Observable | Thread | Multiplicity | Uncorrected | Corrected | Observed | Residual |
| :--- | :--- | :---: | :--- | :--- | :--- | :--- |
| Dark matter fraction $\Omega_{\rm dm}$ | `/Docs/Volume_IV` | 1 (governor transfer) | $26.29\%$ | $26.715\%$ | $26.8\%$ | $0.085\%$ |
| Neutrino ratio $\Delta m^2_{31}/\Delta m^2_{21}$ | Neutrino thread | 1 (b_bit bridge) | $34$ | $33.856$ | $33.831$ | $0.07\%$ |
| Tsirelson bound $S_{\rm max}$ | Bell thread | 2 (squared, $\Delta S \sim (b/72)^2$) | $2\sqrt{2}$ | $2\sqrt{2} - 7.02\times10^{-6}$ | $2\sqrt{2}$ (within $10^{-3}$) | Not yet testable |
| Cosmological constant $\Lambda$ | Vacuum thread | 4 = 3 spatial + 1 b_bit (linear 3+1) | $1.0810 \times 10^{-52}$ m⁻² | $1.0997 \times 10^{-52}$ m⁻² | $1.1000 \times 10^{-52}$ m⁻² | $0.027\%$ |

The same b_bit letter of the canonical 4-bit alphabet $(n_L, n_R, b_{\rm bit}, q)$ contributes the +1 grammar event in three of the four branches (DM at governor transfer, neutrino at the Fibonacci shared-face traversal, Λ at the temporal fold of the 3+1 collapse count). Tsirelson sits in the squared $(b/72)^{2}$ regime and is the residual diagnostic across the bipartite test.

### Geometry Validity ↔ Mirror-Buffer Candidate Connection

The geometry validity thread connects to the mirror-buffer thread via a candidate identification: the frontier renormalization mechanism (healing suppression near failed neighbors, dominant control on $\eta_c$) is a candidate realization of the $b/72$ passive mirror correction at the geometry-failure boundary. See `HPF_boundary_condition_note_mirror_buffer_handoff_2026-04-10` (Obligations Q1–Q3) and `HPF_Geometry_Validity_Threshold_Candidate_Note_2026-04-12.md` (§5.5).

### Photon Ring ↔ Dark Matter Candidate Connection

$f_{\rm forward}(1.05 \times 3M) = 0.5406$ is within $0.5\%$ of $f_{\rm coh} = 0.5434$ from the dark matter branch. Two entirely independent derivation paths — Schwarzschild GR and BCC Fibonacci boundary geometry — arrive at the same coherent support fraction evaluated at the blur anchor. Noted as a candidate observation; not a claimed result.
