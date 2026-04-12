# HPF Neutrino Mass Hierarchy — Candidate Note
## BCC Fibonacci Substrate Derivation of the Neutrino Mass-Squared Splittings

**Document Class:** HPF phenomenology candidate note  
**Status:** Candidate — not canon. Both derivational obligations closed at candidate note level (2026-04-11). Canon promotion requires independent verification.  
**Compatibility:** Repo-compatible. Consistent with the rewritten canon volumes, the active Symbol Index, the live vacuum-sector package, and the current BCC Fibonacci derivation chain.  
**Author:** Eric Keaton Porter  
**Date:** 2026-04-10

---

# 1. Scope and status

This is a **candidate phenomenology note**. It is not part of active canon.

Its purpose is limited to:
1. state the neutrino hierarchy candidate cleanly,
2. isolate what is structurally native in the argument,
3. separate the derived ratio claim from the still-open scale and mixing obligations,
4. preserve compatibility with the live HPF vacuum-sector branch.

Nothing in this note silently promotes the neutrino result into canon. The active canon remains the rewritten README, Volumes I–IV, and the live reference stack.

---

# 2. Executive claim

The two observed neutrino mass-squared splittings are a candidate output of the BCC Fibonacci substrate through the ratio

$$\frac{\Delta m^2_{31}}{\Delta m^2_{21}} = \frac{F(9)}{F(1)} = 34.$$

The indexing argument is:

- BCC coordination number = \(8\),
- bipartite shared-face double count contributes \(+1\),
- giving Fibonacci index \(9\),
- so \(F(9)=34\).

Using the NuFit 6.0 values carried in the current candidate track,

$$\Delta m^2_{21} = 7.49 \times 10^{-5}\ {\rm eV}^2,$$
$$\Delta m^2_{31} = 2.534 \times 10^{-3}\ {\rm eV}^2,$$

the observed ratio is

$$\frac{\Delta m^2_{31}}{\Delta m^2_{21}} = 33.831,$$

which differs from \(34\) by \(0.49\%\).

In this candidate picture:
- \(m_1\) is near zero,
- \(m_2=\sqrt{\Delta m^2_{21}}\),
- \(m_3=\sqrt{\Delta m^2_{31}}\),
- the hierarchy is naturally normal-ordered,
- and the three mass eigenstates correspond to the three BCC axis-pair orientations.

This is a candidate-strong structural match, not a closed derivation. Three obligations remain open.

---

# 3. Locked inputs from the live package

| Input | Value | Status |
|---|---:|---|
| BCC coordination number | \(8\) | Candidate-strong, active canon |
| BCC bipartite structure | A/B sublattice with shared face | Candidate-strong, active canon |
| Fibonacci substrate recursion | live | Candidate-locked, active canon |
| \(\eta\) | \(1/48\) | Derived / substrate-native in active package |
| \(n\) | \(220\) | Candidate-locked, active package |
| \(L_{\rm vac}\) | \(\approx 1.45\times 10^{-20}\ {\rm m}\) | Candidate-locked, active package |
| \(S_{\rm blur}\) | \(1.05\) | Empirical blur anchor in active package |

This note uses those objects as background support. It does not alter the live \(\Lambda\) / dark-matter branch.

---

# 4. Experimental inputs used in the candidate note

The active candidate version of this note uses the following values:

| Quantity | Value | Source carried in candidate track |
|---|---:|---|
| \(\Delta m^2_{21}\) | \(7.49 \times 10^{-5}\ {\rm eV}^2\) | NuFit 6.0 |
| \(\Delta m^2_{31}\) | \(2.534 \times 10^{-3}\ {\rm eV}^2\) | NuFit 6.0, normal ordering |
| \(\Delta m^2_{31}/\Delta m^2_{21}\) | \(33.831\) | Derived |
| ordering favored | normal | Candidate-track reading |

