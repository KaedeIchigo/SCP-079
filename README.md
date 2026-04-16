# SCP-079 (Terminal Remake)

## What this repository was
This repository originally shipped a 2012 Windows batch-file game (`SCP-079.bat`) by DJGHOSTS3V3N: a rough terminal SCP story prototype with memorable route beats and unfinished late-game logic.

The legacy script is preserved as-is in the repository root as historical canon material.

## What the remake is
This remake is a Python 3.11 terminal game that keeps the old route identity but expands it into a complete branching story:
- Player role: Class-D
- 4 major acts
- 12+ meaningful decisions
- 7 endings
- Lightweight state systems that alter branches and outcomes

The writing style intentionally keeps the raw early-terminal feel instead of polished prose.

## Preserved original route beats
The remake keeps and expands the original flow:
1. login/authentication
2. SCP-079 awakening
3. SCP-682 questioning
4. containment breach trigger
5. forced cooperation pressure
6. escape while carrying SCP-079 on a laptop
7. ATM withdrawal
8. battery drain crisis
9. pink-apartment safehouse route

The safehouse section is now a full Act IV branching hub with major end states.

## Run
```bash
python main.py
```

### In-game commands
- `:save <file>` to save
- `:load <file>` to load

## Validate story graph
```bash
python -m scp079.validator
```
Checks:
- missing node references
- duplicate node ids
- invalid conditions
- unreachable endings

## Test
```bash
python -m pytest -q
```
Includes:
- engine flow
- save/load roundtrip
- validator integrity checks
- route sanity tests for preserved legacy beats and required endings

## Project layout
- `SCP-079.bat` — original legacy game (untouched)
- `main.py` — entry point
- `scp079/engine.py` — terminal engine, choices, state, save/load
- `scp079/story.py` — data-driven narrative nodes and route map
- `scp079/validator.py` — story validation
- `tests/` — automated tests
- `AGENTS.md` — contributor/agent workflow guidance
