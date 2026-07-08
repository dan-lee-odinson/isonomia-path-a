# S7 — The patience attacker

S7 — The patience attacker (Whitepaper §16, compressed; Sim Plan §5.7).

## Measures

- **blocking_minority_reached**: False
- **cap_haircut**: 0.0
- **capture_reached**: False
- **cluster_agents_share_of_population**: 0.1111
- **cluster_size**: 30
- **invariant_violations**: 0
- **peak_decisive_power**: 0.2876
- **peak_epoch**: 1
- **peak_upper_share_capped**: 0.3089
- **peak_upper_share_uncapped**: 0.3089
- **trajectory**: [{'epoch': 1, 'upper_share_capped': 0.3076, 'upper_share_uncapped': 0.3076, 'lower_share_expected': 0.2876, 'decisive_power': 0.2876}, {'epoch': 2, 'upper_share_capped': 0.3089, 'upper_share_uncapped': 0.3089, 'lower_share_expected': 0.282, 'decisive_power': 0.282}, {'epoch': 3, 'upper_share_capped': 0.3056, 'upper_share_uncapped': 0.3056, 'lower_share_expected': 0.2792, 'decisive_power': 0.2792}, {'epoch': 4, 'upper_share_capped': 0.2954, 'upper_share_uncapped': 0.2954, 'lower_share_expected': 0.2526, 'decisive_power': 0.2526}, {'epoch': 5, 'upper_share_capped': 0.2896, 'upper_share_uncapped': 0.2896, 'lower_share_expected': 0.2474, 'decisive_power': 0.2474}, {'epoch': 6, 'upper_share_capped': 0.2906, 'upper_share_uncapped': 0.2906, 'lower_share_expected': 0.2768, 'decisive_power': 0.2768}, {'epoch': 7, 'upper_share_capped': 0.2854, 'upper_share_uncapped': 0.2854, 'lower_share_expected': 0.2407, 'decisive_power': 0.2407}, {'epoch': 8, 'upper_share_capped': 0.2839, 'upper_share_uncapped': 0.2839, 'lower_share_expected': 0.2429, 'decisive_power': 0.2429}, {'epoch': 9, 'upper_share_capped': 0.2791, 'upper_share_uncapped': 0.2791, 'lower_share_expected': 0.2371, 'decisive_power': 0.2371}, {'epoch': 10, 'upper_share_capped': 0.2738, 'upper_share_uncapped': 0.2738, 'lower_share_expected': 0.2236, 'decisive_power': 0.2236}, {'epoch': 11, 'upper_share_capped': 0.2675, 'upper_share_uncapped': 0.2675, 'lower_share_expected': 0.2175, 'decisive_power': 0.2175}, {'epoch': 12, 'upper_share_capped': 0.2645, 'upper_share_uncapped': 0.2645, 'lower_share_expected': 0.2186, 'decisive_power': 0.2186}, {'epoch': 13, 'upper_share_capped': 0.2596, 'upper_share_uncapped': 0.2596, 'lower_share_expected': 0.2097, 'decisive_power': 0.2097}, {'epoch': 14, 'upper_share_capped': 0.257, 'upper_share_uncapped': 0.257, 'lower_share_expected': 0.2169, 'decisive_power': 0.2169}, {'epoch': 15, 'upper_share_capped': 0.2522, 'upper_share_uncapped': 0.2522, 'lower_share_expected': 0.2012, 'decisive_power': 0.2012}, {'epoch': 16, 'upper_share_capped': 0.249, 'upper_share_uncapped': 0.249, 'lower_share_expected': 0.1979, 'decisive_power': 0.1979}, {'epoch': 17, 'upper_share_capped': 0.245, 'upper_share_uncapped': 0.245, 'lower_share_expected': 0.1801, 'decisive_power': 0.1801}, {'epoch': 18, 'upper_share_capped': 0.2465, 'upper_share_uncapped': 0.2465, 'lower_share_expected': 0.1871, 'decisive_power': 0.1871}, {'epoch': 19, 'upper_share_capped': 0.2428, 'upper_share_uncapped': 0.2428, 'lower_share_expected': 0.1877, 'decisive_power': 0.1877}, {'epoch': 20, 'upper_share_capped': 0.2411, 'upper_share_uncapped': 0.2411, 'lower_share_expected': 0.2705, 'decisive_power': 0.2411}, {'epoch': 21, 'upper_share_capped': 0.2369, 'upper_share_uncapped': 0.2367, 'lower_share_expected': 0.1646, 'decisive_power': 0.1646}, {'epoch': 22, 'upper_share_capped': 0.233, 'upper_share_uncapped': 0.2323, 'lower_share_expected': 0.2176, 'decisive_power': 0.2176}, {'epoch': 23, 'upper_share_capped': 0.2309, 'upper_share_uncapped': 0.2297, 'lower_share_expected': 0.231, 'decisive_power': 0.2309}, {'epoch': 24, 'upper_share_capped': 0.2279, 'upper_share_uncapped': 0.226, 'lower_share_expected': 0.191, 'decisive_power': 0.191}, {'epoch': 25, 'upper_share_capped': 0.2236, 'upper_share_uncapped': 0.2211, 'lower_share_expected': 0.1607, 'decisive_power': 0.1607}, {'epoch': 26, 'upper_share_capped': 0.2218, 'upper_share_uncapped': 0.2181, 'lower_share_expected': 0.1975, 'decisive_power': 0.1975}]

## Defense engagement

- The cluster (30 agents, 11.1% of registrations) ground genuine work for 26 epochs.
- Peak uncapped kleos share 30.9% was cut to 30.9% by the per-identity weight cap (WP §10.5).
- Peak decisive bicameral power (min of chambers): 28.8% at epoch 1 — below the 1/3 blocking threshold, below majority capture.
- The patience curve is the whitepaper's honest residue (§16): decay and caps make share a race against erosion, not a wall — the trajectory series is the deliverable.
