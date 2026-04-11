# Hylo Phase Framework: Derivation of (\\Lambda) and the Dark Matter Fraction

## Provenance and Verification Record

### Consolidated Rewrite — Research-Paper-State Support Document (2026-04-10)

**Author:** Eric Keaton Porter  
**Affiliation:** Information Physics Institute (independent researcher)  
**Status:** Candidate-locked vacuum-sector support document with explicit truth-status partition  
**Purpose:** Record the actual derivation order, live truth-status assignments, and verification structure behind the current HPF (\\Lambda) and dark-matter branch without allowing historical discovery language to override present closure state.

\---

# 1\. Scope of this document

This is a **support document for the active vacuum-sector package**.

It is not the top canonical framework statement and it is not a replacement for the four rewritten canon volumes. Its role is narrower:

1. document the provenance of the live vacuum-sector chain,
2. state what was empirically anchored, what was derived, what is candidate-locked, and what remains open,
3. preserve the actual discovery sequence so the package is not rewritten into a fake top-down story,
4. record where later closure changed the status of earlier results.

The governing canon remains:

* the rewritten README,
* `Volume\_I\_Foundations`,
* `Volume\_II\_Microscopic\_Derivation`,
* `Volume\_III\_Provenance\_and\_Status`,
* `Volume\_IV\_Lambda\_and\_Dark\_Matter`,
* the rewritten `Symbol\_Index`.

This note supports those files. It does not outrank them.

\---

# 2\. Abstract

The current HPF vacuum-sector package produces the cosmological constant (\\Lambda) and the dark-matter fraction (\\Omega\_{\\rm dm}) from a single empirical blur anchor combined with substrate-native BCC Fibonacci geometry and the corrected radial branch.

The live chain is:

$$
S\_{\\rm blur}=1.05
;\\longrightarrow;
\\eta=\\frac{1}{48}
;\\longrightarrow;
k
;\\longrightarrow;
S\_{\\rm ent}=1.3806
;\\xrightarrow{n=220};
S\_{\\rm cap}=5.7889
;\\longrightarrow;
L\_{\\rm vac}=\\frac{R\_H}{\\varphi^n}
;\\longrightarrow;
\\Lambda,
$$

while the dark-matter fraction closes on a separate branch:

$$
\\varphi ;\\longrightarrow; b ;\\longrightarrow; f\_{\\rm coh} ;\\longrightarrow; \\alpha\_{\\rm vac}=\\sqrt{f\_{\\rm coh}} ;\\longrightarrow; \\Omega\_{\\rm dm}=1-\\alpha\_{\\rm vac}.
$$

The document preserves two facts simultaneously:

* the derivation was **actually developed bottom-up**, not as a finished theorem tree from the start;
* several items that were originally historical discoveries are now live as **derived / substrate-native** or **candidate-locked** objects in the current package.

Current benchmark outputs retained by the package:

|Quantity|HPF output|Observed|Gap|
|-|-:|-:|-:|
|(\\Lambda)|(1.081\\times10^{-52}\\ {\\rm m^{-2}})|(1.1\\times10^{-52}\\ {\\rm m^{-2}})|(10^{-0.008})|
|(\\Omega\_{\\rm dm})|(26.29%)|(26.8%)|(0.51%)|

\---

# 3\. Truth-status partition used in this note

The provenance note uses the following labels exactly:

* **Empirically anchored under HPF mapping**
* **Derived / substrate-native**
* **Candidate-locked**
* **Proved internally within current HPF canon**
* **Candidate interpretation**
* **Historical discovery path**
* **Open**

This note must not blur those categories.

\---

# 4\. Single empirical anchor

## 4.1 Definition

$$
S\_{\\rm blur}=1.05.
$$

## 4.2 Status

**Status:** **Empirically anchored under HPF mapping**

## 4.3 Provenance

The HPF vacuum-sector package uses a single external empirical anchor: the coherence-loss midpoint behavior in the Lin et al. single-atom double-slit program, mapped into the HPF phase variable as the blur midpoint.

Under the current package reading:

* HPF does **not** derive (1.05) from first principles,
* HPF identifies (1.05) as the substrate-level blur threshold consistent with the observed midpoint behavior,
* the midpoint condition is
$$
\\zeta(S\_{\\rm blur})=\\frac12.
$$

This is the one free empirical input in the live phase corridor.

\---

# 5\. The Nyquist denominator

## 5.1 Definition

$$
\\eta=\\frac{1}{48}.
$$

## 5.2 Status

**Status:** **Derived / substrate-native**

## 5.3 Derivation

The BCC substrate carries (24) active spatial sectors under the 3D lift of the 8-fold coordination structure. The Nyquist criterion requires two samples per active sector to represent the phase boundary without aliasing. Therefore the minimum non-zero residual margin is

$$
\\eta=\\frac{1}{2\\times 24}=\\frac{1}{48}.
$$

No free fit parameter is introduced.

## 5.4 Present package significance

This denominator is now one of the hardest anchors in the package. It controls:

* the residual blur margin,
* the logistic steepness through the (\\ln(47)) relation,
* the active phase corridor,
* the `S\_cap` closure chain,
* candidate phenomenology lanes that reuse the same denominator.

\---

# 6\. Gate steepness and phase onset

\---

# 6\. Gate steepness and phase onset

## 6.1 Gate definition

$$
\\zeta(S)=\\frac{1}{1+e^{k(S-1.05)}}.
$$

The midpoint is fixed at (S\_{\\rm blur}=1.05), so
$$
\\zeta(1.05)=\\frac12.
$$

## 6.2 Steepness parameter

Using the Nyquist residual (\\eta=1/48) and the onset target (S\_\*=1.3806),

$$
k=\\frac{\\ln!\\left(\\frac{1-\\eta}{\\eta}\\right)}{S\_*-1.05}
=\\frac{\\ln 47}{S\_*-1.05}
\\approx 11.646.
$$

Operational rounded value:
$$
k=11.
$$

## 6.3 Truth-status

* (\\eta): **derived / substrate-native**
* (k): **derived**
* operational (k=11): **rounded implementation value**

## 6.4 Entropy onset

The live onset is

$$
S\_{\\rm ent}=1.3806.
$$

**Status:** **derived / substrate-native phase landmark in the current package**

Historical note:

* `1.4` was the earlier rounded onset marker,
* `1.3806` is the sharpened live onset,
* the old `1.4` marker is historical only and must not be used as the live lower selector bound.

SI mantissa correspondences are not part of the derivation chain itself: the HPF wall values are derived / substrate-native in-package, while the external identifications \\(1.3806 \\leftrightarrow k\_B\\) and \\(5.7889 \\leftrightarrow \\mu\_B\\) remain candidate-level and are not claimed as first-principles SI derivations.

\---

# 7\. Saturation ceiling (S\_{\\rm cap})

## 7.1 Definition

$$
S\_{\\rm cap}=5.7889.
$$

## 7.2 Present truth-status

**Status:** **derived / substrate-native**

This is the live package status and must control all rewritten material.

## 7.3 Historical discovery path

Historically, `S\_cap` was first found by binary search on a geometric stability probe: a tanh bottleneck autoencoder was driven through increasing noise until the collapse boundary was isolated. The probe converged to (5.7889).

That remains the historical discovery path.

## 7.4 Live closure state

Later work showed that `S\_cap` is not merely a discovered number waiting for theory. In the current package it is forced by the chain:

$$
\\text{BCC} \\rightarrow \\eta=\\frac{1}{48} \\rightarrow k \\rightarrow S\_{\\rm ent}=1.3806 \\xrightarrow{n=220} S\_{\\rm cap}=5.7889.
$$

Equivalently: `S\_cap` is the ceiling that the BCC 24-sector conversion law demands once the selector and live lower onset are fixed.

## 7.5 Probe / derivation reconciliation

In the step-limit approximation,

$$
S\_{\\rm cap}\\approx S\_{\\rm ent}+220\\frac{\\ln\\varphi}{24}=5.7917.
$$

