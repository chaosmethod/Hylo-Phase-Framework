# HPF Candidate External Falsifier
## Irreducible Stochastic Jitter in High-Energy Photon Arrival Times

**Document Class:** HPF phenomenology candidate note  
**Status:** Candidate — not canon. External falsifier lane. Three obligations open.  
**Compatibility:** Repo-compatible. Separate from the active \(\Lambda\)/dark-matter derivation package and separate from the photon-ring note.  
**Author:** Eric Keaton Porter  
**Date:** 2026-04-10

---

# 1. Scope and status

This is a **candidate external-falsifier note**. It is not part of active canon.

Its role is limited and explicit:

1. state the HPF timing-residue prediction in the cleanest possible form,
2. separate propagation-induced jitter from source and detector noise,
3. keep the claim tied to the active substrate objects already in the package,
4. preserve the three open obligations instead of hiding them behind phenomenology language.

This note does **not**:
- modify the active \(\Lambda\) / dark-matter branch,
- borrow amplitude from the dark-matter branch,
- promote the timing claim into canon,
- replace the four rewritten volumes or the Symbol Index.

It is a falsifier lane: useful precisely because it can fail.

---

# 2. Executive claim

HPF predicts that finite scheduler discreteness and finite vacuum transport granularity can produce an **irreducible propagation-induced arrival-time dispersion floor** for sufficiently energetic photons over sufficiently long baselines.

The leading candidate signature is:

- **not** a coherent linear lag,
- **not** an obligatory signed delay,
- **but** a **positive stochastic broadening floor** with near-zero mean shift.

The natural primitive scale is the scheduler tick

$$
t_{\rm sched}=\frac{L_{\rm vac}}{c},
$$

with \(L_{\rm vac}\) the active substrate resolution scale.

Under the current package state, the leading candidate law is the **gated random-walk branch**:

$$
\boxed{
\sigma_t(E,D;S_f)\sim t_{\rm sched}\sqrt{N_{\rm eff}(E,D,S_f)}\,\Gamma(S_f;b,\eta)
}
$$

rather than a deterministic drift law proportional to \(N\,t_{\rm sched}\).

That means the observable targeted by this note is **excess variance**, not compulsory signed delay.

---

# 3. Locked inputs from the live package

This note uses only active or candidate-safe objects already present in the rewritten package.

| Input | Form | Status |
|---|---|---|
| Vacuum resolution scale | \(L_{\rm vac}=R_H/\varphi^n\) | Candidate-locked, active package |
| Scheduler tick | \(L_{\rm vac}=c\,t_{\rm sched}\) | Canonical identity |
| Blur anchor | \(S_{\rm blur}=1.05\) | Empirical anchor under HPF mapping |
| Residual margin | \(\eta=1/48\) | Derived / substrate-native |
| Spiral parameter | \(b=\ln\varphi/(\pi/2)\) | Derived / substrate-native |
| Common two-wall spine | \(\{S_{\rm blur},\eta,b\}\) | Locked internal spine |
| Active lower onset | \(S_{\rm ent}=1.3806\) | Live phase onset |
| Active upper wall | \(S_{\rm cap}=5.7889\) | Live capacity wall |

These are sufficient to state the falsifier lane without mixing in unrelated branches.

---

# 4. Mechanism

The candidate mechanism is:

## 4.1 Finite scheduler discreteness

Propagation is not executed on a continuum with arbitrarily fine temporal resolution. The primitive clock is

$$
t_{\rm sched}=\frac{L_{\rm vac}}{c}.
$$

## 4.2 Vacuum transport granularity

Even vacuum transport remains substrate-executed at finite resolution. The continuum description is effective, not primitive.

## 4.3 Cumulative micro-variance

Microscopic propagation slips need not accumulate with a common sign. Under the current package, there is no canon-safe same-sign microscopic accumulation law that would force a coherent deterministic drift.

That pushes the candidate leading branch toward **variance-style accumulation**, not linear drift.

## 4.4 Regime gating

The effect is not predicted to be universally active at one strength. It is controlled by the same phase architecture that already governs blur onset, entropy onset, and capacity behavior through the common spine

$$
\{S_{\rm blur},\eta,b\}.
$$

