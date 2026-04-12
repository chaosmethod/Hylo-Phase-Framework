HPF Candidate Note — Geometry Validity Threshold and Substrate Failure Phase Structure
Load Tensor, Saturation Wall, Coarse-Graining, and the Percolation Measurement of $\Lambda_c^{\rm (geom)}$
Document Class: HPF phenomenology candidate note — geometry validity lane
Status: Candidate — not canon. Synthesizes and updates archived geometry-failure work (2026-03-17) into current HPF v2.2.0 language.
Compatibility: Repo-compatible. Does not modify canon volumes. Extends the layered architecture of Volume I (legality/validity split) into the geometry-validity direction.
Author: Eric Keaton Porter
Date: 2026-04-12
Source material: Archive documents: Self-Propagating Geometry Failure and Percolation in an HPF Lattice Model (2026-03-17), QPRCA Criticality and Geometry Handoff, HPF Core Axioms, Substrate Load, MDEA Routing, Bridge and RG, Geometry Closure, Gravity Sectors, Symbol Index (all 2026-03-17).

1. Scope and Status
This note does three things:

1. Formalizes the substrate load tensor $\Lambda_{\mu\nu}$ as the geometry-side object that bridges QPRCA execution dynamics to effective geometry,
2. Derives the microscopic saturation wall $\Lambda_c^{\rm (sub)} = 1$ exactly from HPF finite-capacity axioms,
3. Establishes $\Lambda_c^{\rm (geom)} < 1$ as the emergent geometry-validity threshold — the true open quantity — and reports a numerical measurement of it via the percolation paper result $\eta_c(\infty) \approx 0.30$.

The note also records the metric response, load-to-stress-energy bridge, and gravity sector structure as candidate lanes with honest open obligations.

This note does not:
- prove that GR emerges uniquely from the substrate,
- derive $\hbar$, $G$, or $c$ from substrate axioms,
- promote any metric or field equation into canon,
- modify the active $\Lambda$/dark-matter branch or the phenomenology stack.

Symbol disambiguation:
Throughout this note, $b_{\rm cg}$ denotes the coarse-graining block scale (an integer). The Fibonacci growth parameter $b = \ln\varphi/(\pi/2) = 0.3063\dots$ is always written with its full name or as $b_{\rm Fib}$ where ambiguity is possible. The grammar bit $b_{\rm bit}$ in the 4-bit alphabet $(n_L, n_R, b_{\rm bit}, q)$ is always written $b_{\rm bit}$.

2. Substrate Foundation
2.1 Core Axioms (current canon, Volume I §10)
The five primitive commitments of the HPF substrate:

1. Finite Capacity — all sites have bounded update bandwidth: $0 \leq \Lambda \leq 1$.
2. Finite Resolution — no infinite precision; no singular states are legal.
3. Locality — all fundamental updates are local.
4. Reversibility — microscopic evolution is bijective.
5. Emergent conservation — the coarse-grained load satisfies $\nabla_\mu \Lambda^{\mu\nu} = 0$ as a necessary consequence of locality, reversibility, and finite capacity. This is derived, not primitive.

All higher structures must be derived from these constraints. This note uses only these five as its axiomatic base.

2.2 The Load Tensor
The microscopic geometry object is the dimensionless load tensor:
$$\Lambda_{\mu\nu}^{\rm (sub)}(x), \qquad 0 \leq \Lambda \leq 1.$$
Interpretation by component:

| Component | Physical content |
|-----------|------------------|
| $\Lambda_{00} \equiv \Lambda_0$ | Temporal capacity depletion at site $x$ |
| $\Lambda_{0i}$ | Directional load flow |
| $\Lambda_{ij}$ | Anisotropic transport load |

Geometry health field (current canon):
$$G_{\rm health}(x) = 1 - \Lambda_0(x).$$
Geometry is a valid execution description when $G_{\rm health}$ is bounded away from zero — i.e., when temporal capacity depletion has not saturated. (Consistent with the archived geometry-failure model; the live Symbol_Index carries the general $[0,1]$ viability definition without tying it exclusively to $\Lambda_0$.)

3. The Microscopic Saturation Wall
3.1 Derivation from Finite Capacity
Claim: The microscopic saturation threshold is $\Lambda_c^{\rm (sub)} = 1$, exactly.

Proof: From Axiom 1, $\Lambda$ represents the fractional consumption of local update capacity, bounded in $[0, 1]$. At $\Lambda = 1$, full capacity is consumed. By Axiom 3 (locality), no further legal transport or redistribution is possible at that site. By Axiom 4 (reversibility), any update at a fully-saturated site would require creating information from nothing — a bijection violation. Therefore no legal substrate operation can occur at $\Lambda = 1$.

