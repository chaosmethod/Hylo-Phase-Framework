# HPF Correction Note — $B_{\rm cap}$ and $\chi^*_{\rm geom}$

**Date:** 2026-04-01
**Status:** Locked corrections. Both decisions made from source conflict resolution.
**Applies to:** locked starter calibration file, Volume III provenance map

---

## Correction 1: $B_{\rm cap} = 0.25\,M_{\rm cap}$

**Conflict:** The locked starter calibration file carries $B_{\rm cap} = 0.15\,M_{\rm cap}$ with no supersession note and no override rationale. The March 18 closure checkpoint explicitly corrects this to $B_{\rm cap} = 0.25\,M_{\rm cap}$ and states the design objective: preserving the intended separation between transient overflow absorption and durable debt generation.

**Resolution:** $B_{\rm cap} = 0.25\,M_{\rm cap}$ is the live starter value.

**Implementation:** In all files carrying $B_{\rm cap} = 0.15\,M_{\rm cap}$, replace with $B_{\rm cap} = 0.25\,M_{\rm cap}$ and add:

> "The smaller provisional scratch reserve $B_{\rm cap} = 0.15\,M_{\rm cap}$ is superseded by the March 18 closure checkpoint correction, which restores the intended separation between transient overflow absorption and durable debt generation."

**Companion value confirmed:** $D_{\rm cap} = 0.50\,M_{\rm cap}$ is unchanged.

---

## Correction 2: $\chi^*_{\rm geom}$ Promoted to Live Starter Diagnostic

**Conflict:** The equal-weight geometry burden $\chi_{\rm geom}$ remains operative in Volume I's bridge stack. The sharpened geometry-diagnostic checkpoint introduces the dominance-aware form:

$$\chi^*_{\rm geom} = (1 - \gamma)\chi_{\rm lin} + \gamma\chi_{\rm dom}$$

and explicitly states this fixes misclassification of catastrophic single-channel persistence that the equal-weight form diluted.

**Resolution:** $\chi^*_{\rm geom}$ is the live starter operational geometry diagnostic. The equal-weight $\chi_{\rm geom}$ is superseded operationally and retained as provenance only.

**Status of $\chi^*_{\rm geom}$:** Operational/coarse-grained starter diagnostic. Not a constitutive derivation.

**Implementation:** Add the following to Volume III provenance map:

> "The equal-weight starter geometry burden $\chi_{\rm geom}$ is superseded operationally by the dominance-aware starter diagnostic $\chi^*_{\rm geom} = (1-\gamma)\chi_{\rm lin} + \gamma\chi_{\rm dom}$, introduced in the sharpened geometry-diagnostic checkpoint. The equal-weight form remains provenance only."

---

## Summary

| Item | Old value | Corrected value | Source |
|---|---|---|---|
| $B_{\rm cap}$ | $0.15\,M_{\rm cap}$ | $0.25\,M_{\rm cap}$ | March 18 closure checkpoint |
| $D_{\rm cap}$ | $0.50\,M_{\rm cap}$ | $0.50\,M_{\rm cap}$ | Unchanged |
| Live geometry starter | $\chi_{\rm geom}$ (equal-weight) | $\chi^*_{\rm geom}$ (dominance-aware) | Sharpened geometry-diagnostic checkpoint |
| Equal-weight $\chi_{\rm geom}$ | Operative | Provenance only | Superseded |

---

*Apply these corrections before the next canonical package update. Do not carry the old values forward.*
