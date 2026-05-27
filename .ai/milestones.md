# Milestones

This file tracks what each milestone contains, its current status, and its definition of done.
Update status when a milestone starts or completes.

---

## Status legend

| Symbol | Meaning |
|---|---|
| `planned` | Not started |
| `in-progress` | Active development |
| `complete` | All DoD items checked |
| `blocked` | Cannot proceed — reason noted |

---

## M0 — Project Foundation

**Status:** `complete`

**Goal:** Establish the conceptual, legal, and documentation foundation.

**Delivered:**
- `README.md`, `LICENSE.md`, `CONTRIBUTING.md`
- `docs/manifesto.md`, `docs/theory.md`, `docs/architecture.md`
- `docs/roadmap.md`, `docs/ethics.md`, `docs/glossary.md`
- `research/hypotheses.md`, `research/experiments.md`, `research/reading-list.md`
- `concepts/` — six concept files
- `.github/PULL_REQUEST_TEMPLATE.md`
- `packages/bdm-core/` — initial package skeleton

**Definition of Done:**
- [x] Repo has complete documentation structure
- [x] README clearly explains what BDM is and is not
- [x] LICENSE is source-available / all rights reserved
- [x] CONTRIBUTING describes contribution rules
- [x] Roadmap describes all milestones
- [x] No medical or consciousness promises anywhere

---

## M1 — Memory Core

**Status:** `in-progress`

**Goal:** Build the first persistent memory layer — the foundation all other layers depend on.

**Modules:**
- `M1.1` — `MemoryEvent` with type, tags, salience, confidence
- `M1.2` — `MemoryStore` abstract base class
- `M1.3` — `ShortTermBuffer` — bounded in-memory FIFO
- `M1.4` — `LongTermStore` — dict-backed now, SQLite next
- `M1.5` — `EpisodicRecord` — structured episode with session context
- `M1.6` — Memory search (by tag, by text, by type)
- `M1.7` — Importance and confidence scoring

**Files:**
```
packages/bdm-core/src/bdm/memory/
├── event.py        ← done
├── store.py        ← done
├── short_term.py   ← done
├── long_term.py    ← done (in-memory), SQLite pending
├── episodic.py     ← done
└── scoring.py      ← not started
```

**Definition of Done:**
- [x] Can create a `MemoryEvent`
- [x] Can add to `ShortTermBuffer` and `LongTermStore`
- [x] Can retrieve by ID
- [x] Can query by type and tags
- [ ] Can persist to SQLite
- [ ] Can search by text content
- [ ] `scoring.py` computes importance and confidence
- [x] Unit tests exist for event, store, short_term, long_term
- [ ] `examples/memory_demo.py` exists and runs

---

## M2 — Reflection Loop

**Status:** `planned`

**Goal:** Create a loop where the system retrieves memory, reflects on context, and prepares structured response context.

**Flow:**
```
input → retrieve memory → reflect → build context → output → store result
```

**Modules:**
- `M2.1` — Input Analyzer
- `M2.2` — Memory Retrieval (attention layer over memory)
- `M2.3` — Reflection Engine (real comparison logic)
- `M2.4` — Response Context Builder
- `M2.5` — Post-Interaction Memory Updater

**Files:**
```
packages/bdm-core/src/bdm/reflection/
├── analyzer.py      ← not started
├── retriever.py     ← not started
├── loop.py          ← stub exists
├── context_builder.py ← not started
└── updater.py       ← not started
```

**Definition of Done:**
- [ ] Reflection loop works without LLM (rule-based or mock)
- [ ] Retrieves minimum 3 relevant prior events
- [ ] Produces a `ReflectionResult` with verdict and context
- [ ] Updates memory after interaction
- [ ] Tests exist
- [ ] `examples/reflection_demo.py` exists and runs

**Depends on:** M1 complete

---

## M3 — Self-Model

**Status:** `planned`

**Goal:** Create a structured representation of the system's knowledge state, active goals, limitations, and current focus.

