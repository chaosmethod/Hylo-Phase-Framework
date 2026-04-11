# HPF Photon-Ring Echo — Candidate Note
## Three Isolated Obligations

**Document Class:** HPF phenomenology candidate note  
**Status:** Candidate — not canon. Three obligations open.  
**Compatibility:** Repo-compatible. Fills the admitted amplitude gap in the active package while preserving the current vacuum-sector and provenance stack.  
**Author:** Eric Keaton Porter  
**Date:** 2026-04-10

---

# 1. Scope and status

This is a **candidate phenomenology note**. It is not part of active canon.

Its job is narrow and specific:

1. preserve the retained photon-ring location claim already carried in the package,
2. replace the old non-substrate-native amplitude fit with a substrate-native amplitude candidate,
3. isolate the exact bridges that remain open,
4. prevent exploratory photon-ring language from contaminating the truth-status discipline of the core framework.

Nothing in this file promotes the photon-ring claim into canon. The active canon remains the rewritten README, Volumes I–IV, and the live reference stack.

---

# 2. Executive summary

The active HPF package retains the photon-ring echo location

$$r_{\rm echo} = 1.05 \times r_{\rm photon}$$

as the candidate downstream manifestation of the blur boundary

$$S_{\rm blur}=1.05.$$

At the same boundary, the BCC 24-sector Nyquist law gives the minimum unresolved fraction

$$\eta = \frac{1}{48} \approx 0.02083.$$

This note proposes that the intrinsic echo amplitude is therefore the substrate-native residual

$$A_{\rm echo} = \eta = \frac{1}{48} \approx 2.08\%,$$

**but only contingently** and only if three separate bridges close:

1. the GR null-forwarding fraction must be identified as the natural GR realization of HPF \(\zeta\),
2. the \(1.05\times\) radial displacement must be derived from GR-side dynamics rather than carried only by label,
3. the Nyquist residual must be shown to project dominantly into the outgoing null mode family so that the image-plane echo flux ratio is indeed \(\eta\).

Until those are closed, the status is:

- retained location claim: candidate,
- amplitude claim: candidate,
- old fitted amplitude \(\varepsilon = 0.134\): removed and excluded from HPF scope.

---

# 3. Locked inputs from the live package

| Input | Value | Status in active package |
|---|---:|---|
| \(S_{\rm blur}\) | \(1.05\) | Locked empirical anchor under HPF mapping |
| \(\zeta(S_{\rm blur})\) | \(0.5\) | Locked by construction |
| \(\eta\) | \(1/48\) | Derived / substrate-native Nyquist residual |
| Echo location | \(1.05 \times r_{\rm photon}\) | Candidate retained in active package |
| Old amplitude \(\varepsilon = 0.134\) | removed | Explicitly removed; not substrate-native |

This note does not alter the current \(\Lambda\) / dark-matter branch, the 4-bit grammar milestone lock, or the current Symbol Index.

---

# 4. Universality Assumption (UA)

Before the three obligations, one explicit assumption must be stated.

> **Universality Assumption (UA).** The entropic flux variable \(S_f\) is a substrate-native, dimensionless load measure defined at the HPF layer prior to expert routing. The value \(S_{\rm blur}=1.05\) is the unique half-saturation blur boundary of the BCC 24-sector phase-representation law, empirically anchored to the coherence-loss midpoint in the Lin et al. experiment under HPF mapping. Because this boundary is substrate-intrinsic rather than expert-defined, any physical process whose substrate load reaches \(S_{\rm blur}\) encounters the same sector-resolution limit and the same minimum unresolved Nyquist remainder \(\eta=1/48\), while the observable downstream consequence remains domain-dependent.

## 4.1 What UA is claiming

UA claims only that:
- \(S_f\) lives upstream of expert routing,
- the blur boundary is substrate-level rather than expert-owned,
- the same substrate boundary can manifest differently in different downstream domains.

## 4.2 What UA is not claiming

UA does **not** claim:
- that \(S_{\rm blur}\) is the only substrate boundary,
- that every physical system reaches \(S_{\rm blur}\),
- that all downstream observables are identical,
- that the Lin single-atom boundary and an astrophysical photon-ring system are the same physical system.

UA is explicit, physically motivated, and not yet itself a theorem of the package. That is the correct truth-status.

---

# 5. Obligation 1 — Forwarding-Identification Lemma

## 5.1 Target

Show that in the Schwarzschild GR expert regime, the local null escape fraction

$$f_{\rm forward}(r)=1-f_{\rm capture}(r)$$

is the strongest natural candidate realization of the HPF forwarding efficiency \(\zeta\).

## 5.2 Five required properties of \(\zeta\)

Within HPF canon, the relevant forwarding/coherence gate must be:

1. dimensionless,
2. local at the boundary,
3. monotonically degrading as trapping load increases,
4. equal to \(1/2\) at the marginal forwarding boundary,
5. the object that governs whether coherent propagation continues or fails.

