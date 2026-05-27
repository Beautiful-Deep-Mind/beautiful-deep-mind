# Roadmap

## Vision

Beautiful Deep Mind investigates whether structured memory, reflection, self-modeling, and context continuity can improve the long-term coherence of AI-assisted systems.

BDM does not claim to create consciousness. It does not attempt to copy, upload, or preserve a human mind. It is an experimental software and research project. All milestones produce either working software, published research findings, or both.

---

## Milestone 0 — Project Foundation

**Status: Complete**

**Goal:** Establish the conceptual, legal, and documentation foundation. The project must exist as a serious repository with clear scope, rules, and limitations before any code is written.

**Modules:**
- M0.1 — Repository Structure
- M0.2 — Manifesto
- M0.3 — Architecture Concept
- M0.4 — Ethics and Limitations
- M0.5 — License and Contribution Rules
- M0.6 — Roadmap

**Outputs:** `README.md`, `LICENSE.md`, `CONTRIBUTING.md`, `docs/`, `research/`, `concepts/`, `.ai/`, `.github/`

**Limitations:** No working software. All architectural descriptions are conceptual.

---

## Milestone 1 — Memory Core

**Status: In progress**

**Goal:** Build the first persistent memory layer. This is the foundation every other layer depends on. Without working memory, nothing above it can be built meaningfully.

**Modules:**
- M1.1 — `MemoryEvent` with type, tags, salience, confidence
- M1.2 — `MemoryStore` abstract base class
- M1.3 — `ShortTermBuffer` — bounded in-memory FIFO
- M1.4 — `LongTermStore` — in-memory now, SQLite persistence next
- M1.5 — `EpisodicRecord` — structured episode with session context
- M1.6 — Memory search: by tag, by type, by text content
- M1.7 — Importance and confidence scoring

**Expected outputs:**
- Working memory package with tests
- SQLite-backed `LongTermStore`
- `examples/memory_demo.py`

**Limitations:** No reflection or self-model integration. No semantic/embedding-based search yet. SQLite schema is provisional.

---

## Milestone 2 — Reflection Loop

**Status: Planned**

**Goal:** Build a loop where the system retrieves relevant memory, reflects on context, prepares a structured response context, and stores the result after interaction.

**Flow:**
```
input → retrieve memory → reflect → build context → output → store result
```

**Modules:**
- M2.1 — Input Analyzer
- M2.2 — Memory Retrieval (attention layer)
- M2.3 — Reflection Engine (rule-based first, LLM-assisted second)
- M2.4 — Response Context Builder
- M2.5 — Post-Interaction Memory Updater

**Expected outputs:**
- Working reflection loop without LLM dependency
- `examples/reflection_demo.py`
- Tests for each module

**Limitations:** Reflection quality is limited without LLM assistance. Rule-based consistency detection will miss subtle inconsistencies. Latency not yet optimized.

**Depends on:** Milestone 1 complete

---

## Milestone 3 — Self-Model

**Status: Planned**

**Goal:** Create a structured representation of the system's knowledge state: active goals, known limitations, topic coverage, and current focus. This self-model can be queried and injected into LLM prompts.

**Modules:**
- M3.1 — Project State
- M3.2 — Active Goals
- M3.3 — Known Limitations
- M3.4 — Current Focus
- M3.5 — Identity Description

**Expected outputs:**
- `SelfModelState` with goals, limitations, and topic inventory
- Integration with Reflection Loop (self-model injected into reflection context)
- Tests

**Limitations:** Self-model is a data structure, not self-awareness. Confidence scoring is approximate. The self-model reflects stored knowledge, not inferred knowledge.

**Depends on:** Milestone 1 complete

---

## Milestone 4 — Context Continuity

**Status: Planned**

**Goal:** Maintain coherent context across sessions through session serialization, summaries, state tracking, and long-term context reconstruction.

**Modules:**
- M4.1 — Session Model
- M4.2 — Context Summary Generator
- M4.3 — Continuity Tracker
- M4.4 — Session-to-Memory Bridge
- M4.5 — Long-Term Context Reconstruction

**Expected outputs:**
- Sessions with open/close lifecycle
- Session summaries stored in long-term memory
- Context reconstruction from prior summaries
- `examples/continuity_demo.py`

**Limitations:** Long-gap sessions (days, weeks) may produce stale context. Summary quality depends on the quality of stored events. Privacy implications of cross-session storage must be addressed explicitly.

**Depends on:** Milestones 1, 2, 3

---

## Milestone 5 — LLM Integration

**Status: Planned**

**Goal:** Connect BDM Core to a language model through a provider interface. Build memory-aware and reflection-aware chat that uses stored context to improve response coherence.

**Modules:**
- M5.1 — `LLMProvider` abstract interface
- M5.2 — Prompt Context Builder
- M5.3 — Memory-Aware Chat
- M5.4 — Reflection-Aware Chat
- M5.5 — Safety Boundaries

**Expected outputs:**
- Pluggable LLM provider interface (mock + real)
- Memory-aware chat with context injection
- Reflection loop integrated into response pipeline
- Safety layer that prevents consciousness and medical claims in output

**Limitations:** Evaluation of quality is partly subjective. Results are specific to the LLM used. Integration adds latency. API costs constrain experiment scale.

**Depends on:** Milestones 1, 2, 3, 4

---

## Milestone 6 — CLI / Local Demo

**Status: Planned**

**Goal:** A local command-line interface that demonstrates BDM Core's capabilities in a usable form.

**Commands:**
```bash
bdm memory add "..."
bdm memory list
bdm memory search "..."
bdm reflect "..."
bdm chat
bdm session summary
```

**Expected outputs:**
- `packages/bdm-cli/` package
- All listed commands working end-to-end
- `README.md` for `bdm-cli`

**Limitations:** Not a production tool. CLI is a demo and development aid, not a user-facing product.

**Depends on:** Milestones 1 through 5

---

## Milestone 7 — Experiments and Evaluation

**Status: Planned**

**Goal:** Run structured experiments to evaluate whether BDM's layers produce measurable improvements in coherence, consistency, and context retention. Publish results openly, including negative results.

**Experiments:**
- M7.1 — Memory Persistence Test (H1)
- M7.2 — Reflection Consistency Test (H2)
- M7.3 — Belief Update Test (H3)
- M7.4 — Continuity Across Sessions Test (H4)
- M7.5 — Self-Model Stability Test (H3)

**Expected outputs:**
- Experiment scripts in `research/scripts/`
- Results in `research/results/`
- `research/findings.md` — summary of what was learned
- Revised or retired hypotheses based on findings

**Limitations:** Results will be specific to the systems and LLMs tested. Automated metrics for coherence are imperfect. Generalizability is uncertain. Some hypotheses will likely be falsified.

**Depends on:** Milestones 1 through 6

---

*This roadmap is a working document. It will be updated as the project progresses. Milestone statuses are tracked in `.ai/milestones.md`.*
