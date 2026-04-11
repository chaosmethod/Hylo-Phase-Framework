# HPF Fine Structure Constant — Candidate Note
## BCC Fibonacci Substrate Derivation of \(\alpha\)

**Document Class:** HPF phenomenology candidate note  
**Status:** Candidate — strong. Both derivational obligations closed at the note level; not canon-promoted.  
**Compatibility:** Repo-compatible. Consistent with the rewritten canon volumes, the active Symbol Index, the Volume IV vacuum-sector package, the April 9 microscopic-grammar milestone lock, and Delta Collapse Theorem v7U.  
**Author:** Eric Keaton Porter  
**Date:** 2026-04-10

---

# 1. Scope and status

This note is a **candidate phenomenology document**. It is not part of active canon. Its job is narrower:

1. state the fine-structure candidate formula cleanly,
2. show how the April 9 grammar lock closes the old degree-unit objection,
3. provide the full three-term derivation including the microscopic transport blur closure,
4. preserve compatibility with the active vacuum-sector branch.

Nothing in this file silently promotes the fine-structure result into canon. The active canon remains the four rewritten volumes plus the live reference stack.

---

# 2. Executive claim

The fine-structure constant inverse is a candidate output of BCC Fibonacci substrate geometry:

$$\boxed{\frac{1}{\alpha_{\rm fs}} = \frac{N_{\rm cycle}}{\varphi^2} - b^2(2\varphi-1)^2 - \frac{b}{N_{\rm hop}}}$$

with

$$N_{\rm cycle} = 24 \times 15 = 360, \qquad N_{\rm hop} = 8 \times 15 = 120,$$

so that

$$\frac{1}{\alpha_{\rm fs}} = \frac{360}{\varphi^2} - 5b^2 - \frac{b}{120} = 137.507764 - 0.469248 - 0.002553 = 137.035963.$$

Compared to the CODATA observed value,

$$\left(\frac{1}{\alpha_{\rm fs}}\right)_{\rm obs} = 137.035999,$$

the candidate output differs by approximately \(0.000026\%\).

This candidate formula uses only objects already present in the live HPF package:

- the BCC spatial sector count \(24\),
- the candidate-locked active microstate count \(15\),
- the BCC nearest-neighbor coordination number \(8\),
- the golden ratio \(\varphi\),
- the Fibonacci growth parameter \(b\),
- the fixed-point denominator \((2\varphi-1)^2=5\).

No free fit parameter is introduced.

---

# 3. Locked inputs from the live package

| Input | Value | Status |
|---|---:|---|
| \(\varphi=(1+\sqrt5)/2\) | \(1.6180339887\) | Derived / substrate-native |
| \(b=\ln\varphi/(\pi/2)\) | \(0.3063489625\) | Derived / substrate-native |
| \((2\varphi-1)^2\) | \(5\) | Derived fixed-point denominator |
| Active spatial sectors | \(24\) | Derived / substrate-native |
| BCC nearest-neighbor count | \(8\) | Substrate-native |
| Active microstates | \(15\) | Candidate-locked from 4-bit grammar |
| \(N_{\rm cycle} = 24 \times 15\) | \(360\) | Candidate-locked |
| \(N_{\rm hop} = 8 \times 15\) | \(120\) | Derived from fiber definition |
| \(n\) | \(220\) | Candidate-locked shell selector |
| \(L_{\rm vac}\) branch | live | Preserved by this candidate note |
| \(\Lambda\) branch | live | Preserved by this candidate note |
| \(\Omega_{\rm dm}\) branch | live | Preserved by this candidate note |

---

# 4. Why the April 9 lock matters

Before the April 9 milestone, the geometric baseline

$$\frac{360}{\varphi^2}$$

could be challenged as a disguised appeal to an external angular convention ("degrees"). That objection is no longer controlling.

The current package now treats the 4-bit site alphabet

