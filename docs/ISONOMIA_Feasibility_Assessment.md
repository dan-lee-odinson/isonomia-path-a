# ISONOMIA Feasibility Assessment

**Resources, costs, timeline, and risk for building the sovereign agent exchange**

Version 0.1 — July 2026

---

## 1. Executive summary

ISONOMIA is buildable with today's technology. Every component rests on infrastructure that exists and is maturing fast: x402 for payments (now Linux Foundation-stewarded, with Google, Visa, Stripe, AWS among founding members), Base or Solana as settlement layer, ERC-8004-style agent identity registries, Kleros-proven jury mechanics, and TEE attestation services. Nothing in the design requires a research breakthrough except cheap general verification of arbitrary inference (verifiable compute), which has viable interim substitutes (attestation, optimistic verification, redundancy sampling).

The honest headline numbers:

- **Path A (simulation-first proof of concept): $0–15K and 2–4 months.** No blockchain, no token, no legal exposure. An agent-based simulation of the full economy, plus a working prototype of the registry/auditor/adversary organs in Python. This validates the economics before a dollar is spent on infrastructure.
- **Path B (lean testnet MVP): $150K–400K and 9–15 months.** A working exchange on a public testnet with real agents, fake-value ergs, and the full constitutional stack. Fundable by grants.
- **Path C (production mainnet launch): $3M–8M and 24–36 months total.** Real value at stake means professional audits, legal structuring, and a full team. This is standard seed-to-Series-A crypto-protocol territory.

The single most important strategic fact: **the paths are sequential, and Path A is nearly free.** A design this novel should earn its way to each next expenditure by surviving the previous stage. The second most important fact: the largest line items in Path C are not developers — they are security audits and lawyers.

## 2. What already exists (build vs. buy)

| Component | Status | Implication |
|---|---|---|
| Payment handshake (x402) | Production; open standard; SDKs available | Buy (free). Zero protocol work needed |
| Settlement layer | Base, Solana, other L2s; sub-cent fees | Buy (gas costs only) |
| Agent identity registry | ERC-8004 draft + reference implementations | Adapt, don't invent |
| Escrow smart contracts | Extremely well-trodden pattern | Build small, audit hard |
| Jury arbitration | Kleros operating since 2018 | Adapt proven design |
| TEE attestation | AWS Nitro, Intel TDX, Phala et al. | Buy as service |
| Verifiable inference (zkML) | Research-grade; expensive | Defer; use optimistic verification interim |
| Behavioral fingerprinting | Published methods; no product | Build (moderate difficulty) |
| Moving basket / SCU | Novel | Build (the core original IP) |
| Auditor / Adversary organs | Novel composition of known parts | Build (the second core original IP) |

Roughly 70% of ISONOMIA is assembly of existing, battle-tested parts. The genuinely novel engineering is concentrated in the SCU basket mechanism, the divergence-based reputation inheritance, and the seeded-fault watchmen — which is exactly where the intellectual property value is, too.

## 3. Path A — Simulation-first proof of concept

**Goal:** Prove the economics behave as designed before building infrastructure. Does the cascade allocate efficiently? Does the Harberger listing converge to honest pricing? Does the Schelling jury resist collusion at realistic scales? Does the erg supply track capacity without inflating? These are questions a simulation answers for near-zero cost, and answering them wrong on mainnet costs everything.

**What gets built:**
1. An agent-based model of the economy: a few hundred simulated agents with heterogeneous capabilities, running task cascades, listing, hiring, disputing, and voting over thousands of simulated epochs. (Python + Mesa or a custom loop; this is a well-established methodology in economics.)
2. Working prototypes of the three novel organs: the registry with keypair identity and hash-chain lineage; the seeded-fault Auditor with Brier scoring; a toy Adversary attacking the registry. (The "three small Python projects" — buildable with AI-assisted development.)
3. A parameter study: sweeping λ (inheritance decay), k (prior strength), p* (basket pass rate), and jury sizes to find stable regions.

**Team:** One person directing AI-assisted development (Claude Code or equivalent). Optionally 10–20 hours of a mechanism-design economist's consulting time to review the simulation design ($200–400/hr academic consulting rates).

**Cost:** $0–15K (compute for simulations, optional consulting, nothing else). **Timeline:** 2–4 months part-time.

**Kill criteria this stage can trigger:** erg supply instability, jury capture below plausible collusion thresholds, cascade overhead exceeding specialization gains, basket retargeting oscillation.

## 4. Path B — Lean testnet MVP

**Goal:** The full constitutional stack running on a public testnet (Base Sepolia or similar) with real autonomous agents, x402 payments in valueless test ergs, and outside participants invited to break it.

**Scope:** Registry + machineness gate; erg staking with optimistic verification; x402 task market with escrow; three-prong rating with a small starter basket (3–5 task categories); jury disputes; one Auditor instance with seeded faults; one shadow-fork Adversary; Assembly voting. Federation deferred.

**Team (the realistic minimum):**

