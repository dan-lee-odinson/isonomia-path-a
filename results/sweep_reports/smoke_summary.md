# Sweep report — smoke

- 60 LHS points × 3 seeds × 3 variants = 540 runs in 457s (0.85s/run)
- stable points (no LS §10 criterion tripped in any run): 48/60 (80%)
- largest connected stable component: 63% of swept volume (package pass needs ≥20%, Sim Plan §6) → **PASS**

## Run-level trip reasons

- supply_superlinear: 13

## Per-parameter trip rate (low / mid / high tercile)

- `params.alpha`: [0.25, 0.25, 0.1]
- `params.beta_listing`: [0.1, 0.25, 0.25]
- `params.d_erg`: [0.2, 0.1, 0.3]
- `params.l_cap_mult`: [0.15, 0.15, 0.3]
- `params.p_star`: [0.15, 0.25, 0.2]
- `params.k_prior`: [0.25, 0.15, 0.2]
- `params.lambda_inherit`: [0.2, 0.25, 0.15]
- `params.kleos_half_life_days`: [0.2, 0.3, 0.1]
- `params.capacity_min_tasks`: [0.15, 0.2, 0.25]
- `params.settlement_fee_init`: [0.25, 0.0, 0.35]