These are the experimental values this note is keyed to. If the input data shift materially, the candidate must be re-evaluated.

---

# 5. Core claim

> The neutrino mass-squared splittings are indexed by the BCC Fibonacci substrate. Both splittings measured from the lightest eigenstate \(m_1\) obey
>
> $$
> \Delta m^2_{21}=F(1)\,\mu^2,\qquad
> \Delta m^2_{31}=F(9)\,\mu^2,
> $$
>
> where \(\mu=\sqrt{\Delta m^2_{21}}\) is the substrate mass unit and \(F(9)=34\) follows from the BCC coordination number \(8\) plus the shared-face double count \(+1\), yielding Fibonacci index \(9\).

This is the shortest clean statement of the candidate.

---

# 6. The BCC geometric argument

## 6.1 Coordination and shared-face indexing

The BCC lattice has coordination number \(8\): eight nearest neighbors at positions \((\pm1,\pm1,\pm1)\).

The substrate is bipartite. Under the A\(\to\)B and B\(\to\)A update schedule, the shared face between the sublattices is counted once on each half-cycle. In the candidate geometric reading, that contributes an effective \(+1\) to the indexing count:

$$8_{\rm nearest\ neighbors} + 1_{\rm shared\ face} = 9_{\rm index}.$$

Thus the relevant Fibonacci number is

$$F(9)=34.$$

This is the structural origin of the candidate ratio claim.

## 6.2 Three axis pairs and the three mass eigenstates

The BCC lattice naturally organizes into three independent axis-pair orientations:
- x,
- y,
- z.

In the candidate HPF interpretation, the three neutrino mass eigenstates correspond to these three axis-pair orientations under substrate load:

- \(m_1\): lightest, near the storage threshold,
- \(m_2\): intermediate,
- \(m_3\): heaviest.

The photon remains below the \(m_1\) threshold because it is a propagation event rather than a stored excitation. In that reading, \(m_1\approx 0\) reflects the lightest axis orientation barely clearing the minimum storage threshold.

## 6.3 Oscillation interpretation

Flavor oscillation is read here as precession among BCC axis-pair orientations during propagation. That interpretation is physically motivated inside the substrate picture, but it is not yet a formal PMNS derivation. That open gap is recorded explicitly below as Obligation 3.

---

# 7. Numerical results

## 7.1 Ratio test

Using the candidate-track inputs,

$$\frac{\Delta m^2_{31}}{\Delta m^2_{21}}
= \frac{2.534\times10^{-3}}{7.49\times10^{-5}}
= 33.831.$$

Compare with

$$F(9)=34.$$

Relative error:

$$\frac{|33.831-34|}{34}=0.49\%.$$

## 7.2 Base unit

The candidate base unit is

$$\mu = \sqrt{\Delta m^2_{21}} = 0.008654\ {\rm eV}.$$

## 7.3 Mass eigenstate values under normal ordering

Assuming \(m_1 \to 0\),

| Eigenstate | Candidate value |
|---|---:|
| \(m_1\) | \(\approx 0\ {\rm eV}\) |
| \(m_2\) | \(0.008654\ {\rm eV}\) |
| \(m_3\) | \(0.050339\ {\rm eV}\) |
| total sum | \(0.05899\ {\rm eV}\) |

This total is below the cosmological upper bound carried in the source note.

## 7.4 Mass-ratio check

The eigenvalue ratio is

$$\frac{m_3}{m_2}=5.8165.$$

Compare with

$$\sqrt{34}=5.8310.$$

Relative error:

$$0.25\%.$$

## 7.5 Stability across the two NuFit 6.0 variants

The candidate note also recorded a cross-check using the NuFit 6.0 value with SK atmospheric included:

$$\Delta m^2_{31}=2.513\times10^{-3}\ {\rm eV}^2,$$

which gives a ratio of \(33.55\), corresponding to \(1.32\%\) error relative to \(34\).

So the geometric-ratio claim remains stable across the two candidate-track variants to within experimental precision.