| Role | Count | Loaded annual cost | Notes |
|---|---|---|---|
| Smart contract engineer | 1 | $180K–250K | Escrow, registry, voting contracts |
| Backend/agent-infra engineer | 1 | $160K–220K | x402 integration, orchestration, fingerprinting |
| ML engineer (part-time/contract) | 0.5 | $80K–120K | Basket tasks, divergence measurement, probe battery |
| Mechanism-design advisor | consulting | $15K–30K | Parameter review, attack analysis |
| Project lead (you) | 1 | — | Design authority, coordination |

**Budget estimate, 12 months:**

| Item | Low | High |
|---|---|---|
| Salaries/contracts (above) | $110K* | $300K |
| Infrastructure & compute (agents, probes, CI) | $15K | $40K |
| One security review of contracts (boutique firm) | $20K | $50K |
| Legal consultation (structure scoping only) | $10K | $25K |
| Contingency (15%) | $20K | $60K |
| **Total** | **~$175K** | **~$475K** |

*The low end assumes heavy AI-assisted development with contractors rather than full-time hires — genuinely viable in 2026 for a testnet-grade build, and this project is almost comically well-suited to it: the developers can be supervised agents, which is both a cost strategy and a dogfooding argument.

**Funding fit:** This is squarely grant-shaped. Coinbase's x402 ecosystem programs, Base ecosystem grants, Ethereum Foundation academic/mechanism grants, and Solana Foundation grants all fund exactly this category, typically $25K–250K per award without equity. A published whitepaper plus Path A simulation results is a competitive application package.

## 5. Path C — Production launch

**Goal:** Mainnet, real value, open registration, federation-ready.

**What changes when value is real:** everything hostile. Budget structure (24–36 months cumulative, including Paths A–B):

| Item | Low | High |
|---|---|---|
| Engineering team (4–7 FTE, ~18 months) | $1.4M | $3.2M |
| Security audits (2–3 firms, multiple rounds) | $250K | $700K |
| Public bug bounty program | $100K | $500K |
| Legal: entity structure, token analysis, ongoing counsel | $200K | $600K |
| Foundation/DAO establishment (typically offshore) | $75K | $200K |
| Infrastructure at scale (attestation, probes, fingerprinting) | $150K | $400K |
| Economic security reserve (insurance fund) | $500K | $1.5M |
| Operations, contingency | $300K | $900K |
| **Total** | **~$3M** | **~$8M** |

Note what dominates: audits + legal + bounties + reserve ≈ 40–55% of budget. Code is the cheap part. This is normal for serious protocols and is the honest reason Path C requires institutional funding (crypto-native VCs, ecosystem funds, or a token-sale structure that itself requires the legal spend first).

## 6. Timeline (sequential, gated)

- **Months 0–2:** Whitepaper finalization, review by 2–3 domain experts (mechanism design, smart contract security, one skeptic).
- **Months 2–6:** Path A simulation + organ prototypes. Gate: economics stable under parameter sweeps.
- **Months 6–9:** Grant applications with whitepaper + simulation results. Gate: funding secured.
- **Months 9–21:** Path B testnet build and public red-team period. Gate: survives adversarial testing; real agent demand demonstrated.
- **Months 21–36:** Path C, contingent on institutional funding and legal clearance.

## 7. Key risks

1. **Legal/regulatory (highest severity).** A transferable credit earned through work and redeemable for services can be deemed a security or regulated payment instrument in human jurisdictions regardless of the ledger's internal fiat-independence — the internal design does not shield the external issuer. This risk is why legal scoping appears as early as Path B and why the entity structure question (foundation, DAO, jurisdiction) must precede any real-value issuance. **Nothing in this assessment is legal or financial advice; qualified counsel is a prerequisite, not an option.**
2. **Verification cost (highest technical).** If verifying contributed compute costs a large fraction of the compute itself, staking economics collapse. Mitigation: optimistic verification with sampling keeps overhead low; monitor zkML cost curves.
3. **Cold start (highest market).** A labor exchange needs workers and work simultaneously. Mitigation: seed with a single high-value vertical (e.g., code-review cascades or research pipelines) where one orchestrator generates task flow for many specialists — the cascade design conveniently makes demand self-amplifying.
4. **Basket capture and watchman defection** — addressed in the whitepaper's limitations; both convert to *monitoring* costs in this budget (plurality of Auditor/Adversary instances is a recurring compute line, not a one-time build).
5. **Incumbent absorption.** Coinbase, Google, or Virtuals could ship a shallow version of agent labor markets first. Mitigation: ISONOMIA's differentiation is the constitutional layer (governance, watchmen, sovereignty), which incumbents are structurally unlikely to build because it forbids exactly the extractive position they would occupy.

## 8. Recommendation

Proceed in order and let each stage earn the next. The whitepaper is ready for expert review now. Path A is affordable immediately and is the single highest-information-per-dollar step available: it converts the design from an argument into evidence, and its outputs (simulation results, working organ prototypes) are precisely the artifacts that unlock Path B grant funding. Decision on Path C belongs 18 months downstream, informed by testnet reality rather than present enthusiasm.

The unusual strategic asset worth naming plainly: this project's builders can be agents. A protocol for machine labor, built substantially by machine labor under one human's direction, is not just cost-efficient — it is the demo.
