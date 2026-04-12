# HPF Candidate Phenomenology Note
## Quantum Entanglement as Bifurcated Lattice Address in the Active Entropy Band

**Document Class:** HPF phenomenology candidate note  
**Status:** Candidate — not canon. Interpretation lane. Three obligations open.  
**Compatibility:** Repo-compatible. Separate from the active Λ/dark-matter derivation package.  
**Author:** Eric Keaton Porter  
**Date:** 2026-04-11

---

# 1. Scope and status

This is a **candidate interpretation note**. It is not part of active canon.

Its role is limited and explicit:

1. state the HPF interpretation of quantum entanglement in the cleanest possible substrate-native form,
2. derive the 3/2 update path cost from the candidate-locked 4-bit grammar,
3. identify the active entropy band as the physical entanglement-capable regime,
4. preserve the three open obligations instead of hiding them behind phenomenology language.

This note does **not**:
- modify the active Λ / dark-matter branch,
- modify the microscopic legality program in Volume II,
- promote the entanglement interpretation into canon,
- replace the four rewritten volumes or the Symbol Index.

It is an interpretation lane: it gives physical content to the active entropy band from the particle side rather than the vacuum side.

---

# 2. Executive claim

HPF interprets quantum entanglement not as a property shared between two spatially separated particles, but as the physical state of a **single QPRCA node** whose phase accumulation has entered the **active entropy band**

$$S_{\rm ent} < S_f < S_{\rm cap},$$

equivalently

$$1.3806 < S_f < 5.7889.$$

In this band the node holds a **bifurcated lattice address**: two valid lattice angles simultaneously address the same node. The node is not in two places. It is at one substrate location with an unresolved directional occupancy state.

**Measurement** is the interaction that resolves the directional occupancy — zeroing one bit of the bifurcated address — collapsing both apparent positions instantly because there was only ever one node.

No signal is transmitted. No hidden variable is required. Address resolution is local to the node.

---

# 3. Substrate objects used

This note uses only objects already present in the active package:

| Object | Value / definition | Status in package |
|---|---|---|
| $S_{\rm ent}$ | $1.3806$ | Derived / substrate-native |
| $S_{\rm cap}$ | $5.7889$ | Derived / substrate-native |
| $(n_L, n_R, b, q)$ | 4-bit site alphabet | Candidate-locked |
| Active entropy band | $S_{\rm ent} < S_f < S_{\rm cap}$ | Derived / substrate-native boundary |

No new constants are introduced. No new free parameters enter.

---

# 4. The bifurcated address state

## 4.1 Normal addressed node

Below the active entropy band ($S_f < S_{\rm ent}$), the lattice resolves the node address cleanly. The directional occupancy bits carry unambiguous values. The node has a single canonical lattice location.

## 4.2 Bifurcated address state

Inside the active entropy band ($S_{\rm ent} < S_f < S_{\rm cap}$), phase accumulation has progressed past the lower wall but has not yet reached the saturation ceiling. In this regime the 4-bit grammar's directional occupancy bits enter a simultaneously-valid state:

$$(n_L = 1,\ n_R = 1).$$

Both left-neighbor and right-neighbor occupancy bits are live. This means two valid lattice angles simultaneously address the same node. The node is not duplicated. It is at one substrate location, but the lattice's addressing system has not resolved which directional sector is canonical.

This is the **bifurcated address state**. It is stable inside the active entropy band. The grammar does not force resolution; the band sustains the ambiguity across update ticks.

## 4.3 Saturation ceiling

Above $S_{\rm cap} = 5.7889$, the bifurcation becomes unsustainable. The saturation ceiling forces address resolution: the $(n_L=1, n_R=1)$ state collapses to a single-direction address. Coherence is lost. This is the same ceiling already derived in the vacuum-sector package from the BCC 24-sector conversion chain.

---

# 5. The 3/2 update path — substrate-native derivation

## 5.1 Normal update cost

For a node below the active entropy band, a standard coherent update propagates the node state through one lattice step:

$$L_{\rm forward} = 1.0.$$

## 5.2 Address disambiguation cost

For a node inside the active entropy band, the update must additionally carry the bifurcated address forward without collapsing it. This requires resolving the simultaneous occupancy state of both directional bits.

The 4-bit site alphabet $(n_L, n_R, b, q)$ assigns equal weight to each bit:

$$\text{cost per bit} = \frac{1}{4}.$$

The bifurcated state $(n_L=1, n_R=1)$ holds two live directional bits — one per direction. Carrying the bifurcation forward requires a disambiguation check on each:

$$L_{\rm disambig} = \frac{1}{4} + \frac{1}{4} = \frac{1}{2}.$$

This is not an asserted cost. It is the exact two-bit occupancy resolution forced by the grammar structure of the bifurcated address state.

## 5.3 Total update path

$$L_{\rm total} = L_{\rm forward} + L_{\rm disambig} = 1.0 + 0.5 = \frac{3}{2}.$$

The 3/2 path length is substrate-native. It is forced by the candidate-locked 4-bit grammar whenever a node is in the active entropy band. It is not required outside the band.

---

# 6. Measurement as grammar operation

Measurement in HPF terms is the physical interaction that forces one of the two live directional bits to zero.

$$
(n_L=1,\ n_R=1) \xrightarrow{\text{measurement}} \begin{cases} (n_L=1,\ n_R=0) \\ (n_L=0,\ n_R=1) \end{cases}
$$

