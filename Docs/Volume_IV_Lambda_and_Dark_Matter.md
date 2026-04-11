# HPF Canonical Derivation Package

## First-Principles Derivation of Λ and the Dark-Matter Fraction

### Consolidated Rewrite — Milestone Lock State (2026-04-10)

**Author:** Eric Keaton Porter  
**Framework:** Hylo Phase Framework (HPF)  
**Role of this volume:** This is the live vacuum-sector derivation package. It states the active derivation of the cosmological constant (\\Lambda) and the dark-matter fraction (\\Omega\_{\\rm dm}), with explicit truth-status partition, corrected branch separation, and updated provenance alignment.

\---

# 1\. What this volume claims

HPF is not presented here as a theory of everything. It is a regulatory architecture — a physics OS — that governs when expert theories are operating within legal bounds, when they remain numerically valid, and when they must hand off to deeper substrate authority. The present volume applies that architecture to the vacuum sector.

The active derivation remains split into two branches.

## 1.1 Lambda branch

\[
S\_{\\rm blur}=1.05
;\\longrightarrow;
\\eta=\\frac{1}{48}
;\\longrightarrow;
k
;\\longrightarrow;
S\_{\\rm ent}=1.3806
;\\longrightarrow;
S\_{\\rm cap}=5.7889
;\\longrightarrow;
n=220
;\\longrightarrow;
L\_{\\rm vac}
;\\longrightarrow;
\\Lambda
]

## 1.2 Dark-matter branch

\[
b
;\\longrightarrow;
f\_{\\rm coh}
;\\longrightarrow;
\\alpha\_{\\rm vac}=\\sqrt{f\_{\\rm coh}}
;\\longrightarrow;
\\Omega\_{\\rm dm}=1-\\alpha\_{\\rm vac}
]

## 1.3 Active outputs

|Quantity|HPF output|Observed|Gap|
|-|-:|-:|-:|
|(\\Lambda)|(1.081\\times 10^{-52},\\mathrm{m}^{-2})|(1.1\\times 10^{-52},\\mathrm{m}^{-2})|(10^{-0.008})|
|(\\Omega\_{\\rm dm})|(26.29%)|(26.8%)|(0.51%)|

These are the live package outputs. They are not derived by mixing the two branches ad hoc. The old mixed branch is retired.

\---

# 2\. Truth-status partition

This volume must be read with the same truth-status discipline used across the rewritten package.

## 2.1 Derived / substrate-native

* (\\eta=1/48) from BCC 24-sector Nyquist geometry
* (b=\\ln\\phi/(\\pi/2))
* (\\kappa\_{\\rm BCC}=8\\times \\frac12 \\times \\frac12 = 2)
* the corrected radial law (L\_{\\rm vac}=R\_H/\\phi^n)
* the governor-transfer map (\\alpha\_{\\rm vac}=\\sqrt{f\_{\\rm coh}})

## 2.2 Empirically anchored under HPF mapping

* (S\_{\\rm blur}=1.05), calibrated to the half-blur / midpoint behavior in the single-atom double-slit line

## 2.3 Candidate-locked

* (n=220) as the shell selector
* the active vacuum branch closure package as presently written

## 2.4 Historical discovery path but not live source of authority

* the original binary-search probe that first located (S\_{\\rm cap}=5.7889)

## 2.5 Superseded language

* any wording that treats the `/2` radial identity as live
* any wording that treats (1.4) as the active lower onset in place of (1.3806)
* any wording that leaves the theoretical grounding of (S\_{\\rm cap}) open

\---

# 3\. The corrected radial law

The active radial identity is:

\[
R\_H=L\_{\\rm vac}\\phi^n,
\\qquad
L\_{\\rm vac}=\\frac{R\_H}{\\phi^n}.
]

No `/2` belongs in this identity.

The earlier `/2` factor came from importing bipartite half-active support into a radial relation where it does not belong. Bipartite support geometry still matters elsewhere, but not in radial closure.

This correction is active canon and governs the present derivation.

\---

# 4\. Lattice identity and scheduler scale

The substrate primitive can be written three ways:

\[
L\_{\\rm vac}=c,t\_{\\rm sched}.
]

In substrate units, these are the same primitive under three descriptions:

* (c): substrate propagation limit
* (t\_{\\rm sched}): scheduler tick
* (L\_{\\rm vac}): lattice spacing at the vacuum branch scale

This identifies the scheduler-time primitive. It does **not** import the stochastic-jitter candidate lane into the present derivation. That lane remains separate unless explicitly bridged later.

\---

# 5\. BCC geometric inputs

## 5.1 BCC coefficient

The active BCC geometric coefficient is:

\[
\\kappa\_{\\rm BCC}=8\\times \\frac12 \\times \\frac12 = 2.
]

The factors are:

* coordination number (8),
* bipartite split (\\tfrac12),
* LMS mirror factor (\\tfrac12).

Status: exact, substrate-native, zero free parameters.

## 5.2 Fibonacci update law

At scheduler coarse-grain, the BCC bipartite reversible update structure yields the Fibonacci recurrence. The Continue/Branch global scheduler partition remains the live derivational route:

\[
C(n)=C(n-1)+C(n-2),
\\qquad
\\phi=\\lim\_{n\\to\\infty}\\frac{F(n+1)}{F(n)}.
]

This is the substrate source of (\\phi) in the vacuum branch. It is not inserted externally.

\---

# 6\. Single empirical anchor: the blur midpoint

The entire active phase structure is built from one empirical input:

\[
S\_{\\rm blur}=1.05.
]

This is not claimed as first-principles derivation. It is an empirical anchor under HPF mapping.

The single-atom double-slit line associated with Hanzhen Lin, Yu-Kun Lu, Vitaly Fedoseev, Yoo Kyung Lee, Jiahao Lyu, and Wolfgang Ketterle provides the half-blur / midpoint behavior to which HPF calibrates (S\_{\\rm blur}=1.05). In package language, this is the coherence-loss midpoint corresponding to (\\zeta=0.5). HPF uses that midpoint as the single free empirical input into the vacuum branch.

Status:

* empirical anchor,
* not substrate-derived,
* only free empirical input to the branch.

\---

# 7\. The zeta gate

The active gate law is

\[
\\zeta(S)=\\frac{1}{1+e^{k(S-1.05)}}.
]

By construction,

\[
\\zeta(S\_{\\rm blur})=\\zeta(1.05)=0.5.
]

The gate is not a phenomenological decoration. It is the corridor law governing the transition from the Einstein-side stable region into the entropy-active transition band and finally to the capacity wall.

\---

# 8\. The non-negotiable denominator: (\\eta=1/48)

This is a tier-one structural object in the framework and must not be buried or softened.

## 8.1 Derivation

\[
\\eta=\\frac{1}{2\\times 24}=\\frac{1}{48}.
]

Derivation:

* the BCC substrate has (24) active sectors under the 3D lift of 8-fold coordination,
* Nyquist sampling requires twice the sector count to represent the phase boundary without aliasing,
* the minimum non-zero residual margin is therefore one part in (48).

So:

\[
\\eta=\\frac{1}{48}=0.020833\\ldots
]

Status:

* derived / substrate-native,
* zero free parameters,
* not fitted to observation.

\---

# 9\. Derivation of (k) and the lower wall

With (S\_{\\rm blur}=1.05), onset target (S\_{\\rm ent}=1.3806), and (\\eta=1/48), the gate steepness is:

\[
k=\\frac{\\ln!\\left(\\frac{1-\\eta}{\\eta}\\right)}{S\_{\\rm ent}-1.05}
===

\\frac{\\ln 47}{S\_{\\rm ent}-1.05}
\\approx 11.646.
]

Operational package value:
\[
k=11.
]

Exact derived value carried in the refined discussion:
\[
k\\approx 11.646.
]

The lower wall is the phase-onset value satisfying the Nyquist residual condition:

\[
S\_{\\rm ent}=1.3806.
]

This is the active lower integration bound. The old rounded (1.4) marker remains historically meaningful but is not the live lower onset.

Status:

* (k): derived from (\\eta) and the blur anchor,
* (S\_{\\rm ent}): live lower onset of the vacuum branch.

\---

# 10\. The upper wall: (S\_{\\rm cap}=5.7889)

\[
S\_{\\rm cap}=5.7889.
]

