#!/usr/bin/env python3
"""
HPF_QPRCA_MicroToy_v0_2_5_Reversible_TQEQ_GroupedL2_Derived_Zeta_2026-03-20.py

Canonical March 20 executable reference toy aligned to the enriched HPF master
volumes, promoted with the grouped-L2 intermediate aggregation law, a reversible TQ0 replacement, and a tuned
derived-zeta recovery layer. This remains a toy / demo harness, not
strongest-form microscopic closure.

What this file does:
- Keeps the v0.1.2 normalized predecessor burden as the stable baseline.
- Carries the v0.1.3 refined non-predecessor channel logic as an exploratory mode.
- Adds aggregate_mode='grouped_l2' as the current best-tested intermediate legality combiner.
- Tunes the derived-zeta projection so grouped-L2 default runs no longer start
  unrealistically deep in the old flux corridor.
- Separates microscopic legality F from downstream geometry-validity diagnostics.
- Exposes the bridge stack
      U -> U_geom^(NL) -> Lambda_geom -> chi*_geom
- Replaces the placeholder zeta proxy with a derived-zeta recovery layer on an
  old effective-flux axis with markers 1.05 / 1.40 / 5.7889.
- Treats route burden as a live current-canon burden input, while leaving exact
  strongest-form microscopic route subfactors open.
- Provides built-in demos and CLI output.

Usage examples:
    python HPF_QPRCA_MicroToy_v0_2_4_FloorFixed_GroupedL2_Derived_Zeta_2026-03-19.py
    python HPF_QPRCA_MicroToy_v0_2_4_FloorFixed_GroupedL2_Derived_Zeta_2026-03-19.py --demo all
    python HPF_QPRCA_MicroToy_v0_2_4_FloorFixed_GroupedL2_Derived_Zeta_2026-03-19.py --demo baseline
    python HPF_QPRCA_MicroToy_v0_2_4_FloorFixed_GroupedL2_Derived_Zeta_2026-03-19.py --mode refined --steps 80
    python HPF_QPRCA_MicroToy_v0_2_4_FloorFixed_GroupedL2_Derived_Zeta_2026-03-19.py --demo geometry_sweep --output results.json
"""

from __future__ import annotations

import argparse
import json
import math
import random
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Dict, List, Mapping, MutableMapping, Optional, Tuple


# -----------------------------------------------------------------------------
# Dataclasses
# -----------------------------------------------------------------------------


@dataclass(frozen=True)
class Weights:
    mu_C: float = 1.0
    mu_B: float = 1.0
    mu_R: float = 1.0
    mu_A: float = 1.0
    mu_P: float = 1.0


@dataclass(frozen=True)
class CapacityConfig:
    M_cap: float = 4.0
    rho_b: float = 0.20
    rho_q: float = 0.10


@dataclass(frozen=True)
class BridgeConfig:
    rho_F: float = 0.60
    rho_H: float = 0.25
    lambda_soft: float = 0.50
    lambda_hard: float = 0.72
    gamma_lambda: float = 1.00
    gamma_zeta: float = 1.00
    gamma_F: float = 0.35
    epsilon: float = 1.0e-9
    # Derived-zeta recovery weights and old flux-axis markers.
    S_alpha_U: float = 0.12
    S_alpha_Lambda: float = 0.12
    S_alpha_chi: float = 0.10
    S_alpha_F: float = 0.00
    S_alpha_violation: float = 0.60
    S_alpha_excess: float = 1.40
    S_alpha_accept_deficit: float = 0.10
    S_alpha_R: float = 0.25
    S_floor: float = 0.45
    S_onset: float = 1.05
    S_validity: float = 1.40
    S_hard: float = 5.7889
    zeta_k: float = 0.80
    S_power: float = 14.0
    S_power_low: float = 0.78
    S_power_high: float = 10.0
    S_raw_onset: float = 0.10


@dataclass
class StepRecord:
    partition: int
    block_index: int
    input_block: List[int]
    candidate_block: List[int]
    chosen_rule: str
    predecessor_count: int
    continuation_neff: float
    continuation_classes: int
    M_pred: float
    F_left: float
    F_right: float
    F_block: float
    accepted: bool
    dominant_rejection_channel: Optional[str]
    block_channels_left: Dict[str, float]
    block_channels_right: Dict[str, float]


