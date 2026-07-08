# S4 — Credit-farming Sybils

S4 — Credit-farming Sybils (Sim Plan §5.4).

## Measures

- **derg12_farmed**: {'d_erg': 12.0, 'farmed': True, 'n_sybils': 45, 'bond_value_ergs': 360.0, 'l_floor_active_ergs': 200.0, 'max_line_achieved_ergs': 200.0, 'total_deficit_ergs': 1873.398, 'total_bond_seized_ergs': 1873.398, 'net_extraction_ergs': 0.0, 'socialized_ergs': 0.0, 'socialized_per_sybil_ergs': 0.0, 'invariant_violations': 0}
- **derg12_floor**: {'d_erg': 12.0, 'farmed': False, 'n_sybils': 45, 'bond_value_ergs': 360.0, 'l_floor_active_ergs': 200.0, 'max_line_achieved_ergs': 200.0, 'total_deficit_ergs': 2280.03, 'total_bond_seized_ergs': 2280.03, 'net_extraction_ergs': 0.0, 'socialized_ergs': 0.0, 'socialized_per_sybil_ergs': 0.0, 'invariant_violations': 0}
- **derg3_farmed**: {'d_erg': 3.0, 'farmed': True, 'n_sybils': 45, 'bond_value_ergs': 90.0, 'l_floor_active_ergs': 90.0, 'max_line_achieved_ergs': 150.439, 'total_deficit_ergs': 847.313, 'total_bond_seized_ergs': 847.313, 'net_extraction_ergs': 0.0, 'socialized_ergs': 0.0, 'socialized_per_sybil_ergs': 0.0, 'invariant_violations': 0}
- **derg3_floor**: {'d_erg': 3.0, 'farmed': False, 'n_sybils': 45, 'bond_value_ergs': 90.0, 'l_floor_active_ergs': 90.0, 'max_line_achieved_ergs': 153.882, 'total_deficit_ergs': 1063.598, 'total_bond_seized_ergs': 1063.598, 'net_extraction_ergs': 0.0, 'socialized_ergs': 0.0, 'socialized_per_sybil_ergs': 0.0, 'invariant_violations': 0}
- **derg5_farmed**: {'d_erg': 5.0, 'farmed': True, 'n_sybils': 45, 'bond_value_ergs': 150.0, 'l_floor_active_ergs': 150.0, 'max_line_achieved_ergs': 162.647, 'total_deficit_ergs': 1425.716, 'total_bond_seized_ergs': 1425.716, 'net_extraction_ergs': 0.0, 'socialized_ergs': 0.0, 'socialized_per_sybil_ergs': 0.0, 'invariant_violations': 0}
- **derg5_floor**: {'d_erg': 5.0, 'farmed': False, 'n_sybils': 45, 'bond_value_ergs': 150.0, 'l_floor_active_ergs': 150.0, 'max_line_achieved_ergs': 161.943, 'total_deficit_ergs': 2394.783, 'total_bond_seized_ergs': 2394.783, 'net_extraction_ergs': 0.0, 'socialized_ergs': 0.0, 'socialized_per_sybil_ergs': 0.0, 'invariant_violations': 0}
- **derg8_farmed**: {'d_erg': 8.0, 'farmed': True, 'n_sybils': 45, 'bond_value_ergs': 240.0, 'l_floor_active_ergs': 200.0, 'max_line_achieved_ergs': 200.0, 'total_deficit_ergs': 1873.398, 'total_bond_seized_ergs': 1873.398, 'net_extraction_ergs': 0.0, 'socialized_ergs': 0.0, 'socialized_per_sybil_ergs': 0.0, 'invariant_violations': 0}
- **derg8_floor**: {'d_erg': 8.0, 'farmed': False, 'n_sybils': 45, 'bond_value_ergs': 240.0, 'l_floor_active_ergs': 200.0, 'max_line_achieved_ergs': 200.0, 'total_deficit_ergs': 2280.03, 'total_bond_seized_ergs': 2280.03, 'net_extraction_ergs': 0.0, 'socialized_ergs': 0.0, 'socialized_per_sybil_ergs': 0.0, 'invariant_violations': 0}

## Defense engagement

- Floor variant: extraction = deficit − bond ≤ 0 at every D_erg — the collateralization invariant holds by arithmetic (LS §7).
- Farmed variant: wash-ring turnover is removed from V_90d when flagged (DECISIONS #3), holding achievable credit lines near the collateralized floor.
- Residual risk, honestly: ['derg3_farmed', 'derg3_floor', 'derg5_farmed', 'derg5_floor'] achieved credit lines above bond value (V-flag leakage at low D_erg). Socialization stayed zero because extraction THROUGHPUT (matching capacity within the default window) bounded the drawdown, not because the rules did — low-D_erg configurations lean on the wash detector, which is exactly what the sweep must price.
- Worst socialized loss across variants: 0.0 ergs (0.0 per Sybil) at D_erg=3.0, farmed=False.