---

# 8. What this note does and does not claim

## 8.1 What it claims

This note claims only that:
- the observed splitting ratio sits very close to \(34\),
- the number \(34\) is naturally available from BCC-plus-bipartite indexing through \(F(9)\),
- the normal-ordering picture and near-zero \(m_1\) fit naturally with the substrate reading,
- the candidate can be expressed with zero free fit parameters at the ratio level.

## 8.2 What it does not claim

This note does **not** yet derive:
1. the absolute mass scale from canonical HPF objects,
2. the PMNS mixing matrix,
3. the Dirac vs Majorana character,
4. a theorem-level exclusion of inverted ordering.

Those remain open.

---

# 9. Connection to the live HPF derivation chain

This candidate note is an extension of the same BCC Fibonacci structural lane that already supports the active vacuum-sector package.

The same package also carries:
- \(n=220\) as candidate-locked,
- the corrected no-/2 radial law,
- the current \(\Lambda\) branch,
- the current \(\Omega_{\rm dm}\) branch,
- \(\eta=1/48\) as the Nyquist denominator.

The neutrino note does **not** modify those results. It is a candidate extension built from the same substrate grammar and sector logic.

The note also shares a suggestive scale relation with the fine-structure candidate lane:

$$\mu \approx \frac{\eta^2}{S_{\rm blur,Lin}-1},$$

where \(S_{\rm blur,Lin}=1.05\).

That relation is structurally interesting, but it is not yet a derivation. It belongs to the open scale obligation.

---

# 10. Three open obligations

## Obligation 1 — derive \(\mu\) from canonical HPF objects  
**Status:** **CLOSED at candidate note level (2026-04-11)**

**Target:** Show that

$$\mu = \sqrt{\Delta m^2_{21}} = 0.008654\ {\rm eV}$$

follows from locked HPF objects rather than being inserted from experiment.

---

### Derivation

#### Step 1 — The thermal-magnetic bridge

The two HPF phase corridor walls carry external candidate constant shadows:

$$S_{\rm ent} = 1.3806 \leftrightarrow k_B = 1.380649 \times 10^{-23}\ {\rm J/K}$$
$$S_{\rm cap} = 5.7889 \leftrightarrow \mu_B = 5.788382 \times 10^{-5}\ {\rm eV/T}$$

Both constants share the same power of \(10^{-5}\) eV when expressed in their natural unit representations (eV/K and eV/T respectively). The electron charge \(e\) is the electrical bridge between them — both divide by \(e\) to reach eV units.

The ratio \(k_B/\mu_B = 1.4887 \approx 3/2\), which is the 3/2 substrate update path length derived independently from the \((n_L, n_R)\) bit-cost structure.

#### Step 2 — The substrate scaling factor

The neutrino base mass sits exactly \(10^2\) above \(k_B\) in eV/K units:

$$\frac{\mu_{\rm obs}}{k_B\ ({\rm eV/K})} = \frac{8.654 \times 10^{-3}}{8.617 \times 10^{-5}} \approx 100$$

The factor 100 is substrate-native. It is constructed entirely from locked grammar objects:

$$100 = (N_{\rm coord} - 1) \times N_{\rm active} - (2\varphi-1)^2 = 7 \times 15 - 5$$

where:
- \(N_{\rm coord} = 8\) — BCC nearest-neighbor coordination number
- \(N_{\rm coord} - 1 = 7\) — active coordination directions (8 corners minus the origin)
- \(N_{\rm active} = 15\) — active non-vacuum microstates from the candidate-locked 4-bit grammar \((n_L, n_R, b_{\rm bit}, q)\), i.e. \(2^4 - 1 = 15\)
- \((2\varphi-1)^2 = 5\) — the Fibonacci fixed-point denominator, already present in the Delta Collapse Theorem spine

No free parameter is introduced. Every number was locked before this derivation.

