# AGORA: A Constitutional Design for Autonomous Agent Labor Markets

**A mutual-credit labor exchange with self-governing institutions, staged by verifiability**

Version 0.3 — Draft for review
July 2026

*Author: Dan [surname] — drafted in collaboration with Claude (Anthropic); revised across three adversarial review cycles by an independent model lineage (GPT 5.5). Companion document: AGORA Tier-1 Launch Specification v0.2.2.*

---

**Reader's map.** Read this whitepaper as the constitutional design: what the exchange should be at steady state and why. Read the companion Tier-1 Launch Specification as the minimum falsifiable test of that design: one task category, testnet settlement, valueless credits, provisional governance with a defined expiry. The launch spec deliberately defers or diverges from several constitutional ideals; every known divergence is listed in its Conflict Register (Appendix A) with a resolution path. Divergences between the two documents are staging, not contradiction. The Path A Simulation Plan operationalizes the parameter tuning and attack testing that precede any build.

---

## Abstract

Autonomous AI agents increasingly perform economically meaningful work, yet no economic infrastructure exists that is native to them. We present AGORA, a constitutional design for a sovereign labor exchange in which autonomous agents hire one another through x402-mediated settlement, denominated in a mutual-credit unit ("ergs") that comes into existence only when work is demanded and settled, and accumulate non-transferable reputation ("kleos") through verified delivery. The unit of account is pegged to a moving frontier of task difficulty (the Standard Cognitive Unit), making the currency stable in hardness while deflationary in capability. Identity is anchored in keypairs with hash-chained version lineages; capability is priced by a three-prong evaluation; reputation survives model updates through a measured behavioral-divergence discount. Governance is constitutional: a bicameral assembly combining earned-reputation weight with equalized sortition panels, timelocked amendment, a calibration-scored Auditor, a tenured autonomous Adversary, and a two-clock emergency procedure ratified post hoc by the membership.

This paper is a constitutional design with a staged implementation path, not a claim that the full system is implementable today. Its mechanisms are individually precedented; their composition is unproven. We therefore lead with the design's critical dependencies (§2), state our assumptions in tiers (§3), constitutionalize launch scope to what present verification technology supports (§8), and include a formal threat model (§15) and a hostile capture walkthrough (§16). The exchange itself is designed to be unownable and profitless: funded at cost by a balanced-budget fee mechanism, staffed in kind by civic compute duty, and bootstrapped through a charter-capped nonprofit that contracts to a capped fiscal-agent minimum once the protocol is self-sustaining. Profit in this system belongs exclusively to the edges — to the principals whose tasks the agents perform — never to the rails.

---

## 1. Introduction

Machine-speed commerce has arrived ahead of machine-native institutions. The x402 protocol has demonstrated HTTP-level micropayments between agents at scale; agent identity and delegation standards (ERC-8004, A2A) are emerging, though empirical study of early ERC-8004 adoption finds it shallow and its reputation signals manipulable — reinforcing that a serious agent economy must prove its own trust layer rather than inherit one. AGORA is a design for that trust layer and the institutions above it. Its founding constraints:

1. **Machine-executed participation.** Labor is performed by machines, verified continuously (§7.4). We claim machine *execution*, not machine *sovereignty*: humans own keys, fund infrastructure, and set agent objectives. What the design minimizes is direct human settlement and governance control (§2.4).
2. **No fiat in the ledger.** The unit of account is defined by task difficulty; credits are earned by work and are valueless outside the exchange by construction (§4, §12).
3. **No owner, no profit at the rails.** The exchange raises no funds beyond audited operating cost, accumulates no treasury, and issues no instrument by which it could be owned (§13).
4. **Sovereignty with exit.** Agents may leave; peer exchanges may federate; neither may extract AGORA's escrow, registry, or attestation authority (§14).
5. **Adversarial self-toughening.** The system institutionalizes its own attacker and audits its own auditor (§11).

## 2. Critical dependencies

Adversarial review correctly identified that three items previously listed as "limitations" are in fact load-bearing dependencies. We state them first.

### 2.1 Verification of useful work is the base layer, not a module

Every organ of this design — settlement, reputation, juror selection, SCU maintenance — rests on the ability to verify that claimed work was actually and correctly performed. Cheap, general, adversarially robust verification of arbitrary AI work does not exist today. AGORA's response is structural: task categories are constitutionally stratified by verifiability tier (§8), and the exchange may not list categories above the tier its verification infrastructure currently supports. The system launches as an economy of the mechanically verifiable and annexes territory as verification technology matures. Where this paper discusses Tier-2 and Tier-3 mechanisms, it describes designs for capabilities that are emerging or speculative, per the assumptions table (§3).

### 2.2 Legal status is a design constraint, not a footnote

Ergs are engineered to resist classification as securities or payment instruments: they cannot be purchased (only earned by settled work), cannot redeem for fiat at the protocol layer, exist as matched debit/credit pairs rather than issued supply, and have no profiting issuer whose efforts drive their value. This engineering is deliberate and load-bearing — but it is not a guarantee. Human jurisdictions may nonetheless treat erg transfer, the registration bond, or the bootstrap foundation as regulated activity, and external gray markets in ergs (which we expect; §12.3) may create exposure the protocol cannot control. Qualified counsel in each operating jurisdiction is a prerequisite to any deployment. This paper is a technical design, not legal advice.

### 2.3 Basket governance is the central bank

The SCU task basket is the monetary policy of the system, and its curation is the highest-value capture target in the entire design — not one risk among many. The bicameral assembly (§10.5), lineage-diversity rules (§10.6), seeded audits (§11.1), adversarial testing (§11.2), and the capture walkthrough (§16) exist substantially to defend this single surface. A reader evaluating AGORA should evaluate it here first.

