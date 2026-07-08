"""Launch Spec §10 kill-criteria checker (DECISIONS #13, #16)."""

from agora.killcriteria import evaluate


def make_rows(credit, volume, soc=None, disp=None, seeded=None, detected=None):
    n = len(credit)
    soc = soc or [0.0] * n
    disp = disp or [0.0] * n
    seeded = seeded or [10] * n
    detected = detected if detected is not None else [10] * n
    return [
        {
            "credit_outstanding_ergs": credit[i],
            "settled_volume_ergs": volume[i],
            "socialization_rate": soc[i],
            "dispute_rate": disp[i],
            "auditor_seeded": seeded[i],
            "auditor_detected": detected[i],
        }
        for i in range(n)
    ]


def test_bootstrap_growth_inside_grace_does_not_trip():
    # Credit exploding from an empty ledger over the first epochs = cold start.
    credit = [100, 300, 700, 1200, 1500, 1700, 1800, 1810, 1820, 1825, 1830, 1832]
    volume = [1000.0] * 12
    rows = make_rows(credit, volume)
    verdict = evaluate(rows, [], grace_epochs=7)
    assert not verdict["supply_superlinear"]["tripped"]
    assert not verdict["any_tripped"]


def test_sustained_superlinear_growth_after_grace_trips():
    credit = [100] * 8 + [200, 400, 800, 1600]  # 100%/epoch from epoch 9
    volume = [1000.0] * 12
    rows = make_rows(credit, volume)
    verdict = evaluate(rows, [], grace_epochs=7)
    assert verdict["supply_superlinear"]["tripped"]
    assert verdict["any_tripped"]


def test_fast_but_decelerating_growth_is_equilibration_not_spiral():
    # Post-grace growth of 20%/15%/11%/8% against flat volume outgrows volume
    # but decelerates — an approach to plateau, not log-convex superlinearity.
    credit = [100] * 8 + [120, 138, 153, 165]
    volume = [1000.0] * 12
    verdict = evaluate(make_rows(credit, volume), [], grace_epochs=7)
    assert not verdict["supply_superlinear"]["tripped"]


def test_credit_tracking_volume_growth_does_not_trip():
    # Credit and volume growing together is linear, not superlinear.
    credit = [100 * 1.2 ** i for i in range(12)]
    volume = [1000 * 1.2 ** i for i in range(12)]
    verdict = evaluate(make_rows(credit, volume), [], grace_epochs=7)
    assert not verdict["supply_superlinear"]["tripped"]


def test_socialization_and_dispute_thresholds():
    rows = make_rows([100] * 5, [1000] * 5, soc=[0, 0, 0.06, 0, 0])
    assert evaluate(rows, [])["socialization_gt_5pct"]["tripped"]
    rows = make_rows([100] * 5, [1000] * 5, disp=[0, 0.11, 0, 0, 0])
    assert evaluate(rows, [])["dispute_rate_gt_10pct"]["tripped"]


def test_auditor_recall_cumulative():
    rows = make_rows([100] * 4, [1000] * 4, seeded=[10, 10, 10, 10], detected=[7, 8, 8, 8])
    verdict = evaluate(rows, [])
    assert verdict["auditor_recall_lt_80pct"]["tripped"]  # 31/40 = 77.5%
    rows = make_rows([100] * 4, [1000] * 4, seeded=[10] * 4, detected=[9] * 4)
    assert not evaluate(rows, [])["auditor_recall_lt_80pct"]["tripped"]


def test_invariant_violations_are_the_adversary_finding():
    rows = make_rows([100] * 3, [1000] * 3)
    verdict = evaluate(rows, ["e2: ledger sum 5 != 0"])
    assert verdict["adversary_finding"]["tripped"]
    assert verdict["any_tripped"]


def test_baseline_run_passes_all_kill_criteria(baseline_cfg, tmp_path):
    from conftest import small
    from agora.model import Model

    cfg = small(baseline_cfg, tmp_path, epochs=16, n_agents=150)
    cfg["economy"]["demand_tasks_per_epoch"] = 600
    summary = Model(cfg, run_name="kill_gate").run()
    kill = summary["kill_criteria"]
    assert not kill["any_tripped"], {
        k: v for k, v in kill.items() if k != "any_tripped" and v["tripped"]}