So the candidate signature is a **thresholded stochastic floor**, not a universal continuum-LIV style deformation applied everywhere equally.

---

# 5. Leading branch choice

The current package supports the branch

$$
\boxed{\sigma_t \propto \sqrt{N_{\rm eff}}\,t_{\rm sched}}
$$

with regime gating, rather than

$$
\sigma_t \propto N_{\rm eff}\,t_{\rm sched}.
$$

The reason is structural:

- a linear-in-\(N\) law would read as a coherent systematic drift,
- the current package does not supply a same-sign microscopic accumulation principle,
- the support/availability logic and square-root transfer structure point more naturally toward variance-like accumulation.

So the clean candidate ansatz is

$$
\boxed{
\sigma_t(E,D;S_f)=t_{\rm sched}\sqrt{N_{\rm eff}(E,D,S_f)}\,\Gamma(S_f;b,\eta).
}
$$

This is the right branch to test first.

---

# 6. Minimal scaling ansatz

A minimal separable form is:

$$
\sigma_t(E,D)=A\,F(E)\,G(D)\,H(b,\eta,L_{\rm vac}),
$$

with the HPF candidate identification

$$
H(b,\eta,L_{\rm vac})=\frac{L_{\rm vac}}{c}\,\Xi(b,\eta),
$$

$$
G(D)=\sqrt{\frac{D}{L_{\rm corr}(E,S_f)}},
$$

$$
F(E)=\mathcal{G}(E;S_f).
$$

Thus

$$
\boxed{
\sigma_t(E,D;S_f)=
\frac{L_{\rm vac}}{c}\,
\sqrt{\frac{D}{L_{\rm corr}(E,S_f)}}\,
\Xi(b,\eta)\,
\mathcal{G}(E;S_f).
}
$$

At the current truth-status level:

- \(L_{\rm corr}\) is an open candidate placeholder,
- \(\Xi(b,\eta)\) is an open candidate substrate factor,
- \(\mathcal{G}\) is the candidate energy/load gate,
- no closed derivation of these objects is claimed here.

That openness must remain explicit.

---

# 7. Regime prediction

The candidate HPF regime statement is:

$$
\Gamma(S_f;b,\eta)\approx 0
\qquad \text{for } S_f \lesssim S_{\rm blur}=1.05,
$$

then the gate turns on through the blur-to-onset corridor,

and becomes active once the path samples the instability corridor strongly enough.

Operationally this gives three regimes:

## 7.1 Low-load coherent regime
No detectable propagation jitter beyond a tiny upper bound.

## 7.2 Transition regime
Onset of excess broadening.

## 7.3 Instability-active regime
Nonzero stochastic broadening floor.

This thresholded structure is what keeps the note HPF-native rather than generic Lorentz-violation phenomenology.

---

# 8. Separation from source and detector noise

A useful version of this note must separate three distinct effects:

## 8.1 Source-intrinsic variability
Emission-time structure native to the source.

## 8.2 Detector timing noise
Instrument response, trigger logic, timestamp uncertainty, event reconstruction, and binning artifacts.

## 8.3 Propagation-induced irreducible floor
A source-independent residual broadening accumulated during transit.

The HPF claim concerns **only 8.3**.

So the observable decomposition is

$$
\sigma_{\rm obs}^2=
\sigma_{\rm src}^2+
\sigma_{\rm det}^2+
\sigma_{\rm prop}^2,
$$

with HPF targeting

$$
\sigma_{\rm prop}=\sigma_t(E,D;S_f).
$$

The note should be considered failed if no allowed \(\sigma_{\rm prop}\) survives once source and detector contributions are brought below the predicted bound.

---

# 9. Sign of the effect

Leading candidate sign prediction:

- **mean shift:** approximately zero,
- **variance:** positive definite,
- **observable consequence:** extra arrival-time broadening rather than compulsory late arrival.

This is one of the cleanest distinctions between the HPF candidate and standard one-parameter signed-lag models.

So the front-line claim is:

> **HPF predicts stochastic broadening first, not compulsory coherent lag first.**

---

# 10. Kill conditions

This falsifier lane is killed if any of the following occur:

1. **No excess propagation broadening.**  
   After credible subtraction or bounding of source and detector terms, no propagation-induced excess remains above the HPF-derived upper bound.

2. **Wrong distance scaling.**  
   The measured propagation component scales incompatibly with the candidate \(\sqrt{D}\)-type accumulation law.

3. **Wrong energy/load behavior.**  
   The excess broadening fails to show the predicted thresholded energy/load dependence, or trends the wrong way.

4. **Compulsory signed lag without broadening.**  
   A persistent signed propagation lag appears as the dominant effect while stochastic broadening does not.

5. **Inconsistent multi-source behavior.**  
   Different long-baseline high-energy sources fail to obey any common propagation law after source and detector contributions are separated.

These are proper kill conditions because they attack the propagation claim itself.

---

# 11. Open obligations

Three obligations remain open before this note is stronger than a structurally motivated falsifier sketch.

## Obligation 1 — derive the \(\sqrt{N}\) branch microscopically  
**Status:** **OPEN**

Show from substrate transport or QPRCA-style microscopic mechanics why the leading accumulation is variance-like rather than coherent linear drift.

## Obligation 2 — define \(N_{\rm eff}\) and \(L_{\rm corr}\) canon-safely  
**Status:** **OPEN**

Replace the placeholder effective-domain count with a transport object that belongs cleanly to the HPF/QPRCA package.

## Obligation 3 — derive the gate \(\Gamma(S_f;b,\eta)\)  
**Status:** **OPEN**

Show how the common spine

$$
\{S_{\rm blur},\eta,b\}
$$

produces the activation/suppression law for observable propagation jitter.

Until these are closed, the note must remain candidate-level.

---

# 12. Instrument relation

Only after the mechanism and obligations are stated should the note connect to instruments.

The instrument-facing claim is intentionally modest:

> Fermi-LAT- and CTA-class high-energy timing datasets are the natural place to test whether any irreducible source-independent propagation broadening exists at a level compatible with the HPF candidate floor.

That is enough for this note. Instrument language should not lead the derivation.

---

# 13. Truth-status partition

To keep the lane disciplined:

## 13.1 Active inputs
- \(L_{\rm vac}\)
- \(t_{\rm sched}\)
- \(S_{\rm blur}=1.05\)
- \(\eta=1/48\)
- \(b=\ln\varphi/(\pi/2)\)
- \(S_{\rm ent}=1.3806\)
- \(S_{\rm cap}=5.7889\)

## 13.2 Candidate placeholders
- \(N_{\rm eff}\)
- \(L_{\rm corr}\)
- \(\Xi(b,\eta)\)
- \(\Gamma(S_f;b,\eta)\) in explicit observational form

## 13.3 Candidate result
- the stochastic broadening law

## 13.4 What is not claimed
- no canon-level jitter prediction yet,
- no closed amplitude,
- no compulsory deterministic lag law,
- no branch mixing with dark matter or photon-ring amplitude.

---

# 14. Freeze wording

> HPF predicts that any propagation-induced timing residue from finite substrate discreteness should appear first as an irreducible stochastic broadening floor, not as a compulsory coherent lag. The natural primitive scale is the scheduler tick \(t_{\rm sched}=L_{\rm vac}/c\). Under the current package, the leading candidate law is
> 
> $$
> \sigma_t(E,D;S_f)\sim t_{\rm sched}\sqrt{N_{\rm eff}(E,D,S_f)}\,\Gamma(S_f;b,\eta),
> $$
> 
> where \(\Gamma\) is a regime gate controlled by the common substrate spine \(\{S_{\rm blur},\eta,b\}\). The predicted signature is positive excess arrival-time variance with near-zero mean shift after separation of source and detector contributions. The note is falsified if no such propagation-induced broadening exists above the derived bound, or if the observed scaling with distance and energy is incompatible with the candidate HPF law.

---

# 15. Non-promotion clause

This file remains a **candidate note**.

It does **not**:
- enter active canon by itself,
- replace the four rewritten volumes,
- replace the Symbol Index,
- prove that scheduler-induced timing residue is closed at the same truth-status level as the current vacuum-sector branch.

Promotion would require closure of all three obligations and a separate package-level decision.

