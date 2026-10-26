# Quality gate adoption — 2026-10-26

This adopts reviewed practices from official upstream GitHub projects, without importing source code or requiring new paid hosted services.

- https://github.com/rhysd/actionlint: GitHub Actions workflow static validation, pinned `v1.7.12` Go release.
- https://github.com/astral-sh/ruff: already in `tests.yml`, no duplicate linter CI added.
- https://github.com/microsoft/playwright: existing browser smoke in `tests/browser_smoke.py` and `browser.yml`, which tests responsive 375px layouts and core journeys.
- https://github.com/google/osv-scanner: evaluated as a future supply-chain audit; dependency vulnerability analysis is **not** a substitute for code review.
- https://github.com/EtemSakin/CodexMasterpiece: shared security and integration verification skills, adopted through project-local instructions rather than copying external agents.

## Completion criteria

A change affecting vote anonymity or aggregation cannot be considered complete unless the relevant Django tests cover privacy threshold, duplicate prevention and local-day boundary. Each PR should attach CI links to the exact SHA, browser screenshots from synthetic data and any known limitations.

`CLAUDE.md` remains authoritative, and `staging` remains the integration branch.