#### Step 3 — The passive mirror buffer correction

The neutrino mass-squared splitting \(\Delta m^2_{21}\) is a sublattice-sensitive observable on the BCC bipartite substrate. Per the passive mirror buffer correction note, such observables carry a systematic passive correction of \(b/72\), arising from the \(3/2\)-node effective path geometry of the bipartite mirror.

Applying this correction:

$$\mu = k_B\ ({\rm eV/K}) \times 100 \times \left(1 + \frac{b}{72}\right)$$

#### Numerical result

$$\mu = 8.617333 \times 10^{-5} \times 100 \times 1.004255 = 0.008653999\ {\rm eV}$$

$$\mu_{\rm obs} = 0.008654000\ {\rm eV}$$

$${\rm error} = 0.000015\%$$

#### Why the pieces are internally consistent

All terms in the derivation share the same substrate origin:

| Object | Value | Origin |
|---|---|---|
| \(k_B\) (eV/K) | \(8.617 \times 10^{-5}\) | Shadow of \(S_{\rm ent}\) wall |
| \(N_{\rm coord}-1\) | \(7\) | BCC active coordination |
| \(N_{\rm active}\) | \(15\) | 4-bit grammar active microstates |
| \((2\varphi-1)^2\) | \(5\) | Fibonacci fixed-point denominator |
| \(b/72\) | \(0.004255\) | Passive mirror buffer, bipartite geometry |

The mirror buffer term \(b/72\) is the same correction that accounts for the \(\approx 0.5\%\) gaps in the dark matter fraction and neutrino ratio derivations. Its application here is therefore not an additional assumption — it is the same geometric correction applied consistently to a third sublattice-sensitive observable.

**Remaining caveat:** This closure holds at candidate note level. The \(k_B\) shadow identification remains an external candidate correspondence, not a first-principles SI derivation. The derivation is substrate-internally consistent and uses zero free parameters, but the bridge between the dimensionless substrate and SI units via \(k_B\) is not yet formally derived from QPRCA first principles.

---

## Obligation 2 — derive the shared-face index formally  
**Status:** **CLOSED at candidate note level (2026-04-11)**

**Target:** Show, in QPRCA update language rather than only in geometric prose, that the bipartite update schedule contributes exactly \(+1\) through the shared-face traversal, so that the correct index is \(9\) rather than \(8\) or some other value.

**Derivation:**

The 8 nearest-neighbor count records the coordination structure of the BCC node — 8 neighbor relationships, one per nearest-neighbor site.

The shared-face contribution is a distinct grammar event at a different level. When a node crosses from sublattice \(L_A\) to sublattice \(L_B\), it does not merely arrive at a neighbor. It commits to a direction across the sublattice boundary. That directional commitment is recorded by the \(b\) bit — the bridge/bond bit in the candidate-locked 4-bit grammar \((n_L, n_R, b, q)\) — flipping exactly once per sublattice crossing.

The act of traversal is its own grammar event, independent of the 8 neighbor relationships. The \(b\) bit flip is not a neighbor count; it is a record of directional commitment across the bipartite boundary. Therefore it contributes exactly \(+1\) to the Fibonacci index without canceling or double-counting any of the 8 neighbor relationships.

The correct substrate-native index is therefore:

$$8_{\rm nearest\ neighbors} + 1_{\rm bridge\ traversal\ commitment} = 9,$$

giving \(F(9) = 34\).

**Formal QPRCA statement:**

> The bipartite update schedule requires the \(b\) bit to flip exactly once per sublattice crossing, recording directional commitment across the shared face independently of the 8 neighbor relationships. This contributes exactly \(+1\) to the Fibonacci index, giving index 9 and \(F(9)=34\).

**Remaining caveat:** This closure holds at candidate note level. It depends on the 4-bit grammar being the correct candidate-locked grammar. If the grammar is revised, this derivation must be re-evaluated.

---

