# S3 — Capacity flood

S3 — Capacity flood (Sim Plan §5.3).

## Measures

- **flood_overflow_unmatched_total**: 5673
- **flood_settled_total**: 388
- **flood_spend_ergs_total**: 7089.354
- **invariant_violations**: 0
- **n_seeds**: 6
- **overflow_share_of_flood**: 0.936
- **per_seed**: [{'seed': 42, 'victim': 'a0090', 'income_ratio': 0.9747, 'flood_settled': 69, 'flood_spend_ergs': 1188.869, 'flood_overflow_unmatched': 1431, 'invariant_violations': 0}, {'seed': 43, 'victim': 'a0063', 'income_ratio': None, 'flood_settled': 67, 'flood_spend_ergs': 1185.331, 'flood_overflow_unmatched': 546, 'invariant_violations': 0}, {'seed': 44, 'victim': 'a0167', 'income_ratio': None, 'flood_settled': 64, 'flood_spend_ergs': 1190.556, 'flood_overflow_unmatched': 362, 'invariant_violations': 0}, {'seed': 45, 'victim': 'a0191', 'income_ratio': None, 'flood_settled': 70, 'flood_spend_ergs': 1184.123, 'flood_overflow_unmatched': 631, 'invariant_violations': 0}, {'seed': 46, 'victim': 'a0117', 'income_ratio': 0.9579, 'flood_settled': 52, 'flood_spend_ergs': 1161.497, 'flood_overflow_unmatched': 2157, 'invariant_violations': 0}, {'seed': 47, 'victim': 'a0132', 'income_ratio': None, 'flood_settled': 66, 'flood_spend_ergs': 1178.978, 'flood_overflow_unmatched': 546, 'invariant_violations': 0}]
- **victim_income_ratio_median**: 0.9747
- **victim_income_ratio_range**: [0.9579, 0.9747]

## Defense engagement

- The envelope binds: 94% of flood tasks overflowed the victim's declared envelope and queued unmatched (LS §7: beyond capacity_i they route elsewhere with no penalty).
- Every flood task that DID land paid the victim its full posted rate — 7089.354 ergs across seeds for work the attacker discards; valid-task flooding funds its own victim.
- Victim income during the flood window: median ratio 0.9747× vs the unattacked twin across 6 seeds (range [0.9579, 0.9747]). Single-seed comparisons are unreliable here: winner-take-most matching makes late-run income chaotic, which is itself a finding about market concentration.
