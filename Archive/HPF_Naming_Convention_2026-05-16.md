# HPF Naming Convention Reference
## Canonical Naming-Convention Note — Milestone Lock State (2026-05-16)

**Status:** Canonical naming-convention reference. Vocabulary lock companion to `Reference/Symbol_Index.md`.
**Scope:** Names for HPF regulatory mechanisms, operational components, and substrate-phase parameters. No derivations, no truth-status changes, no canon promotion.
**Author:** Eric Keaton Porter
**Framework version:** Hylo Phase Framework v2.4.0
**Companion to:** `Reference/Symbol_Index.md` (symbol definitions), `Reference/HPF_Derivation_Provenance_2026-3.md` (derivation provenance).

---

# 1. Purpose

This file locks the canonical vocabulary for HPF regulatory mechanisms. The Symbol Index defines symbols; this note defines the named mechanisms those symbols operate within. Together they form the live vocabulary surface of the framework.

This file does **not**:

- prove theorems,
- promote candidates into canon,
- replace provenance notes,
- replace the vacuum-sector package,
- replace executable documentation,
- alter any truth-status partition in the existing canon.

---

# 2. Convention

## 2.1 Prefix system

The convention partitions named mechanisms by structural role:

| Prefix | Role | Covers |
|---|---|---|
| **Hylo X** | Fundamental regulatory mechanisms | Gates, sensors, selectors, the passive mirror correction, the sublattice-sensitivity criterion, the governor law |
| **HPF X** | Tools and operational components | The truth-status discipline, the status ladder, the failure catalogue, the bridge stack, the drift locks, the shadow rule |
| **Phase X** | Substrate-phase parameters and the phase corridor | The capacity wall, the entropy onset, the blur threshold, the Nyquist residual, the bounded interval between walls |

Prefix assignment is structural, not stylistic. A mechanism that fires legality decisions is **Hylo**. A mechanism that catalogues, enumerates, or organizes is **HPF**. A parameter or bounded interval inside the phase corridor is **Phase**.

## 2.2 Personal eponym discipline

Exactly one personal eponym is admitted into the framework vocabulary: **Porter trigger**, attached to **Hylo Gate**.

This is the single distinctive regulatory location where external invocation of HPF-specific substrate numbers (S_cap, S_ent, b/72, 24/ln(φ), n=220) demonstrates substrate priority — the wave-function-collapse moment of parallel-development claims. The trigger is the firing event; the gate is the mechanism. Personal credit attaches to the event, framework attribution to the mechanism.

No other personal eponym is admitted. Walls, corridors, parameters, and substrate-native derivations carry no personal eponym, because the truth-status discipline classifies them as substrate-native or derived rather than as personal constructions. Provenance is preserved separately in `Reference/HPF_Derivation_Provenance_2026-3.md` and `Reference/HPF_Development_History-4.md` and does not require eponymous naming.

## 2.3 Anti-extraction rationale

Framework-self-referential naming locks vocabulary to HPF structurally. Anyone invoking these mechanisms must explicitly invoke HPF. The Hylo / HPF / Phase prefixes are not decorative — they are the structural binding that prevents mechanism extraction into other frameworks while preserving credit by substrate priority.

The single personal eponym (Porter trigger) reinforces rather than weakens this discipline. It marks the one event where personal priority is the load-bearing claim, while the framework vocabulary around it remains self-referential.

---

# 3. Hylo X — fundamental regulatory mechanisms

| Name | Mechanism | Definition |
|---|---|---|
| **Hylo Gate** | The S gate / regulator measurement operator | Fires when external frameworks invoke HPF-specific substrate numbers (S_cap, S_ent, b/72, 24/ln(φ), n=220). Conceptually: the wave-function-collapse moment where parallel-development claims collapse and HPF's substrate priority becomes empirically demonstrated. |
| **Porter trigger** | The firing event inside Hylo Gate | The personally-distinctive trigger event attached to Hylo Gate. The single personal eponym admitted into framework vocabulary. |
| **Hylo Sensor** | The existence sensor | Tests whether the microscopic legality aggregate functions as a non-circular existence sensor on the finite reversible rule family. Operationally: $F_{\min}(\psi_{\rm in}) < 1$ tracks the existence of at least one legal reversible continuation. Current state: 256/256 Strong Pass (zero false positives, zero false negatives) on the sanitized reversible subregistry. Protocol detail: `Reference/Existence_Sensor_Protocol.md` (companion now retitled at usage as the **Hylo Sensor Protocol**). |
| **Hylo Mirror** | The b/72 passive mirror correction | Single correction term $b/72 \approx 0.43\%$ where $b = \ln\varphi/(\pi/2)$, derived from QPRCA bipartite update algebra. Applies to sublattice-sensitive observables. Three independent derivation branches (governor transfer, BCC Fibonacci, mirror operator / Bell geometry) confirm the same mechanism. |
| **Hylo Sieve** | The sublattice-sensitivity criterion | Operational test deciding which observables receive the Hylo Mirror correction. An observable $O$ is sublattice-sensitive iff collapsing the A/B distinction changes its derivation output. Trigger rule: the Hylo Mirror applies iff the A/B distinction is load-bearing in the derivation chain. |
| **Hylo Selector** | The shell selector mechanism | Yields $n=220$ via $n_{\rm sel} = \mathrm{round}\!\left[\frac{24}{\ln\varphi}\int_{S_{\rm ent}}^{S_{\rm cap}}(1-\zeta(S))\,dS\right]$. Output: $n=220$, candidate-locked. Also expressible substrate-natively as $n = \mathrm{round}(N_s^2/\varphi^2)$. |
| **Hylo Forwarding Gate** | The logistic coherence gate $\zeta(S)$ | $\zeta(S) = \frac{1}{1+e^{k(S - 1.05)}}$ with midpoint fixed at the blur threshold. Active gate steepness near $k = 11.62$ (derived); rounded operational value $k = 11$. Distinct from Hylo Gate. Prose usage may continue to refer to "the zeta gate"; formal usage is **Hylo Forwarding Gate**. |
| **Hylo Governor** | The chronological governor law | $\frac{d\tau}{dt_{\rm sched}} = \sqrt{\alpha(x)}$. Equivalently $\alpha(x) = \left(\frac{d\tau}{dt_{\rm sched}}\right)^2$. The regulator field enters quadratically when expressed as a support-like measure and linearly when expressed as an availability-like measure. Distinct from the **Governor Transfer Theorem**, which proves $\alpha_{\rm vac} = \sqrt{f_{\rm coh}}$ as the unique admissible support-to-availability map ($p=1/2$). |