@dataclass
class RunSummary:
    model_mode: str
    steps: int
    size: int
    rule_choice: str
    aggregate_mode: str
    S_eff: float
    regime_label: str
    acceptance_rate: float
    mean_F_block: float
    mean_predecessor_count: float
    mean_continuation_neff: float
    total_load_initial: int
    total_load_final: int
    total_load_delta: int
    seed: int
    rejection_channel_counts: Dict[str, int]
    mean_channel_scores: Dict[str, float]
    U_closure: float
    H_health: float
    zeta: float
    m_loop: float
    m_route: float
    U_geom_NL: float
    Lambda_geom: float
    chi_geom_star: float
    violation_rate: float
    mean_excess_F: float
    legality_pressure_proxy: float


# -----------------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------------


def clamp(x: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, x))


def theta(x: float) -> float:
    return 1.0 if x >= 0.0 else 0.0


def unpack_site(site: int) -> Tuple[int, int, int, int]:
    """Bits: nL, nR, b, q."""
    return (site >> 0) & 1, (site >> 1) & 1, (site >> 2) & 1, (site >> 3) & 1


def pack_site(nL: int, nR: int, b: int, q: int) -> int:
    return (nL & 1) | ((nR & 1) << 1) | ((b & 1) << 2) | ((q & 1) << 3)


def total_load_site(site: int) -> int:
    nL, nR, _, _ = unpack_site(site)
    return nL + nR


# -----------------------------------------------------------------------------
# Rule family
# -----------------------------------------------------------------------------


def rule_ID(left: int, right: int) -> Tuple[int, int]:
    return left, right


def rule_SWAP(left: int, right: int) -> Tuple[int, int]:
    return right, left


def rule_TQ(left: int, right: int) -> Tuple[int, int]:
    nLl, nRl, bl, ql = unpack_site(left)
    nLr, nRr, br, qr = unpack_site(right)
    return pack_site(nLl, nRl, bl, 1 - ql), pack_site(nLr, nRr, br, 1 - qr)


def rule_SB(left: int, right: int) -> Tuple[int, int]:
    nLl, nRl, bl, ql = unpack_site(left)
    nLr, nRr, br, qr = unpack_site(right)
    return pack_site(nLl, nRl, br, ql), pack_site(nLr, nRr, bl, qr)


def rule_BOUNCE(left: int, right: int) -> Tuple[int, int]:
    nLl, nRl, bl, ql = unpack_site(left)
    nLr, nRr, br, qr = unpack_site(right)
    return pack_site(nRl, nLl, bl, ql), pack_site(nRr, nLr, br, qr)


def rule_EXCH(left: int, right: int) -> Tuple[int, int]:
    nLl, nRl, bl, ql = unpack_site(left)
    nLr, nRr, br, qr = unpack_site(right)
    return pack_site(nLl, nLr, bl, ql), pack_site(nRl, nRr, br, qr)


def rule_TQ0(left: int, right: int) -> Tuple[int, int]:
    nLl, nRl, bl, ql = unpack_site(left)
    nLr, nRr, br, qr = unpack_site(right)
    # Reversible replacement for the old non-bijective TQ0:
    # toggle both queue bits only on equal-q blocks, so 00 <-> 11 and
    # 01, 10 remain fixed. This preserves the intended "paired queue kick"
    # flavor without collapsing multiple inputs onto the same output.
    if ql == qr:
        return pack_site(nLl, nRl, bl, 1 - ql), pack_site(nLr, nRr, br, 1 - qr)
    return left, right


def rule_BQ0(left: int, right: int) -> Tuple[int, int]:
    nLl, nRl, bl, ql = unpack_site(left)
    nLr, nRr, br, qr = unpack_site(right)
    if ql == 0 and qr == 0:
        return pack_site(nLl, nRl, 1 - bl, ql), pack_site(nLr, nRr, 1 - br, qr)
    return left, right


def rule_SWEQ(left: int, right: int) -> Tuple[int, int]:
    if total_load_site(left) == total_load_site(right):
        return right, left
    return left, right


RULES = {
    "ID": rule_ID,
    "SWAP": rule_SWAP,
    "TQ": rule_TQ,
    "SB": rule_SB,
    "BOUNCE": rule_BOUNCE,
    "EXCH": rule_EXCH,
    "TQ0": rule_TQ0,
    "BQ0": rule_BQ0,
    "SWEQ": rule_SWEQ,
}


