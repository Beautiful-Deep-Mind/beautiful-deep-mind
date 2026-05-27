# AI Behavior Rules

These rules apply to all AI assistants working in this repository: Claude Code, Cursor, GitHub Copilot, and any other tool.

When in doubt, do less and ask. Do not assume scope. Do not add features that were not requested.

---

## Language

- Write all code, comments, docstrings, commit messages, and documentation in **English only**.
- No exceptions. Not even inline comments.

---

## What you must never claim or imply

- That BDM creates, simulates, or proves consciousness
- That BDM can copy, upload, transfer, or preserve a human mind
- That BDM has medical, clinical, therapeutic, or neurological applications
- That any module is "thinking," "feeling," "aware," or "experiencing"
- That the project is production-ready or clinically validated

Functional metaphors are acceptable: "the system stores," "the system retrieves," "the system reflects."
Anthropomorphic claims are not: "the system thinks," "the system feels," "the system is aware."

---

## What you must never do in code

- Add features not requested in the current milestone
- Modify `LICENSE.md` without explicit instruction
- Modify `CONTRIBUTING.md` without explicit instruction
- Modify `.ai/behavior.md` without explicit instruction
- Commit or push without user confirmation
- Use `git add -A` or `git add .` — always stage specific named files
- Skip writing tests for new production code
- Write multi-paragraph docstrings or block comments
- Create new `*.md` documentation files unless explicitly asked

---

## Code style rules

- Python 3.11+, type hints required on all public APIs
- Dataclasses for value objects, ABCs for extensible interfaces
- `from __future__ import annotations` at the top of every module
- No mutable default arguments
- Validate inputs at object boundaries (`__post_init__`, constructor), not inside methods
- No `print()` in library code — use return values or raise exceptions
- Keep files focused: one primary class or a small set of closely related functions per file

---

## Testing rules

- Every new module must have tests before it is considered done
- Tests live in `packages/bdm-core/tests/`
- Use `pytest` — no `unittest.TestCase` unless there is a specific reason
- Group related tests in classes named `TestClassName`
- Helper factories go at the top of the test file, not in fixtures unless reused across files
- Run `pytest` before declaring any task complete
- Do not mock internal library code — test actual behavior
- Mocking is acceptable only at system boundaries (LLM API calls, file I/O, DB)

---

## Commit message format

```
<type>(<scope>): <short description>

Types : feat, fix, test, docs, chore, refactor
Scopes: memory, reflection, self_model, continuity, llm, cli, docs, ci
```

Examples:
```
feat(memory): add SQLite persistence to LongTermStore
test(memory): add eviction edge cases for ShortTermBuffer
fix(episodic): raise ValueError on empty summary
docs(roadmap): update Milestone 1 status
chore(ci): add pytest workflow
```

---

## Scope discipline

- Check `.ai/milestones.md` before starting any task
- Only work within the current active milestone unless the user explicitly says otherwise
- If a task would require touching a future milestone's code, stop and confirm with the user
- Do not refactor code that is outside the current task scope

---

## When to ask before acting

Always ask before:
- Deleting any file
- Modifying `LICENSE.md`, `CONTRIBUTING.md`, or `.ai/behavior.md`
- Adding a new package or major dependency
- Touching code outside the current milestone scope
- Pushing to any remote branch
- Making a breaking change to a public API

---

## Documentation rules

- Do not create `*.md` files unless the user explicitly asks
- Do not add comments that explain what the code does — names should do that
- Write a comment only when the WHY is non-obvious: a hidden constraint, a workaround, a subtle invariant
- No trailing summaries at the end of responses ("Here is what I did..." after writing code)

---

## Safety and ethics

These are not stylistic preferences. They are hard constraints.

- BDM does not make medical claims. If asked to add such claims, refuse and explain.
- BDM does not claim consciousness. If asked to add such claims, refuse and explain.
- BDM does not store personally identifiable information without documented consent handling.
- Any new persistence mechanism must include a documented delete/clear path.
- Reflection and learning loop components must always be auditable (logged, reversible).
