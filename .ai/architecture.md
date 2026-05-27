# Architecture Decisions

This file records key architectural decisions for BDM Core. When a decision is made and agreed upon, it is recorded here. Do not change these decisions without updating this file.

---

## Layer model

BDM Core is organized as a set of composable functional layers. Each layer has a single clear responsibility and communicates through defined interfaces. The processing order is:

```
Interface Layer
    ↓
Context Continuity
    ↓
Self-Model
    ↓
Learning Loop
    ↓
Reflection
    ↓
Attention (memory retrieval)
    ↓
Memory Layer
```

Each layer depends on the ones below it. Higher layers must not be built before lower ones are stable.

---

## Package: `bdm-core`

All core cognitive layers live in `packages/bdm-core/src/bdm/`.

Subpackages map 1:1 to layers:

| Subpackage | Layer | Milestone |
|---|---|---|
| `bdm.memory` | Memory + Attention | M1 |
| `bdm.reflection` | Reflection + Learning Loop | M2 |
| `bdm.self_model` | Self-Model | M3 |
| `bdm.continuity` | Context Continuity | M4 |
| `bdm.llm` | Interface Layer | M5 |

---

## Memory design decisions

**Decision: Abstract base class for all stores**
`MemoryStore` is an ABC. `ShortTermBuffer` and `LongTermStore` are concrete implementations. This allows swapping backends (in-memory, SQLite, vector DB) without changing callers.

**Decision: Separate `MemoryEvent` from `EpisodicRecord`**
`MemoryEvent` is the atomic unit — a single raw event. `EpisodicRecord` is a composed, summarized record with temporal and contextual metadata. They serve different retrieval purposes and must not be conflated.

**Decision: `ShortTermBuffer` uses bounded deque, not a time window**
Capacity-based eviction is simpler and more predictable than time-based eviction at this stage. Time-based expiry will be considered in a later phase.

**Decision: `LongTermStore` is in-memory first, SQLite second**
The current implementation is a dict. SQLite persistence is deferred to Milestone 1 completion. The ABC ensures this is a backend swap, not a redesign.

**Decision: salience is a float [0.0, 1.0], validated at construction**
Salience is validated in `__post_init__`. Values outside range raise `ValueError`. Callers are responsible for computing salience before storing; the store does not compute it.

---

## Reflection design decisions

**Decision: `ReflectionLoop.review()` is synchronous and blocking**
The first implementation is synchronous. Async support may be added later if latency becomes a problem. This keeps the initial design simple.

**Decision: `ReflectionVerdict` is an enum, not a boolean**
Three states: `CONSISTENT`, `INCONSISTENT`, `UNCERTAIN`. A boolean would lose the `UNCERTAIN` case, which is important for partial comparisons or low-confidence checks.

**Decision: Rule-based stub first, LLM-assisted second**
The current `ReflectionLoop` is a placeholder. Real comparison logic (LLM-assisted or rule-based) is deferred to Milestone 2 proper. The interface is stable; the implementation is not.

---

## Self-model design decisions

**Decision: `SelfModelState` is a plain class, not a dataclass**
It has mutable internal state and methods. A dataclass would encourage treating it as immutable. A plain class with explicit methods makes mutation intentional.

**Decision: `TopicEntry` is a dataclass**
It is a value object: immutable, compared by value, no methods. Dataclass is appropriate.

---

## Continuity design decisions

**Decision: `SessionSnapshot` is serializable by design**
Fields are limited to standard types and BDM dataclasses. This ensures JSON serialization is straightforward when persistence is added.

**Decision: `ContinuityContext` stores snapshots keyed by `session_id`**
Sessions are identified by a UUID generated at save time unless a `session_id` is provided. The caller controls identity, not the store.

---

## General coding decisions

**Decision: `from __future__ import annotations` in every module**
Required for forward references and consistent behavior across Python 3.11+.

**Decision: No `print()` in library code**
Library code communicates through return values and exceptions. Print is reserved for CLI and demo scripts.

**Decision: No external dependencies in `bdm-core` until Milestone 1 completion**
The memory layer must be implemented without requiring any external library beyond the stdlib. SQLite is stdlib. numpy, sentence-transformers, etc. are deferred.

---

## Open decisions (not yet made)

- Embedding model for semantic search in memory (deferred to M1 completion)
- SQLite schema version management strategy
- Session serialization format (JSON vs. msgpack vs. pickle)
- Whether `LongTermStore` and `EpisodicRecord` share the same table or separate ones
- Whether `ReflectionLoop` calls LLM directly or through the Interface Layer