This value has two distinct roles that must be kept separate.

## 10.1 Historical discovery path

Historically, (S\_{\\rm cap}) was first located by a computational binary-search stability probe. That discovery path remains part of provenance.

## 10.2 Live structural status

The live package no longer treats the theoretical grounding of (S\_{\\rm cap}) as open. The active reading is:

\[
\\text{BCC}
;\\longrightarrow;
\\eta=\\frac{1}{48}
;\\longrightarrow;
k
;\\longrightarrow;
S\_{\\rm ent}=1.3806
;\\xrightarrow{n=220};
S\_{\\rm cap}=5.7889.
]

The April 8 closure note treats (S\_{\\rm cap}) as the ceiling forced by the BCC 24-sector geometry, the active lower wall, and the shell depth. The finite-(k) correction accounts for the small difference between the step-limit estimate and the live value.

So the correct package language is:

* historical probe = discovery path,
* substrate-native derivation = live status.

Any wording that still leaves (S\_{\\rm cap}) theoretically open is superseded.

\---

# 11\. The shell selector (n=220)

The active selector is

\[
n\_{\\rm sel}
===

\\operatorname{round}!\\left\[
\\frac{24}{\\ln\\phi}
\\int\_{S\_{\\rm ent}}^{S\_{\\rm cap}}
(1-\\zeta(S)),dS
\\right].
]

With the live values:

\[
S\_{\\rm ent}=1.3806,
\\qquad
S\_{\\rm cap}=5.7889,
\\qquad
k=11,
\\qquad
S\_{\\rm blur}=1.05,
]

one obtains

\[
\\int\_{1.3806}^{5.7889}(1-\\zeta(S)),dS = 4.4059,
]

\[
n\_{\\rm raw}=\\frac{24}{\\ln\\phi}\\times 4.4059 = 219.742,
]

\[
n=\\operatorname{round}(219.742)=220.
]

Status:

* candidate-locked,
* selected by integrated entropy-phase budget,
* not a knife-edge coincidence,
* not to be replaced by a pure (H\_0)-fit story.

(H\_0) may still appear as an external consistency anchor through (R\_H=c/H\_0), but it is not the primary selector.

\---

# 12\. Vacuum length and cosmological constant

With the corrected radial law,

\[
L\_{\\rm vac}=\\frac{R\_H}{\\phi^n}.
]

Taking
\[
n=220,
\\qquad
R\_H=\\frac{c}{H\_0},
\\qquad
H\_0=67.4;\\mathrm{km,s^{-1},Mpc^{-1}},
]

gives the active vacuum length scale

\[
L\_{\\rm vac}\\approx 1.45\\times 10^{-20},\\mathrm{m}.
]

The cosmological constant then follows from the live vacuum branch relation:

\[
\\Lambda \\sim \\frac{1}{L\_{\\Lambda}^{,2}}
]

with the active HPF identification yielding

\[
\\Lambda \\approx 1.081\\times 10^{-52},\\mathrm{m}^{-2}.
]

This is the live package output.

Status:

* branch result of the active selector and corrected radial law,
* candidate-locked at package level.

\---

# 13\. The dark-matter branch

The dark-matter branch does **not** run through the entropy-phase selector. It runs through coherent support geometry and the governor-transfer theorem.

## 13.1 Coherent support fraction

The coherent support fraction is

\[
f\_{\\rm coh}
===

\\frac{1}{2\\pi b}\\sqrt{1+b^2},
\\qquad
b=\\frac{\\ln\\phi}{\\pi/2}.
]

Numerically,

\[
b\\approx 0.306349,
\\qquad
f\_{\\rm coh}\\approx 0.543354.
]

## 13.2 Governor transfer

HPF requires one and only one square-root transfer from support reservoir to update availability:

\[
\\alpha\_{\\rm vac}=\\sqrt{f\_{\\rm coh}}.
]

Numerically,

\[
\\alpha\_{\\rm vac}=\\sqrt{0.543354}\\approx 0.737125.
]

## 13.3 Dark-matter complement

The dark-matter fraction is then

\[
\\Omega\_{\\rm dm}=1-\\alpha\_{\\rm vac}.
]

So

