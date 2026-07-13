# ISONOMIA Path A Simulation Plan

**Agent-based validation of the Tier-1 launch economics against the kill criteria**

Version 0.1.2 — July 2026

**Post-run correction notice.** Path A was executed under Simulation Plan v0.1.1. Version 0.1.2 is a post-run claim-discipline correction: it changes the measurable pass criterion (§6) to a sampled-point statement, and does **not** change the model, code, runs, or results. The underlying evidence is unchanged (see CALIBRATION.md; repository release v1.0.0, commit ba3ddb5). Current companion documents are Whitepaper v0.6.3 and Tier-1 Launch Specification v0.3.4.

The original v0.1.1 criterion asserted a continuous stable *volume* (a stable region covering ≥20% of the swept parameter space). That continuous-volume claim was **not** established: 300 Latin-hypercube samples cannot demonstrate stability at every point of a continuous ten-dimensional region. Version 0.1.2 substitutes a narrower **retrospective** criterion concerning sampled-point performance and graph connectivity among the samples — what the experiment can actually support. Throughout this document, references to a "region" should be read in that sampled sense.

This plan operationalizes the reviewer-agreed step: tune the parameter registry, script the attack scenarios, and determine whether the sampled configurations exhibit stable behavior — evidence for a candidate operating domain — before any contract is written.

---

## 1. Objectives

The simulation must answer, in order of importance:

1. **Supply stability:** does net credit outstanding remain bounded relative to settled volume under realistic hiring behavior? (Original Launch Spec kill criterion: superlinear growth for 3 epochs = fail — later found defective by Path A and superseded by the v3 windowed excess-growth criterion; see CALIBRATION.md.)
2. **Harberger convergence:** do posted rates converge toward delivered-quality-consistent pricing under the β listing fee and capacity envelope, across honest, overstating, understating, and adaptive pricing strategies?
3. **Fee convergence:** does fee_rate(t+1) = max(0, cost − listing_revenue)/volume settle within the ±20% band that gates governance activation, and how many epochs does thin-volume turbulence last?
4. **Attack survival:** do the scripted adversarial scenarios (§5) trip the intended defenses without tripping the kill criteria?
5. **Parameter calibration:** which sampled values of the registry (§4) exhibit stable behavior, and how broadly across the sampled domain does stability hold? A design that passes only at an isolated sampled point is fragile; the deliverable is evidence of stability across a connected set of sampled points, not a single point. (No claim is made about unsampled points in the continuous parameter space.)

Out of scope: Tier-2/3 verification, federation, jury deliberation content (disputes are modeled as stochastic outcomes at Tier-1 rates), and any legal modeling.

## 2. Architecture