## 5.3 Current derivation

Against those requirements, \(f_{\rm forward}(r)\) in Schwarzschild satisfies:

- **Property 1:** dimensionless, because it is a ratio of solid angles.
- **Property 2:** local, because it is computed for a static observer at radius \(r\).
- **Property 3:** monotone, because capture increases as \(r \to 3M\), so forwarding decreases.
- **Property 4:** exact midpoint at the photon sphere:
  $$
  f_{\rm forward}(3M)=\frac{1}{2}.
  $$
- **Property 5:** above the photon sphere, forwarding dominates; below it, trapping dominates. Under the HPF routing interpretation, that makes the photon sphere the marginal handoff boundary.

Properties 1–4 are strong. Property 5 is where the candidate bridge enters, because that step layers HPF routing logic onto a GR object.

## 5.4 Elimination argument

The main low-complexity GR competitors fail in more obvious ways:

| GR scalar / object | Value at \(r_{\rm photon}\) | Problem |
|---|---:|---|
| Redshift \(\sqrt{1-2M/r}\) | \(1/\sqrt3\) | Wrong midpoint value |
| Compactness \(2M/r\) | \(2/3\) | Wrong midpoint value |
| Effective potential \(V_{\rm eff}\) | maximum | Wrong object type; not bounded in \([0,1]\) |
| Lyapunov exponent \(\lambda_L\) | instability rate | Wrong object type; not a forwarding fraction |

This is an elimination argument, not a full classification theorem over every imaginable GR scalar.

## 5.5 Status of Obligation 1

**Status:** **OPEN**

What is strong already:
- \(f_{\rm forward}\) satisfies Properties 1–4,
- \(f_{\rm forward}(3M)=1/2\) is a hard GR midpoint fact,
- \(f_{\rm forward}\) is the strongest natural low-complexity GR candidate for \(\zeta\).

What remains open:
- the full identification of \(f_{\rm forward}\) with \(\zeta\) as an HPF routing bridge rather than only an analogy.

---

# 6. Obligation 2 — Radial Blur Displacement Law

## 6.1 Target

Derive

$$r_{\rm echo} = 1.05 \times r_{\rm photon}$$

from GR-side dynamics rather than treating it as a label transfer from the blur anchor alone.

## 6.2 Current candidate path

Under the forwarding identification

$$\zeta_{\rm GR}(r)=f_{\rm forward}(r),$$

the radial profile of \(f_{\rm forward}\) near the photon sphere determines how a blur-margin in substrate load maps to a radius displacement.

Near \(r=3M\), the derivative

$$\frac{df_{\rm forward}}{dr}\Bigg|_{r=3M}$$

is finite and computable. A local displacement law would have the form

$$\Delta r \sim \frac{\Delta f_{\rm forward}}{\left|df_{\rm forward}/dr\right|_{3M}}.$$

If the forwarding-identification map is locally linear near the midpoint, the blur margin \(\Delta S = S_{\rm blur}-1 = 0.05\) can be translated into the corresponding \(\Delta f_{\rm forward}\), and therefore into a radial displacement.

The candidate claim is that this should recover

$$\frac{\Delta r}{r_{\rm photon}} = 0.05,$$

which would close the \(1.05\times\) factor from the GR side.

## 6.3 Status of Obligation 2

**Status:** **OPEN**

What exists:
- a physically motivated attack path,
- the retained location claim in the active package.

What does not yet exist:
- the completed calculation.

So the location is retained as a candidate, but it is not derivationally closed by this note.

---

# 7. Obligation 3 — Mode-Indexing and Reflection Bridge

## 7.1 Target

Show that the Nyquist residual

$$\eta=\frac{1}{48}$$

at the blur boundary projects dominantly into the outgoing null mode family so that the intrinsic echo fraction is exactly \(\eta\).

## 7.2 What is already proved

At \(S_f=S_{\rm blur}\), the BCC 24-sector substrate imposes the minimum non-zero unresolved phase fraction

$$\eta=\frac{1}{2N_s}=\frac{1}{48}.$$

That is the smallest irreducible sector-resolution remainder.

HPF substrate evolution is reversible, so that unresolved fraction cannot simply disappear through absorption without illegal information loss. Therefore:

> **What is proved:** \(\eta\) survives as a minimum reversible residual scale.

## 7.3 What is not yet proved

Three additional steps are still missing:

1. **Exact partition:** reversibility forbids destruction, but not scrambling, lateral redistribution, temporary trapping, or mode mixing. So it is not yet proved that the surviving redirected fraction is exactly \(\eta\) in the relevant image-producing channel.
2. **Outward projection:** even if a residual survives, it must project dominantly into the outgoing null mode family rather than isotropic scatter or trapped reprocessing.
3. **Image-plane translation:** the substrate residual fraction must be shown to map to the observed image-plane flux fraction for a distant telescope.

Without those bridges, the statement

$$A_{\rm echo} = \eta$$

