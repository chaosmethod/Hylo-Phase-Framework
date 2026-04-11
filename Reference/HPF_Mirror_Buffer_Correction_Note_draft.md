# HPF Candidate Note — Passive Mirror Buffer Correction
## The 0.5% Systematic Gap and Its Proposed Substrate Origin

**Document Class:** HPF candidate working note  
**Status:** Candidate — proposed. Not yet closed. For review and stress-test.  
**Author:** Eric Keaton Porter  
**Date:** 2026-04-10

---

# Part I — The Problem

## 1. A Systematic Residual Across Two Independent Branches

The current HPF package carries two observational gaps that have not been
explained by the active derivation chain.

### 1.1 Dark matter fraction

The governor-transfer branch produces:

$$\Omega_{\rm dm} = 1 - \alpha_{\rm vac} = 26.29\%$$

The observed value is approximately $26.8\%$.

Gap: $0.51\%$

### 1.2 Neutrino mass-squared ratio

The BCC Fibonacci indexing branch produces:

$$\frac{\Delta m^2_{31}}{\Delta m^2_{21}} = F(9) = 34$$

The observed value from NuFit 6.0 is $33.831$.

Gap: $0.49\%$

### 1.3 The pattern

These two gaps are:

- nearly identical in magnitude ($\approx 0.5\%$),
- produced by entirely independent derivation branches,
- both connected to BCC lattice geometry,
- both ratio-type or fractional observables sensitive to local substrate
  load rather than global geometric identities.

A systematic residual of consistent magnitude appearing across two
independent branches is not coincidence. It points to a single
geometric effect that both derivations are missing.

---

## 2. Why the Current Package Does Not Already Account for It

The BCC bipartite mirror structure is already present in the package
through the $\kappa_{\rm BCC}$ coefficient:

$$\kappa_{\rm BCC} = 8 \times \frac{1}{2} \times \frac{1}{2} = 2$$

The two $\frac{1}{2}$ factors are the bipartite split and the LMS mirror
factor respectively.

The $/2$ radial correction was previously removed from the vacuum-sector
radial law because it was being double-counted in a global geometric
identity. That removal was correct.

However, removing the $/2$ from the radial law does not make the mirror
geometry disappear. The BCC substrate is always bipartite. The scheduler
always alternates between A and B sublattices. The mirror is a permanent
geometric fact of the substrate whether or not a given derivation
explicitly invokes it.

The question the current package has not answered is:

> Does the bipartite mirror contribute a passive systematic offset to
> observables that are sensitive to sublattice-level sampling, even when
> the derivation does not reach for it?

The radial law is a global identity spanning both sublattices
simultaneously — the mirror correctly cancels there.

The dark matter fraction and the neutrino ratio are both local load
measurements. They sample the substrate at a scale where the A/B
alternation has not averaged out. These are precisely the observables
where a passive mirror buffer would show up as a residual offset.

---

## 3. The Gap Has No Current Explanation in the Package

The active package does not contain:

- a derivation of why both gaps are $\approx 0.5\%$,
- a correction term that accounts for the bipartite buffer in
  sublattice-sensitive observables,
- a connection between the lattice mirror geometry and the quantum
  entanglement ½ factor.

This is the open problem this note addresses.

---

# Part II — The Proposed Solution

## 4. The Physical Argument

### 4.1 The mirror path geometry

On a BCC bipartite substrate, when an excitation propagates to a
neighboring site, the mirror image of that excitation does not travel
the full return path. It meets the forward excitation at the midpoint.

The physical path is therefore:

- Forward leg: 1 full lattice node length
- Mirror return: $\frac{1}{2}$ node length

Total effective path: $1 + \frac{1}{2} = \frac{3}{2}$ node lengths.

This is not a correction that is applied actively by any rule in the
derivation. It is a passive geometric property of the bipartite
structure — the mirror image is always present, always returning at
half the node length, regardless of whether the derivation that produces
the observable accounts for it.

### 4.2 The connection to quantum entanglement

The same geometry explains the $\frac{1}{2}$ factor in quantum
entanglement. Entangled particles are not two independent objects
traveling apart from each other. They are one substrate object and its
mirror image. The mirror does not need to travel the full separation
distance — it meets at the midpoint.

The entanglement ½ factor and the lattice mirror buffer are the same
geometric object viewed from different scales. This is an internal
consistency of the substrate picture, not an additional assumption.

---

## 5. The Proposed Correction Term

### 5.1 Derivation of $\eta_{\rm passive}$

The active Nyquist residual is derived as:

$$\eta = \frac{1}{2 \times 24} = \frac{1}{48}$$

The factor of 2 reflects full two-sample-per-cycle Nyquist resolution
across both sublattices.

For a passive mirror buffer, the effective sampling multiplier is not 2
but $\frac{3}{2}$, because the mirror contributes one half-node passively
rather than a full return pass:

$$\eta_{\rm passive} = \frac{1}{\frac{3}{2} \times 48} = \frac{1}{72}$$

### 5.2 The correction magnitude

The passive mirror correction enters sublattice-sensitive observables
as:

$$\delta_{\rm mirror} = \frac{b}{72}$$

where $b = \ln\varphi/(\pi/2) = 0.3063489625$ is the Fibonacci growth
parameter already present in the package.

Numerically:

$$\frac{b}{72} = \frac{0.3063489625}{72} = 0.004254$$

As a fractional correction this is $\approx 0.43\%$ to $0.49\%$
depending on the observable scale — consistent with both observed gaps.

### 5.3 Cross-check against the two gaps

**Dark matter fraction:**

$$\Omega_{\rm dm}^{\rm corrected} = 26.29\% + \delta_{\rm mirror}
= 26.29\% + 0.4254\% = 26.715\%$$

Observed: $26.8\%$. Remaining gap after correction: $0.085\%$.

**Neutrino ratio:**

The raw gap in ratio units is $34 - 33.831 = 0.169$.

The correction $b/72 \times 34 \approx 0.1446$ accounts for the
bulk of the gap. Remaining gap: $0.0244$, or $0.07\%$.

Both residuals after correction drop from $\approx 0.5\%$ to
$\approx 0.08\%$ — an order of magnitude improvement using a single
correction term derived from the same substrate geometry.

---

## 6. Why This Is Structurally Native

The correction term $b/72$ uses only objects already present in the
live package:

- $b$: the Fibonacci growth parameter, substrate-native
- $72 = \frac{3}{2} \times 48$: the passive mirror Nyquist factor,
  derived from the $\frac{3}{2}$ path geometry and the active sector
  count 24
- The $\frac{3}{2}$ path itself: derived from the bipartite forward-plus-half-return
  mirror geometry

No external fit parameter is introduced.

---

## 7. What Remains Open

This note is a proposed solution, not a closed derivation. The
following obligations are open:

### Obligation 1 — formal derivation of the $\frac{3}{2}$ path factor

The physical argument for $1 + \frac{1}{2}$ node lengths is stated
here in geometric prose. A formal derivation in QPRCA update language
— showing that the bipartite scheduler produces exactly this effective
path length for sublattice-sensitive observables — is not yet written.

### Obligation 2 — derive the application rule

The correction applies to sublattice-sensitive observables but not to
global geometric identities like the radial law. The formal criterion
for which observables receive the passive mirror correction needs to be
derived, not just identified by pattern-matching.

### Obligation 3 — verify against additional observables

The correction has been checked against two gaps. A third independent
sublattice-sensitive observable would strengthen or falsify the proposal.

---

## 8. Falsifiability

This candidate is falsified if:

1. A formal QPRCA derivation of the bipartite update schedule produces
   an effective mirror path length other than $\frac{3}{2}$ node lengths.
2. The criterion for sublattice-sensitive observables, once formally
   derived, excludes either the dark matter fraction or the neutrino ratio.
3. A third sublattice-sensitive observable shows a gap inconsistent with
   $b/72$.

---

## 9. Freeze wording

> The HPF package carries a consistent $\approx 0.5\%$ residual gap
> across two independent branches: the dark matter fraction
> ($\Omega_{\rm dm} = 26.29\%$ vs $26.8\%$) and the neutrino
> mass-squared ratio ($F(9)=34$ vs $33.831$). Both are sublattice-sensitive
> observables on the BCC bipartite substrate. The proposed explanation is
> a passive mirror buffer correction of $b/72$, arising from the
> $\frac{3}{2}$-node effective path geometry of the bipartite mirror:
> one forward node length plus one half-node mirror return. This is the
> same geometry as the quantum entanglement $\frac{1}{2}$ factor —
> entangled states are one substrate object and its mirror image meeting
> at the midpoint. The correction term is substrate-native (no free
> parameters), reduces both gaps by an order of magnitude, and connects
> the lattice mirror geometry to quantum entanglement from the substrate
> up. Three obligations remain open: formal QPRCA derivation of the
> $\frac{3}{2}$ path factor, derivation of the application criterion for
> sublattice-sensitive observables, and verification against a third
> independent observable.