**Modules:**
- `M3.1` — Project State
- `M3.2` — Active Goals
- `M3.3` — Known Limitations
- `M3.4` — Current Focus
- `M3.5` — Identity Description

**Files:**
```
packages/bdm-core/src/bdm/self_model/
├── state.py      ← stub exists
├── goals.py      ← not started
├── limitations.py ← not started
└── identity.py   ← not started
```

**Definition of Done:**
- [ ] System has `SelfModelState` with topics and confidence
- [ ] Can add and update active goals
- [ ] Can record known limitations
- [ ] Can set and update current focus
- [ ] Self-model can be used inside Reflection Loop
- [ ] Tests exist

**Depends on:** M1 complete

---

## M4 — Context Continuity

**Status:** `planned`

**Goal:** Maintain coherent context across sessions through serialization, summaries, and context reconstruction.

**Modules:**
- `M4.1` — Session Model
- `M4.2` — Context Summary
- `M4.3` — Continuity Tracker
- `M4.4` — Session-to-Memory Bridge
- `M4.5` — Long-Term Context Reconstruction

**Files:**
```
packages/bdm-core/src/bdm/continuity/
├── context.py        ← stub exists
├── session.py        ← not started
├── summary.py        ← not started
├── tracker.py        ← not started
└── reconstruction.py ← not started
```

**Definition of Done:**
- [ ] Can start and end a named session
- [ ] Session generates a summary on close
- [ ] Summary is stored in long-term memory
- [ ] System can reconstruct last context from stored summaries
- [ ] Tests exist
- [ ] `examples/continuity_demo.py` exists and runs

**Depends on:** M1, M2, M3

---

## M5 — LLM Integration

**Status:** `planned`

**Goal:** Connect BDM Core to a language model through a provider interface with memory-aware prompt context.

**Modules:**
- `M5.1` — `LLMProvider` interface
- `M5.2` — Prompt Context Builder
- `M5.3` — Memory-Aware Chat
- `M5.4` — Reflection-Aware Chat
- `M5.5` — Safety Boundaries

**Files:**
```
packages/bdm-core/src/bdm/llm/
├── provider.py    ← not started
├── prompt.py      ← not started
├── chat.py        ← not started
└── safety.py      ← not started
```

**Definition of Done:**
- [ ] `LLMProvider` is an abstract interface
- [ ] A mock provider exists for tests
- [ ] Chat uses memory to build prompt context
- [ ] Chat runs reflection loop before responding
- [ ] Safety layer prevents consciousness and medical claims from being output
- [ ] Tests exist (mock provider only)

**Depends on:** M1, M2, M3, M4

---

## M6 — CLI / Local Demo

**Status:** `planned`

**Goal:** A local command-line interface for testing memory, reflection, and continuity.

**Commands:**
```bash
bdm memory add "..."
bdm memory list
bdm memory search "..."
bdm reflect "..."
bdm chat
bdm session summary
```

**Package:**
```
packages/bdm-cli/
```

**Definition of Done:**
- [ ] `bdm memory add` works
- [ ] `bdm memory search` works
- [ ] `bdm reflect` works
- [ ] `bdm chat` starts an interactive session
- [ ] `bdm session summary` prints last session context
- [ ] README for `bdm-cli` exists

**Depends on:** M1 through M5

---

## M7 — Experiments & Evaluation

**Status:** `planned`

**Goal:** Run structured experiments to evaluate whether BDM's layers produce measurable improvements.

**Experiments:**
- `M7.1` — Memory Persistence Test
- `M7.2` — Reflection Consistency Test
- `M7.3` — Belief Update Test
- `M7.4` — Continuity Across Sessions Test
- `M7.5` — Self-Model Stability Test

**Output location:** `research/results/`

**Definition of Done:**
- [ ] Each experiment has a script in `research/scripts/`
- [ ] Each experiment has a written description
- [ ] Results are recorded in `research/results/`
- [ ] `research/findings.md` summarizes what was learned
- [ ] Negative results are published alongside positive ones

**Depends on:** M1 through M6
