# AGENTS.md — entity_addict

> Navigation map, not a reference manual. Follow the links; don't read
> everything upfront.

entity_addict is an extended version of `addict` — a Python dictionary
whose values are both gettable and settable using attributes.

---

## Repository Contract

**This is a small Poetry-managed library with no CI workflow; run the tools
declared in `pyproject.toml`.**

| Task | Command |
|------|---------|
| Install (editable, with dev deps) | `poetry install` |
| Test | `poetry run pytest` |
| Test with coverage | `poetry run pytest --cov=entity_addict` |
| Format | `poetry run black . && poetry run isort .` |
| Lint | `poetry run flake8 entity_addict` |
| Type check | `poetry run mypy entity_addict` |

**Repository layout**

| Path | Role |
|------|------|
| `entity_addict/` | Package — `entity.py`, `__version__.py`, and the test suite |
| `pyproject.toml` | Poetry package metadata and dev dependencies |
| `poetry.lock` | Locked dependency set |
| `CHANGELOG.md` | Release history |

**Release flow** — `release-please` on `master` drives `CHANGELOG.md` and the version in
`pyproject.toml` from Conventional Commit subjects. Tagging and PyPI
publishing run in CI. Never edit `CHANGELOG.md` or a version string by hand.

**Prohibitions**

- Do not edit `CHANGELOG.md` or version strings manually.
- Do not add a second agent contract file at the repository root; `AGENTS.md` is the single source.
- Do not widen the runtime dependencies — the package only depends on `addict`.
- Do not break `addict` behaviour that downstream code relies on; this package is a superset.

---

## Agent Contract Files

`AGENTS.md` is the **only** agent contract file at the repository root. It is the
native instruction file for Codex, OpenCode, Cursor, GitHub Copilot, Windsurf,
Cline, Roo Code, Kiro, Trae, and Augment, and Claude Code falls back to it when
no `CLAUDE.md` exists — so do not add `CLAUDE.md`, `GEMINI.md`, `CURSOR.md`, or
any other vendor-specific variant.

**Gemini CLI exception:** Gemini CLI defaults its context file to `GEMINI.md`. To
make it read `AGENTS.md`, set `context.fileName` once in `~/.gemini/settings.json`:

```json
{
  "context": {
    "fileName": ["AGENTS.md", "GEMINI.md"]
  }
}
```
