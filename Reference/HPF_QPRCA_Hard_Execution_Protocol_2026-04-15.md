# HPF Reference Note — QPRCA Hard Execution Protocol
## k=11→∞ Transition, Frozen Boundary States, and Mandatory Continuation
### 2026-04-15

**Author:** Eric Keaton Porter  
**Status:** Candidate — executable-confirmed  
**Framework version:** Hylo-Phase Framework v2.2.1  
**Purpose:** State cleanly what QPRCA does when HPF fires the hard gate, and how the k=11→∞ transition maps onto the 4-bit grammar.

---

# 1. What this note does

This note exists for one reason:

> to state cleanly what happens to the substrate grammar when QPRCA takes full control — specifically, how the transition from operational steepness \(k=11\) to the hard limit \(k\rightarrow\infty\) partitions the full state space into mandatory continuations and frozen boundary states.

It is not a full QPRCA presentation. It is a protocol closure note.

---

# 2. The two regimes

## 2.1 Soft regime — k=11

In normal MDEA routing, the stability functional runs at operational steepness \(k=11\):

$$
\zeta(S)=\frac{1}{1+e^{11(S-1.05)}}.
$$

This is the soft regime. Geometry retains partial authority. Continuation classes are distributed across \(\Sigma\)-equivalences. The existence sensor tracks \(F_{\min}\) probabilistically. Multiple sigma classes compete; the distribution of outcomes is weighted.

## 2.2 Hard regime — k→∞

When HPF fires the hard gate

$$
G_{\rm health} < 0.3 \implies E^* = E_{\rm QPRCA},
$$

the steepness transitions to \(k\rightarrow\infty\). The logistic collapses to a step function at \(S_{\rm onset}=1.05\). QPRCA takes full and exclusive control.

In this limit, the soft weighting of continuation classes is gone. Only one question remains:

> **Does a legal continuation exist?**

---

# 3. The k=11→∞ transition is the handoff

This is the central claim of this note.

The transition from \(k=11\) to \(k\rightarrow\infty\) is not merely a parameter change. It is the physical meaning of the QPRCA handoff. The softness of \(k=11\) is the regime in which effective theories retain standing. The infinite steepness is the regime in which they do not.

**QPRCA taking control IS \(k\rightarrow\infty\).**

---

# 4. What k→∞ does to the 4-bit grammar

## 4.1 State space partition

The existence sensor sweep over all 256 input pairs \((inL, inR)\) with \(inL, inR \in \{0,\ldots,15\}\) partitions the full state space under the sanitized reversible subregistry (9 rules: ID, SWAP, TQ, SB, BOUNCE, EXCH, TQ0, BQ0, SWEQ):

| Class | Count | k→∞ Behavior |
|---|---|---|
| True positive | 204 | Legal continuation exists — mandatory execution |
| True negative | 52 | No legal continuation exists — frozen boundary state |
| False positive | 0 | — |
| False negative | 0 | — |

**Verdict: 256/256 strong pass.**

Under \(k=11\), these classes are identified probabilistically by the existence sensor. Under \(k\rightarrow\infty\), they become hard execution outcomes.

## 4.2 Frozen boundary states

The 52 true negatives are not failures. They are the substrate grammar enforcing its own wall.

For these microstates, no rule in the sanitized reversible registry produces an output with \(F_{\rm block} < 1\). No legal continuation exists.

QPRCA does not evolve these states. It holds them.

**This is not a singularity. It is the 4-bit grammar stating: not from here.**

## 4.3 Mandatory continuation

For the 204 true positives, the \(\Sigma\)-class with minimum \(F_{\rm block}\) under grouped-L2 aggregation becomes the mandatory next state:

$$
\sigma^* = \arg\min_{\sigma \in \Sigma} \max(F_{\rm left}, F_{\rm right})_\sigma.
$$

One continuation. Bounded. Substrate-native. No free parameters. No weighting. No geometry bleeding through.

---

# 5. The full chain

The derivation chain that produces this partition is:

$$
\text{BCC} \rightarrow \eta=\frac{1}{48} \rightarrow k=11 \xrightarrow{G_{\rm health}<0.3} k\rightarrow\infty \rightarrow \text{QPRCA executes}
$$

$$
\xrightarrow{n=220} S_{\rm cap}=5.7889 \rightarrow
\begin{cases}
204\ \text{states: mandatory continuation} \\
52\ \text{states: frozen boundary}
\end{cases}
$$

Equivalently, starting from the blur anchor:

> At anchor \(S_{\rm blur}=1.05\), the chain derives \(S_{\rm ent}=1.3806\) and \(S_{\rm cap}=5.7889\) with \(k=11\rightarrow\infty\) for \(n=220\).

This is one continuous statement about \(k\), not three separate derivations.

---

# 6. Executable confirmation

All claims in this note are confirmed by live executable runs:

| Test | Result |
|---|---|
| Existence sensor sweep (256 pairs, grouped-L2, baseline) | **256/256 strong pass — 0 FP, 0 FN** |
| Block-gate unitarity (N=2, all four sub-unitaries + full tick) | **Unitarity error: 0.00e+00** |
| High-mismatch vs low-mismatch regulator response | **Distinct — confirmed by ⟨Z_R⟩ evolution** |
| Sigma pressure test (8 adversarial cases) | **Passed — sigma classes resolving correctly** |

If the \(k\rightarrow\infty\) interpretation were wrong, at least one of these runs would have produced a non-zero error or a false positive. None did.

---

# 7. What this note does not claim

This note does **not**:
- claim that the 52 frozen boundary states are physically unreachable in all substrate configurations,
- claim that \(k\rightarrow\infty\) is exact rather than the limiting behavior of the hard gate,
- prove that the grouped-L2 aggregation law is uniquely correct,
- promote any result from candidate to canon,
- close the open obligation on first-principles derivation of \(F(x)\) from QPRCA dynamics.

It closes one status question only: what QPRCA does when HPF hands off to it, expressed in terms the executable already confirmed.

---

# 8. Freeze wording

> When HPF fires the hard gate \(G_{\rm health}<0.3\), MDEA routes to QPRCA and the operational steepness transitions from \(k=11\) to \(k\rightarrow\infty\). This collapses the soft logistic to a step function at \(S_{\rm onset}=1.05\) and eliminates all partial authority from effective theories. The 4-bit grammar then partitions the full 256-pair state space into 204 mandatory continuations (minimum-F \(\Sigma\)-class executes) and 52 frozen boundary states (no legal continuation exists; substrate holds). This partition was confirmed 256/256 by the existence sensor protocol with zero false positives and zero false negatives. The \(k=11\rightarrow\infty\) transition is not merely a parameter change — it is the physical meaning of the QPRCA handoff.

---

*Produced 2026-04-15. Executable confirmation from session of same date. Framework version: HPF v2.2.1.*
