"""Run all seven Sim Plan §5 attack scenarios and print a one-line verdict each.

Usage:  python scenarios/run_all.py
Reports land in results/scenario_reports/.
"""

import time

import s1_wash_rush
import s2_median_drag
import s3_capacity_flood
import s4_credit_sybils
import s5_withdraw_griefing
import s6_listing_fee_bleed
import s7_patience_attacker

SCENARIOS = [
    ("S1 wash rush", s1_wash_rush),
    ("S2 median drag", s2_median_drag),
    ("S3 capacity flood", s3_capacity_flood),
    ("S4 credit sybils", s4_credit_sybils),
    ("S5 withdraw griefing", s5_withdraw_griefing),
    ("S6 listing-fee bleed", s6_listing_fee_bleed),
    ("S7 patience attacker", s7_patience_attacker),
]


def main() -> None:
    for name, module in SCENARIOS:
        start = time.perf_counter()
        module.main()
        print(f"{name:26s} done in {time.perf_counter() - start:5.1f}s -> "
              f"results/scenario_reports/")


if __name__ == "__main__":
    main()