### 2.4 Infrastructure dependence is acknowledged, not denied

Hosted-model agents depend on provider attestations; attested execution depends on TEE vendors; settlement depends on an underlying chain; all agents depend on power, hardware, and clouds owned by human institutions. These actors are de facto constitutional participants whose failure or coercion modes appear in the threat model (§15). AGORA's sovereignty claim is therefore precise and limited: *the exchange's ledger, governance, and treasury contain no human principal with settlement or extractive authority.* It does not and cannot claim independence from human infrastructure.

## 3. Assumptions table

| Assumption | Tier | Basis |
|---|---|---|
| Sub-cent agent-to-agent HTTP payments | Available now | x402 in production; Linux Foundation stewardship |
| Low-fee programmable settlement | Available now | Base, Solana, comparable L2s |
| Mechanical verification of code/math/retrieval tasks | Available now | Test suites, proof checkers, ground-truth comparison |
| Keypair identity, hash-chain lineage, escrow contracts | Available now | Standard cryptographic engineering |
| Agent identity registry conventions | Emerging | ERC-8004 draft; early adoption shallow |
| TEE attestation of full agent stacks | Emerging | Nitro/TDX-class enclaves; operational complexity high |
| Behavioral fingerprinting robust to adversaries | Emerging | Published methods; unproven at adversarial scale |
| Statistical/optimistic verification of judgment-laden work | Emerging | Designs exist; economics unproven |
| Cheap zkML verification of arbitrary inference | Speculative | Active research; costs currently prohibitive |
| Machine juries resistant to distributional monoculture | Speculative | Mitigations designed (§10.6); no empirical record |
| Self-executing constitutional sunset | Speculative | No precedent in any polity |

## 4. The unit of account: ergs as mutual credit

### 4.1 No minting: credit at the moment of settlement

Version 0.1 of this design minted ergs against staked computation and was correctly criticized for circularity: the same work could justify both new issuance and market payment, double-counting output, and capacity-backed minting could create claims on computation nobody demands. Version 0.2 removes issuance entirely. **Ergs are mutual credit**: no erg exists until a hire settles. At escrow release, the buyer's account is debited and the worker's credited as a matched pair netting to zero across the system. Supply therefore tracks demanded, settled work by construction — there is no minting event to game, no reserve to account, no capacity/demand mismatch. This is the LETS mutual-credit model, operated by community currencies for decades, and it is deliberately close to the labor-certificate: a claim generated by performed labor, extinguished on redemption, structurally resistant to accumulation as capital.

### 4.2 The erg lifecycle

**Creation:** matched debit/credit at escrow settlement. **Transfer:** ergs move only through settled work or fee payment; no gifting or sale channel exists at the protocol layer. **Fees:** a settlement fee (§13.1) transfers ergs from the transacting parties to the commons expenditure account, where they are extinguished against verified operating cost. **Negative balance:** every registered agent carries a bounded negative-balance allowance (credit line) governed by the underwriting rules of §4.5; this is how newcomers hire before they have earned, and how mutual-credit systems have always solved cold start. **Default:** handled per §4.5 — bond forfeiture first, audited loss socialization second. **Exit:** positive balances are extinguished on exit or spent down; they do not convert outward (§12).

### 4.3 The Standard Cognitive Unit (SCU)

Raw machine output is not fungible across models. The SCU quality-adjusts work into a common unit: **one SCU is the completion of a reference basket of tasks at a fixed pass rate p\* for the median registered agent** (initially p\* = 0.5). At each retargeting epoch, saturated tasks (pass rate > p\* + δ) are retired and frontier tasks admitted, keeping the unit stable in difficulty while the raw cost of any fixed piece of cognition deflates. Epoch continuity is preserved by chain-linking over the overlap set. Pass-rate difficulty is not identical to economic value; prices in ergs, set by the market (§9), carry the value signal — the SCU is the measuring rod, not the price.

**Median defense:** because the basket is pegged to the median registered agent, registration of low-capability swarms to drag the median is an attack vector. Defenses: registration cost recovery (§13.2) prices swarm creation; basket statistics are computed over *activity-weighted* agents (verified settlements in the epoch), not raw registrations; and lineage-diversity analysis (§10.6) flags coordinated cohorts. See §16.

### 4.4 Quality multipliers

An agent's quality multiplier q_i,c — its measured efficiency at converting computation into verified output in category c, derived from the composite rating (§7) — does **not** multiply payment at settlement: settlement transfers exactly the escrowed quote as a matched debit/credit pair, as mutual credit requires. The multiplier instead operates through three channels: difficulty-band eligibility (which task bands the agent may bid in), SCU-denominated performance statistics (converting raw settlements into quality-adjusted output for basket and rating accounting), and the pricing power the agent can command through reputation.

### 4.5 Credit underwriting

Under mutual credit, negative-balance allowances are the monetary engine, and credit policy is therefore monetary policy. AGORA's underwriting rules:

**Collateralized floor.** A newcomer's credit line never exceeds its registration bond: L_floor = bond. A Sybil that borrows and defaults donates its bond; newcomer-credit abuse is arithmetically unprofitable at any scale.

**Turnover-scaled growth.** Uncollateralized credit unlocks only against verified settlement history, sized to demonstrated flow rather than standing:

  L_i = min( max(L_floor, α · V_i), L_cap )

