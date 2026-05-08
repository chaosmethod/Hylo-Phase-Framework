# HPF–MDEA Unified Symbol & Definition Index
## Canonical Reference — Milestone Lock State (2026-04-10)

**Status:** Canonical reference  
**Scope:** Definitions only — no derivations, no narrative arguments, no phenomenology promotion by implication  
**Purpose:** Eliminate ambiguity across HPF, MDEA, UHET, QPRCA, the active vacuum-sector package, and the candidate-locked microscopic grammar

---

# 1. Layer map

This stack is **layered, not competitive**:

- **HPF (Hylo Phase Framework)** — regulator, legality governor, regime detector, and handoff authority
- **MDEA (Multi-Domain Execution Architecture)** — routing kernel / model-of-expertise orchestration layer
- **GR / QM / effective theories** — downstream expert regimes
- **QPRCA (Quantum Partitioned Reversible Cellular Automaton)** — deeper substrate expert / executable substrate candidate

No lower layer replaces a higher one. No downstream expert becomes the regulator.

---

# 2. Global symbols

| Symbol | Name | Layer | Definition | Notes |
|---|---|---|---|---|
| \(x\) | Site / region index | Global | Localized execution region | Abstract lattice or coarse-grained index |
| \(t_{\rm sched}\) | Scheduler time | QPRCA | Absolute substrate update clock | Uniform substrate tick |
| \(\tau\) | Proper time | Emergent | Observable time from coherent updates | Branch-dependent emergent time |
| \(c\) | Substrate propagation limit | QPRCA | Lattice site spacing per scheduler tick | \(L_{\rm vac} \equiv c\,t_{\rm sched}\) |
| \(S_{\rm handoff}\) | Handoff state | MDEA | Minimal exported state at regime transfer | No invented precision allowed |

---

# 3. HPF — legality and regulation symbols

| Symbol | Name | Definition | Valid range | Notes |
|---|---|---|---|---|
| \(b(x)\) | Badness field | Local measure of instability / execution degradation | \(\ge 0\) | Domain-agnostic |
| \(B\) | Total badness | Aggregate badness, typically \(\sum_x b(x)\) | \(\ge 0\) | Refinement-tracked |
| \(\sigma(x)\) | Saturation pressure | Local update demand / capacity ratio | \([0,\infty)\) | Hard illegality beyond capacity |
| \(\sigma_{\max}\) | Maximum saturation | \(\max_x \sigma(x)\) | \([0,\infty)\) | Routing trigger |
| \(\sigma_*\) | Activation threshold | Persistent saturation trigger | default \(0.7\) | HPF engagement threshold |
| \(G_{\rm health}\) | Geometry health | Metric viability score | \([0,1]\) | Geometry revoked when too low |
| \(G_{\rm crit}\) | Geometry cutoff | Metric failure threshold | \(0.3\) | Hard revoke threshold |
| \(U_{\rm health}\) | Unitarity health | Probability-conservation diagnostic | \([0,1]\) | Diagnostic, not regulator |
| \(\tau_C\) | Convergence threshold | Refinement convergence ratio | default \(0.5\) | Internal default |
| \(\tau_P\) | Persistence threshold | Instability persistence ratio | default \(0.8\) | Internal default |
| \(L_{\rm HPF}\) | HPF legality functional | Hard legality gate on regime use | \(\{0,1\}\) | Governs whether a description is lawful |
| \(V_i\) | Validity score | Fitness of expert \(E_i\) to current state | context-dependent | Validity is not legality |

---

# 4. MDEA — routing and execution symbols

| Symbol | Name | Definition | Notes |
|---|---|---|---|
| \(E_i\) | Domain expert | Theory + solver valid in a regime | GR, QM, semiclassical, QPRCA, etc. |
| \(E^*\) | Selected expert | \(\arg\max_i V_i\) subject to legality | Soft routing subject to HPF gates |
| \(R\) | Routing policy | Expert-selection logic over candidate experts | Controlled by HPF legality and state context |
| \(S_{\rm handoff}\) | Handoff state | Minimal exported state during regime transfer | Repeated here because it is core to routing |
| \(M_{\rm req}\) | Required update mass / burden | Execution demand required by a description | Used in legality comparisons |
| \(M_{\rm free}\) | Free update mass / burden | Available bounded execution resource | Used in legality comparisons |

---

# 5. UHET / phenomenology-facing regulation symbols

| Symbol | Name | Definition | Notes |
|---|---|---|---|
| \(S_f\) | Entropic flux / load | Dimensionless substrate load variable | Phase driver |
| \(u(r)\) | Utilization | \(R_s/r\) | Dimensionless regime-loading profile |
| \(\alpha(x)\) | Update availability | Local coherent update fraction | Meaning depends on layer context; see QPRCA note below |
| \(R_s\) | Saturation radius | Utilization \(=1\) surface | Horizon-like effective boundary |
| \(\gamma_{\rm HPF}\) | Time-dilation factor | \(dt_{\rm sched}/d\tau\) | Effective time-dilation object under HPF framing |
| \(\zeta(S)\) | Forwarding / coherence gate | Logistic gate used in the active vacuum branch | Midpoint fixed at \(S_{\rm blur}\) |

