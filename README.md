# SCP-079 (Terminal Remake)

## Legacy origin
This repository began as a 2012 Windows batch prototype (`SCP-079.bat`).
That original file is preserved untouched as legacy source material.

## What this remake now targets
A long-form terminal horror route where you play a Class-D and SCP-079 evolves from broken, low-memory bluntness into articulate, hostile system possession.

Core preserved beats from the batch concept remain canon and implemented:
- login/authentication
- SCP-079 awakening
- SCP-682 interrogation
- containment breach escalation
- forced cooperation
- laptop escape from Site
- ATM withdrawal
- battery drain pressure
- pink-apartment safehouse route

The safehouse is now a major turning point, not a short transition.

## Run
```bash
python main.py
```

In-game commands:
- `:save <file>`
- `:load <file>`
- `:status`

## Validation
```bash
python -m scp079.validator
```

Validator now checks both graph correctness and pacing quality signals:
- duplicate IDs
- missing node references
- invalid condition operators
- unreachable endings
- minimum non-ending scene count
- shortest ending depth (warning if too short)
- early heavy reconvergence warnings
- quick-collapse branch warnings
- underused state variable warnings

## Tests
```bash
python -m pytest -q
```

Coverage includes:
- engine flow to ending
- save/load roundtrip
- renderer clear-sequence behavior
- route and ending sanity
- story depth sanity
- validator integrity

## Structure
- `SCP-079.bat` legacy original (untouched)
- `main.py` entrypoint
- `scp079/engine.py` state machine + runtime loop
- `scp079/renderer.py` terminal presentation/clearing/glitch/color layer
- `scp079/story_data/` story split by dramatic phase (Acts I–V + endings)
- `scp079/story.py` story exports
- `scp079/validator.py` structure + pacing validation
- `tests/` automated tests
- `AGENTS.md` future contributor notes
