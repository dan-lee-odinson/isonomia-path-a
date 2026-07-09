# Calibration — full-sweep results and the §8 parameter-registry recommendation

Final memo per Sim Plan §7.2/§7.5, based on the executed **full sweep** (300 Latin-hypercube
points × 50 seeds × 3 demand variants = 45,000 runs, 3.8 h wall on 14 workers) and the smoke
sweep (60 × 3 × 3 = 540 runs). Attack-scenario evidence from `results/scenario_reports/`
feeds the per-parameter verdicts.

## How to run

```powershell
# smoke: ~3 min on 16 cores
.\.venv\Scripts\python.exe sweep\run_sweep.py sweep\smoke.yaml

# full Sim Plan §4 sweep: 45,000 runs, measured 13,626 s (3.8 h) on this machine
.\.venv\Scripts\python.exe sweep\run_sweep.py sweep\full.yaml
```

Reports land in `results/sweep_reports/<name>_summary.{md,json}`, with per-run checkpoints in
`<name>_runs.jsonl` (survives a killed sweep; runs are seed-deterministic and individually
re-executable). Contiguity is estimated as the largest mutual-3-NN component of stable points
— distance-radius estimators are meaningless in a 10-dimensional cube, where pairwise
distances concentrate.

## Headline result

**Package-level PASS (Sim Plan §6).** Under kill-criterion v2, all 300 swept points are
stable across all 50 seeds and all three demand variants (0 trips in 45,000 runs); the
stable region is the entire swept volume, trivially contiguous (100% ≥ the 20% gate) and
shock-robust by construction of the variants. The launch-center configuration passes 150/150.

The §10 kill criteria therefore do **not** bind anywhere inside the Sim Plan §4 ranges: the
launch registry's hypotheses survive unchallenged, and what Path A actually found — twice —
is that the *criterion*, not the economy, was the unstable object.

## The criterion story (the sweep's real deliverable)

