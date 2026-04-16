# AGENTS.md

Guidance for coding agents working on `KaedeIchigo/SCP-079`.

## Project identity
- `SCP-079.bat` is legacy source material from 2012 and must remain untouched.
- The Python remake is terminal-first and narrative-first.
- Keep tone raw, cold, direct, and hostile.

## Run
- Python version target: 3.11+
- Start game:
  - `python main.py`

## Validate and test
- Story validator:
  - `python -m scp079.validator`
- Test suite:
  - `python -m pytest -q`

## Architecture expectations
- Engine logic lives in `scp079/engine.py`.
- Story content lives in `scp079/story.py` and should stay data-driven.
- Validation logic lives in `scp079/validator.py`.
- Add tests under `tests/` for new branches and state behavior.

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
- Keep branching meaningful and ensure choices have downstream effects.
- When adding endings, ensure validator still reports no unreachable endings.