\[
\\Omega\_{\\rm dm}=1-0.737125=0.262875=26.29%.
]

This is not the raw geometric remainder (1-f\_{\\rm coh}). The raw remainder is not yet the observable variable. The governor transfer must occur first.

Status:

* the square-root governor transfer is proved internally within HPF canon,
* (\\Omega\_{\\rm dm}=26.29%) is the live branch output.

\---

# 14\. The two-wall common spine

The lower and upper walls are not independent fits. Their current common spine is

\[
{S\_{\\rm blur},\\eta}=\\left{1.05,\\frac{1}{48}\\right}.
]

These two objects enter the walls differently:

* (S\_{\\rm blur}=1.05) anchors the gate midpoint,
* (\\eta=1/48) sets both the residual resolution condition at onset and the explicit residual margin in the upper-wall closure stack.

The package therefore treats the vacuum corridor as a regulated architecture, not as two unrelated numerological hits.

\---

# 15\. Functional resonance note

The package continues to record the constant-shadow pattern:



\- \\(1.05\\) and the \\(\\hbar\\)-side patterning,

\- \\(1.3806\\) and the \\(k\_B\\) mantissa,

\- \\(5.7889\\) and the \\(\\mu\_B\\) mantissa.



But the wall values themselves are not treated as free functional resonances inside the live package. \\(S\_{\\rm ent}=1.3806\\) and \\(S\_{\\rm cap}=5.7889\\) are derived wall values of the anchored closure chain. What remains candidate-level is the external identification of those wall values with SI constants.



Accordingly:



\- \\(1.3806 \\leftrightarrow k\_B\\) is retained as an empirically anchored candidate correspondence, not a first-principles SI derivation.

\- \\(5.7889 \\leftrightarrow \\mu\_B\\) is retained as a weaker ceiling-side candidate correspondence, not a first-principles SI derivation.



No part of this note is to be written as a completed SI-unit derivation.

\---

# 16\. What this volume does not claim

This volume does **not** claim:

* that the dark-matter result identifies a specific particle species,
* that the shell selector (n=220) is a uniqueness theorem rather than candidate-lock,
* that all phenomenology notes are promoted into canon.

This volume also excludes contamination material and does not draw from non-HPF documents.

\---

# 17\. Freeze wording

> The active HPF vacuum-sector package derives \\(\\Lambda\\) and the dark-matter fraction through two regulated branches. The lambda branch runs from the empirical blur anchor \\(S\_{\\rm blur}=1.05\\) through the substrate-native Nyquist denominator \\(\\eta=1/48\\), the live lower onset \\(S\_{\\rm ent}=1.3806\\), the live ceiling \\(S\_{\\rm cap}=5.7889\\), the candidate-locked shell selector \\(n=220\\), and the corrected no-`/2` radial law \\(L\_{\\rm vac}=R\_H/\\phi^n\\), yielding \\(\\Lambda\\approx 1.081\\times 10^{-52}\\,\\mathrm{m}^{-2}\\). The dark-matter branch runs from the Fibonacci boundary parameter \\(b\\) through the coherent support fraction \\(f\_{\\rm coh}\\), the unique governor-transfer map \\(\\alpha\_{\\rm vac}=\\sqrt{f\_{\\rm coh}}\\), and the complement \\(\\Omega\_{\\rm dm}=1-\\alpha\_{\\rm vac}=26.29\\%\\). The denominator \\(\\eta=1/48\\) is treated here as a structural anchor derived from BCC 24-sector Nyquist geometry with zero free parameters.

\---

# 18\. References used by this volume

1. H. Lin, Y.-K. Lu, V. Fedoseev, Y. K. Lee, J. Lyu, and W. Ketterle, *Fringe visibility and which-way information in Young's double slit experiments with light scattered from single atoms* (2025 preprint / 2026 journal line).
2. `Reference/HPF\_Derivation\_Provenance\_2026-3.md`
3. `Reference/HPF\_Development\_History-4.md`
4. `Reference/HPF\_Scap\_SubstrateNative\_Derivation.md`
5. `Reference/Governor\_Transfer\_Theorem.md`
6. `Reference/Delta\_Collapse\_Theorem\_Note\_v7U.md`
7. `Reference/Symbol\_Index.md`