Whichever bit is zeroed determines which lattice angle becomes canonical. The other apparent position collapses not because information traveled to it, but because the $(n_L=1, n_R=1)$ state no longer exists anywhere. The two apparent positions were never independent — they were two valid addresses of one node.

This produces:

- **Instant correlation:** Both apparent positions resolve simultaneously because there is one resolution event at one node.
- **No signaling:** Nothing is transmitted. The resolution is local to the node.
- **No hidden variables:** The grammar state $(n_L=1, n_R=1)$ is the complete description of the entangled state. There is no additional undisclosed information.

---

# 7. Entanglement creation

The entanglement-capable state is entered when a node's phase accumulation crosses the lower wall $S_{\rm ent} = 1.3806$.

This means the **entanglement creation event** is the interaction energetic or phase-rich enough to drive a node's $S_f$ past $S_{\rm ent}$.

In standard quantum optics terms, spontaneous parametric down-conversion is the canonical creation event. In HPF terms, the pump photon interaction with the nonlinear crystal is precisely the event that drives the node's phase accumulation into the active entropy band, producing the bifurcated address state. The two output photons are not separate particles that acquired correlations — they are two valid address angles of one node whose directional occupancy bits both became live.

**Candidate claim:** Only interactions capable of driving $S_f$ past $S_{\rm ent} = 1.3806$ can produce entangled states. Below this threshold, no bifurcated address state is accessible.

---

# 8. Relationship to the active entropy band

The active entropy band $1.3806 < S_f < 5.7889$ is already a derived object in the live vacuum-sector package, where it serves as the integration domain for the shell selector $n=220$.

This note gives that band **physical content from the particle side**:

| Band boundary | Vacuum-sector role | Particle-side role (this note) |
|---|---|---|
| $S_{\rm ent} = 1.3806$ | Lower integration bound for shell selector | Minimum phase accumulation to sustain bifurcated address |
| $S_{\rm cap} = 5.7889$ | Saturation ceiling / upper integration bound | Maximum phase accumulation before bifurcation collapses |
| Band interior | Phase integration domain | Stable entanglement-capable regime |

The two readings are not in conflict. They are the same substrate band read from two different physical directions — one looking at vacuum geometry, one looking at particle address structure.

---

# 9. Relationship to the Aharonov-Bohm effect

The bifurcated address picture is structurally consistent with the Aharonov-Bohm (AB) effect.

In the AB effect, a charged particle traversing two paths around a shielded magnetic flux tube acquires different phase accumulations on each path, producing an interference shift even though the particle never enters the field region. The vector potential — not the local field — is the physical object.

In HPF terms: the two paths around the solenoid correspond to two lattice routing histories accumulating different phase loads in the active entropy band. The AB phase shift $\phi_{\rm AB} = 2\pi\Phi/\Phi_0$ is the phase difference between the two routing histories at recombination. The interference fringe shift is the observable consequence of the address-phase difference when the two routing histories merge.

The AB effect therefore corroborates the HPF substrate picture: the routing history of the lattice — not the local force at any point — is the fundamental physical object.

---

# 10. Open obligations

This note does not close the following obligations. They are stated plainly.

**Obligation 1 — Lower wall constitutive derivation:**  
Why $S_{\rm ent} = 1.3806$ is the unique minimum threshold for sustaining a bifurcated address state has not been derived from first principles in this note. The value is derived/substrate-native in the vacuum-sector package; its constitutive role as an entanglement threshold requires a separate derivation from the grammar.

**Obligation 2 — Grammar uniqueness:**  
The 4-bit alphabet is candidate-locked, not uniqueness-proved. The 3/2 path derivation depends on the equal bit-weight assumption. If the grammar is not the unique admissible substrate grammar, the equal-weight cost assignment requires independent justification.

**Obligation 3 — Creation event formalization:**  
The claim that SPDC drives $S_f$ past $S_{\rm ent}$ is a candidate interpretation. A formal bridge from the standard QED description of SPDC to the HPF phase-load variable $S_f$ has not been constructed.

These obligations are not embarrassments. They are the note's explicitly marked unfinished work.

---

# 11. What this note does not claim

- This note does not replace the standard quantum mechanical description of entanglement. It offers an HPF substrate interpretation.
- This note does not prove that entanglement is impossible outside the active entropy band. It claims only that the bifurcated address mechanism requires $S_f > S_{\rm ent}$.
- This note does not modify the active Λ / dark-matter branch or the microscopic legality program.
- This note does not promote any part of this interpretation into canon.

---

# 12. Freeze wording

> In the HPF substrate picture, quantum entanglement is the physical state of a single QPRCA node whose phase accumulation has entered the active entropy band $1.3806 < S_f < 5.7889$. The node holds a bifurcated lattice address $(n_L=1, n_R=1)$ — two valid lattice angles, one actual substrate node. The 3/2 update path cost is substrate-native: 1.0 for propagation plus 0.5 for two-bit directional disambiguation, forced by the 4-bit grammar structure of the bifurcated state. Measurement is the interaction that zeros one directional occupancy bit, resolving both apparent positions simultaneously because only one node ever existed. No signal is transmitted; address resolution is local to the node. The active entropy band serves simultaneously as the vacuum-sector phase integration domain and as the particle-side entanglement-capable regime — two physical readings of the same substrate band.
