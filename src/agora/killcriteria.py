"""Kill-criteria evaluation (Launch Spec §10) as automated checks over run outputs.

Launch Spec v0.3 §10 (which adopted this module's formulation after the original
"growing superlinearly for 3 epochs" wording was shown to halt every honest launch
during bootstrap) names this file the operative authority:

    "credit-to-volume ratio exhibiting log-convex growth (non-decreasing
    epoch-over-epoch growth rates — the signature of a runaway spiral rather than
    healthy bootstrap fill) sustained for 3 consecutive epochs after a bootstrap
    grace window (grace length simulation-derived; see repository killcriteria.py
    and CALIBRATION.md for the operative formulation, which is authoritative);
    default socialization > 5% of volume; dispute rate > 10% of settlements;
    Auditor seeded-fault recall < 80%; any Adversary finding of class 'settlement
    forgery' or 'credit-line inflation'."

The precise operative test below is stated on the credit STOCK, not literally on
the credit-to-volume ratio — see DECISIONS #28 for the alignment audit (a volume
crash with flat credit grows the ratio but is not a credit spiral; the code
correctly does not trip on it).

Operationalizations (DECISIONS #13, #16, #29):
  * superlinear supply — 3+ consecutive epoch transitions with
    Δlog(credit) > max(0, Δlog(volume)) + 0.02, non-decreasing Δlog(credit)
    across the streak, AND cumulative streak growth ≥ 0.5 log-points (+65%).
    The acceleration requirement is what "superlinear" means on a log scale: an
    equilibrating stock approaches its plateau at DECAYING rates (a cold start
    filling up, WP §4.2), while a spiral grows at non-decreasing rates. The
    magnitude floor is the full sweep's empirical noise separator (DECISIONS
    #29): across 45,000 runs, shock-recovery transients that satisfy the first
    two conditions never accumulated more than 0.38 log-points (p99 = 0.26),
    while even a modest 20%/epoch compounding spiral accumulates 0.55 in three
    epochs and a doubling spiral 2.08. Evaluation starts only after the credit
    system's trailing window has filled;
  * socialization and dispute rates — epoch-level, any epoch trips;
  * auditor recall — cumulative over the run (per-epoch seeded counts are too
    small for a rate);
  * adversary findings — any runtime ledger-invariant violation (zero-sum,
    credit-line ceiling, collateralization) is the sim-level equivalent.
"""

from __future__ import annotations

import math

SUPPLY_MARGIN = 0.02
SUPPLY_STREAK = 3
SUPPLY_MIN_MAGNITUDE = 0.5  # cumulative Δlog(credit) over the streak (DECISIONS #29)
SOCIALIZATION_MAX = 0.05
DISPUTE_MAX = 0.10
RECALL_MIN = 0.80


def evaluate(epoch_rows: list[dict], invariant_violations: list[str],
             grace_epochs: int = 7) -> dict:
    """Evaluate all five criteria over a run's epoch rows. Returns a dict with
    one entry per criterion ({tripped, detail}) plus 'any_tripped'."""
    credit = [float(r["credit_outstanding_ergs"]) for r in epoch_rows]
    volume = [float(r["settled_volume_ergs"]) for r in epoch_rows]
    socialization = [float(r["socialization_rate"]) for r in epoch_rows]
    disputes = [float(r["dispute_rate"]) for r in epoch_rows]
    seeded = sum(int(r["auditor_seeded"]) for r in epoch_rows)
    detected = sum(int(r["auditor_detected"]) for r in epoch_rows)

    # -- 1. supply stability ------------------------------------------------
    streak = 0
    streak_magnitude = 0.0
    prev_dlog_credit = None
    trip_epochs: list[int] = []
    supply_tripped = False
    for i in range(1, len(credit)):
        epoch = i + 1  # rows are 1-based epochs
        if epoch <= grace_epochs:
            continue
        if credit[i] <= 0 or credit[i - 1] <= 0 or volume[i] <= 0 or volume[i - 1] <= 0:
            streak, streak_magnitude, prev_dlog_credit = 0, 0.0, None
            continue
        dlog_credit = math.log(credit[i] / credit[i - 1])
        dlog_volume = math.log(volume[i] / volume[i - 1])
        if dlog_credit > max(0.0, dlog_volume) + SUPPLY_MARGIN:
            if streak > 0 and dlog_credit + 1e-9 < prev_dlog_credit:
                streak, streak_magnitude = 1, dlog_credit  # decelerating: restart
            else:
                streak += 1
                streak_magnitude += dlog_credit
            prev_dlog_credit = dlog_credit
            if streak >= SUPPLY_STREAK and streak_magnitude >= SUPPLY_MIN_MAGNITUDE:
                supply_tripped = True
                trip_epochs.append(epoch)
        else:
            streak, streak_magnitude, prev_dlog_credit = 0, 0.0, None

    # -- 2..5 ----------------------------------------------------------------
    soc_bad = [i + 1 for i, s in enumerate(socialization) if s > SOCIALIZATION_MAX]
    disp_bad = [i + 1 for i, d in enumerate(disputes) if d > DISPUTE_MAX]
    recall = detected / seeded if seeded else 1.0

    result = {
        "supply_superlinear": {
            "tripped": supply_tripped,
            "detail": f"streak epochs {trip_epochs}" if supply_tripped else
                      f"no {SUPPLY_STREAK}-epoch streak after grace={grace_epochs}",
        },
        "socialization_gt_5pct": {
            "tripped": bool(soc_bad),
            "detail": f"epochs {soc_bad}" if soc_bad else
                      f"max {max(socialization):.4f}" if socialization else "no data",
        },
        "dispute_rate_gt_10pct": {
            "tripped": bool(disp_bad),
            "detail": f"epochs {disp_bad}" if disp_bad else
                      f"max {max(disputes):.4f}" if disputes else "no data",
        },
        "auditor_recall_lt_80pct": {
            "tripped": recall < RECALL_MIN,
            "detail": f"cumulative recall {recall:.4f} ({detected}/{seeded} seeded)",
        },
        "adversary_finding": {
            "tripped": bool(invariant_violations),
            "detail": (f"{len(invariant_violations)} invariant violation(s): "
                       f"{invariant_violations[:3]}") if invariant_violations else
                      "no ledger-invariant violations",
        },
    }
    result["any_tripped"] = any(v["tripped"] for k, v in result.items() if k != "any_tripped")
    return result
