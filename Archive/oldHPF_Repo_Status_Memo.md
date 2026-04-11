# HPF Repo Status Memo — Keep / Supersede / Candidate Track

**Date:** 2026-04-01
**Source:** Cross-audit of older closure/geometry batch against current uploaded canonical package
**Purpose:** Single reference for what stays live, what is provenance only, and what is deliberately held as candidate track

---

## KEEP — Live Closure Stack

### 1. $B_{\rm cap} = 0.25\,M_{\rm cap}$
March 18 closure checkpoint correction. Preserves intended separation between transient overflow absorption and durable debt generation. Supersedes $0.15\,M_{\rm cap}$ in locked starter calibration. $D_{\rm cap} = 0.50\,M_{\rm cap}$ unchanged.

### 2. Sharpened Geometry Diagnostic $\chi^*_{\rm geom}$ — Live Starter
$$\chi^*_{\rm geom} = (1-\gamma)\chi_{\rm lin} + \gamma\chi_{\rm dom}$$
Starter calibration:
$$w_B = 0.30,\quad w_A = 0.25,\quad w_D = 0.45,\quad \gamma = 0.50$$
Status: operational/coarse-grained starter diagnostic. Not constitutive.

### 3. Quartet Closure-Demand Law — Candidate-Locked Form
$$M_{\rm req} = M_{\rm coll} + M_{\rm amb} + M_{\rm loop} + M_{\rm route}$$
Use the quartet-locked master spec only. All older "loop open / route open" wording is stale.

### 4. Exact Primitive/Derived Hierarchy
Geometry is not an independent primitive substrate sector. $U$, $R$, and related closure diagnostics are derived, not primitive law. This correction must remain visible in the package.

### 5. Subordinate $F(x)$ Interface
$F$ is a regulatory interface subordinate to the exact sector law. Not the sovereign object. Checkpoint version preserved.

### 6. Candidate $R_{\rm debt}$ / Debt-Evolution Detail
Keep debt-stock evolution note as checkpoint detail. Not promoted to primitive law. Retained as explicit useful piece.

---

## KEEP — Active Gravity Material

### 7. Substrate-to-Geometry Bridge Chain
Full coarse-grained bridge:
- load-to-stress mapping
- blocked coarse-graining
- running coupling
- fluctuation suppression
- weak-field normalization

### 8. Weak-Field Einstein Normalization / $\kappa$ Derivation
Weak-load matching result fixing Einstein coupling in the geometry expert. Preserved and active.

### 9. Gravity Extensions
Vector-sector, rotating-source (Kerr-like), interior gravity, gravitomagnetic extensions. Active geometry-expert material. Not discard.

---

## KEEP — Active Substrate / Architecture Material

### 10. Candidate Substrate Note
BCC as registry-derived working default, not HPF axiom. Repo-worthy supporting architecture. *(Tightened 2026-04-01.)*

### 11. Bell-State / Admissible Substrate-Class Note
Bell constraints support reversible QCA-style substrate class. Not BCC uniqueness. Supporting architecture. *(Tightened 2026-04-01.)*

### 12. Regulated Single-Dirac QPRCA/BCC Substrate Line
Reversible BCC/QPRCA single-Dirac construction. Preserved substrate architecture.

---

## CANDIDATE TRACKS — Keep Deliberately, Do Not Promote

### 13. Photon-Ring Candidate Note
Three isolated obligations:
1. Forwarding-identification bridge
2. Radial blur displacement law
3. Mode-indexing / reflection bridge

Status: candidate only. Do not promote until all three closed. *(Frozen 2026-04-01.)*

### 14. Vacuum Catastrophe Candidate Note
Core claim: QFT vacuum catastrophe is effective-theory overcount. $L_{vac}$ is the regulated substrate scale. Physical cosmological branch is $L_{vac} \to \Lambda$. Three obligations open. DM branch mixing prohibited until bridge derived. Stochastic-jitter phenomenology has been explicitly split to a separate candidate note. *(Built 2026-04-01.)*

