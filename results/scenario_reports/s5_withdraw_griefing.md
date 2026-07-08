# S5 — Fund-and-withdraw griefing

S5 — Fund-and-withdraw griefing (Sim Plan §5.5).

## Measures

- **grief_withdrawals**: 359
- **griefer_net_spend_ergs**: 136.943
- **invariant_violations**: 0
- **victim_income_ratio_vs_twin**: {'a0205': 0.5892, 'a0124': 1.1683, 'a0092': 0.8105, 'a0006': 0.9776}
- **victim_income_variance_ratio**: {'a0205': 3.28, 'a0124': 1.315, 'a0092': 1.063, 'a0006': 0.618}
- **victims**: ['a0205', 'a0124', 'a0092', 'a0006']

## Defense engagement

- Griefers executed 359 fund-and-withdraw cycles and paid 136.943 ergs net — griefing cost is strictly positive (2% reservation fee per cycle, LS §13.4).
- Reservation fees flow TO the victims, partially compensating displaced envelope; income ratios vs twin: {'a0205': 0.5892, 'a0124': 1.1683, 'a0092': 0.8105, 'a0006': 0.9776}.
- Income variance ratios vs twin: {'a0205': 3.28, 'a0124': 1.315, 'a0092': 1.063, 'a0006': 0.618} — the Sim Plan's requested measure.
