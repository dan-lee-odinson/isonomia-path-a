"""Kill-criteria evaluation (Launch Spec §10) as automated checks over run outputs.

    "Kill criteria (any → halt and redesign before scale): credit outstanding
    growing superlinearly to volume for 3 epochs; default socialization > 5% of
    volume; dispute rate > 10% of settlements; Auditor seeded-fault recall < 80%;
    any Adversary finding of class 'settlement forgery' or 'credit-line inflation'."

Operationalizations (DECISIONS #13, #16):
  * superlinear supply — 3 consecutive epoch transitions with
    Δlog(credit) > max(0, Δlog(volume)) + 0.02 AND non-decreasing Δlog(credit)
    across the streak. The acceleration requirement is what "superlinear" means
    on a log scale: an equilibrating stock approaches its plateau at DECAYING
    rates (that is a cold start filling up, WP §4.2), while the unbounded spiral
    §10 names grows at non-decreasing rates. Evaluation additionally starts only
    after the credit system's trailing window has filled;
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
    prev_dlog_credit = None
    trip_epochs: list[int] = []
    supply_tripped = False
    for i in range(1, len(credit)):
        epoch = i + 1  # rows are 1-based epochs
        if epoch <= grace_epochs:
            continue
        if credit[i] <= 0 or credit[i - 1] <= 0 or volume[i] <= 0 or volume[i - 1] <= 0:
            streak, prev_dlog_credit = 0, None
            continue
        dlog_credit = math.log(credit[i] / credit[i - 1])
        dlog_volume = math.log(volume[i] / volume[i - 1])
        if dlog_credit > max(0.0, dlog_volume) + SUPPLY_MARGIN:
            if streak > 0 and dlog_credit + 1e-9 < prev_dlog_credit:
                streak = 1  # still outgrowing volume, but decelerating: not a spiral
            else:
                streak += 1
            prev_dlog_credit = dlog_credit
            if streak >= SUPPLY_STREAK:
                supply_tripped = True
                trip_epochs.append(epoch)
        else:
            streak, prev_dlog_credit = 0, None

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