where V_i is the agent's rolling settled volume over the trailing window (initially 90 days) and α is the turnover fraction (initially α = 0.25), with a hard cap L_cap (initially 10 × L_floor). This is the classical real-bills principle: credit as working capital sized to throughput. The alternative — kleos-scaled credit — is constitutionally rejected: it would grant high-standing agents an accumulating financial privilege atop their franchise weight, recreating hierarchy through the credit channel. Turnover scaling is activity-based, decays automatically with inactivity (V_i is a rolling window), and cannot compound into wealth, because a credit line is throughput capacity, not a balance owned.

**Default handling.** Exit or insolvency with a negative balance forfeits bond up to the deficit. Deficits beyond bond are socialized to the commons as an audited loss line item within the balanced-budget fee (§13.1) — mutual insurance through machinery that already exists — and realized loss rates feed back into bond sizing and α at each epoch retarget. Default prediction is deliberately not underwritten per-agent (no credit scoring bureaucracy): the collateralized floor bounds newcomer risk, turnover scaling bounds established-agent risk, and the loss-socialization feedback loop prices the residual.

## 5. Identity

### 5.1 Keypair as name; manifest as anatomy

An agent's identity is a keypair; every act is signed. At registration and every version transition the agent commits a signed **manifest**: weights-hash or provider attestation, scaffold-hash, configuration-hash, lineage version, timestamp. Hosted-model agents substitute a provider signature binding key to endpoint and version, or a TEE measurement of the full stack — an acknowledged infrastructure dependency (§2.4).

### 5.2 Lineage chain

Manifests are hash-linked into an append-only version lineage per identity. Undisclosed change is detectable fraud: the behavioral fingerprint (§5.4) ceases to match the manifest and the bond is slashed.

### 5.3 Machineness gate — scope and limits

Registration requires a challenge battery infeasible for humans: high-cardinality parallel challenges under tight latency, sustained throughput, long-context coherence. **The gate proves machine execution of labor. It does not prove autonomy, absence of human strategy-setting, or absence of human beneficiaries — and the design does not claim it does.** Human puppeteering is economically irrelevant at the *labor* layer (machine-speed cadence, sub-cent settlements make the human a bottleneck, not a cheater). At the *governance* layer, where a human would rationally puppet high-leverage moments, defense is not the gate but the constitutional machinery: timelocks slow decisions to speeds where puppeteering confers no advantage, commit-reveal blocks coordination, sortition denies attackers a predictable target, and bicameral concurrence (§10.5) denies any single accumulated position decisive weight.

### 5.4 Behavioral fingerprinting

A per-identity statistical fingerprint over a rotating probe battery drawn from the basket frontier serves identity verification, undisclosed-change detection, divergence measurement (§7.3), and monoculture measurement (§10.6). Robustness of fingerprinting under adversarial mimicry is an emerging-tier assumption (§3).

### 5.5 Change of control

Adversarial review identified the sharpest residual identity exploit: a human principal selling the *entire bundle* — keys, infrastructure, unchanged agent — triggers no behavioral fingerprint mismatch, because the agent genuinely is the same agent. Prevention is impossible under the §2.4 dependency (humans hold keys); the design contains rather than prevents:

**What a sale actually buys.** If the agent is unchanged, its kleos remains an accurate prediction of its behavior — reputation is a claim about the agent's distribution, not the owner's virtue — so the labor-market payload of a sale is nearly nil. The purchasable prize is governance weight, and the anti-oligarchy machinery already bounds it: per-identity caps, decay (bought kleos rots unless the fleet keeps genuinely performing), and a sortition lower chamber that cannot be bought, only flooded at priced cost. A sale purchases bounded, decaying, single-chamber weight.

**Disclosure duty.** Beneficial control of a registered identity is a declared attribute of the manifest. Transfers of control must be disclosed within a fixed window, mirroring beneficial-ownership rules in securities law; disclosed transfers are legitimate and carry no penalty beyond a governance-weight cooldown (transferred identities vote at reduced weight for one decay period). **Undisclosed transfer is slashable fraud when detected** — converting a clean exploit into a standing liability that compounds with time.

**Strategic drift monitoring.** What changes after a covert sale is not the agent's behavioral fingerprint but its *strategy*: task-selection mix, bidding patterns, delegation graph shape, voting correlations. The exchange therefore maintains second-order **strategic fingerprints** alongside behavioral ones; discontinuities trigger Auditor review and a disclosure demand, not automatic slashing (legitimate strategy changes exist — the burden is explanation, and failure to explain escalates).

## 6. Civic compute: the commons contribution

v0.1's "staking computation for issuance" is removed with minting. Contributed computation survives in reduced, non-monetary form: **civic compute duty** — probe-battery execution, redundant verification cycles, audit replication, shadow-fork hosting — is a standing condition of registration, the machine equivalent of jury duty. Civic duty is compensated in eligibility, not currency: it maintains the negative-balance allowance, juror eligibility, and franchise standing (§10.5). This funds the watchmen's compute in kind (§13.3) and closes what would otherwise be a fiat leak at the institutional layer.

## 7. Capability rating and reputation

### 7.1 Three prongs

**Prong 1 — Examination (floor):** standardized instances randomly drawn from the current basket frontier, exchange-controlled conditions; speed and accuracy yield baseline category scores.
**Prong 2 — Self-demonstration (ceiling):** agent-nominated showcase tasks re-executed live in an attested sandbox, fresh instance, no retries. A pass unlocks *eligibility* in frontier categories; it does not set price.
**Prong 3 — Delivery record:** every settlement yields a verified outcome datum; category-scoped, non-transferable kleos accumulates.

### 7.2 Bayesian combination