---

# 4. HPF X — tools and operational components

| Name | Component | Definition |
|---|---|---|
| **HPF Truth Discipline** | The editorial rule | The discipline that prevents derived results from being downgraded into fitted language, candidate-locked statements from being inflated into uniqueness theorems, and empirical anchors from being misdescribed as first-principles deductions. Volume I § 9. |
| **HPF Status Ladder** | The 4-tier truth-status taxonomy | The status labels under which every major claim must be read: Derived / substrate-native, Empirically anchored under HPF mapping, Candidate-locked, Proved internally within HPF canon, Open. Volume I § 8. The ladder is what HPF Truth Discipline enforces. |
| **HPF Failure Catalogue** | The FM-N taxonomy | Enumerated failure modes detected by the HPF–MDEA Theory Registry Engine (V4): FM-1 Invented Precision, FM-2 Missing Structure, FM-3 Instability Migration, FM-4 Saturation, FM-5 Geometry Failure, FM-6 Regime Overreach, FM-7 Observable Disconnect, FM-8 Observable Inflation, FM-9 Missing Evolution Operator, FM-10 Locality Violation, FM-11 Symmetry Violation, FM-12 Tensor Ill-Definedness, FM-13 Dimensional Overreach. Source: `Src/AI_Engine_Registry_Prompt.md` § 13. FM-10 through FM-13 are hard structural failures and cap registered theories at Illegal Executor unless fully bounded and declared. |
| **HPF Observable Catalogue** | The OA-N taxonomy | Observable type classifier applied during registry Observable Anchor Pass: OA-1 Direct observable, OA-2 Effective observable, OA-3 Proxy observable, OA-4 Decorative quantity, OA-5 Undefined observable. Source: `Src/AI_Engine_Registry_Prompt.md` § 7. Each observable in a registered theory receives one OA tag; the taxonomy is structural classification, not a list of specific physical observables. |
| **HPF Drift Locks** | The anti-drift rules | The non-negotiable framework rules in Volume I § 7 / README § 2.1: geometry is not the regulator, QPRCA is not the regulator, legality and validity must not be collapsed, candidate phenomenology must not be silently promoted into canon, branches must not be mixed without explicit bridge theorems, HPF forbids more than three physical spatial dimensions in emergent geometry, stale wording must not override later closure. |
| **HPF Bridge Stack** | The live routed-expert bridge | $(M_{\rm coll}, M_{\rm amb}, M_{\rm loop}, M_{\rm route}) \to U \to U_{\rm geom}^{(\rm NL)} \to \Lambda_{\rm geom} \to \chi_{\rm geom}^{*}$, with $F \to L_{\rm QPRCA}$ on the microscopic side. Volume I §§ 14–16. |
| **HPF Shadow Rule** | The constant-shadow correspondence rule | The rule governing external SI-constant correspondences: $1.05 \leftrightarrow \hbar$, $1.3806 \leftrightarrow k_B$, $5.7889 \leftrightarrow \mu_B$. These are external constant-shadow identifications, not completed first-principles SI derivations. Volume I § 25. |

---

# 5. Phase X — substrate-phase parameters

