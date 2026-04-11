# Lattice Mirror Symmetry (LMS) — Updated Candidate Note

**Document Class:** HPF phenomenology candidate note
**Status:** Candidate — not canon. One obligation open.
**Compatibility:** Repo-compatible. Consistent with Volume IV active package.
**Author:** Eric Keaton Porter
**Date:** 2026-04-04

---

## Abstract

Lattice Mirror Symmetry (LMS) identifies quantum entanglement as a single informational structure viewed from dual lattice angles. This provides a local-substrate explanation for Einstein's "spooky action at a distance" without invoking nonlocal signaling.

This version replaces the decapitated mirror-reflection derivation of the 1/2 factor with a substrate-native derivation. The 1/2 in the weak-field metric is the GR-phase expression of symmetric round-trip substrate accounting at the $L_{vac}$ resolution scale. Because $L_{vac}$ is universal — every object is equidistant from the substrate — the two legs of any metric measurement are always equal, and the observer always catches exactly half the total exchange. The bipartite sublattice structure of the BCC substrate and the round-trip accounting are two descriptions of the same geometric fact.

---

## Locked Inputs From Active Package

| Input | Value | Status |
|---|---|---|
| $L_{vac} = R_H / \phi^n$ | $n = 220$, $L_{vac} \approx 1.45 \times 10^{-20}$ m | Candidate-locked, active canon |
| $S_{\rm blur} = 1.05$ | Decoherence boundary | Locked empirical anchor |
| $S_{\rm cap} = 5.7889$ | Saturation ceiling | Locked |
| No $/2$ in radial law | Explicit March 29 correction | Locked |
| BCC bipartite structure | A-sublattice / B-sublattice | Candidate-strong, active canon |

---

## 1. Entanglement as Substrate Unity

In HPF, entangled particles are not independent objects exchanging nonlocal signals. They are subsystems of a single globally evolving lattice state.

The BCC substrate is bipartite — partitioned into two disjoint sublattices:

```
A-sublattice
B-sublattice
```

All nearest-neighbor interactions connect A to B and B to A. No A-to-A or B-to-B direct interactions exist at the primitive level.

Entangled particles share the same substrate update logic. Their apparent spatial separation is a projection effect — they occupy different lattice positions but remain one informational structure at the substrate level. Measurements reveal correlations already encoded in the substrate rather than creating them through superluminal interactions.

**Status:** Substrate-native. Consistent with Bell-State Constraints note. Not dependent on the 1/2 factor derivation.

---

## 2. The Substrate-Native Derivation of the 1/2 Factor

### 2.1 The round-trip accounting argument

Any metric measurement made by an internal observer is one leg of a two-leg lattice exchange:

1. The object warps the substrate outward at the $L_{vac}$ resolution scale.
2. The substrate returns that warp to the observer at the same $L_{vac}$ resolution scale.

The observer catches only the return leg — half the total exchange.

### 2.2 Why the two legs are always equal

Every object sits on the substrate at the $L_{vac}$ resolution scale. There is no object closer to or further from the lattice than any other — the substrate is the universal medium everything exists in. The outbound and return legs are therefore structurally identical by construction.

Symmetry is not assumed. It is a consequence of $L_{vac}$ being universal.

### 2.3 The bipartite equivalence

The bipartite sublattice structure and the round-trip accounting are two descriptions of the same geometric fact:

- A-sublattice → substrate → B-sublattice is the outbound leg
- B-sublattice → substrate → A-sublattice is the return leg

An observer on A always measures B through the substrate and receives the return through the substrate. The bipartite handoff IS the round trip.

### 2.4 The metric consequence

In the GR-phase (Einstein phase, $S_f < 1.4$), this substrate-native 1/2 expresses itself as the familiar weak-field metric factor:

$$g_{tt} \approx 1 + \frac{1}{2}\frac{R_s}{r}$$

The 1/2 is not a GR assumption. It is the GR-phase expression of symmetric round-trip substrate accounting at $L_{vac}$.

**Status:** Candidate. The round-trip argument is substrate-native and closes the main attack surface via the universality of $L_{vac}$. One obligation remains — see Section 4.

---

## 3. Three Levels of Substrate Locality

The LMS framework distinguishes three physically distinct regimes of lattice interaction — not a continuum, but three categorically different relationships between objects and the substrate.

### 3.1 Local — object to adjacent lattice site

Rate is $c$. One scheduler tick, one bipartite handoff. The (1/2) per leg operates at the substrate's own clock rate. This is the primitive update event from which all other interactions are built.

### 3.2 Non-local propagation — light travel across distance

A photon carries a record of a lattice event across a spatial separation. The 8-minute travel time from Sun to Earth is simply the number of scheduler ticks required for the record to traverse the intervening lattice sites. The Sun's lattice event already occurred. The observer receives the record late. This is not time travel — it is the substrate communicating with itself across a delay determined entirely by tick count and geometry. $c$ governs the per-tick rate; distance governs the total tick count.

