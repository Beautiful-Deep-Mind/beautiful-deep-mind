# Spec: MemoryStore, ShortTermBuffer, LongTermStore

**Module:** `bdm.memory.store`, `bdm.memory.short_term`, `bdm.memory.long_term`
**Milestone:** M1.2, M1.3, M1.4

---

## `MemoryStore` (abstract base)

`MemoryStore` is the contract all store implementations must satisfy.

### Required methods

| Method | Signature | Description |
|---|---|---|
| `add` | `(event: MemoryEvent) -> None` | Store an event |
| `get` | `(event_id: str) -> MemoryEvent \| None` | Retrieve by ID |
| `query` | `(*, limit, event_type, tags) -> Sequence[MemoryEvent]` | Filtered retrieval |
| `delete` | `(event_id: str) -> bool` | Remove by ID, return True if found |
| `clear` | `() -> None` | Remove all events |

All arguments to `query` are keyword-only. All are optional (defaults: `limit=10`, others `None`).

---

## `ShortTermBuffer`

**Purpose:** Active session context. Fast, bounded, non-persistent.

**Backend:** `collections.deque(maxlen=capacity)`

**Behavior:**
- When `capacity` is reached, the oldest event is evicted automatically
- The evicted event is also removed from the internal index
- `query()` returns results in reverse-insertion order (most recent first)
- Does not persist to disk — contents are lost when the process ends

**Constructor:**
```python
ShortTermBuffer(capacity: int = 64)
```

**When to use:** Hold the events of the current session for fast access during reflection and context building.

---

## `LongTermStore`

**Purpose:** Persistent storage for events that should survive across sessions.

**Current backend:** In-memory dict (placeholder)
**Planned backend:** SQLite (Milestone 1, M1.4 completion)

**Behavior:**
- No capacity limit (bounded only by available memory/disk)
- `query()` returns results sorted by `created_at` descending (most recent first)
- SQLite schema and migration strategy: open decision (see `.ai/architecture.md`)

**Constructor:**
```python
LongTermStore()
```

**When to use:** Store any event that should be available in future sessions.

---

## Query behavior

Both stores support the same `query()` signature:

```python
def query(
    self,
    *,
    limit: int = 10,
    event_type: MemoryEventType | None = None,
    tags: list[str] | None = None,
) -> Sequence[MemoryEvent]:
```

- `event_type` filter: exact match on `MemoryEventType`
- `tags` filter: event must contain at least one of the provided tags (OR logic)
- Filters are applied before `limit` is enforced
- Return order: most recent first

---

## What is not yet implemented

- SQLite persistence for `LongTermStore`
- Text/semantic search (Milestone 1, M1.6)
- Importance/confidence scoring (Milestone 1, M1.7)
- Combined AND tag filtering (currently OR)
