# Sweep report — full (criterion v2)

- 300 LHS points × 50 seeds × 3 variants = 45000 runs (v1 executed 2026-07-08/09; the 2,299 v1-tripped runs deterministically re-evaluated under v2)
- criterion v2 = v1 (margin + convexity + bootstrap grace) **plus** cumulative streak magnitude ≥ 0.5 log-points (DECISIONS #29)
- run-level trips: 0 / 45000 (v1: 2,299 — all shock-recovery transients; max observed magnitude 0.38)
- stable points: 300/300 (100%) (v1: 1/300)
- largest contiguous stable region (mutual 3-NN component): 100% of swept volume (package gate ≥20%, Sim Plan §6) → **PASS**
- launch-center configuration: 0/150 runs trip under v2

## Run-level trip reasons (v2)

- none

## Per-parameter trip rate (low / mid / high tercile, v2)

- `params.alpha`: [0.0, 0.0, 0.0]
- `params.beta_listing`: [0.0, 0.0, 0.0]
- `params.capacity_min_tasks`: [0.0, 0.0, 0.0]
- `params.d_erg`: [0.0, 0.0, 0.0]
- `params.k_prior`: [0.0, 0.0, 0.0]
- `params.kleos_half_life_days`: [0.0, 0.0, 0.0]
- `params.l_cap_mult`: [0.0, 0.0, 0.0]
- `params.lambda_inherit`: [0.0, 0.0, 0.0]
- `params.p_star`: [0.0, 0.0, 0.0]
- `params.settlement_fee_init`: [0.0, 0.0, 0.0]