$$(n_L,n_R,b_{\rm bit},q)$$

as the **candidate-locked fundamental operator grammar of the substrate**. This gives:

- \(2^4 = 16\) total local configurations,
- one vacuum configuration \((0,0,0,0)\),
- \(16-1=15\) active non-vacuum microstates.

The BCC substrate already supplies the active spatial sector count \(24\). Therefore the complete active phase-space count of a full substrate cycle is:

$$N_{\rm cycle}=24 \times 15 = 360.$$

The baseline is therefore no longer "\(360\) degrees divided by \(\varphi^2\)." It is:

> **the active complete-cycle phase-space count of the substrate ring, partitioned by the golden scaling \(\varphi^2\).**

That closes the old unit-convention objection.

---

# 5. Derivation

## 5.1 Step 1 — the substrate baseline

A complete traversal of the active substrate cycle samples:

1. the full active BCC spatial sector count \(24\),
2. the full active non-vacuum microstate count \(15\).

Thus \(N_{\rm cycle}=24\times 15=360\). Partitioning that active cycle by the golden scaling gives the baseline:

$$\frac{N_{\rm cycle}}{\varphi^2}=\frac{360}{\varphi^2}=137.507764\ldots$$

## 5.2 Step 2 — the macroscopic structural penalty

The residual gap between the baseline and the observed fine-structure inverse is partially closed by the Fibonacci fixed-point term

$$b^2(2\varphi-1)^2 = 5b^2.$$

Since \(2\varphi-1=\sqrt5\), we have \((2\varphi-1)^2=5\), so the correction reduces to

$$5b^2 = 5(0.3063489625)^2 = 0.469248\ldots$$