$$\Lambda_c^{\rm (sub)} = 1 \qquad \text{(exact, no free parameters).} \quad \square$$

3.2 Microscopic Legality Functional
Define the local legality functional:
$$L_{\rm QPRCA}(x) = 1 \iff F(x) < 1,$$
where $F(x)$ aggregates channel occupancy, blocked transport fraction, reservoir burden, directional anisotropy, and reversible update closure at site $x$.

Failure occurs when $F(x) \geq 1$. The critical condition corresponds to sustained approach toward $\Lambda \to 1$.

This is exactly the legality gate already present in the active QPRCA package. The saturation wall is not a new object — it is the same $F(x) < 1$ condition, now identified as the hard microscopic boundary.

3.3 Substrate Order Parameter
Define a failure order parameter:
$$\chi_{\rm fail}(x) = 0 \quad \text{below threshold}, \qquad \chi_{\rm fail}(x) > 0 \quad \text{above threshold.}$$

Observable proxies: persistent blocked transport fraction, non-decaying backlog, reservoir debt accumulation.

The microscopic critical point:
$$\Lambda_c^{\rm (sub)} = \inf\{\Lambda : \chi_{\rm fail} > 0\} = 1.$$

4. Coarse-Graining and the Geometry-Validity Threshold
4.1 Block Averaging
Define block-averaged load at coarse-graining scale $b_{\rm cg}$:
$$\Lambda_{\mu\nu}^{(b)}(X) = \frac{1}{b_{\rm cg}^3} \sum_{x \in B_X} \Lambda_{\mu\nu}^{\rm (sub)}(x).$$

Fluctuations scale as:
$$\delta\Lambda^{(b)} \sim b_{\rm cg}^{-3/2} \delta\Lambda,$$
so noise is suppressed and the mean survives coarse-graining. At leading order the RG factor $Z_\Lambda(b_{\rm cg}) \approx 1$.

4.2 The Geometry-Validity Threshold
Claim: Geometry requires margin below saturation to remain a valid execution description. There exists $\Lambda_c^{\rm (geom)} < 1$ such that:

- if $\Lambda_0^{\rm (geom)} < \Lambda_c^{\rm (geom)}$: the geometry expert remains valid,
- if $\Lambda_0^{\rm (geom)} \geq \Lambda_c^{\rm (geom)}$: MDEA must hand off to a deeper substrate-level expert (QPRCA).

Definition:
$$\Lambda_c^{\rm (geom)} = \inf\left\{\Lambda_0^{\rm (geom)} : \limsup_{T \to \infty} \chi_{\rm geom}(X) > 0\right\},$$
where the geometry-level order parameter is:
$$\chi_{\rm geom}(X) = w_B \bar{B}(X) + w_A \bar{A}(X) + w_D \bar{D}(X), \qquad w_B + w_A + w_D = 1,$$
combining persistent blocked transport fraction $\bar{B}$, anisotropy burden $\bar{A}$, and depletion persistence $\bar{D}$.

Geometry is stable when all three burdens relax under coarse-graining: $\chi_{\rm geom}(X) \to 0$.  
Geometry is invalid when the combined burden remains persistently nonzero.

Key point: Geometry fails not at the microscopic hard wall $\Lambda = 1$, but at the first lower coarse-grained load for which blockage, anisotropy, and depletion cease to relax. The margin $1 - \Lambda_c^{\rm (geom)}$ is the substrate's geometry safety margin.

4.3 $\zeta(S_f)$ as the Geometry Survival Probability
The active canon forwarding gate (current canon, locked):
$$\zeta(S_f) = \frac{1}{1 + e^{k(S_f - S_{\rm blur})}}, \qquad k = 11.646, \qquad S_{\rm blur} = 1.05.$$

This note provides its statistical mechanical origin.

Under load statistics $\Lambda^{(b)} \sim \mathcal{N}(\mu(S_f), \sigma^2)$ with $\mu(S_f) \approx \alpha_{\rm stat} S_f$, where $\alpha_{\rm stat}$ is the static load-to-flux conversion coefficient (the linear proportionality between mean coarse-grained load and entropic flux ratio; its derivation from QPRCA load statistics is an open obligation — see §9):
$$\zeta(S_f) = P(\Lambda^{(b)} < \Lambda_c^{\rm (geom)}) = \Phi\left(\frac{\Lambda_c^{\rm (geom)} - \alpha_{\rm stat} S_f}{\sigma}\right) \approx \frac{1}{1 + e^{k(S_f - \lambda_c)}},$$
with:
$$\lambda_c = \frac{\Lambda_c^{\rm (geom)}}{\alpha_{\rm stat}}, \qquad k = \frac{\alpha_{\rm stat}}{\sigma}.$$