### 3.3 Quantum entanglement — object distance to the lattice

Entanglement is not propagation. An entangled pair is a single informational structure held in the substrate. The apparent 3D spatial separation between the two particles is irrelevant at the substrate level because what matters is the distance between each particle and the lattice itself — which is $L_{vac}$, universal and identical for all objects everywhere.

There is no signal traveling between entangled particles. The lattice already holds both states as one object. Measurement on one reveals the other without delay because there is no substrate gap between them — both are equidistant from the lattice at $L_{vac}$, and the lattice holds their joint state as a single entry.

Entanglement is therefore not faster-than-light signaling. It is not in the same category as propagation at all. It is a different kind of substrate relationship: the object's distance to the lattice, not the object's distance to another object.

**Summary table:**

| Regime | What travels | Rate | Delay | Substrate mechanism |
|---|---|---|---|---|
| Local update | Bipartite handoff | $c$ | One tick | A → B or B → A |
| Non-local propagation | Lattice record (photon) | $c$ | Distance / $c$ | Sequential tick chain |
| Entanglement | Nothing | — | Zero | Single substrate object at $L_{vac}$ |

---

## 4. Decoherence and Entanglement Load

Maintaining the shared substrate state across a lattice is an active execution cost.

**Entanglement load** ($L_{ent}$): Consumes a portion of the local update capacity $\alpha$.

**Saturation trigger:** When local entropic flux $S_f$ exceeds $S_{\rm blur} = 1.05$, the scheduler begins losing coherent resolution. When $S_f$ exceeds $S_{\rm cap} = 5.7889$, the scheduler can no longer sustain the shared state.

**Mandatory handoff:** To preserve fundamental reversibility, HPF forces state partitioning, producing the observable loss of nonlocal correlation — decoherence.

Decoherence is therefore not a fundamental collapse. It is a routing event: the substrate hands off to a lower-coherence execution mode when the entanglement load exceeds available update capacity.

**Status:** Substrate-native. Consistent with Chronological Governor and Cyclic Reinitialization documents.

---

## 4. Open Obligation

### Obligation 1: Derive the metric factor formally from round-trip accounting

**Target:** Show formally that the round-trip substrate accounting at $L_{vac}$ produces exactly the 1/2 coefficient in the weak-field metric, rather than demonstrating it through geometric argument alone.

**What is needed:** A derivation showing that the two-leg exchange at $L_{vac}$ resolution, under the BCC bipartite update schedule, produces the correct Schwarzschild weak-field limit with the 1/2 coefficient as a substrate output rather than a GR input.

**Status:** Open. The geometric argument is strong and substrate-native. The formal derivation connecting $L_{vac}$ round-trip accounting to the metric coefficient is the remaining closure step.

---

## 5. What Is Already Closed

- Entanglement as substrate unity — closed, substrate-native
- Decoherence as routing event — closed, consistent with active canon
- The 1/2 factor is substrate-native, not an observer artifact — strong candidate
- The bipartite split and round-trip accounting are the same geometric fact — closed
- The old mirror-reflection derivation — decapitated, not carried forward
- $L_{vac} \approx 1.45 \times 10^{-20}$ m as the universal substrate floor — candidate-locked

---

## Full Status Table

| Claim | Status |
|---|---|
| Entanglement as single substrate informational structure | Substrate-native, consistent with canon |
| Decoherence as saturation-triggered routing event | Substrate-native, consistent with canon |
| Every object equidistant from substrate at $L_{vac}$ | Strong candidate — follows from $L_{vac}$ universality |
| Round-trip accounting produces 1/2 factor | Strong candidate — geometric argument closed |
| Bipartite split = round trip, same geometric fact | Strong candidate |
| Formal metric derivation from $L_{vac}$ round-trip | Open — Obligation 1 |
| Old mirror-reflection derivation of 1/2 | Decapitated — removed |

---

## Freeze Wording

> In HPF, the 1/2 factor in the weak-field metric is the GR-phase expression of symmetric round-trip substrate accounting. Every object is equidistant from the substrate at $L_{vac} \approx 1.45 \times 10^{-20}$ m — the universal resolution floor of the BCC lattice. Any metric measurement catches one leg of a two-leg exchange: the object warps the substrate, the substrate returns that warp to the observer. Because $L_{vac}$ is universal, both legs are always equal, and the observer always catches exactly half the total exchange. The BCC bipartite sublattice structure and the round-trip accounting are two descriptions of the same geometric fact. One obligation remains open: a formal derivation connecting $L_{vac}$ round-trip accounting to the weak-field metric coefficient as a substrate output rather than a GR input.

---

*End of candidate note. Do not promote to canon until Obligation 1 is closed.*