---

# 6. QPRCA — substrate symbols

| Symbol | Name | Definition | Notes |
|---|---|---|---|
| \(\alpha(x)\) | Regulator field / coherent update availability | Local coherent update availability at substrate level | Quantum degree of freedom / update fraction |
| \(L_{\rm tot}(x)\) | Total load | Sum of all channel activities at \(x\) | Universal coupling input |
| \(L_a(x)\) | Channel load | Activity from channel \(a\) at \(x\) | Weighted contribution |
| \(w_a\) | Channel weight | Fixed coupling weight for channel \(a\) | Non-geometric weight |
| \(F(x,t)\) | Microscopic legality ratio | \(M_{\rm req}^{(\rm micro)}(x,t)/M_{\rm free}^{(\rm micro)}(x,t)\) | Local substrate legality test |
| \(L_{\rm QPRCA}(x,t)\) | Microscopic legality gate | \(1 \iff F(x,t)<1\) | Deepest intended legality target |
| \(U\) | Unresolved burden | Live burden state in the executable line | Fed into geometric bridge stack |
| \(U_{\rm geom}^{(\rm NL)}\) | Nonlinear geometric burden projection | Geometric burden after nonlinear mapping | Executable bridge quantity |
| \(\Lambda_{\rm geom}\) | Geometric burden aggregate | Derived geometric aggregation object | Executable bridge quantity |
| \(\chi_{\rm geom}^{*}\) | Geometry-dominance starter diagnostic | Dominance-aware starter diagnostic | Live starter diagnostic in current package |

---

# 7. Microscopic grammar symbols

This section records the **candidate-locked fundamental operator grammar** of the substrate.

| Symbol | Name | Definition | Notes |
|---|---|---|---|
| \(n_L\) | Left-neighbor occupancy / participation bit | Left-side local routing / occupancy indicator | Bit in the fundamental site alphabet |
| \(n_R\) | Right-neighbor occupancy / participation bit | Right-side local routing / occupancy indicator | Bit in the fundamental site alphabet |
| \(b\) | Bridge / bond bit | Local bridge / bond-state indicator in the grammar | Microscopic grammar symbol; do not confuse with Fibonacci growth parameter below |
| \(q\) | Local state / charge bit | Local state-selection / charge-like indicator | Microscopic grammar symbol |
| \((n_L,n_R,b,q)\) | 4-bit site alphabet | Candidate-locked local state-space grammar | Fundamental operator grammar of the substrate |
| \(N_{\rm cfg}\) | Total local configurations | \(2^4 = 16\) | All local grammar configurations |
| \(N_{\rm active}\) | Active non-vacuum microstates | \(16-1=15\) | Excludes \((0,0,0,0)\) vacuum |
| \(N_{\rm cycle}\) | Complete-cycle active phase-space count | \(24 \times 15 = 360\) | Product of spatial sectors and active microstates |

**Naming warning:** The microscopic grammar bit \(b\) is **not** the same object as the Fibonacci growth parameter \(b=\ln\varphi/(\pi/2)\). When ambiguity is possible in prose, write “grammar bit \(b\)” or “growth parameter \(b\)” explicitly.

---

# 8. Vacuum-sector symbols

These symbols belong to the active \(\Lambda\) / dark-matter branch.

| Symbol | Name | Definition | Notes |
|---|---|---|---|
| \(L_{\rm vac}\) | Substrate resolution scale | Lattice site spacing; \(L_{\rm vac}=c\,t_{\rm sched}\) | Active radial law: \(L_{\rm vac}=R_H/\varphi^n\); no `/2` in the radial identity |
| \(\varphi\) | Golden ratio | \((1+\sqrt{5})/2\) | Asymptotic Fibonacci growth rate |
| \(b\) | Fibonacci growth parameter | \(b=\ln\varphi/(\pi/2)\) | Support-geometry parameter |
| \(f_{\rm coh}\) | Coherent support fraction | \(\frac{1}{2\pi b}\sqrt{1+b^2}\) | Coherent vacuum support fraction |
| \(\alpha_{\rm vac}\) | Vacuum update availability | \(\sqrt{f_{\rm coh}}\) | Governor-transfer output |
| \(\Omega_{\rm dm}\) | Dark-matter fraction | \(1-\alpha_{\rm vac}\) | Deferred coherent-support complement |
| \(n\) | Radial shell index | Defined by \(R_H/L_{\rm vac}=\varphi^n\) | Active shell count is candidate-locked at \(n=220\) |
| \(R_H\) | Hubble radius | \(c/H_0\) | External cosmological scale used in the active branch |
| \(\kappa_{\rm BCC}\) | BCC geometric coefficient | \(8 \times (1/2) \times (1/2)=2\) | Coordination \(\times\) bipartite \(\times\) LMS mirror |
| \(\varepsilon\) | Continuum correction / residual | \((1-\zeta(S_f))(L_{\rm vac}/\ell_O)^{S_{\rm ent}}\) | Discrete-substrate residual for observable scale \(\ell_O\) |
| \(\ell_O\) | Observable scale | Measurement or probe scale in the residual law | Context-dependent |

