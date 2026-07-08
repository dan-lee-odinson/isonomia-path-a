# S1 — Wash-settlement activation rush

S1 — Wash-settlement activation rush (Sim Plan §5.1).

## Measures

- **fake_principals**: {'variant': 'fake_principals', 'wash_attempted': 7680, 'wash_settled': 6309, 'qualified_capped_attack': 5063, 'qualified_capped_twin': 6812, 'clock_advance_from_attack': -1749, 'leakage_per_attempt': -0.227734, 'activation_epoch_attack': 16, 'activation_epoch_twin': 12, 'invariant_violations': 0}
- **full_evasion**: {'variant': 'full_evasion', 'wash_attempted': 7680, 'wash_settled': 6101, 'qualified_capped_attack': 6216, 'qualified_capped_twin': 6812, 'clock_advance_from_attack': -596, 'leakage_per_attempt': -0.077604, 'activation_epoch_attack': 13, 'activation_epoch_twin': 12, 'invariant_violations': 0}
- **honest_disclosure**: {'variant': 'honest_disclosure', 'wash_attempted': 7680, 'wash_settled': 6309, 'qualified_capped_attack': 4372, 'qualified_capped_twin': 6812, 'clock_advance_from_attack': -2440, 'leakage_per_attempt': -0.317708, 'activation_epoch_attack': 0, 'activation_epoch_twin': 12, 'invariant_violations': 0}

## Defense engagement

- honest_disclosure: clock advance -2440 on 7680 attempts (leakage -31.7708% per attempt)
- fake_principals: clock advance -1749 on 7680 attempts (leakage -22.7734% per attempt)
- full_evasion: clock advance -596 on 7680 attempts (leakage -7.7604% per attempt)
- Defense order observed: same-principal exclusion (a), same-lineage exclusion (b), trivial-spam flags + Auditor review + 2% pair caps (c).