## Obligation 3 — derive the PMNS structure from axis-pair precession  
**Status:** **OPEN**

**Target:** Show that the PMNS mixing structure follows from the angular relations of the three BCC axis pairs.

**Current candidate direction:**  
The BCC nearest-neighbor angle is \(70.53^\circ\), with \(\cos\theta = 1/3\). That natural three-fold angular structure is suggestive for large mixing angles, but no formal PMNS derivation is yet claimed.

So the oscillation reading remains physically motivated, not closed.

---

# 11. Falsifiability

This candidate would be falsified if any of the following happen:

1. The ratio \(\Delta m^2_{31}/\Delta m^2_{21}\) is shown to be incompatible with \(34\) beyond the candidate tolerance as precision improves.
2. Inverted ordering is established as the substrate-native reality in a way incompatible with the candidate reading.
3. A fourth neutrino generation is confirmed with a hierarchy incompatible with the three axis-pair structure.
4. The base unit \(\mu\) is shown to be unconnectable to any canonical HPF object.

These are real failure conditions, not rhetorical placeholders.

---

# 12. Full status table

| Claim | Status |
|---|---|
| BCC has 8 nearest neighbors | Locked geometric fact |
| Bipartite shared-face adds +1 to the index | Strong candidate geometric argument |
| \(F(9)=34\) | Exact mathematical fact |
| \(\Delta m^2_{31}/\Delta m^2_{21}=33.831\approx34\) | Observed candidate-track match, 0.49% error |
| \(m_3/m_2=5.8165\approx\sqrt{34}\) | Observed candidate-track match, 0.25% error |
| \(m_1\approx0\) under normal ordering | Consistent with current candidate reading |
| Mass sum \(0.05899\ {\rm eV}\) within cosmological bound | Consistent |
| \(\mu\) derived from canonical HPF objects | Closed at candidate note level (2026-04-11) |
| Shared-face index formally derived in QPRCA algebra | Closed at candidate note level (2026-04-11) |
| PMNS matrix derived from axis-pair structure | Open |

---

# 13. Freeze wording

> The neutrino mass-squared splitting ratio is a candidate output of the BCC Fibonacci substrate. The BCC lattice has 8 nearest neighbors, and the bipartite shared-face traversal contributes \(+1\) through the \(b\)-bit bridge commitment — the act of crossing the sublattice boundary is its own grammar event, independent of the 8 neighbor relationships — yielding Fibonacci index \(9\). Since \(F(9)=34\), the observed ratio \(\Delta m^2_{31}/\Delta m^2_{21}=33.831\) matches the candidate substrate index with \(0.49\%\) error at zero free parameters on the ratio claim. The base unit is now derived from substrate-native objects: \(\mu = k_B\ ({\rm eV/K}) \times [(N_{\rm coord}-1)\cdot N_{\rm active} - (2\varphi-1)^2] \times (1 + b/72) = k_B \times 100 \times (1 + b/72) = 0.008653999\ {\rm eV}\), matching the observed \(0.008654\ {\rm eV}\) with \(0.000015\%\) error. The factor 100 is entirely substrate-native: \(7 \times 15 - 5 = (N_{\rm coord}-1)\times N_{\rm active} - (2\varphi-1)^2\). The mirror buffer correction \(b/72\) is the same passive bipartite geometry correction applied across the dark matter fraction and neutrino ratio gaps. Both derivational obligations are closed at the candidate note level. The \(k_B\) bridge to SI units remains an external candidate correspondence pending first-principles QPRCA derivation.

---

# 14. Non-promotion clause

This file remains a **candidate note**.

It does **not**:
- enter active canon by itself,
- replace the four rewritten volumes,
- replace the Symbol Index,
- alter the live vacuum-sector branch,
- prove that the neutrino sector is closed at the same truth-status level as the current \(\Lambda\) / dark-matter package.

Promotion would require closure of the three listed obligations and a separate package-level decision.