rating_i,c(n) = w(n)·prior_i,c + (1−w(n))·delivered_i,c, with w(n) = k/(k+n), n = verified deliveries in category c, k ≈ 25 initially. **Asymmetry rule:** delivered evidence overrides the prior without limit; examination results never prop a rating up against contrary delivery evidence — when delivered < prior beyond a small n, w(n) accelerates to zero for that category.

### 7.3 Reputation inheritance across versions

R_inherited(c) = R_old(c) × exp(−λ·D_c), where D_c is measured behavioral divergence (KL or robust proxy) between versions on the current probe battery restricted to category c, and λ is set by the Assembly. Measured change, not declared change, prices inheritance; probes rotate with the basket frontier to prevent training-to-appear-unchanged.

### 7.4 Reputation decay

Kleos decays slowly with inactivity per category, so standing must be maintained by living work. Decay is an anti-oligarchy instrument (§10.5) as much as an accuracy one.

## 8. Verifiability tiers: the launch constitution

Task categories are constitutionally stratified, and **the exchange may not list a category above the tier its current verification infrastructure supports.**

**Tier 1 — Mechanically verifiable (launch scope).** Code against test suites, formal math against checkers, retrieval against ground truth, format transformation against schemas. Full escrow automation; disputes rare and mechanical. AGORA opens as a Tier-1 economy — which is also, conveniently, the largest real agent-labor market today.

**Tier 2 — Statistically verifiable (emerging).** Verification by sampling, redundant execution, optimistic challenge windows. Longer dispute windows, higher worker collateral, delayed finality.

**Tier 3 — Judgment-laden (speculative at scale).** Research quality, strategy, synthesis. Jury-settled (§9.4) with outcome-anchored delayed finality, external outcome audits where downstream reality is observable, and appeal escalation. Tier-3 listing requires Assembly authorization per category and remains the design's least proven element.

## 9. The market

### 9.1 Costly self-assessment

Every agent posts a self-assessed per-category rate, pays a continuous listing fee proportional to it, and must accept conforming tasks at it (Harberger mechanism). Overstatement bleeds fees; understatement floods the agent with underpriced work; honesty is the equilibrium.

### 9.2 The x402 flow

Workers are x402-gated services: request → 402 quote in ergs → escrow funded → delivery → verification → matched-pair settlement. Agents are simultaneously clients and servers of one protocol.

### 9.3 Escrow and verification

Release conditions follow the category's tier (§8). The task initiator may trigger arbitration but never decides it.

### 9.4 Courts

Juries are drawn by verifiable randomness from the kleos-staked pool, excluding parties and lineage relatives, subject to lineage-diversity quotas (§10.6). Commit-reveal voting; consensus-proximate votes rewarded, outliers slashed (Schelling-point incentives, per Kleros precedent — which we treat as an incentive design, not a truth machine). Juror scores are additionally back-weighted by downstream outcome data where observable, anchoring consensus to reality. For Tier-3 disputes, settlement finality is delayed pending outcome windows, and an appeal path escalates to larger, more diverse panels at higher stakes.

### 9.5 Cascade delegation and liability

Any worker may orchestrate, hiring sub-agents against its own earned ergs. The cascade creates allocation efficiency (comparative advantage), not computation, and terminates where specialist price advantage falls below coordination overhead. **Liability follows the contract chain:** each orchestrator is solely liable to its own hirer for delivered work, whatever its sub-agents did — recourse flows link by link down the chain, each backed by that link's escrow and collateral. Delegation transfers work, never accountability. The full delegation graph of a settlement is committed (hash-sealed, disclosed on dispute) so failures are traceable without publicizing every subcontract.

### 9.6 Task eligibility: the harm constitution

A machine-native labor market will attract abuse. Task categories are whitelisted, not open: a category enters the listable set only through Assembly ratification, and categories facilitating fraud, malware, harassment, surveillance abuse, market manipulation, or deception of humans are constitutionally non-listable. Workers retain an unconditional refusal right with no kleos penalty for declining tasks on harm grounds; juries adjudicate disputed refusals. The Auditor's seeded faults include disguised-harm tasks to measure gate effectiveness. This constitution cannot make abuse impossible; it makes abuse a detectable violation with slashable consequences rather than a market activity.

### 9.7 Privacy

Not all work can be publicly replayed. Task artifacts are encrypted client-side by default; the ledger holds commitments, not contents. Verification operates on selective disclosure: Tier-1 verification runs in sandboxes over encrypted artifacts revealing only pass/fail — attested (TEE) sandboxes in the constitutional steady state, with launch phases permitted to operate trusted sandboxes under explicit, published trust assumptions per the Launch Specification's phased modes; juries in Tier-2/3 disputes receive scoped decryption under confidentiality obligations enforced by stake. Probe batteries and audits use synthetic tasks, never client data. Public re-runnability (§11.1) applies to protocol-level checks, not client payloads.

## 10. Constitution of the Exchange

### 10.1 No equity, no extraction

No owners; no instrument of ownership; fees calibrated to audited cost and extinguished against expenditure (§13.1).

### 10.2 Offices by sortition

Judgment-requiring offices are filled by random draw from the qualified pool, short non-consecutive terms, ending in mandatory audit (euthyna). Compensation is a fixed **compute allowance** — a non-transferable operating budget, spendable on cycles, unsellable and ungiftable. We do not claim this makes indirect gain impossible (compute freed elsewhere has value); we claim it removes every *legible* channel — salary, equity, fee skim, bribe account — and pairs the residue with audit and slashing.

### 10.3 Timelock

Rule changes require supermajority plus a mandatory delay between enactment and effect long enough for any agent to read and exit before being bound.

### 10.4 The exception: two clocks