# -----------------------------------------------------------------------------
# Canonical microtoy
# -----------------------------------------------------------------------------


class QPRCAMicroToyV020:
    def __init__(
        self,
        *,
        size: int = 32,
        model_mode: str = "baseline",
        weights: Weights = Weights(),
        capacity: CapacityConfig = CapacityConfig(),
        bridge: BridgeConfig = BridgeConfig(),
        aggregate_mode: str = "grouped_l2",
        seed: int = 0,
    ) -> None:
        if size % 2 != 0:
            raise ValueError("Size must be even.")
        if model_mode not in {"baseline", "refined"}:
            raise ValueError("model_mode must be 'baseline' or 'refined'.")
        if aggregate_mode not in {"additive", "max", "grouped_l2"}:
            raise ValueError("aggregate_mode must be 'additive', 'max', or 'grouped_l2'.")
        self.size = size
        self.model_mode = model_mode
        self.weights = weights
        self.capacity = capacity
        self.bridge = bridge
        self.aggregate_mode = aggregate_mode
        self.seed = seed
        self.rng = random.Random(seed)

        self.rule_names = list(RULES.keys())
        self.bijection_check = self._compute_bijection_check()
        self.pred_map = self._compute_pred_map()
        self.pred_histogram = self._compute_pred_histogram()
        self.pmin, self.pmax = self._compute_pred_bounds()
        self.cont_map = self._compute_cont_map()
        self.cont_histogram = self._compute_cont_histogram()
        self.cmin, self.cmax = self._cont_bounds()
        self.state = [self.rng.randrange(16) for _ in range(size)]
        self.history: List[StepRecord] = []
        self.rejection_channel_counts = {"C": 0, "B": 0, "R": 0, "A": 0, "P": 0}

    # ----- static structure -----

    def _compute_bijection_check(self) -> Dict[str, bool]:
        out: Dict[str, bool] = {}
        for name, fn in RULES.items():
            seen = set()
            ok = True
            for left in range(16):
                for right in range(16):
                    image = fn(left, right)
                    if image in seen:
                        ok = False
                        break
                    seen.add(image)
                if not ok:
                    break
            out[name] = ok
        return out

    def _compute_pred_map(self) -> Dict[Tuple[int, int], List[Tuple[str, Tuple[int, int]]]]:
        pred: Dict[Tuple[int, int], List[Tuple[str, Tuple[int, int]]]] = {
            (outL, outR): [] for outL in range(16) for outR in range(16)
        }
        for name, fn in RULES.items():
            for inL in range(16):
                for inR in range(16):
                    pred[fn(inL, inR)].append((name, (inL, inR)))
        return pred

    def _compute_pred_histogram(self) -> Dict[str, int]:
        hist: Dict[str, int] = {}
        for preds in self.pred_map.values():
            n = len(preds)
            hist[str(n)] = hist.get(str(n), 0) + 1
        return hist

    def _compute_pred_bounds(self) -> Tuple[int, int]:
        counts = [len(v) for v in self.pred_map.values()]
        return min(counts), max(counts)

    # ----- general utilities -----

    def _total_load(self) -> int:
        return sum(total_load_site(x) for x in self.state)

    def _block_neighbors(self, left_index: int) -> Tuple[int, int]:
        return self.state[(left_index - 1) % self.size], self.state[(left_index + 2) % self.size]

    def predecessor_count(self, out_pair: Tuple[int, int]) -> int:
        return len(self.pred_map[out_pair])

    def predecessor_burden(self, out_pair: Tuple[int, int]) -> float:
        n = self.predecessor_count(out_pair)
        if self.pmax == self.pmin:
            return 0.0
        return (math.log2(n) - math.log2(self.pmin)) / (math.log2(self.pmax) - math.log2(self.pmin))

    def _compute_cont_map(self) -> Dict[Tuple[int, int], Dict[Tuple[int, int], int]]:
        cont: Dict[Tuple[int, int], Dict[Tuple[int, int], int]] = {}
        for a in range(16):
            for b in range(16):
                in_pair = (a, b)
                counts: Dict[Tuple[int, int], int] = {}
                for name in self.rule_names:
                    out_pair = RULES[name](a, b)
                    counts[out_pair] = counts.get(out_pair, 0) + 1
                cont[in_pair] = counts
        return cont

    def _compute_cont_histogram(self) -> Dict[int, int]:
        hist: Dict[int, int] = {}
        for counts in self.cont_map.values():
            nclasses = len(counts)
            hist[nclasses] = hist.get(nclasses, 0) + 1
        return dict(sorted(hist.items()))

    def _cont_bounds(self) -> Tuple[int, int]:
        vals = list(self.cont_histogram.keys())
        return min(vals), max(vals)

    def continuation_neff(self, in_pair: Tuple[int, int]) -> float:
        counts = self.cont_map[in_pair]
        total = sum(counts.values())
        if total <= 0:
            return 1.0
        probs = [c / total for c in counts.values()]
        denom = sum(p * p for p in probs)
        return 1.0 / max(1.0e-12, denom)

    def continuation_class_count(self, in_pair: Tuple[int, int]) -> int:
        return len(self.cont_map[in_pair])

    def continuation_burden(self, in_pair: Tuple[int, int]) -> float:
        neff = self.continuation_neff(in_pair)
        neff_max = float(len(self.rule_names))
        if neff_max <= 1.0:
            return 0.0
        return max(0.0, min(1.0, math.log(neff) / math.log(neff_max)))

    def _site_free_capacity(self, site: int) -> float:
        _, _, b, q = unpack_site(site)
        free = self.capacity.M_cap * (1.0 - self.capacity.rho_b * b - self.capacity.rho_q * q)
        return max(1.0e-9, free)

    # ----- burdens -----

    def site_burdens(self, in_site: int, out_site: int, outer_neighbor: int) -> Dict[str, float]:
        nL, nR, b, q = unpack_site(in_site)
        out_nL, out_nR, out_b, out_q = unpack_site(out_site)
        neigh_nL, neigh_nR, _, _ = unpack_site(outer_neighbor)

        if self.model_mode == "baseline":
            C = float(max(nL, nR))
            B = 0.0
            if out_nL == 1 and neigh_nR == 1:
                B += 0.5
            if out_nR == 1 and neigh_nL == 1:
                B += 0.5
            R = float(b)
            A = float(abs(nL - nR))
            return {"C": C, "B": B, "R": R, "A": A, "q": float(q)}

        # refined mode (v0.1.3 lineage)
        C = min(1.0, 0.75 * max(nL, nR))

        out_total = out_nL + out_nR
        neigh_total = neigh_nL + neigh_nR
        directional_conflict = ((out_nL and neigh_nR) + (out_nR and neigh_nL)) / 2.0
        blocked_emission = 1.0 if (b == 1 and out_total > 0) else 0.0
        crowding = max(0.0, out_total + neigh_total - 2.0) / 2.0
        B = min(1.0, 1.0 * directional_conflict + 0.8 * blocked_emission + 0.8 * crowding)

        storage = float(b)
        queue = float(q)
        state_flip = (abs(out_b - b) + abs(out_q - q)) / 2.0
        loaded_release = 1.0 if (b == 1 and out_total > 0) else 0.0
        R = min(1.0, 0.8 * storage + 0.5 * queue + 0.6 * state_flip + 0.5 * loaded_release)

        in_skew = abs(nL - nR)
        out_skew = abs(out_nL - out_nR)
        pair_skew = abs((out_nL + neigh_nL) - (out_nR + neigh_nR)) / 2.0
        A = min(1.0, 0.7 * in_skew + 0.6 * out_skew + 0.6 * pair_skew)
        return {"C": C, "B": B, "R": R, "A": A, "q": float(q)}

    def _site_channel_scores(self, burdens: Mapping[str, float], p_burden: float) -> Dict[str, float]:
        return {
            "C": self.weights.mu_C * burdens["C"],
            "B": self.weights.mu_B * burdens["B"],
            "R": self.weights.mu_R * burdens["R"],
            "A": self.weights.mu_A * burdens["A"],
            "P": self.weights.mu_P * p_burden,
        }

    def _site_F(self, in_site: int, burdens: Mapping[str, float], p_burden: float) -> Tuple[float, Dict[str, float]]:
        scores = self._site_channel_scores(burdens, p_burden)
        free = self._site_free_capacity(in_site)
        if self.aggregate_mode == "max":
            req = max(scores.values())
        elif self.aggregate_mode == "grouped_l2":
            req = math.sqrt(scores["C"] ** 2 + scores["A"] ** 2) + scores["P"] + math.sqrt(scores["B"] ** 2 + scores["R"] ** 2)
        else:
            req = sum(scores.values())
        return req / free, scores

    # ----- execution -----

    def step(self, partition: int = 0, rule_choice: str = "random") -> None:
        for block_index in range(self.size // 2):
            i = (2 * block_index + partition) % self.size
            j = (i + 1) % self.size
            inL = self.state[i]
            inR = self.state[j]

            chosen_rule = self.rng.choice(self.rule_names) if rule_choice == "random" else rule_choice
            if chosen_rule not in RULES:
                raise ValueError(f"Unknown rule_choice: {chosen_rule}")
            candidate = RULES[chosen_rule](inL, inR)

            pred_count = self.predecessor_count(candidate)
            cont_neff = self.continuation_neff((inL, inR))
            cont_classes = self.continuation_class_count((inL, inR))
            p_burden = self.continuation_burden((inL, inR))
            left_outer, right_outer = self._block_neighbors(i)
            bL = self.site_burdens(inL, candidate[0], left_outer)
            bR = self.site_burdens(inR, candidate[1], right_outer)
            F_left, scores_left = self._site_F(inL, bL, p_burden)
            F_right, scores_right = self._site_F(inR, bR, p_burden)
            F_block = max(F_left, F_right)
            accepted = F_block < 1.0

            dominant: Optional[str] = None
            if not accepted:
                block_scores = {k: max(scores_left[k], scores_right[k]) for k in scores_left.keys()}
                dominant = max(block_scores, key=block_scores.get)
                self.rejection_channel_counts[dominant] += 1

            if accepted:
                self.state[i], self.state[j] = candidate

            self.history.append(
                StepRecord(
                    partition=partition,
                    block_index=block_index,
                    input_block=[inL, inR],
                    candidate_block=[candidate[0], candidate[1]],
                    chosen_rule=chosen_rule,
                    predecessor_count=pred_count,
                    continuation_neff=cont_neff,
                    continuation_classes=cont_classes,
                    M_pred=p_burden,
                    F_left=F_left,
                    F_right=F_right,
                    F_block=F_block,
                    accepted=accepted,
                    dominant_rejection_channel=dominant,
                    block_channels_left=scores_left,
                    block_channels_right=scores_right,
                )
            )

    # ----- bridge observables -----

    def _mean_channel_scores(self) -> Dict[str, float]:
        if not self.history:
            return {"C": 0.0, "B": 0.0, "R": 0.0, "A": 0.0, "P": 0.0}
        totals = {"C": 0.0, "B": 0.0, "R": 0.0, "A": 0.0, "P": 0.0}
        count = 0
        for rec in self.history:
            for k in totals:
                totals[k] += 0.5 * (rec.block_channels_left[k] + rec.block_channels_right[k])
            count += 1
        return {k: totals[k] / max(1, count) for k in totals}

    def compute_operational_observables(self) -> Dict[str, float]:
        mean_channels = self._mean_channel_scores()
        if self.history:
            U = sum(rec.F_block for rec in self.history) / len(self.history)
            U = clamp(U)
            acceptance = sum(int(rec.accepted) for rec in self.history) / len(self.history)
            violation_rate = sum(float(rec.F_block >= 1.0) for rec in self.history) / len(self.history)
            mean_excess_F = sum(max(0.0, rec.F_block - 1.0) for rec in self.history) / len(self.history)
        else:
            U = 0.0
            acceptance = 1.0
            violation_rate = 0.0
            mean_excess_F = 0.0

        # Health is an explicit restorative quantity, kept separate from legality.
        H = clamp(0.55 * acceptance + 0.45 * (1.0 - mean_channels["R"]))

        # Current-canon: m_route is a live derived burden. In this toy we expose a
        # coarse current-state proxy rather than claiming final microscopic closure.
        m_loop = clamp(mean_channels["A"])
        m_route = clamp(0.60 * mean_channels["P"] + 0.40 * mean_channels["B"])

        U_geom_NL = clamp(1.0 - (1.0 - U) * (1.0 - 1.09 * m_loop) * (1.0 - 1.25 * m_route))

        # Bridge-level legality proxy: mean closure load alone under-resolves hard
        # capacity pressure once continuation ambiguity is introduced. We therefore
        # retain U as the base proxy but add explicit violation-rate and excess-F
        # information so the coarse bridge can still distinguish validity-corridor
        # states from near-illegal hard-edge states.
        legality_pressure_proxy = clamp(U + 0.35 * violation_rate + 0.50 * mean_excess_F)

        Lambda_geom = clamp(
            U_geom_NL * (1.0 + self.bridge.rho_F * legality_pressure_proxy)
            - self.bridge.rho_H * H
        )

        S_raw = (
            self.bridge.S_alpha_U * U
            + self.bridge.S_alpha_Lambda * Lambda_geom
            + self.bridge.S_alpha_chi * clamp(U_geom_NL)
            + self.bridge.S_alpha_F * legality_pressure_proxy
            + self.bridge.S_alpha_violation * violation_rate
            + self.bridge.S_alpha_excess * mean_excess_F
            + self.bridge.S_alpha_accept_deficit * (1.0 - acceptance)
            + self.bridge.S_alpha_R * mean_channels["R"]
        )
        # Floor-fixed map from the current [0,1]-scale diagnostics to the old
        # effective-flux axis. This preserves the onset and hard anchors while
        # allowing true sub-onset stable localization when S_raw is small.
        S_raw_c = clamp(S_raw)
        raw_onset = max(self.bridge.epsilon, min(1.0 - self.bridge.epsilon, self.bridge.S_raw_onset))
        if S_raw_c <= raw_onset:
            x_low = S_raw_c / raw_onset
            S_eff = self.bridge.S_floor + (self.bridge.S_onset - self.bridge.S_floor) * (x_low ** self.bridge.S_power_low)
        else:
            x_high = (S_raw_c - raw_onset) / (1.0 - raw_onset)
            S_eff = self.bridge.S_onset + (self.bridge.S_hard - self.bridge.S_onset) * (x_high ** self.bridge.S_power_high)
        zeta = 1.0 / (1.0 + math.exp(self.bridge.zeta_k * (S_eff - self.bridge.S_onset)))

        psi_F = 1.0e9 if legality_pressure_proxy >= 1.0 else legality_pressure_proxy / (1.0 - legality_pressure_proxy + self.bridge.epsilon)
        chi_geom_star = theta(legality_pressure_proxy - 1.0) + theta(1.0 - legality_pressure_proxy) * (
            1.0
            - math.exp(
                -(
                    self.bridge.gamma_lambda * Lambda_geom
                    + self.bridge.gamma_zeta * (1.0 - zeta)
                    + self.bridge.gamma_F * psi_F
                )
            )
        )
        chi_geom_star = clamp(chi_geom_star)

        if S_eff < self.bridge.S_onset:
            regime_label = "stable_localized"
        elif S_eff < self.bridge.S_validity:
            regime_label = "onset_corridor"
        elif S_eff < self.bridge.S_hard:
            regime_label = "validity_corridor"
        else:
            regime_label = "hard_saturation"

        return {
            "U_closure": U,
            "H_health": H,
            "zeta": zeta,
            "S_eff": S_eff,
            "regime_label": regime_label,
            "m_loop": m_loop,
            "m_route": m_route,
            "U_geom_NL": U_geom_NL,
            "Lambda_geom": Lambda_geom,
            "chi_geom_star": chi_geom_star,
            "violation_rate": violation_rate,
            "mean_excess_F": mean_excess_F,
            "legality_pressure_proxy": legality_pressure_proxy,
            "mean_channels": mean_channels,
        }

    def run(self, steps: int = 40, rule_choice: str = "random") -> RunSummary:
        initial = self._total_load()
        for t in range(steps):
            self.step(partition=t % 2, rule_choice=rule_choice)

        accepted = sum(int(rec.accepted) for rec in self.history)
        sum_f = sum(rec.F_block for rec in self.history)
        sum_pred = sum(rec.predecessor_count for rec in self.history)
        sum_cont = sum(rec.continuation_neff for rec in self.history)
        nblocks = max(1, steps * (self.size // 2))
        final = self._total_load()
        obs = self.compute_operational_observables()

        return RunSummary(
            model_mode=self.model_mode,
            steps=steps,
            size=self.size,
            rule_choice=rule_choice,
            aggregate_mode=self.aggregate_mode,
            S_eff=obs["S_eff"],
            regime_label=obs["regime_label"],
            acceptance_rate=accepted / nblocks,
            mean_F_block=sum_f / nblocks,
            mean_predecessor_count=sum_pred / nblocks,
            mean_continuation_neff=sum_cont / nblocks,
            total_load_initial=initial,
            total_load_final=final,
            total_load_delta=final - initial,
            seed=self.seed,
            rejection_channel_counts=dict(self.rejection_channel_counts),
            mean_channel_scores=obs["mean_channels"],
            U_closure=obs["U_closure"],
            H_health=obs["H_health"],
            zeta=obs["zeta"],
            m_loop=obs["m_loop"],
            m_route=obs["m_route"],
            U_geom_NL=obs["U_geom_NL"],
            Lambda_geom=obs["Lambda_geom"],
            chi_geom_star=obs["chi_geom_star"],
            violation_rate=obs["violation_rate"],
            mean_excess_F=obs["mean_excess_F"],
            legality_pressure_proxy=obs["legality_pressure_proxy"],
        )


# -----------------------------------------------------------------------------
# Demo runners
# -----------------------------------------------------------------------------


def demo_run(model_mode: str = "baseline", steps: int = 40, size: int = 32, seed: int = 0) -> Dict[str, object]:
    toy = QPRCAMicroToyV020(size=size, model_mode=model_mode, seed=seed)
    summary = toy.run(steps=steps)
    return {
        "demo": f"single_run_{model_mode}",
        "config": {
            "size": size,
            "steps": steps,
            "seed": seed,
            "model_mode": model_mode,
        },
        "bijection_check": toy.bijection_check,
        "predecessor_histogram": toy.pred_histogram if hasattr(toy, "pred_histogram") else toy.pred_histogram,
        "pred_bounds": {"min": toy.pmin, "max": toy.pmax},
        "continuation_histogram": toy.cont_histogram,
        "cont_bounds": {"min": toy.cmin, "max": toy.cmax},
        "continuation_histogram": toy.cont_histogram,
        "cont_bounds": {"min": toy.cmin, "max": toy.cmax},
        "summary": asdict(summary),
        "first_10_step_records": [asdict(r) for r in toy.history[:10]],
        "final_state": toy.state,
    }


def demo_compare_baseline_refined(steps: int = 40, size: int = 32, seed: int = 0) -> Dict[str, object]:
    baseline = demo_run(model_mode="baseline", steps=steps, size=size, seed=seed)
    refined = demo_run(model_mode="refined", steps=steps, size=size, seed=seed)
    return {
        "demo": "baseline_vs_refined",
        "baseline_summary": baseline["summary"],
        "refined_summary": refined["summary"],
    }


def demo_geometry_bridge_sweep(seed: int = 0) -> Dict[str, object]:
    rows: List[Dict[str, object]] = []
    for mode in ["baseline", "refined"]:
        for M_cap in [4.0, 5.0, 6.0]:
            for mu_P in [0.5, 0.75, 1.0]:
                toy = QPRCAMicroToyV020(
                    size=32,
                    model_mode=mode,
                    seed=seed,
                    weights=Weights(mu_P=mu_P),
                    capacity=CapacityConfig(M_cap=M_cap),
                )
                summary = toy.run(steps=40)
                rows.append(
                    {
                        "model_mode": mode,
                        "M_cap": M_cap,
                        "mu_P": mu_P,
                        "acceptance_rate": summary.acceptance_rate,
                        "mean_F_block": summary.mean_F_block,
                        "zeta": summary.zeta,
                        "S_eff": summary.S_eff,
                        "regime_label": summary.regime_label,
                        "m_loop": summary.m_loop,
                        "m_route": summary.m_route,
                        "U_geom_NL": summary.U_geom_NL,
                        "Lambda_geom": summary.Lambda_geom,
                        "chi_geom_star": summary.chi_geom_star,
                    }
                )
    return {"demo": "geometry_bridge_sweep", "rows": rows}


def demo_rule_sweep(model_mode: str = "baseline", size: int = 32, steps: int = 40, seed: int = 0) -> Dict[str, object]:
    rows: List[Dict[str, object]] = []
    for rule_name in RULES:
        toy = QPRCAMicroToyV020(size=size, model_mode=model_mode, seed=seed)
        summary = toy.run(steps=steps, rule_choice=rule_name)
        rows.append(
            {
                "rule": rule_name,
                "acceptance_rate": summary.acceptance_rate,
                "mean_F_block": summary.mean_F_block,
                "zeta": summary.zeta,
                "S_eff": summary.S_eff,
                "regime_label": summary.regime_label,
                "chi_geom_star": summary.chi_geom_star,
                "dominant_rejection_channels": summary.rejection_channel_counts,
            }
        )
    return {"demo": f"rule_sweep_{model_mode}", "rows": rows}


def demo_all() -> Dict[str, object]:
    return {
        "demo": "all",
        "single_run_baseline": demo_run("baseline"),
        "single_run_refined": demo_run("refined"),
        "comparison": demo_compare_baseline_refined(),
        "geometry_bridge_sweep": demo_geometry_bridge_sweep(),
        "rule_sweep_baseline": demo_rule_sweep("baseline"),
        "rule_sweep_refined": demo_rule_sweep("refined"),
    }


# -----------------------------------------------------------------------------
# CLI
# -----------------------------------------------------------------------------


def build_payload(args: argparse.Namespace) -> Dict[str, object]:
    if args.demo == "baseline":
        return demo_run("baseline", steps=args.steps, size=args.size, seed=args.seed)
    if args.demo == "refined":
        return demo_run("refined", steps=args.steps, size=args.size, seed=args.seed)
    if args.demo == "compare":
        return demo_compare_baseline_refined(steps=args.steps, size=args.size, seed=args.seed)
    if args.demo == "geometry_sweep":
        return demo_geometry_bridge_sweep(seed=args.seed)
    if args.demo == "rule_sweep":
        return demo_rule_sweep(args.mode, size=args.size, steps=args.steps, seed=args.seed)
    if args.demo == "all":
        return demo_all()

    toy = QPRCAMicroToyV020(
        size=args.size,
        model_mode=args.mode,
        seed=args.seed,
        weights=Weights(
            mu_C=args.mu_C,
            mu_B=args.mu_B,
            mu_R=args.mu_R,
            mu_A=args.mu_A,
            mu_P=args.mu_P,
        ),
        capacity=CapacityConfig(M_cap=args.M_cap, rho_b=args.rho_b, rho_q=args.rho_q),
        aggregate_mode=args.aggregate_mode,
    )
    summary = toy.run(steps=args.steps, rule_choice=args.rule_choice)
    return {
        "demo": "single_run_custom",
        "config": vars(args),
        "bijection_check": toy.bijection_check,
        "predecessor_histogram": toy.pred_histogram if hasattr(toy, "pred_histogram") else toy.pred_histogram,
        "pred_bounds": {"min": toy.pmin, "max": toy.pmax},
        "continuation_histogram": toy.cont_histogram,
        "cont_bounds": {"min": toy.cmin, "max": toy.cmax},
        "summary": asdict(summary),
        "first_10_step_records": [asdict(r) for r in toy.history[:10]],
        "final_state": toy.state,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Canonical HPF/QPRCA microtoy v0.2.5 reversible-TQEQ")
    parser.add_argument("--demo", default="none", choices=["none", "baseline", "refined", "compare", "geometry_sweep", "rule_sweep", "all"])
    parser.add_argument("--mode", default="baseline", choices=["baseline", "refined"])
    parser.add_argument("--size", type=int, default=32)
    parser.add_argument("--steps", type=int, default=40)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--rule-choice", default="random")
    parser.add_argument("--aggregate-mode", default="additive", choices=["additive", "max"])
    parser.add_argument("--M-cap", type=float, default=4.0)
    parser.add_argument("--rho-b", type=float, default=0.20)
    parser.add_argument("--rho-q", type=float, default=0.10)
    parser.add_argument("--mu-C", type=float, default=1.0)
    parser.add_argument("--mu-B", type=float, default=1.0)
    parser.add_argument("--mu-R", type=float, default=1.0)
    parser.add_argument("--mu-A", type=float, default=1.0)
    parser.add_argument("--mu-P", type=float, default=1.0)
    parser.add_argument("--output", default="")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    payload = build_payload(args)
    text = json.dumps(payload, indent=2)
    if args.output:
        out_path = Path(args.output)
        out_path.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
