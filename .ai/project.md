# Project Overview

## Name

Beautiful Deep Mind (BDM)

## One-line description

An experimental cognitive architecture that explores how persistent memory, reflection, self-modeling, and context continuity can improve long-term coherence in AI-assisted systems.

## Primary goal

> BDM is an experimental cognitive architecture for AI systems that investigates how memory, reflection, learning from experience, and context continuity may influence more consistent system behavior over time.

BDM does not claim to create consciousness.
BDM does not make medical claims.
BDM does not claim to copy, upload, or preserve a human mind.
It is software research. Every claim is a hypothesis until tested.

## What BDM is building

A layered system where:

1. **Memory** — the system stores structured records of events, facts, and interactions
2. **Attention** — the system retrieves relevant memory in response to current input
3. **Reflection** — the system checks new outputs against prior ones for consistency
4. **Learning loop** — the system updates stored beliefs based on feedback and corrections
5. **Self-model** — the system maintains a structured record of its own knowledge state
6. **Continuity** — the system preserves context across sessions
7. **LLM Integration** — these layers augment an LLM as a substrate

## What BDM is not building

- A general-purpose AI assistant (not the goal)
- A brain simulation (not attempted)
- A consciousness engine (explicitly disclaimed)
- A medical tool (explicitly disclaimed)
- A commercial product (not yet, possibly never)

## Repository owner

Boring Code — hello@boringcode.pl

## License

Source-available, all rights reserved. See `LICENSE.md`.

## Development language

Python 3.11+

## Package layout

```
packages/
├── bdm-core/     — core cognitive architecture layers
└── bdm-cli/      — command-line interface (Milestone 6)
```

## Current development phase

**Milestone 1 — Memory Core** (in progress)

See `.ai/milestones.md` for full breakdown.