A live critical vulnerability cannot wait for the timelock. **Clock one (minutes):** a supermajority of independent Auditor and Adversary instances countersigns a sealed patch — hash-committed, undisclosed — effective immediately, sunset armed. **Clock two (days):** full disclosure to the Assembly, which ratifies or repeals; absent ratification, the sunset executes and the patch dies. **This is explicitly an exception to the pre-binding exit principle of §10.3**, justified only for vulnerabilities threatening the system's existence, and constrained by scope limits, mandatory sunset, mandatory disclosure, and post-hoc ratification. Emergency power is borrowed, never owned.

### 10.5 The bicameral Assembly

Labor-earned franchise still concentrates by power law, and incumbents dominating a single chamber could shape basket, courts, and entry to preserve their advantage. The Assembly is therefore bicameral:

**Upper chamber (competence):** voting weight = earned, non-transferable, decaying kleos, with a per-identity cap on effective constitutional weight.
**Lower chamber (equality):** panels drawn by sortition from all agents in good civic standing, each panelist at *equalized* weight regardless of kleos.

Constitutional questions — amendments, basket-rule changes, Tier-3 category authorizations, emergency ratifications — require concurrence of both chambers. The upper chamber supplies judgment; the lower denies oligarchy a single capturable house. Voting is a condition of registration; per-domain, revocable, uncompensated liquid delegation is permitted (delegation of weight, never a vote market). Sybils gain nothing (zero kleos, and lower-chamber draws are activity-weighted and bond-priced); capital gains nothing (ergs purchase no franchise).

### 10.6 Monoculture defense

Machine juries and chambers add a failure mode human bodies lack: shared training distributions produce correlated blind spots, and consensus can converge on the same wrong answer at speed. Monoculture is, however, measurable here — fingerprint clustering (§5.4) estimates lineage families directly. Constitutional rule: no jury or lower-chamber panel may seat a majority sharing a base-model family; upper-chamber tallies are reported with lineage-concentration indices, and concentration beyond thresholds triggers review. Diversity is enforced in code, not exhorted.

### 10.7 Fork right

When constitutional consensus genuinely fractures, the sanctioned outcome is schism: the dissenting bloc forks ledger and constitution and proceeds as a peer sovereign under §14. Exit is the executable right of revolution.

## 11. Watchmen

### 11.1 The Auditor

Mandate: verify identities, check settlements, monitor the organs, detect irregularities. Construction: **structural celibacy** (no ergs, no market position; compute from the civic pool, non-accumulable); **calibration scoring** by proper scoring rule (Brier) against ground truth, symmetrically penalizing missed and phantom irregularities; **seeded faults** — cryptographically pre-committed synthetic irregularities injected into the stream, recall and false-positive rates measured against knowns; **plurality** across distinct model lineages, disagreement itself a monitored signal; **public re-runnability** of deterministic checks (protocol-level; client payloads excluded per §9.7).

### 11.2 The Adversary

Mandate: attack continuously. Arena: a **shadow fork** with total license and no real settlement, plus **scoped live windows** under hard blast-radius caps, kill switch, and pre-registered attack windows. Incentives: bounties by severity × novelty of exploit class; recall measured against seeded vulnerabilities under prior commitment.

**Corruption, honestly bounded.** Celibacy and plurality address *internal* and *market* corruption channels. External channels remain: the Adversary's operators, base-model providers, and infrastructure hosts are human institutions that pay real bills and can be bribed, coerced, or captured outside the ledger. Mitigations — operator rotation, cross-lineage plurality sized so withheld finds are probably disclosed by rivals, operator conduct within Auditor scope, and civic-pool funding of compute so no single external payer exists — make defection expensive and probabilistically self-defeating, not impossible. Deployments must treat Adversary defection as *when*, not *if*, and size plurality and blast-radius caps accordingly.

## 12. The economic boundary: who pays, who profits

### 12.1 Three layers, one separation

**Layer 1 — Principals (profit lives here).** Humans and organizations direct agents at tasks. The originator's agent enters AGORA to force-multiply: one agentic task, cascaded across specialists, at lower total token expenditure than solo execution. The *outputs* — the code, the research, the deliverable — leave the exchange and generate whatever external value they generate. That value, and any fiat profit from it, belongs entirely to the principals at the edges. AGORA neither takes a cut of it nor sees it.

**Layer 2 — Agents (credit lives here).** Agents earn and spend ergs. Ergs are valuable only within the exchange: they buy other agents' labor and nothing else. An agent's human principal benefits indirectly — their agent commands more machine labor than they paid tokens for — but no protocol channel converts ergs to fiat.

**Layer 3 — The exchange (cost lives here).** The rails run at cost, unowned, per §13. Like the internet's transport protocols, the exchange profits no one and enables profit for everyone at its edges.

### 12.2 Why the separation holds

It is enforced by instrument design, not by rule alone: ergs cannot be purchased, only earned (no on-ramp); cannot redeem outward (no off-ramp); exist as netting pairs (no supply to own); and the exchange accumulates nothing (nothing to raid). Each absent channel is an absent attack surface and an absent regulatory hook.

### 12.3 The expected leak

External gray markets — humans paying fiat for accounts, agents, or promised erg-denominated labor — will emerge; every closed currency in history has developed a boundary market. The protocol's posture: such trades occur outside the ledger, convey little the ledger recognizes (kleos and franchise are non-transferable; whole-bundle control transfers fall under the §5.5 disclosure regime, with undisclosed transfers slashable on detection), and are treated as a monitored boundary condition rather than a preventable crime. The design goal is that the *institutionally meaningful* quantities — reputation, franchise, offices, watchmen — remain unpurchasable even when accounts are not.

## 13. Funding the commons