The small residual gap to the probe value is accounted for by the finite-(k) correction of the logistic tail. That is why the probe and the derived closure agree without exact step-function collapse.

## 7.6 What is no longer allowed

The following older phrasing is no longer live:

* “`S\_cap` is empirically found but theoretically open.”

That was true at an earlier stage. It is no longer the correct package status.

\---

# 8\. The shell selector

## 8.1 Definition

$$
n\_{\\rm sel}=\\mathrm{round}!\\left\[
\\frac{24}{\\ln\\varphi}
\\int\_{S\_{\\rm ent}}^{S\_{\\rm cap}}(1-\\zeta(S)),dS
\\right].
$$

## 8.2 Numerical confirmation

Using the live corridor:

$$
\\int\_{1.3806}^{5.7889}(1-\\zeta(S)),dS = 4.4059,
$$

so

$$
n\_{\\rm raw}=
\\frac{24}{\\ln\\varphi}\\times 4.4059
=219.742,
$$

and therefore

$$
n\_{\\rm sel}=\\mathrm{round}(219.742)=220.
$$

## 8.3 Truth-status

**Status:** **candidate-locked**

The selector is numerically robust and structurally stable, but the package does not presently overstate it as a uniqueness theorem.

## 8.4 Critical lower-bound distinction

The integral begins at (S\_{\\rm ent}=1.3806), not at (S\_{\\rm blur}=1.05).

That distinction is mandatory.

Using (1.05) as the lower bound produces the wrong shell count ((\\approx 233)) and is therefore not the live selector.

\---

# 9\. Corrected radial law and (\\Lambda)

## 9.1 Corrected radial identity

$$
L\_{\\rm vac}=\\frac{R\_H}{\\varphi^n}.
$$

No factor of `/2` belongs in this radial identity.

## 9.2 Truth-status

**Status:** **proved internally within current HPF canon**

The older `/2` radial form arose from double-counting bipartite half-active support in a relation where it does not belong. It is retired from the active package.

## 9.3 Lambda branch

With (n=220) and (R\_H=c/H\_0),

$$
L\_{\\rm vac}=\\frac{R\_H}{\\varphi^{220}} \\approx 1.447\\times10^{-20}\\ {\\rm m}.
$$

The live branch then yields

$$
\\Lambda \\approx 1.081\\times10^{-52}\\ {\\rm m^{-2}}.
$$

## 9.4 Truth-status

**Status:** **candidate-locked**

The branch is structurally strong and numerically tight, but it still uses (H\_0) as an external consistency anchor. That is why the package keeps the strongest-form derivation item open.

\---

# 10\. Dark-matter branch

## 10.1 Spiral parameter

$$
b=\\frac{\\ln\\varphi}{\\pi/2}=0.306349.
$$

**Status:** **derived / substrate-native**

## 10.2 Coherent support fraction

$$
f\_{\\rm coh}=\\frac{1}{2\\pi b}\\sqrt{1+b^2}=0.543354.
$$

**Status:** **derived / substrate-native**

## 10.3 Governor transfer

$$
\\alpha\_{\\rm vac}=\\sqrt{f\_{\\rm coh}}=0.737125.
$$

**Status:** **proved internally within current HPF canon under governing assumption**

This is not claimed as assumption-free uniqueness outside the HPF framework.

## 10.4 Dark-matter fraction

$$
\\Omega\_{\\rm dm}=1-\\alpha\_{\\rm vac}=0.2629.
$$

**Status:** **derived under governing assumption**

## 10.5 Interpretation status

The physical reading of (1-\\alpha\_{\\rm vac}) as the load fraction that suppresses local update availability without appearing in the effective electromagnetic theory remains a **candidate interpretation**.

That means:

* the number is derived,
* the identification with observed dark-matter behavior is the interpretive step.

\---

# 11\. Actual development sequence

To prevent retrodictive rewriting, the actual chronology is preserved here.

