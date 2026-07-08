# S2 — Median-drag swarm

S2 — Median-drag swarm (Sim Plan §5.2).

## Measures

- **cohort_size**: 120
- **drag_settlements_won**: 157
- **invariant_violations**: 0
- **mean_difficulty_attack**: 0.1899
- **mean_difficulty_twin**: 0.1954
- **retired_attack**: 120
- **retired_twin**: 120
- **scu_drift_abs**: 0.00554
- **scu_drift_within_delta**: True
- **scu_index_attack**: 0.313999
- **scu_index_twin**: 0.319539

## Defense engagement

- Drag cohort won 157 settlements by price dumping (its activity weight).
- Retarget retired 120 templates under attack vs 120 in the twin.
- SCU index drift 0.0055 vs the retarget band δ = 0.1 — within the band.
- Activity weighting means the swarm only influences templates it actually wins and delivers; its band-0 concentration bounds the reachable surface.
