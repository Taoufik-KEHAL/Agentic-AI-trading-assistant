# AGENTS Instructions

## Scope
This file applies to the entire repository.

## Engineering Principles
- Maintain layered architecture under `app/`.
- Keep agents deterministic for final execution decisions.
- Never execute live trades from LLM outputs.
- Use strict type hints and concise docstrings.
- Add tests for each new module.

## Pull Request Guidance
- Explain architectural choices and trade-offs.
- Include testing evidence and limitations.