remains candidate, not proved.

## 7.4 Status of Obligation 3

**Status:** **OPEN**

What is strong already:
- \(\eta = 1/48\) is live and substrate-native,
- reversibility preserves a minimum surviving residual.

What remains open:
- proving that the relevant outward observable is exactly the same fraction.

---

# 8. Candidate prediction, contingent on all three obligations

If all three obligations close, the candidate prediction is:

## 8.1 Echo location
$$r_{\rm echo}=1.05 \times r_{\rm photon}.$$

## 8.2 Echo amplitude
$$A_{\rm echo}=\eta=\frac{1}{48}\approx 2.08\%.$$

## 8.3 Observable framing
For the M87* photon ring, the candidate observational target is:
- angular position near the ring with a \(1.05\times\) displacement,
- flux fraction of approximately \(2.1\%\) of the ring flux.

This remains **contingent**, not live canon.

---

# 9. What this note removes from HPF scope

The old amplitude values

$$\varepsilon = 0.134,\ 0.124,\ 0.083$$

and similar optimizer-style echo amplitudes are **not HPF derivations**.

They are observational-fit artifacts from exploratory code and do not belong in canonical HPF. The active package already decapitated that material, and this note preserves that exclusion.

So the live distinction is:

- **retained:** \(1.05\times\) location as candidate,
- **removed:** fitted amplitude \(\varepsilon=0.134\),
- **introduced here as candidate:** \(A_{\rm echo}=1/48\) contingent on all three bridges.

---

# 10. Compatibility with the live package

This candidate note is built to be compatible with:
- the active blur anchor \(S_{\rm blur}=1.05\),
- the live Nyquist denominator \(\eta=1/48\),
- the active vacuum-sector package in Volume IV,
- the truth-status partition in Volume III,
- the updated Symbol Index.

It does **not**:
- alter the current \(\Lambda\) derivation,
- alter the dark-matter branch,
- alter the 4-bit grammar milestone lock,
- promote photon-ring phenomenology into canon.

---

# 11. Falsifiability

This candidate would be weakened or falsified if:

1. the GR forwarding-identification bridge fails — i.e. \(f_{\rm forward}\) is shown not to be the right HPF-side candidate object,
2. the completed displacement calculation misses the \(1.05\times\) factor in a structurally significant way,
3. the reversible residual fails to project into the outgoing null mode family at the \(\eta\)-scale,
4. future high-resolution ring data exclude both a \(1.05\times\) echo location and an \(\eta\)-scale flux residual in the relevant regime.

These are real failure conditions, not rhetorical placeholders.

---

# 12. Full status table

| Claim | Status |
|---|---|
| \(S_{\rm blur}=1.05\), \(\zeta=0.5\) midpoint | Locked in active package |
| \(\eta=1/48\) from BCC Nyquist | Derived / substrate-native in active package |
| UA | Explicit assumption, well-motivated |
| \(f_{\rm capture}=1/2\) at \(r=3M\) in Schwarzschild | Strong GR fact in candidate argument |
| \(f_{\rm forward}\) satisfies Properties 1–4 required of \(\zeta\) | Strong candidate support |
| \(f_{\rm forward}\) realizes Property 5 under HPF routing interpretation | Candidate bridge |
| Photon sphere as candidate GR locus of \(S_{\rm blur}\) | Strong candidate contingent on identification |
| \(r_{\rm echo}=1.05 \times r_{\rm photon}\) | Candidate; Obligation 2 open |
| Reversibility preserves an \(\eta\)-scale residual | Proved under HPF axioms |
| Residual projects outward as echo | Candidate; Obligation 3 open |
| \(A_{\rm echo}=1/48\) | Candidate contingent on Obligations 1–3 |
| Image-plane flux ratio \(=\eta\) | Not yet proved |

---

# 13. Freeze wording

> At \(S_{\rm blur}=1.05\), the 24-sector BCC substrate imposes a minimum unresolved phase fraction \(\eta=1/48\). Reversibility forbids that residual from being destroyed, so \(\eta\) survives as a reversible remainder. The GR null-forwarding fraction provides the strongest natural candidate realization of HPF \(\zeta\), placing the photon sphere at the candidate GR locus of the blur boundary. The remaining open bridges are: (1) formal identification of \(f_{\rm forward}\) with \(\zeta\) in the GR expert regime; (2) derivation of the \(1.05\times\) radial displacement from GR-side dynamics; (3) proof that the Nyquist residual projects dominantly into the outgoing null mode family. Contingent on all three, the intrinsic echo fraction is \(\eta = 1/48 \approx 2.08\%\).

---

# 14. Non-promotion clause

This file remains a **candidate note**.

It does **not**:
- enter active canon by itself,
- replace the four rewritten volumes,
- replace the Symbol Index,
- prove that photon-ring phenomenology is closed at the same status level as the current vacuum-sector package.

Promotion would require closure of all three obligations and a separate package-level decision.