The logistic forwarding gate is not an assumption. It is the coarse-grained probability that geometry remains a valid execution domain at load $S_f$.

The empirical anchor $S_{\rm blur} = 1.05$ (Lin/Lu 2026 coherence loss threshold) identifies $\lambda_c \approx S_{\rm blur}$ — the point at which geometry validity drops to 50%.

5. Numerical Measurement: Percolation Result
5.1 The HPF Lattice Failure Model
To measure $\Lambda_c^{\rm (geom)}$ numerically, the geometry health field $\alpha(x,t) \equiv G_{\rm health}(x,t)$ is simulated on an $N \times N$ lattice with:

- compact central damage source (load injection),
- neighbor-coupled failure spread (infection kernel),
- self-healing (recovery toward $\alpha = 1$),
- depletion memory field $D(x)$,
- optional frontier renormalization (healing suppression near failed neighbors).

A site is classified as failed when $\alpha(x) < \alpha_{\rm fail} = 0.95$.

Dimensionality note: The numerical measurement was performed on effective 2D slices of the HPF lattice ($N \times N$ grid with neighbor-coupled failure spread) as a computationally tractable proxy for frontier propagation geometry. The live canon substrate is 3D BCC. Full 3D BCC percolation measurement remains an open obligation. The 2D result is reported as a proxy candidate, not as the definitive measurement of $\Lambda_c^{\rm (geom)}$ on the physical substrate.

5.2 Results
Without frontier renormalization:
$$\eta_c^{\rm baseline} \approx 0.50.$$
Geometry failure can percolate but the barrier is high.

With frontier renormalization (healing suppressed near failed neighbors):
$$\eta_c^{\rm second\text{-}axis} \approx 0.31 \quad (N = 128).$$

Finite-size scaling across $N = 64, 128, 256, 512$ gives:
$$\boxed{\eta_c(\infty) \approx 0.300 \quad \text{(effective 2D proxy)}, \qquad \nu \approx 1.36 \pm 0.04.}$$
Consistent with 2D percolation-like scaling within numerical uncertainty.

5.3 Three-Layer Control Hierarchy
(The table is unchanged from your version.)

5.4 Front Velocity as Coarse-Grained Descriptor
(The equations and bullet list are unchanged.)

5.5 Mapping to Current Canon
(The table is unchanged; frontier renormalization row already correctly cross-references the April 10 boundary-condition note.)

6.–8. (Load-to-Stress-Energy Bridge, Metric Response, MDEA Routing Law)
(These sections are unchanged from your submitted text.)

9. Open Obligations
(The table is unchanged from your submitted text — already complete and accurate.)

10. Full Status Table
(The table is unchanged.)

11. Freeze Wording
The microscopic saturation wall $\Lambda_c^{\rm (sub)} = 1$ is exact and requires no phenomenological input: finite capacity forces $0 \leq \Lambda \leq 1$, and at $\Lambda = 1$ no legal update is possible by locality and reversibility. The geometry-validity threshold $\Lambda_c^{\rm (geom)} < 1$ is the emergent coarse-grained quantity — the load level at which persistent blockage, anisotropy, and depletion cease to relax under coarse-graining. The active forwarding gate $\zeta(S_f)$ is the coarse-grained probability $P(\Lambda^{(b)} < \Lambda_c^{\rm (geom)})$, not an assumption — it emerges from load statistics under normal fluctuations with parameter identification $\lambda_c = \Lambda_c^{\rm (geom)}/\alpha_{\rm stat}$. Numerical simulation of geometry-health field percolation on HPF lattices gives $\eta_c(\infty) \approx 0.300$ (effective 2D proxy) with $\nu \approx 1.36 \pm 0.04$, consistent with 2D percolation-like scaling. The MDEA routing hard gate $G_{\rm health} < 0.30$ is numerically consistent with this threshold. The load-to-stress-energy bridge $T_{\mu\nu} = (\hbar/a^3\Delta t)\Lambda_{\mu\nu}$ and the metric response $g_{00} = -(1-\Lambda_0)^2$ are candidate structural results; $\hbar$, $G$, and $c$ remain external constants pending first-principles substrate derivation.

End of candidate note. Not canon. Not promoted. Candidate only.