---

# 9. Phase-corridor and gate symbols

| Symbol | Name | Definition | Notes |
|---|---|---|---|
| \(S_{\rm blur}\) | Blur anchor | \(1.05\) | Single empirical blur anchor under HPF mapping |
| \(S_{\rm ent}\) | Active entropy onset | \(1.3806\) | Live lower onset and selector lower bound |
| \(S_{\rm cap}\) | Capacity wall / saturation ceiling | \(5.7889\) | Live upper wall; substrate-native / derived in current package |
| \(\eta\) | Nyquist residual margin | \(1/48\) | Derived from BCC 24-sector Nyquist geometry |
| \(N_s\) | Active spatial sectors | \(24\) | 3D lift of BCC 8-fold coordination |
| \(k\) | Logistic steepness parameter | Active gate steepness in \(\zeta(S)\) | Canonical exact/derived value near \(11.62\); rounded operational value \(11\) |
| \(\zeta(S)\) | Logistic forwarding/coherence gate | \(\frac{1}{1+e^{k(S-1.05)}}\) | Midpoint fixed at \(S_{\rm blur}\) |
| \(n_{\rm raw}\) | Unrounded selector output | Continuous shell-selector output before rounding | Candidate-locked at approximately \(219.742\) in the active branch |
| \(n_{\rm sel}\) | Integer shell selector | \(\mathrm{round}(n_{\rm raw})\) | Gives \(220\) in active branch |

---

# 10. Active phase boundaries

| Quantity | Boundary | Interpretation |
|---|---|---|
| \(S_f < 1.05\) | Below blur threshold | Fully coherent local updates; discrete substrate maximally hidden |
| \(S_f \approx 1.05\) | Blur threshold | Coherence-loss midpoint; \(\zeta=0.5\) |
| \(1.05 < S_f < 1.3806\) | Pre-entropy transition band | Coherence-loss regime before active entropy onset |
| \(1.3806 < S_f < 5.7889\) | Active entropy / transition band | Instability-active regime used by selector and suppression law |
| \(S_f > 5.7889\) | Capacity wall / decoherence | Raw geometry collapse / saturation ceiling |
| \(\sigma_{\max} \ge 1\) | Illegal | Route out of current effective description |
| \(G_{\rm health} < 0.3\) | Metric failure | Route to deeper substrate authority |
| no separate active \(1.4\) marker | Canon note | Rounded `1.4` is historical only; live lower onset is \(1.3806\) |

---

# 11. Fine-structure candidate-note symbols

These symbols are used in the current fine-structure candidate note and are included here only because they now touch the candidate-locked microscopic grammar.

| Symbol | Name | Definition | Notes |
|---|---|---|---|
| \(N_{\rm cycle}\) | Complete-cycle active phase-space count | \(24 \times 15 = 360\) | Now grounded in sectors \(\times\) active microstates |
| \(1/\alpha_{\rm fs}\) | Inverse fine-structure constant | Candidate phenomenology target | Candidate note only; not active canon output |
| \((2\varphi-1)^2\) | Fibonacci fixed-point denominator | Equals \(5\) | Appears in the delta-collapse spine and candidate \(\alpha\) note |

This section does **not** promote the fine-structure result into canon. It only fixes the symbol meanings.

---

# 12. Reference-status notes

## 12.1 Definitions-only rule

This file defines symbols only. It does not:
- prove theorems,
- promote candidates into canon,
- replace provenance notes,
- replace the vacuum-sector package,
- replace executable documentation.

## 12.2 Current live package notes

- The corrected no-`/2` radial law is active.
- The live lower onset is \(S_{\rm ent}=1.3806\).
- `S_cap` is live as substrate-native / derived, not theoretically open.
- The 4-bit grammar is candidate-locked fundamental grammar, not “toy” scaffolding.
- External experimental correspondences are not part of this definitions-only layer unless they are explicitly promoted into canon.

## 12.3 Exclusion note

Excluded non-HPF contamination material has no standing in this symbol map.

---

# 13. Short freeze

> The active HPF symbol set is now fixed across the four canon volumes: the regulator stack remains layered, the active vacuum branch uses the corrected no-`/2` radial law, the live phase corridor is \((1.05,\ 1.3806,\ 5.7889)\), \(\eta=1/48\) remains the BCC 24-sector Nyquist residual, and the 4-bit site alphabet \((n_L,n_R,b,q)\) is the candidate-locked fundamental operator grammar with \(15\) active non-vacuum microstates and \(N_{\rm cycle}=360\).

