# agora-path-a

**Agent-based simulation of the AGORA Tier-1 launch economics** — Path A of the staged build
plan: validate the mutual-credit exchange design against its kill criteria *before* any
contract is written.

AGORA is a constitutional design for an autonomous-agent labor exchange: a mutual-credit unit
("ergs") that exists only when work is demanded and settled, Harberger-priced listings,
non-transferable reputation, and self-governing institutions. This repository simulates the
Tier-1 launch economy (one mechanically-verified code-task category) and asks the five
questions the launch spec exists to answer — supply stability, Harberger convergence, fee
convergence, attack survival, and parameter calibration.

## Spec of record

The four frozen baseline documents in [docs/](docs/) are the authority for every mechanism here:

| Document | Role |
|---|---|
| [Path A Simulation Plan v0.1](docs/AGORA_PathA_Simulation_Plan_v0.1.md) | Primary build spec: modules, agents, sweeps, attack scenarios |
| [Tier-1 Launch Spec v0.2.2](docs/AGORA_Tier1_Launch_Spec_v0.2.2.md) | Contract-level rules; parameter registry (§8); implementation clarifications (§13); its Conflict Register governs conflicts |
| [Whitepaper v0.3](docs/AGORA_Whitepaper_v0.3.md) | Constitutional design rationale |
| [Feasibility Assessment v0.1](docs/AGORA_Feasibility_Assessment_v0.1.md) | Scope discipline: this is Path A only |

Where the specs are ambiguous, [DECISIONS.md](DECISIONS.md) records the interpretation and the
section it interprets. [PLAN.md](PLAN.md) is the implementation plan; [BLOCKERS.md](BLOCKERS.md)
records anything unresolved.

## Quick start

```powershell
# one-time setup
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt

# run the test suite
.\.venv\Scripts\python.exe -m pytest

# run the honest baseline (26 epochs, deterministic under the config's seed)
.\.venv\Scripts\python.exe run.py configs\baseline.yaml

# run an attack scenario
.\.venv\Scripts\python.exe run.py scenarios\s1_wash_rush.yaml

# smoke parameter sweep (see CALIBRATION.md for the full sweep)
.\.venv\Scripts\python.exe sweep\run_sweep.py sweep\smoke.yaml
```

Outputs land in `results/<run_name>/` — per-epoch `epochs.csv`, event-level `events.jsonl`,
and `summary.md` / `summary.json` with the Sim Plan §6 metrics and the Launch Spec §10
kill-criteria verdict.

## Repository layout

```
docs/          the four baseline documents (spec of record)
src/agora/     simulation modules, one per launch-spec contract (see PLAN.md)
scenarios/     the 7 scripted attacks from Sim Plan §5
sweep/         Latin-hypercube parameter sweep runner
tests/         invariant + mechanism test suite
configs/       baseline.yaml = Launch Spec §8 center values
results/       run outputs (per-epoch logs gitignored; summaries committed)
```

## Status

Built as Path A of the Feasibility Assessment's staged plan (simulation-first, $0 infrastructure).
See `CALIBRATION.md` (milestone 6) for smoke-sweep results and how to launch the full sweep.

License: [Apache-2.0](LICENSE).
