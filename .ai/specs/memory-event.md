# Spec: MemoryEvent

**Module:** `bdm.memory.event`
**File:** `packages/bdm-core/src/bdm/memory/event.py`
**Milestone:** M1.1

---

## Purpose

`MemoryEvent` is the atomic unit of memory in BDM. It represents a single recorded event — an interaction, a fact, a correction, a reflection output, or a system event. Every other memory structure is either a collection of events or a derived record built from events.

---

## Fields

| Field | Type | Default | Description |
|---|---|---|---|
| `id` | `str` | `uuid4()` | Unique identifier, auto-generated |
| `content` | `str` | required | The event content |
| `event_type` | `MemoryEventType` | required | Category of event |
| `tags` | `list[str]` | `[]` | Free-form tags for filtering |
| `metadata` | `dict[str, Any]` | `{}` | Arbitrary additional data |
| `salience` | `float` | `1.0` | Importance weight in [0.0, 1.0] |
| `created_at` | `datetime` | `now(utc)` | Creation timestamp |

---

## `MemoryEventType` values

| Value | Meaning |
|---|---|
| `INTERACTION` | A user–system exchange |
| `FACT` | A stored general fact |
| `CORRECTION` | An explicit correction of a prior event |
| `REFLECTION` | Output of the reflection loop |
| `SYSTEM` | Internal system event |

---

## Validation

- `salience` must be in `[0.0, 1.0]` — raises `ValueError` otherwise
- `content` must not be checked for emptiness at this layer (the store layer may enforce this)

---

## What it is not

`MemoryEvent` is not an `EpisodicRecord`. It does not carry a `session_id` or a list of source events. It is a flat, atomic record. If you need a composed record with temporal/contextual metadata, use `EpisodicRecord`.

---

## Example

```python
from bdm.memory.event import MemoryEvent, MemoryEventType

event = MemoryEvent(
    content="The user wants to build BDM Core before anything else.",
    event_type=MemoryEventType.FACT,
    tags=["bdm", "goal", "priority"],
    salience=0.95,
)
```