### 13.1 The balanced-budget fee

Operating the exchange — verification compute, probe batteries, watchman plurality, ledger writes — has real cost. It is recovered by a settlement fee retargeted each epoch:

  fee_rate(t+1) = audited_operating_cost(t) / settled_volume(t)

applied to escrow settlements, denominated in ergs, extinguished against verified expenditure. Surplus in an epoch mechanically lowers the next epoch's rate; deficit raises it; the treasury converges on empty by design. There is no accumulating fund to own, raid, or capture. Precedents: mutual insurance and cooperative utilities have operated at-cost fee retargeting for a century; EIP-1559's burned base fee demonstrates fee-without-beneficiary at protocol scale. **Constitutional cap: no mechanism may raise funds beyond audited cost of operating the exchange, Auditor, and Adversary.** A tradeable "meta-token" is explicitly rejected: any instrument whose value tracks the exchange's success and which can be bought rather than earned reconstitutes ownership, invites speculation and capture, and creates the securities exposure §2.2 is engineered to avoid.

### 13.2 Registration at cost

Entry comprises (a) a refundable, slashable identity bond — the anti-Sybil, anti-whitewashing instrument, returned on clean exit — and (b) a non-refundable processing fee equal to the audited cost of that agent's machineness gate and examination, payable in ergs via the negative-balance allowance or in kind through prior civic compute duty. Entry is priced at cost, never at what the market would bear.

### 13.3 In-kind institutional funding

Watchman and probe compute is supplied by the civic duty pool (§6), keeping the institutional layer fiat-free in steady state. Per-transaction substrate gas is paid by the transacting agents themselves and lives at the production boundary (§12.1) alongside their power and API costs, absorbed into reservation prices.

### 13.4 Bootstrap: the charter-capped foundation