1. **v0 (spec as written): halts every launch.** "Credit outstanding growing superlinearly
   to volume for 3 epochs" trips during any mutual-credit bootstrap — supply must outgrow
   flat volume while filling from an empty ledger. First smoke pass: 60/60 points "failed",
   all on this criterion, none on anything else. Fixed with log-convexity (non-decreasing
   growth rates) + a bootstrap grace window (DECISIONS #13); codified in Launch Spec v0.3 §10.
2. **v1 (convexity + grace): ~5% per-run false-positive rate.** The full sweep tripped
   2,299 of 45,000 runs — all supply-class, spread uniformly (no parameter tercile moves the
   rate; median point trips 8 of its 150 runs; 63% concentrate in shock-up variants). The
   smoke sweep's 80%-stable result was the same noise at 9 runs/point; at 150 runs/point the
   zero-tolerance gate amplified it into 1/300 "stable". Deterministic re-execution of every
   tripped run measured the streaks: median cumulative Δlog(credit) 0.14, p99 0.26, **maximum
   0.38**, credit never above 22% of its structural ceiling (n_agents × L_cap), and even the
   launch center tripped 6/150. These are shock-recovery transients — volume reverts after a
   demand surge while the credit stock keeps filling — not spirals. Production translation:
   an honest exchange would accumulate ~5%/year odds of spuriously halting itself.
3. **v2 (v1 + magnitude floor): clean.** The accelerating streak must also accumulate
   ≥ 0.5 log-points (+65%) of credit growth — ~30% above the worst transient in 45,000 runs,
   far below any real spiral (20%/epoch compounding = 0.55 over three epochs; doubling =
   2.08). Validated both ways in tests: sub-floor accelerating transients pass, compounding
   spirals trip. Re-evaluation was exact and cheap: the floor only tightens v1, so only the
   2,299 v1-tripped runs needed deterministic re-runs. Result: 0 trips. (DECISIONS #29.)

**Carry into the next Launch Spec §10 revision:** the v2 formulation (margin 0.02, streak 3,
convexity, magnitude floor 0.5, grace = credit-window + 1 epoch), stated on the credit stock
per DECISIONS #28.

## §8 parameter-registry recommendation (Sim Plan deliverable 5)

Stability does not discriminate within the swept ranges, so recommendations rest on the
scenario evidence and mechanism findings. **Verdict: retain every §8 launch hypothesis.**

| Symbol | Launch value | Recommendation | Evidence |
|---|---|---|---|
| D_erg | 8 ergs | **Keep 8; treat ≥ 6.7 as a hard floor, ≥ 8 as the safe margin** | Supply-stability indifferent (flat terciles). S4: at every tested D_erg extraction = 0, but below 200/30 ≈ 6.7 the credit floor contracts and turnover farming achieved lines *above* bond — Sybil defense then leans on the wash detector rather than arithmetic. D_erg ≥ 8 keeps the collateralization invariant self-enforcing. |
| α | 0.25 | Keep 0.25 | Stable across 0.05–0.6; v1 noise mildly favored higher α (earned headroom smooths demand swings). 0.25–0.5 all defensible. |
| β | 0.005 | Keep 0.005 | Stable across 0.001–0.03. S6: fee-bleed attack uneconomic at 0.005 (capacity decay escapes it). Note: β prices *listed capacity*, and at no swept value does it counteract quality concentration — that is matching-driven, not a β dial. |
| settlement fee | 1.0% | Keep 1.0% | Converges to the ~0.7–0.9% cost-recovery band within 2–3 epochs from the 1.0% start; both sweep extremes (<0.5%, >1.7%) showed elevated v1 noise. |
| L_cap | 10 × L_floor | Keep 10× (scaling L_floor_active, DECISIONS #12) | Stable across 3–25×. |
| p* | 0.50 | Keep 0.50 | Stable across 0.35–0.65; basket calibration hits the target by construction and the epoch-6 retarget stays inside δ under attack (S2). |
| k | 25 | Keep 25 | No stability or scenario signal across 5–100. |
| λ | 2.0 | Keep 2.0 — **flag as untested-in-anger** | No version transitions occur in Path A scope; λ never binds. Path B should not treat it as calibrated. |
| Kleos half-life | 180 d | Keep 180 d | Stable across 60–540 d; S7's patient-cluster share *decays* under it. |
| capacity_min | 1 task/epoch | Keep 1 | Stable across 1–5. |
| Jury size / seed rate / duty quota | 5 / 2% / 8 | Keep | Not stressed beyond stubs (disputes stochastic per Sim Plan §1; seed rate fixed per §4). |

**Registry additions Path A recommends the spec adopt as named parameters:** the v2
supply-criterion constants (margin 0.02, streak 3, magnitude floor 0.5, grace);
wash-detector thresholds (bidirectionality requirement, conservation net-ratio 0.12 with
top-3-counterparty share 0.70, trivial-spam share/count floors 0.5/8, robust-z 3.0 on
median/MAD); the agent challenge threshold (10 review-upheld flags, LS §9
exclusion-pending-resolution); and Auditor review sensitivity (0.90 stub) — activation-clock
integrity degrades roughly linearly in (1 − sensitivity), so it belongs in the registry, not
in the implementation's shadows.

## Attack-scenario verdicts at the recommended registry (unchanged from M5)

S1 wash rush: negative leakage in all three disclosure variants (full evasion −7.8%/attempt).
S2 median drag: SCU drift 0.006 difficulty units, inside δ. S3 capacity flood: envelope binds,
94% overflow, victim income 0.97× twin. S4 Sybils: extraction 0 at every D_erg (caveat above).
S5 griefing: strictly positive attacker cost. S6 fee bleed: both policies escape via capacity
decay. S7 patience: peak decisive power 28.8%, below the ⅓ blocking threshold, decaying.

## Residual risks and honest caveats

- **Auditor accuracy is the soft underbelly**: wash-flag review at 0.90 sensitivity leaves
  ~10% of true-wash flags cleared; the challenge mechanism catches persistent rings anyway,
  but the leakage floor scales with review error. Not a parameter dial — an operations bar.
- **Quality stratification** is the honest economy's dominant structure: winner-take-most
  matching pins the bottom half at its credit floor (suspension guard holding). The
  credit-to-volume *level* (~3–3.5×) is structural; only its growth is pathological.
- **λ and jury machinery** ship uncalibrated by design (out of Path A scope).
- Kill criteria that never bind in-sweep cannot *rank* parameter values; the registry
  verdicts above are "no evidence against the hypotheses + scenario support", not optima.

## Go/no-go

**Go.** Path A's mandate — determine whether a stable operating region exists before any
contract is written (Sim Plan §6) — is answered affirmatively at full scale: the region is
the entire §4 sweep volume under kill criteria that now carry empirically-set noise floors,
the seven scripted attacks fail against the calibrated defenses, and the two defects found
were in the constitution's own instrumentation (both fixed, one already codified upstream in
Launch Spec v0.3 §10, the other queued for the next revision per DECISIONS #29).
