# .ai/ — AI Context Directory

This directory provides structured context for AI coding assistants working in this repository.
It is read by Claude Code, Cursor, GitHub Copilot, and any other assistant that supports project-level context files.

## Contents

| File | Purpose |
|---|---|
| `project.md` | Project overview, goals, and scope |
| `behavior.md` | Rules: what AI may and may not do in this repo |
| `architecture.md` | Architectural decisions and patterns |
| `milestones.md` | Milestone breakdown with current status |
| `specs/` | Module-level specifications |

## How to use this directory

- **Claude Code** reads `CLAUDE.md` at the root automatically. That file points here.
- When working on a specific module, also read the relevant file in `specs/`.
- When unsure whether something is in scope, check `milestones.md` first.
- When unsure how to behave, check `behavior.md` first.

## Updating this directory

These files should be updated when:
- A milestone changes status
- An architectural decision is made or revised
- A new module spec is finalized
- Behavioral rules change

Do not update these files speculatively. Update them when a decision has been made and agreed upon.