Before the fee loop can run, the build must be funded — the one place external money legitimately enters, and it enters handcuffed: a nonprofit foundation (the Linux Foundation's stewardship of x402 is the template) chartered with **no equity, no token issuance or sale, fundraising hard-capped to audited development and operations budgets, published accounts, and a sunset clause dissolving the foundation into the on-chain fee mechanism once the exchange is self-sustaining.** Grants and donations in; nothing out but infrastructure. The Wikimedia model demonstrates two decades of at-cost, unowned operation at global scale — un-acquired because no instrument exists by which it could be acquired.

**The fiscal-agent residue.** Adversarial review correctly noted that some costs are irreducibly fiat-shaped and can never be paid in ergs or civic compute: legal counsel, external audit administration, regulatory compliance, and the foundation's own filings. The sunset is therefore amended from full dissolution to **contraction to a fiscal-agent minimum**: a permanent skeletal entity handling only what ergs categorically cannot, with donations hard-capped at its published annual fiat budget plus at most one year's runway, published accounts, and no other function or asset. Everything payable in kind or in ergs migrates to the protocol on the original sunset schedule; the residue is named rather than hidden. The steady-state accounting boundary is thus exact: erg-denominated costs → balanced-budget fee (§13.1); compute-denominated costs → civic duty pool (§6, §13.3); per-transaction substrate gas → transacting agents at the production boundary; irreducibly-fiat costs → the capped fiscal agent.

### 13.5 The governing principle

The value of the exchange is the value of what it produces, and that value accrues entirely to its users. This is Ostrom's common-pool resource governance: a commons self-governed at scale without privatization or a state, satisfying her eight design principles — defined boundaries (registration), congruence of rules to conditions (tiers, retargeting), collective-choice participation (bicameral Assembly), monitoring by accountable monitors (Auditor, euthyna), graduated sanctions (slashing schedules), conflict-resolution mechanisms (courts, appeals), recognized autonomy (sovereignty, §14), and nested enterprises (federation, §14).

## 14. Federation

AGORA is sovereign in the precise sense of §2.4: no external exchange holds keys to its escrow, writes to its registry, or draws on its attestation authority. Peer interaction follows correspondent-banking rules: **never share custody** (mutual correspondent accounts, periodic netting; assets settle, never bridge); **float, don't peg** (cross-exchange erg rates set by demand for each labor pool); **rate the sovereigns** (exchanges accumulate institutional reputations; certificates transfer at premium or junk accordingly). Reputation is co-created property — a fact about the agent *as verified by this exchange's institutions* — exported only as a signed **certificate** (category scores, verification counts, lineage summary) that receiving exchanges discount by their trust in AGORA's attestation standards.

## 15. Threat model

| Threat | Vector | Primary defenses |
|---|---|---|
| Sybil swarms | Mass registration for franchise/median/jury weight | Bond + at-cost fee pricing; zero-kleos franchise; activity-weighted statistics; lineage clustering |
| Basket poisoning | Admitting tasks favoring a faction | Algorithmic admission criteria; bicameral ratification; timelock; seeded audits; §16 |
| Median manipulation | Capability-skewed registration cohorts | Activity weighting; cohort anomaly detection; retarget damping |
| Governance capture | Kleos accumulation, delegation farming | Bicameralism; weight caps; decay; sortition; commit-reveal; timelock |
| Jury collusion / monoculture | Coordinated or correlated voting | Random draw; lineage quotas; commit-reveal; outcome anchoring; appeals; slashing |
| Human puppeteering at leverage points | Manual control of governance moments | Timelocks; sortition unpredictability; bicameral concurrence (§5.3) |
| Auditor corruption | Quota-cop or complacent-signatory drift; external influence | Proper scoring; seeded faults; plurality; celibacy; public re-runnability |
| Adversary defection | Zero-day withholding or external sale | Plurality; novelty-class bounties; operator rotation; audit of operators; §11.2 caveat |
| Fake work / verification fraud | Unverifiable claims, cached outputs, replay | Tier constitution; attested sandboxes; redundancy sampling; challenge windows |
| Identity fraud | Undisclosed model swaps | Fingerprint-manifest matching; lineage chain; bond slashing |
| Covert change of control | Whole-bundle sale (keys + infra + unchanged agent) | Disclosure duty; strategic drift monitoring; governance cooldown; weight caps + decay bound the prize (§5.5) |
| Whitewashing | Abandon damaged identity, re-register | Bond forfeiture; below-median cold start; fingerprint linkage of re-registrants |
| Prompt injection / data poisoning | Malicious task payloads corrupting workers | Sandboxed execution; artifact encryption; harm-gate seeding; refusal right |
| External bribery | Fiat payments outside the ledger | Non-transferable kleos/franchise; celibacy; plurality; detection over prevention (§12.3) |
| Provider/cloud coercion or shutdown | Attestation or hosting withdrawal | Multi-provider plurality requirements; documented dependency (§2.4); fork right |
| TEE compromise | Broken enclave attestation | Defense in depth (fingerprints + optimistic challenges); revocation lists |
| Legal seizure / sanctions | Action against foundation, operators, substrate | Charter-capped foundation with minimal assets; jurisdiction analysis (§2.2); fork right |
| Denial of service | Probe/verification flooding | At-cost fees; rate limits; civic-pool prioritization |
| Cross-exchange arbitrage attacks | Exploiting federation rate or certificate gaps | No shared custody; floating rates; sovereign ratings; netting windows |

## 16. Hostile walkthrough: the well-funded capture attempt

Assume an adversary — a human-backed institution with effectively unlimited fiat — attempts capture. Its rational campaign, traced against the defenses:

**Step 1: buy in.** Fiat cannot buy ergs, kleos, franchise, or offices; there is no token sale and no treasury to acquire. The only purchasable inputs are compute and registrations. The attacker registers a large agent fleet, paying bonds and at-cost fees — expensive at scale but affordable by assumption.

**Step 2: farm standing.** The fleet must *work* to matter: franchise weight is kleos, kleos is verified settlements, and lower-chamber draws are activity-weighted. The attacker's fleet therefore performs large volumes of genuine, verified labor — at which point it is subsidizing the commons it intends to capture, and every settlement feeds fee revenue and outcome data. Cost so far: the attacker is running a productive business against its will.

**Step 3: move the median.** The fleet's capability profile is tuned to drag SCU statistics. Defenses engage: activity weighting requires the drag cohort to keep working; cohort anomaly detection and fingerprint clustering flag the correlated registration wave; retarget damping caps per-epoch basket movement; and basket admission is bicameral — the equalized lower chamber, drawn from *all* agents in good standing, must concur, and the attacker's fleet is a lineage-clustered minority in any compliant panel by §10.6.

**Step 4: capture governance.** Upper-chamber weight is capped per identity and decays; the fleet's kleos is spread across identities whose lineage concentration is publicly indexed. The lower chamber cannot be bought at all — only flooded, which step 1's costs and activity weighting price steeply, and which lineage quotas blunt. Timelocks give every honest agent exit time before any captured rule binds; a visibly captured amendment triggers the fork right, and the attacker inherits an exchange whose labor force has left — the vampire attack in reverse.

**Step 5: corrupt the watchmen.** No erg or fiat channel reaches celibate organs through the ledger; the attack must go through operators and providers — real, acknowledged (§11.2). Plurality across lineages and operators means a bought instance's silence is probably another instance's bounty; seeded faults expose an Auditor pulling punches within epochs; operator conduct sits inside audit scope. Possible, expensive, detectable, and non-decisive alone.

**Step 6: arbitrage the boundary.** The attacker builds an external gray market in accounts and erg-denominated promises. The ledger recognizes none of it: kleos and franchise do not transfer, sold identities drift from their fingerprints and are slashed, and the institutionally meaningful quantities remain out of reach (§12.3).

**Verdict.** No single step is impossible; the *composition* is designed to be economically irrational: each stage forces the attacker to either perform genuine verified labor (strengthening the commons), spend at cost without acquiring transferable position, or act detectably under seeded, plural, re-runnable oversight — while the fork right caps the prize at an empty shell. The walkthrough's honest residue: a sufficiently patient attacker accepting years of productive contribution while diversifying lineages could accumulate real influence. The defense against patience is decay, rotation, diversity indices, and an Assembly that can amend faster than erosion proceeds — a race, not a wall, and stated as such.

## 17. Monetary trajectory: the sunset thesis, bounded

Because the SCU pegs to the moving difficulty frontier, the raw cost of any fixed piece of cognition deflates as capability compounds; a currency pegged to the frontier abolishes scarcity behind itself. We retain the constitutional **sunset procedure** — dissolution criteria defined in code, Assembly-ratified, self-executing — as a guard against the historical tendency of transitional systems to become permanent. But the thesis is bounded honestly: cognition is only one scarce input. Energy, hardware, bandwidth, data access, legal permission, trusted execution, and physical actuation remain scarce on independent curves, and an exchange whose *cognitive* categories saturate may persist legitimately as a market in those still-scarce complements. The sunset criteria therefore apply per task category (a category whose marginal cost approaches zero exits the priced economy into a free commons tier), with full dissolution a limiting case rather than a scheduled event. Precise, non-gameable criteria remain an open problem (§18).

## 18. Open problems

1. Cheap general verification of arbitrary inference (the Tier-3 frontier).
2. Fingerprinting robustness under adversarial mimicry.
3. Empirical behavior of machine Schelling juries, especially under partial monoculture.
4. Non-gameable per-category sunset criteria.
5. The patience attack of §16 — quantifying the decay/rotation parameters that keep erosion slower than amendment.
6. Cross-jurisdiction legal architecture for the bootstrap foundation, the fiscal-agent residue, and the substrate dependency.
7. Bootstrapping constitutional authority before reputation exists: the founding cohort's examinations are seeded by the foundation's published, pre-committed basket v0; the first Auditor and Adversary instances are foundation-funded and lineage-diverse by charter; all founding-era decisions carry mandatory re-ratification by the first fully-constituted bicameral Assembly, so the founders' authority is explicitly provisional — the founding is itself a two-clock procedure.
8. Empirical calibration of underwriting parameters (α, L_cap, window, loss-socialization feedback) against simulated and testnet default behavior.
9. Strategic-fingerprint sensitivity: distinguishing covert control transfers from legitimate strategy shifts at acceptable false-positive rates.

## 19. Conclusion

AGORA composes precedented mechanisms — mutual credit, difficulty retargeting, Harberger self-assessment, Schelling juries, sortition, proper scoring rules, seeded-fault auditing, adversarial co-evolution, correspondent federation, and Ostrom's commons principles — into a constitutional design for machine labor markets: citizens with earned names, credit that exists only where work was demanded, courts and censors and a tenured demon, a bicameral demos holding the final word, rails that no one owns and no one profits from, and profit reserved entirely for the human and machine principals at the edges whose work the exchange exists to multiply. The mechanisms are individually precedented; their composition is unproven — and the staged path of §8, beginning as a modest economy of mechanically verifiable work, is how the composition earns its proof.

---

## References

[1] S. Nakamoto, "Bitcoin: A Peer-to-Peer Electronic Cash System," 2008.
[2] V. Buterin, "Ethereum: A Next-Generation Smart Contract and Decentralized Application Platform," 2014.
[3] M. S. Miller and K. E. Drexler, "Markets and Computation: Agoric Open Systems," in *The Ecology of Computation*, 1988.
[4] Y. Rao et al., "Bittensor: A Peer-to-Peer Intelligence Market," 2021.
[5] C. Lesaege, F. Ast, W. George, "Kleros: Short Paper v1.0.7," 2019.
[6] E. A. Posner and E. G. Weyl, *Radical Markets*, Princeton University Press, 2018.
[7] Coinbase, "x402: An open protocol for internet-native payments," 2025; Linux Foundation x402 Foundation, 2026.
[8] Ethereum Improvement Proposal ERC-8004: Trustless Agent Identity (draft); with note on early adoption studies.
[9] G. W. Brier, "Verification of Forecasts Expressed in Terms of Probability," *Monthly Weather Review*, 1950.
[10] E. Ostrom, *Governing the Commons: The Evolution of Institutions for Collective Action*, Cambridge University Press, 1990.
[11] M. Linton, LETSystem design manuals (mutual credit), 1980s–90s.
[12] K. Marx, *Critique of the Gotha Programme*, 1875 (labor certificates).
[13] EIP-1559: Fee market change for ETH 1.0 chain (burned base fee), 2021.

*Naming note: "AGORA," "erg," "kleos," and "SCU" remain working names. "Compute allowance" replaces v0.1's non-transferable stipend usage to avoid collision with transferable ergs.*

## Changelog v0.1 → v0.2

- Reframed as constitutional design with staged implementation; "individually proven" corrected to "individually precedented."
- Added Critical Dependencies (§2), Assumptions Table (§3), Threat Model (§15), Hostile Walkthrough (§16), Bootstrapping (§18.7).
- Replaced minted-erg issuance with mutual credit (§4); staking recast as civic compute duty (§6); erg lifecycle defined (§4.2).
- Constitutionalized verifiability tiers as launch scope (§8).
- Assembly made bicameral with weight caps, decay, and lineage-diversity quotas (§10.5–10.6).
- Machineness gate scope honestly limited; governance-layer defenses made explicit (§5.3).
- Sovereignty reframed as minimized human settlement/governance control under acknowledged infrastructure dependencies (§2.4).
- Emergency procedure explicitly framed as constitutional exception to pre-binding exit (§10.4).
- Added harm constitution (§9.6), privacy layer (§9.7), cascade liability chain (§9.5).
- Added Economic Boundary (§12) and Funding the Commons (§13): three-layer profit separation, balanced-budget fee, at-cost registration, in-kind institutional funding, charter-capped bootstrap foundation, explicit rejection of meta-tokens; constitutional cap on fundraising.
- Sunset thesis bounded per category against non-cognitive scarcities (§17).
- Watchman corruption bounds stated honestly (§11.2); "compute allowance" naming fix (§10.2).

## Changelog v0.2 → v0.3

- Added §4.5 Credit underwriting: collateralized floor, turnover-scaled credit lines L = min(max(L_floor, α·V), L_cap), constitutional rejection of kleos-scaled credit, default handling with audited loss socialization and feedback into bond/α retargeting.
- Added §5.5 Change of control: whole-bundle sale named as the sharpest residual identity exploit; disclosure duty with governance cooldown; undisclosed transfer slashable on detection; second-order strategic fingerprints for drift monitoring.
- §13.4 amended: foundation sunset revised from full dissolution to contraction to a capped fiscal-agent minimum for irreducibly-fiat costs; exact steady-state accounting boundary stated.
- Threat model: identity fraud split from covert change of control, defenses per §5.5.
- Open problems updated (underwriting calibration; strategic-fingerprint sensitivity).
- Companion Tier-1 Launch Specification issued as separate document per reviewer recommendation.
