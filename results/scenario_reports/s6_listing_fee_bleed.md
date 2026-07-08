# S6 — Listing-fee bleed attack

S6 — Listing-fee bleed attack (Sim Plan §5.6).

## Measures

- **end_capacity**: {'a0035': 9, 'a0072': 23, 'a0080': 24, 'a0154': 24, 'a0224': 1, 'a0076': 24, 'a0175': 4, 'a0006': 3}
- **invariant_violations**: 0
- **listing_fees_paid_ergs**: {'a0035': 24.683, 'a0072': 26.734, 'a0080': 18.712, 'a0154': 22.868, 'a0224': 15.148, 'a0076': 27.502, 'a0175': 21.348, 'a0006': 15.81}
- **peak_capacity**: {'a0035': 14, 'a0072': 24, 'a0080': 24, 'a0154': 24, 'a0224': 14, 'a0076': 24, 'a0175': 14, 'a0006': 15}
- **post_flood_mean_capacity_adaptive**: 18.75
- **post_flood_mean_capacity_honest**: 10.73
- **targets_adaptive**: ['a0035', 'a0072', 'a0080', 'a0154']
- **targets_honest**: ['a0224', 'a0076', 'a0175', 'a0006']
- **twin_end_capacity**: {'a0035': 1, 'a0072': 24, 'a0080': 24, 'a0154': 24, 'a0224': 21, 'a0076': 24, 'a0175': 1, 'a0006': 13}

## Defense engagement

- During the flood, victims' fill-driven capacity adaptation ratcheted envelopes up to peaks of 24 tasks/epoch.
- After the flood vanished, the −1/epoch shrink rule walked capacity back down; post-flood mean capacity: adaptive 18.75 vs honest 10.73 (both escape, symmetric rule; the bleed tail is the asymmetry between +1 ratchet-up under flood and −1 decay).
- The attack's lever is real: every flood task was funded and settled at full price — the adversary paid workers market rates to inflate their fee base. β at the launch value (0.005) makes the induced fee burn small relative to flood spend; the sweep explores whether higher β turns this attack economic.
