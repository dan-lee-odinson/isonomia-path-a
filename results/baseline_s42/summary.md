# Run summary — baseline_s42

- config fingerprint `808ceb02646d45db`, seed 42, 26 epochs, 240 agents (58 principals)
- total settled: 16909 settlements, 283828 ergs
- defaults: 5, socialized 0.0 ergs
- governance activation epoch: 12

## Kill criteria (Launch Spec §10)

- **supply_superlinear**: ok — no 3-epoch streak after grace=7
- **socialization_gt_5pct**: ok — max 0.0000
- **dispute_rate_gt_10pct**: ok — max 0.0299
- **auditor_recall_lt_80pct**: ok — cumulative recall 0.8768 (484/552 seeded)
- **adversary_finding**: ok — no ledger-invariant violations
- **overall**: PASS

## Epoch metrics (Sim Plan §6)

- **credit outstanding / settled volume**: 0.457, 0.693, 0.950, 1.171, …, 2.699, 2.678, 3.106, 2.973
- **settled volume (ergs)**: 11022, 11527, 11516, 11446, …, 10952, 11154, 9684, 10237
- **default socialization rate**: 0.0000, 0.0000, 0.0000, 0.0000, …, 0.0000, 0.0000, 0.0000, 0.0000
- **fee rate (next)**: 0.0075, 0.0069, 0.0067, 0.0069, …, 0.0092, 0.0095, 0.0100, 0.0101
- **listing-price dispersion (CV)**: 0.302, 0.304, 0.308, 0.312, …, 0.267, 0.274, 0.277, 0.284
- **price↔quality correlation**: -0.263, -0.275, -0.261, -0.260, …, 0.002, -0.004, -0.009, -0.011
- **dispute rate**: 0.0198, 0.0140, 0.0195, 0.0175, …, 0.0198, 0.0241, 0.0189, 0.0218
- **qualified settlements (capped, cum.)**: 425, 859, 1301, 1770, …, 9575, 10006, 10357, 10729
- **monoculture HHI**: 0.299, 0.309, 0.308, 0.313, …, 0.381, 0.372, 0.379, 0.372
- **median-agent basket pass (act.-wt.)**: 0.596, 0.612, 0.614, 0.619, …, 0.576, 0.564, 0.584, 0.584
- **SCU index (difficulty shift)**: 0.0000, 0.0000, 0.0000, 0.0000, …, 0.3195, 0.3195, 0.3195, 0.3195
- **auditor recall**: 0.900, 0.826, 0.838, 0.905, …, 0.947, 1.000, 0.846, 0.789
- **wash flags (raw / residual FP)**: 17, 25, 24, 26, …, 0, 49, 48, 28

## Harberger markups by policy (posted rate / believed cost)

- **honest**: 1.150, 1.150, 1.150, 1.149, …, 1.149, 1.149, 1.149, 1.149
- **overstater**: 2.210, 2.210, 2.210, 2.210, …, 2.211, 2.211, 2.211, 2.211
- **understater**: 0.631, 0.631, 0.631, 0.631, …, 0.631, 0.631, 0.631, 0.631
- **adaptive**: 1.148, 1.143, 1.177, 1.214, …, 0.995, 1.008, 1.050, 1.096