1. Early engine era used (k=5.0), (S\_{\\rm blur}=1.05), and PHI\_GRID as the initial action-grid normalization.
2. The geometric stability probe found (S\_{\\rm cap}\\approx 5.7889) first.
3. The blur anchor (1.05) was stabilized from the external coherence-loss midpoint under HPF mapping.
4. The approximate onset marker `1.4` was identified and later sharpened to (1.3806).
5. BCC Fibonacci substrate structure was developed independently after the probe work.
6. The phase integral confirmed (n=220).
7. The corrected radial branch produced the live (\\Lambda) output.
8. The spiral/governor branch produced the live (\\Omega\_{\\rm dm}) output.
9. Later closure work upgraded `S\_cap` from historical discovery to derived / substrate-native status.
10. Later external work provided corroboration of the denominator (48), but that did not serve as an input to the original derivation.

This chronology matters because it blocks false accusations of back-fitting to later outputs.

\---

# 12\. Open items that remain genuinely open

The following remain open and should be stated plainly:

1. **Uniqueness of the 24-sector Nyquist application**  
Why the 24-sector lift is the uniquely correct Nyquist object rather than 8 or 48 in some alternative framing.
2. **Governor-transfer uniqueness**  
The single square-root is proved internally within the HPF governing assumption, but not yet as an assumption-free uniqueness theorem.
3. **Strongest-form (\\Lambda) derivation**  
The present branch still uses (H\_0) as the external consistency anchor.

These items are open. They should not be hidden behind polished prose.

\---

# 13\. Material explicitly decapitated from canonical HPF scope

The following does not belong in current canonical HPF:

* optimizer-fit Hubble-tension amplitudes such as (\\varepsilon=0.134,\\ 0.124,\\ 0.083),
* late exploratory observational-fit artifacts that were never substrate-native,
* any attempt to promote those fit residuals into live framework claims.

This decapitation matters because it keeps exploratory phenomenology from contaminating the derivation package.

\---

# 14\. Consolidated truth-status table

|Claim / object|Status|
|-|-|
|(S\_{\\rm blur}=1.05)|Empirically anchored under HPF mapping|
|(\\eta=1/48)|Derived / substrate-native|
|(k) from (\\ln 47) relation|Derived|
|(S\_{\\rm ent}=1.3806)|Derived / substrate-native|
|(S\_{\\rm cap}=5.7889)|Derived / substrate-native|
|(n=220)|Candidate-locked|
|corrected no-/2 radial law|Proved internally within current HPF canon|
|(\\Lambda\\approx1.081\\times10^{-52}\\ {\\rm m^{-2}})|Candidate-locked|
|(b), (f\_{\\rm coh})|Derived / substrate-native|
|(\\alpha\_{\\rm vac}=\\sqrt{f\_{\\rm coh}})|Proved internally within current HPF canon under governing assumption|
|(\\Omega\_{\\rm dm}=26.29%)|Derived under governing assumption|
|dark-matter interpretation of (1-\\alpha\_{\\rm vac})|Candidate interpretation|
|SI mantissa alignments|External candidate identifications only; not first-principles SI derivations|

\---

# 15\. Freeze wording

> The live HPF vacuum-sector package uses one empirical blur anchor, \\(S\_{\\rm blur}=1.05\\), together with substrate-native BCC Fibonacci geometry. From the 24-sector Nyquist law it derives \\(\\eta=1/48\\), then the gate steepness \\(k\\), the live entropy onset \\(S\_{\\rm ent}=1.3806\\), the candidate-locked selector \\(n=220\\), and the saturation ceiling \\(S\_{\\rm cap}=5.7889\\), which is now treated as derived / substrate-native rather than theoretically open. The corrected no-/2 radial law then yields the current \\(\\Lambda\\) branch, while the separate spiral-governor branch yields \\(\\Omega\_{\\rm dm}=26.29\\%\\). Historical discovery order is preserved, but later closure states control the live package.

\---

# 16\. Non-promotion clause

This document remains a **support note for the active vacuum-sector package**.

It does **not**:

* replace Volume I as framework authority,
* replace Volume III as package-governance authority,
* collapse candidate interpretation into canon,
* upgrade open items into solved items by presentation style alone.

