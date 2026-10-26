# TeamPulse Codex bridge

The canonical product architecture, development constraints and privacy rules are in `CLAUDE.md`.
Codex should read `CLAUDE.md` and the feature's `specs/` files rather than replacing those existing instructions.

Quality-specific procedure: `.agents/skills/teampulse-quality-gate/SKILL.md`.
Shared Codex tools/patterns: https://github.com/EtemSakin/CodexMasterpiece (adopt selectively, no blind third-party execution).

- Preserve Django + SQLite implementation and privacy threshold (five daily submissions).
- Use `feature/*` or `fix/*`, PRs against `staging`; do not merge automatically.
- No raw real-world personal data in screenshots, fixtures or CI logs.
- Run `python manage.py check`, `python manage.py makemigrations --check --dry-run`,
  `python manage.py test`, `ruff check --select E4,E7,E9,F .`, and real browser smoke test when feasible.
- A passing Playwright desktop/mobile viewport test is not the same as physical mobile-device QA.