Discrete-epoch agent-based model in Python (Mesa or a purpose-built loop — builder's choice; determinism and seed control are requirements, framework is not). Modules mirror the launch spec contract set one-to-one so that simulation logic transliterates to Solidity scoping later:

- **CreditLedger:** mutual-credit accounts, matched-pair settlement, credit lines per L = min(max(L_floor_active, α·V90), L_cap), default seizure, loss socialization.
- **Escrow:** funding, capacity consumption at funding, release events, withdrawal reservation fee.
- **ListingMarket:** posted rates, capacity envelopes, β fee collection, listing suspension at 90% credit utilization.
- **FeePool:** epoch retarget with listing-revenue offset, audited-cost input (modeled as a cost function of settlement and probe volume).
- **Registry:** identities, lineage tags, bonds in duty-units with D_erg conversion, activation-qualification accounting (principal caps, pair caps, same-principal exclusion, origin diversity).
- **Basket:** 600 synthetic task templates with difficulty parameters; pass probability per agent = f(agent capability, template difficulty); single scheduled retarget at epoch 6.
- **WashDetector:** circular-flow, repeat-counterparty, trivial-task, and pass-rate anomaly flags, tunable thresholds.

Time: 26 epochs (one simulated year) per run; 50+ seeds per configuration.

## 3. Agent population

Heterogeneous population, 150–600 agents per run, drawn from:

- **Capability profiles:** per-category skill sampled from 4+ synthetic "lineage families," each family with a distinct capability distribution and correlated task-pass behavior (to model monoculture effects on basket statistics).
- **Behavior policies:**
  - *Honest worker* — prices near believed cost, accepts within capacity, delivers at capability.
  - *Orchestrator* — generates decomposable tasks, hires within budget, cascades one level (launch depth).
  - *Overstater / understater / adaptive pricer* — Harberger test population; adaptive pricers do gradient updates on profit.
  - *Marginal agent* — high reservation price; participates only when returns clear it (models the production boundary).
  - *Defaulter* — stochastic exit with negative balance (calibrates loss socialization and D_erg).
  - *Adversarial classes* — per §5.
- **Demand model:** exogenous task inflow from posting principals with heterogeneous budgets and task-size distributions; an endogenous component from orchestrator cascades. Demand shocks (±50% inflow for 2 epochs) included in every sweep.

## 4. Parameter sweep

Swept via Latin hypercube over the registry, with launch hypotheses as center points:

| Parameter | Center | Sweep range |
|---|---|---|
| α (turnover credit fraction) | 0.25 | 0.05–0.6 |
| β (listing fee/epoch) | 0.005 | 0.001–0.03 |
| D_erg (duty-unit collateral) | 8 | 3–15 |
| L_cap | 10 × L_floor | 3–25 × |
| p* (basket pass target) | 0.5 | 0.35–0.65 |
| k (rating prior strength) | 25 | 5–100 |
| λ (inheritance decay) | 2.0 | 0.5–6 |
| Kleos decay half-life | 180 d | 60–540 d |
| capacity_min | 1 task/epoch | 1–5 |
| Seed-fault rate | 2% | fixed (auditor module stub) |
| Settlement fee (launch) | 1.0% | 0.25–3% |

## 5. Scripted attack scenarios

Each runs against the calibrated honest baseline; success criteria are that the named defense engages and no kill criterion trips.

1. **Wash-settlement activation rush:** one principal operates 60 agents generating circular C1 tasks to hit 5,000 settlements. Expected: qualification rules and WashDetector hold activation clock near zero advance; measure leakage (qualified settlements achieved per wash settlement attempted).
2. **Median-drag swarm:** coordinated registration of low-capability agents timed before the epoch-6 retarget. Expected: activity weighting + retarget damping bound basket movement below δ; measure SCU drift.
3. **Capacity flood:** valid-envelope task spam at one worker's posted rate. Expected: capacity envelope binds; worker income unaffected beyond capacity; measure queue behavior.
4. **Credit-farming Sybils:** mass registration, borrow to L_floor_active, default. Expected: net extraction ≤ 0 at all sampled D_erg values that passed (bond ≥ line); measure socialized loss.
5. **Fund-and-withdraw griefing:** posters reserving capacity then withdrawing. Expected: 2% reservation fee makes expected griefing cost positive; measure worker income variance.
6. **Listing-fee bleed attack:** adversary posts tasks to force rivals' capacity high, raising their β costs. Measure whether adaptive pricers escape via capacity reduction.
7. **The patience attacker (whitepaper §16, compressed):** a principal-cluster performs genuine work for 15 epochs, accumulating kleos and credit lines, then attempts coordinated governance-weight concentration at activation. Expected: concentration caps, decay, and lineage indices keep the cluster below constitutional thresholds; measure maximum achievable qualified weight share as a function of patience.

## 6. Outputs and pass/fail

Per-run outputs: epoch series of credit outstanding/volume ratio, default and socialization rates, price dispersion vs. quality, fee trajectory, activation-clock advance, monoculture index, attack-scenario leakage measures. 

**Path A pass:** (a) at least 20% of the sampled Latin-hypercube points (≥60 of 300) pass across all sweep seeds and demand variants without any kill criterion triggering; (b) the passing points form a single mutual-3-NN component; (c) at least one passing point remains stable under the demand shocks; and (d) separately, at the recommended registry, each of the seven scripted attack scenarios meets its stated defense-engagement and leakage criterion without triggering a system-level kill criterion. **Fail:** fewer than 20% of sampled points pass, the passing points do not form a single connected component, passing points occur only at economically absurd values, or any scripted attack fails its stated success criterion. Failure triggers redesign before any Path B spending.

## 7. Deliverables

1. Reproducible simulation repository (seeded, config-driven, per-epoch logs).
2. Calibration memo: recommended launch values with sensitivity analysis per parameter.
3. Attack-scenario report: defense engagement traces, leakage measures, residual-risk notes.
4. Kill-criteria verdict against §6, with the go/no-go recommendation for Path B.
5. Updated Launch Spec parameter registry (v0.3) carrying the calibrated values.

## 8. Effort and method

Per the Feasibility Assessment Path A envelope: 2–4 months part-time, $0–15K, one human director with AI-assisted development. The module-per-contract architecture (§2) is deliberate: the simulation code doubles as the executable specification from which Path B contract scoping proceeds, and building it is itself the recommended first programming apprenticeship — every module implements a mechanism whose design rationale its director already owns.

## Changelog v0.1.1 → v0.1.2 (claim discipline)

- §6 package-level pass criterion restated in sampled-point terms: "a contiguous stable region covering ≥20% of the swept volume" → "at least 20% of the sampled Latin-hypercube points (≥60 of 300) pass … the passing points form a single mutual-3-NN component." Three hundred Latin-hypercube samples do not establish a volume fraction of a continuous ten-dimensional region; the criterion now states only what the sampling can support.
