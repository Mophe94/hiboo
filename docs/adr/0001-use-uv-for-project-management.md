# 0001. Use uv for Python and dependency management

- **Status:** Accepted
- **Date:** 2026-10-20

## Context

Hiboo depends on heavy libraries (PyTorch, sentence-transformers, FastAPI) and must be easy to install for anyone reviewing it: same Python version, same dependency versions, one command.

The traditional Python toolchain splits this job across several tools (pyenv, venv, pip, pip-tools or Poetry), each with its own commands and failure modes.

## Options considered

- **pip + venv + requirements.txt** — universal and simple, but no built-in lockfile for transitive dependencies, no Python version management, and slow installs.
- **Poetry** — mature with a lockfile, but slower and does not manage Python versions.
- **uv** — a single tool that manages Python versions, virtual environments, dependencies and a lockfile, based on the standard `pyproject.toml`; written in Rust and much faster than pip.

## Decision

Use **uv** for everything: `uv python pin` for the interpreter, `uv add` for dependencies, `uv.lock` committed to the repository, `uv run` to execute tools.

## Consequences

- Reproducible environments: `uv sync` recreates the exact environment from `uv.lock`.
- Faster local installs and faster CI.
- Standard `pyproject.toml`, so the project stays portable if the tooling ever changes.
- Contributors need to install uv first (a single command), which is documented in the README.
