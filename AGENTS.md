# AGENTS.md

Guidance for coding agents working on `KaedeIchigo/SCP-079`.

## Project identity
- `SCP-079.bat` is legacy 2012 source material and must remain untouched.
- The remake must stay terminal-based and narrative-first.
- Keep tone raw, cold, direct, hostile, and machine-haunted.

## Run
- Python target: 3.11+
- Start game:
  - `python main.py`

## Validate and test
- Story validation:
  - `python -m scp079.validator`
- Test suite:
  - `python -m pytest -q`

## Architecture expectations
- Engine/runtime: `scp079/engine.py`
- Renderer/presentation: `scp079/renderer.py`
- Story content split by phase: `scp079/story_data/`
- Story exports: `scp079/story.py`
- Validator: `scp079/validator.py`
- Tests: `tests/`

## Extension rules
- Preserve legacy route beats:
  - login/auth
  - awakening
  - SCP-682 question
  - breach trigger
  - forced cooperation
  - laptop escape
  - ATM withdrawal
  - battery drain
  - pink apartment safehouse
- Maintain delayed consequences; avoid fake branches collapsing immediately.
- SCP-079 voice should evolve with memory growth (`memory_tier`).
- If adding endings or branches, keep validator passing and update tests.