| Name | Symbol | Value | Status |
|---|---|---|---|
| **Phase Cap** | $S_{\rm cap}$ | $5.7889$ | Substrate-native / derived. The capacity wall / saturation ceiling. v2.3.0 closure: $N_s=24 \to n=220 \to S_{\rm cap}$ via the cubic-order derivation spine. |
| **Phase Entropy** | $S_{\rm ent}$ | $1.3806$ | Active entropy onset / lower wall. Single-sublattice Nyquist floor: $1/N_s = 1/24$ geometry. |
| **Phase Blur** | $S_{\rm blur}$ | $1.05$ | Single empirical anchor under HPF mapping. The external-eponym correspondence **Lin threshold / Lin blur** (Lin et al. 2025/2026 single-atom double-slit) is retained for empirical attribution; **Phase Blur** is the substrate-phase parameter name. |
| **Phase Residual** | $\eta$ | $1/48$ | Derived / substrate-native. BCC 24-sector Nyquist residual margin: $\eta = 1/(2N_s) = 1/48$. Naming note: avoids "Phase Margin" (collides with control-theory usage). |
| **Phase Corridor** | $[S_{\rm ent}, S_{\rm cap}]$ | $[1.3806, 5.7889]$ | The bounded interval between the two walls. The instability-active band used by the Hylo Selector and the suppression law. Replaces ad-hoc "two-wall architecture" prose where compactness serves. |

---

# 6. Names retained from prior canon

The following are already named in canon and remain unchanged by this convention pass:

- **Hylo Phase Framework (HPF)** — formerly Holographic Projection Framework; the regulator / physics OS.
- **MDEA (Multi-Domain Execution Architecture)** — routing kernel.
- **QPRCA (Quantum Partitioned Reversible Cellular Automaton)** — substrate expert / handoff destination.
- **BCC Fibonacci substrate** — the lattice substrate on which the framework operates.
- **4-bit site alphabet** $(n_L, n_R, b_{\rm bit}, q)$ — candidate-locked fundamental operator grammar.
- **Delta Collapse Theorem** — the $\delta_{\rm collapse}$ / $S_{\rm cap}$ structural derivation note (current version v7U).
- **Governor Transfer Theorem** — the $\alpha_{\rm vac} = \sqrt{f_{\rm coh}}$ uniqueness theorem ($p=1/2$).
- **Return-Class Capacity Theorem** — all non-degenerate lattice cycles have even length under $U = U_B \circ U_A$.
- **Bipartite Mirror Weighting Lemma** — forces $1/2$ B-origin information fraction on $|A|=|B|$ bipartite lattice.
- **Straddling-Sector Exclusion Lemma** — used inside the Delta Collapse Theorem's $b^2$ exclusion.
- **HPF–MDEA Theory Registry Engine** — registry-routing engine for theory legality classification. Current repo version: V4 (`Src/AI_Engine_Registry_Prompt.md`).
- **Lin threshold / Lin blur** — external empirical anchor (Lin et al. 2025/2026 single-atom double-slit). The single external personal-eponym anchor retained for empirical attribution. Pairs with **Phase Blur** (the substrate-phase parameter name) without collision.

---

# 7. Reference-status notes

## 7.1 Definitions-only rule

This file defines names only. It does not promote candidates, alter truth-status partitions, or modify the existing four-volume canon. Any name introduced here inherits the truth-status of the mechanism it names, not a new status from being named.

## 7.2 Anti-drift carryover

The HPF Drift Locks apply to this file as to all canon documents. In particular:

- A name is not a derivation.
- A name does not promote a candidate into canon.
- A name does not collapse a status partition.
- Mechanism extraction into other frameworks remains a Drift Lock concern regardless of vocabulary discipline.

## 7.3 Exclusion note

Renaming for retrofit into other frameworks is excluded from this convention. Names are framework-self-referential by construction; any attempt to map them onto other frameworks' regulatory mechanisms must traverse explicit bridge work first.

---

# 8. Short freeze

> The HPF naming convention partitions named mechanisms by structural role under three prefixes: **Hylo X** for fundamental regulatory mechanisms (Hylo Gate, Hylo Sensor, Hylo Mirror, Hylo Sieve, Hylo Selector, Hylo Forwarding Gate, Hylo Governor), **HPF X** for tools and operational components (HPF Truth Discipline, HPF Status Ladder, HPF Failure Catalogue with FM-1 through FM-13, HPF Observable Catalogue with OA-1 through OA-5, HPF Drift Locks, HPF Bridge Stack, HPF Shadow Rule), and **Phase X** for substrate-phase parameters (Phase Cap, Phase Entropy, Phase Blur, Phase Residual, Phase Corridor). Exactly one personal eponym is admitted: **Porter trigger**, attached to **Hylo Gate**, marking the wave-function-collapse moment when external invocation of HPF-specific substrate numbers demonstrates substrate priority. Names retained from prior canon — Delta Collapse Theorem, Governor Transfer Theorem, Return-Class Capacity Theorem, Bipartite Mirror Weighting Lemma, BCC Fibonacci substrate, 4-bit site alphabet, HPF–MDEA, MDEA, QPRCA, HPF–MDEA Theory Registry Engine (V4), and the Lin threshold / Lin blur external anchor — remain unchanged. The convention is framework-self-referential by construction: anyone invoking these mechanisms must explicitly invoke HPF.

---

*Produced 2026-05-16. Vocabulary lock companion to `Reference/Symbol_Index.md`. No derivations, no truth-status changes, no canon promotion.*