### 15. Gauge-Complete Regulated QPRCA Line
Separate candidate track. Real content: exact gauged update, current, continuity, holonomy/field strength, discrete Maxwell structure, saturation bounds. **Do not merge into active canon until rewritten against exact-sector corrections.** Hold as candidate track.

### 16. Stochastic Jitter Falsifier Candidate Note
Core claim: finite scheduler discreteness and vacuum transport granularity may produce an irreducible propagation-induced arrival-time broadening floor for high-energy photons over long baselines. Preferred candidate branch is stochastic broadening,
\[
\sigma_t \sim \sqrt{N_{\rm eff}}\,t_{sched}
=
\sqrt{N_{\rm eff}}\,\frac{L_{vac}}{c},
\]
with regime gating by the common spine \(\{S_{\rm blur},\eta,b\}\). Separate from the vacuum-catastrophe note and separate from the active \(\Lambda\)/DM branch. Do not promote until the \(\sqrt{N}\) branch, \(N_{\rm eff}\), and the gate law are derived.

---

## SUPERSEDED — Provenance Only

### 17. Equal-Weight Geometry Metric
$$\chi_{\rm geom} = \frac{\bar{B} + \bar{A} + \bar{D}}{3}$$
Superseded by $\chi^*_{\rm geom}$. Diluted catastrophic single-channel persistence. Provenance only.

### 18. All "$M_{\rm route}$ Remains Open" Wording
Any older master-spec file still marking $M_{\rm loop}$ or $M_{\rm route}$ as open is stale under the quartet-locked spec. Provenance only.

### 19. Unified Saturation Notes with $\sigma_{\rm geom}$ as Peer Primitive
Old unified saturation/backreaction notes treating $\sigma_{\rm geom}$ as peer primitive sector are obsolete under exact-sector correction. Provenance only. Do not recover verbatim.

### 20. Old Phenomenology File / Old Mind-Map
Stale: older $L_{vac}$ values, older thresholds, older interpretive language. Provenance only. Do not recover.

---

## RECOVERED — Compact MDEA Architecture Law

From older closure batch. Cleanest compact statement of the HPF/MDEA execution law identified in audit. Keep visible in active package.

$$E^*(X_t) = \arg\max_{E \in \mathcal{E},\; L_{\rm HPF}(E,X_t)=1} V_{\rm HPF}(E,X_t), \qquad X_{t+1} = F_{E^*(X_t)}(X_t)$$

**What this states:**
- $X_t$ — current state
- $\mathcal{E}$ — expert set (GR, QFT, semiclassical, QPRCA, related regimes)
- $L_{\rm HPF}(E, X_t) = 1$ — legality gate; illegal experts are excluded before validity scoring
- $V_{\rm HPF}(E, X_t)$ — validity score; maximized over the legal subset
- $F_{E^*}$ — reversible update operator of the selected expert

**Ordering:** legality is prior, not co-equal. The argmax runs only over the legal subset. Among legal experts, validity scoring selects.

**Status:** Compact architecture law. Keeper. Replaces older cluttered gate prose and the sloppy $\arg\max(V, L)$ pair form in older files.

**Note on old form:** The older $\arg\max\big(V_{\rm HPF}(E,X_t), L_{\rm HPF}(E,X_t)\big)$ reads as a max over a pair — ambiguous and mathematically sloppy. The constrained form above is the correct reading and should replace it wherever it appears.



| Category | Items |
|---|---|
| Live closure stack | $B_{\rm cap}=0.25$, $\chi^*_{\rm geom}$ starter, quartet law, primitive/derived hierarchy, subordinate $F$, debt detail |
| Active gravity | Bridge chain, $\kappa$ derivation, gravity extensions |
| Active substrate/architecture | Candidate substrate note, Bell/QCA-class note, single-Dirac BCC/QPRCA |
| Candidate tracks (hold) | Photon ring, vacuum catastrophe, stochastic jitter, gauge-complete QPRCA |
| Superseded | Equal-weight $\chi_{\rm geom}$, open-route wording, $\sigma_{\rm geom}$-as-primitive, old phenom file |

---

*This memo supersedes ad hoc status calls across older files. Apply before next canonical package update.*
