---
name: teampulse-quality-gate
description: Verify TeamPulse daily-vote privacy, thresholded weekly trends, Django migrations, browser interaction and GitHub workflow security before PR review.
---

# TeamPulse Quality Gate

Read `CLAUDE.md`, changed code, `specs/` acceptance criteria and the relevant test plan.
Do not copy Django logic into CoParent's FastAPI codebase.

1. Check single-day duplicate constraints, including malicious cookie resets and stated limitations.
2. Ensure reports never reveal counts or averages for a group of fewer than five submissions; verify weighted aggregations and local date handling.
3. Run Django config, migrations dry-run, test suite and focused Ruff checks.
4. Run the Playwright browser-smoke workflow and check keyboard focus, accessibility, 375px layout and screenshots. Never claim Chromium equals a real Android/iOS device.
5. Audit CI workflow security and dependencies when they change; avoid secrets, broad permissions or copied executable GitHub skills.
6. Distinguish a green test against a synthetic database from guarantees about actual respondent anonymity or tamper resistance.
7. Document checks and exact commit SHA in the PR, keeping `staging` as the integration base; merging remains an owner action.

Related universal skills are maintained independently at https://github.com/EtemSakin/CodexMasterpiece under `codex-masterpiece/skills`.
