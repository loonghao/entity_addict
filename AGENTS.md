# AGENTS.md — entity_addict

> Small pure-Python library: an extended `addict` that works as a decorator,
> converting a function's returned dict (or nested list of dicts) into
> attribute-accessible `Dict` objects. Consumed as the `entity_addict` PyPI
> package.
> Navigation map for AI agents, not a reference manual. Follow the links; do
> not read everything up front.

## Build & test

No justfile, no noxfile, and **no GitHub Actions workflows** — `.travis.yml` is
legacy and no longer runs. Use poetry (the `pyproject.toml` is
`[tool.poetry]`-based) or plain pytest.

```bash
poetry install
poetry run pytest entity_addict/test -v
poetry run pytest entity_addict/test --cov=entity_addict
poetry build                   # sdist + wheel via poetry-core
```

Equivalent without poetry:

```bash
python -m pip install addict pytest
python -m pytest entity_addict/test -v
```

Style gates run through pre-commit (`.pre-commit-config.yaml`): flake8,
autopep8, pyupgrade, reorder-python-imports, add-trailing-comma, mypy, and a
commitizen `commit-msg` hook that enforces Conventional Commits.

```bash
pre-commit install
pre-commit run --all-files
```

## Repo layout

| Path | Role |
|---|---|
| `entity_addict/entity.py` | The whole implementation: the `entity_addict` decorator |
| `entity_addict/__init__.py` | Public export (`from entity_addict.entity import entity_addict`) |
| `entity_addict/__version__.py` | `__version__` — release-please writes this file |
| `entity_addict/test/` | The test suite — `test_entity.py` (dict, list-of-dict, nested-list cases) |
| `pyproject.toml` | Poetry metadata, `[tool.poetry.version]`, and isort/black config |
| `.pre-commit-config.yaml` | Lint and commit-message gates |

Note: there is no top-level `tests/` directory. Tests live inside the package
at `entity_addict/test/`.

## Release

- release-please drives versioning from Conventional Commits on `main`
  (`release-please-config.json`, `release-type: python`).
  `.release-please-manifest.json` is the single source of version truth.
- `feat:` → minor, `fix:` → patch, `chore:`/`docs:`/`ci:` → **no release**.
- Use `chore:`/`docs:` for config and doc work so release-please does not cut a
  valueless version.
- release-please rewrites the version in **two** places via `extra-files`:
  `pyproject.toml` (`$.tool.poetry.version`) and
  `entity_addict/__version__.py`. Never hand-edit those versions.

## Do / Don't

- **Do** keep the dependency surface minimal — `addict` is the only runtime
  dependency, and Python 3.6+ compatibility is declared in the classifiers.
- **Do** add cases to `entity_addict/test/test_entity.py` for any new nesting
  or type-handling behaviour; that file is the entire regression suite.
- **Do** keep the decorator signature typed so mypy and the `wraps`-based type
  retention in `entity.py` keep working.
- **Don't** hand-edit `__version__.py` or the poetry version — release-please
  owns both.
- **Don't** hardcode an exact version in tests (`assert __version__ == "X.Y.Z"`)
  — release-please bumps will break it. Use `>=` or read package metadata.
- **Don't** add `CLAUDE.md` / `GEMINI.md` / `CURSOR.md` / `ANTHROPIC.md` /
  `OPENAI.md` / `COPILOT.md` / `CODEBUDDY.md` / `.cursorrules` / `.clinerules` /
  `.windsurfrules` at the root. This file is the only agent contract file.
- **Don't** commit build artifacts to the repo root (`dist/`, `build/`,
  `.coverage`, `*.egg-info/`).