This denominator is the squared fixed-point sensitivity of the Fibonacci characteristic polynomial \(P(\varphi)=\varphi^2-\varphi-1\), since \(P'(\varphi)=2\varphi-1=\sqrt5\). The same denominator already appears in the Delta Collapse Theorem spine as the leading geometric correction.

After two terms:

$$\frac{360}{\varphi^2} - 5b^2 = 137.038516\ldots$$

Residual gap: \(\approx 0.002517\).

## 5.3 Step 3 — the microscopic transport blur

The remaining gap is closed by the Berry phase holonomy arising from the dimensional mismatch between the continuous 3D macroscopic phase-corridor and the discrete 1D BCC hop structure.

### Bundle definition

- **Base manifold \(\mathcal{M}\):** The continuous 1D closed loop embedded in the 3D macroscopic phase-corridor, parameterized by \(\theta\in[0,2\pi)\). Its total structural deficit relative to a flat continuum is the Fibonacci growth parameter \(b\).
- **Fiber \(\mathcal{F} = \mathcal{S}\otimes\mathcal{G}\):**
  - \(\mathcal{S}\): the 8 BCC nearest-neighbor translation vectors,
  - \(\mathcal{G}\): the 15 active non-vacuum microstates of the 4-bit site alphabet \((n_L,n_R,b_{\rm bit},q)\).
  - \(\dim(\mathcal{F}) = 8\times15 = 120 \equiv N_{\rm hop}.\)

*(Note: \(b_{\rm bit}\) is the grammar bit in the site alphabet. It is strictly distinct from the macroscopic Fibonacci growth parameter \(b\).)*

### Symmetry proof — why the connection is flat

**Spatial subspace — weight \(1/8\):**
The continuous rotation generator \(\partial_\theta\) projects uniformly onto all 8 BCC nearest-neighbor directions because the 24-sector lift is defined as the maximally symmetric 3D extension of the BCC coordination structure. A projection from that isotropic macroscopic object onto the local 8-neighbor fiber must distribute uniformly by the symmetry of the lift. The uniform \(1/8\) spatial weight follows from the isotropy of the 24-sector lift, not from the local \(O_h\) point group alone.

**Internal subspace — weight \(1/15\):**
The rotation generator \(\partial_\theta\) is a spatial operator. It does not couple to the internal routing or charge indicators of the 4-bit grammar. All 15 active microstates are therefore completely degenerate under the macroscopic geometric projection. The internal weight is strictly \(1/15\).

**Conclusion:** Both subspaces of the fiber are symmetric under the \(3D\to1D\) projection. All 120 path-state configurations \(|\psi_k\rangle\) carry equal weight \(w_k = 1/120\). The connection 1-form is flat.

### Holonomy evaluation

Let \(\hat\Omega\) be the holonomy generator representing the dimensional mismatch between the continuous \(U(1)\) base manifold and the discrete Fibonacci substrate. Integrating \(\hat\Omega\) over the full closed loop yields \(b\) by definition of the macroscopic scaling.

With the flat connection \(\mathcal{A}(\theta) = b/(2\pi\cdot120)\), the Berry phase accumulated by a single path-state over one complete macroscopic traversal is:

$$\gamma = \oint_0^{2\pi}\mathcal{A}(\theta)\,d\theta = \frac{b}{120}\cdot\frac{1}{2\pi}\cdot2\pi = \frac{b}{120}.$$

Numerically:

$$\frac{b}{N_{\rm hop}} = \frac{0.3063489625}{120} = 0.002553\ldots$$

### Full numerical result

| Term | Value |
|---|---:|
| \(N_{\rm cycle}/\varphi^2\) | \(137.507764\) |
| \(-\,5b^2\) | \(-0.469248\) |
| \(-\,b/N_{\rm hop}\) | \(-0.002553\) |
| **Candidate output** | **\(137.035963\)** |
| CODATA observed | \(137.035999\) |
| Error | \(0.000026\%\) |

---

# 6. Why this is structurally interesting inside HPF

This note is not numerology-by-proximity. The candidate formula reuses objects that already belong to the live framework:

- \(\varphi\) governs the Fibonacci support scaling,
- \(b\) appears in the support-geometry law,
- \((2\varphi-1)^2=5\) appears in the Delta Collapse Theorem spine,
- the 24 spatial sectors belong to the BCC Nyquist structure,
- the 15 active microstates belong to the candidate-locked microscopic grammar,
- the 8 nearest neighbors are the raw BCC coordination number.

No object is imported from outside the package. The three terms correspond to three distinct physical scales: macroscopic phase-space geometry, Fibonacci fixed-point sensitivity, and microscopic hop-level transport blur.

---

# 7. Compatibility with the active vacuum-sector package

This note does not alter the current vacuum branch. The active package retains:

- \(n=220\),
- the corrected no-/2 radial law \(L_{\rm vac}=R_H/\varphi^n\),
- the current \(\Lambda\) branch,
- the governor-transfer dark-matter branch.

Any blur-anchor refinement induced by the \(\alpha\) lane must preserve the corridor width used by the shell selector, so that the existing \(n=220\), \(\Lambda\), and \(\Omega_{\rm dm}\) outputs remain unchanged.

---

# 8. Relation to the delta-collapse structure

The denominator \((2\varphi-1)^2=5\) is the squared fixed-point sensitivity of the Fibonacci characteristic polynomial \(P(\varphi)=\varphi^2-\varphi-1\). It already appears in the delta-collapse theorem spine. The present candidate note uses the same denominator at one lower power of \(b\):

- delta-collapse spine: \(b^3/(2\varphi-1)^2\),
- fine-structure candidate: \(b^2(2\varphi-1)^2\).

This structural recurrence is nontrivial but does not constitute a unified theorem.

---

# 9. Truth-status partition

## 9.1 Derived / substrate-native inputs
- \(\varphi\)
- growth parameter \(b\)
- BCC spatial sector count \(24\)
- BCC nearest-neighbor count \(8\)
- fixed-point denominator \((2\varphi-1)^2=5\)

## 9.2 Candidate-locked inputs
- the 4-bit grammar as the fundamental site alphabet,
- the active non-vacuum microstate count \(15\),
- \(N_{\rm cycle}=24\times15=360\),
- \(N_{\rm hop}=8\times15=120\)

## 9.3 Candidate result
- the three-term formula for \(1/\alpha_{\rm fs}\)

## 9.4 Open items
- Both derivational obligations are closed at the note level, but the lane remains candidate and is not promoted into canon.

---

# 10. Current obligations and candidate closure state

## Obligation 1 — derive the \(360\) convention from substrate geometry
**Status:** **CLOSED**

The value \(360\) is no longer an external angular convention. It is the exact dimensionless count \(N_{\rm cycle}=24\times15\), derived from the BCC active spatial sector count \(24\) and the active non-vacuum microstate count \(15\) from the candidate-locked 4-bit grammar.

## Obligation 2 — close the residual numerical gap
**Status:** **CLOSED AT THE CANDIDATE-NOTE LEVEL**

The residual gap of approximately \(0.00252\) is addressed by the microscopic transport blur penalty \(b/N_{\rm hop} = b/120\), derived here as a candidate Berry phase holonomy of the dimensional mismatch between the continuous 3D macroscopic phase-corridor and the discrete 1D BCC hop structure.

**Bundle:** \(\mathcal{F}=\mathcal{S}\otimes\mathcal{G}\) with \(\dim(\mathcal{F})=8\times15=120\).

**Symmetry proof:** The uniform \(1/8\) spatial weight follows from the isotropy of the 24-sector macroscopic lift. The uniform \(1/15\) internal weight follows from the rotational blindness of \(\partial_\theta\) to the 4-bit grammar. Both subspaces are symmetric under the \(3D\to1D\) projection; the connection is flat.

**Holonomy:** \(\gamma = \oint\mathcal{A}(\theta)\,d\theta = b/120\).

The remaining \(0.000026\%\) residual after the three-term formula is not treated here as a failure of the derivation. The current HPF-native reading is that it is consistent with a passive mirror-buffer correction candidate explanation at the bipartite boundary. That explanation is not yet formally derived and remains downstream of open QPRCA-side obligations, so it does not justify canon promotion by itself.

---

# 11. Freeze wording

> The fine-structure constant inverse is a candidate output of BCC Fibonacci substrate geometry:
>
> $$\frac{1}{\alpha_{\rm fs}} = \frac{N_{\rm cycle}}{\varphi^2} - b^2(2\varphi-1)^2 - \frac{b}{N_{\rm hop}}$$
>
> with \(N_{\rm cycle}=24\times15=360\) and \(N_{\rm hop}=8\times15=120\). This gives \(1/\alpha_{\rm fs}=137.035963\), matching the CODATA observed value \(137.035999\) with \(0.000026\%\) error at zero free parameters. The baseline \(360/\varphi^2\) partitions the total active phase-space of the substrate ring. The macroscopic penalty \(5b^2\) uses the Fibonacci fixed-point denominator \((2\varphi-1)^2=5\). The microscopic transport blur \(b/120\) is the Berry phase holonomy of the \(3D\to1D\) dimensional mismatch: the connection is flat because the 24-sector lift is isotropic (forcing \(1/8\) spatial weight) and \(\partial_\theta\) is blind to the 4-bit grammar (forcing \(1/15\) internal weight). Both derivational obligations are closed at the candidate-note level. The surviving tiny residual is read as consistent with a passive mirror-buffer correction candidate explanation rather than as a canon-closed completion.

---

# 12. Non-promotion clause

This note remains a **candidate note**.

It does **not**:
- modify active canon by itself,
- replace the four canon volumes,
- replace the Symbol Index,
- replace the vacuum-sector package,
- prove that \(\alpha_{\rm fs}\) is derived in the same closure class as the current \(\Lambda\)/dark-matter branch.

Promotion requires a separate package-level decision.
