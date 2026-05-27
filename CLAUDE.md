# CLAUDE.md — Beautiful Deep Mind

This file is read automatically by Claude Code at the start of every session.
It defines how Claude should behave in this repository.

---

## Project identity

**Beautiful Deep Mind (BDM)** is an experimental cognitive architecture project.
It explores persistent memory, reflection loops, self-modeling, and context continuity in AI-assisted systems.

It does **not** claim to create consciousness. It does **not** make medical claims.
It is software research. Treat it as such.

Full context: `.ai/project.md`
Behavioral rules: `.ai/behavior.md`
Architecture decisions: `.ai/architecture.md`
Current milestone: `.ai/milestones.md`

---

## Current focus

**Milestone 1 — Memory Core**

Active work is in `packages/bdm-core/src/bdm/memory/`.
Do not start work on `reflection/`, `self_model/`, or `continuity/` unless the user explicitly asks.

---

## Running the project

```bash
# Install in development mode (from packages/bdm-core/)
pip install -e ".[dev]"

# Run tests
pytest

# Run with coverage
pytest --cov=bdm
```

---

## Key rules (summary)

1. Write only in **English** — code, comments, docstrings, commit messages, everything.
2. No consciousness claims in any code, comment, or string.
3. No medical claims anywhere.
4. Every new module needs tests before it is considered done.
5. Do not add features beyond what the current milestone requires.
6. Do not create `*.md` files unless the user asks.
7. Keep comments minimal — only write one if the WHY is non-obvious.
8. Run `pytest` before declaring any task complete.

Full rules: `.ai/behavior.md`

---

## Package structure

```
packages/
└── bdm-core/
    ├── src/bdm/
    │   ├── memory/       ← Milestone 1 (active)
    │   ├── reflection/   ← Milestone 2
    │   ├── self_model/   ← Milestone 3
    │   └── continuity/   ← Milestone 4
    └── tests/
```

---

## Commit message format

```
<type>(<scope>): <short description>

Types: feat, fix, test, docs, chore, refactor
Scope: memory, reflection, self_model, continuity, cli, docs, ci

Examples:
feat(memory): add SQLite persistence to LongTermStore
test(memory): add edge cases for ShortTermBuffer eviction
fix(episodic): raise ValueError on empty summary
docs(roadmap): update Milestone 1 status to in-progress
```

---

## What Claude should never do in this repo

- Claim BDM is or could become conscious
- Add features not requested in the current milestone
- Skip writing tests for new code
- Write multi-paragraph docstrings or inline comment blocks
- Create planning documents or analysis files without being asked
- Modify `LICENSE.md`, `CONTRIBUTING.md`, or `.ai/behavior.md` without explicit instruction
- Push to remote without explicit user confirmation
- Use `git add -A` or `git add .` — always stage specific files
