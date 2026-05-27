# Spec: SelfModelState

**Module:** `bdm.self_model.state`
**File:** `packages/bdm-core/src/bdm/self_model/state.py`
**Milestone:** M3 (stub exists)

---

## Purpose

`SelfModelState` is a structured record of the system's own knowledge state. It tracks:
- What topics the system has stored knowledge about
- Confidence levels attached to stored beliefs
- Known limitations and acknowledged gaps
- A summary suitable for injection into an LLM prompt

**This is a data structure. It is not self-awareness. It does not imply consciousness.**

---

## Current state

The stub implementation includes:
- `set_topic(topic, confidence, note)` — add or update a topic entry
- `get_topic(topic)` — retrieve a topic entry
- `remove_topic(topic)` — delete a topic entry
- `topics()` — iterate all entries
- `add_limitation(description)` — record a known limitation
- `limitations()` — retrieve all limitations
- `summary()` — return a dict for prompt injection

This is sufficient for M3 stub purposes. Goals and identity are deferred to M3 full implementation.

---

## `TopicEntry`

```python
@dataclass
class TopicEntry:
    topic: str
    confidence: float  # [0.0, 1.0]
    note: str = ""
    updated_at: datetime = ...
```

Confidence is validated at construction. Values outside [0.0, 1.0] raise `ValueError`.

---

## `summary()` output

Used to inject self-model state into LLM prompts:

```python
{
    "topic_count": 3,
    "topics": [
        {"topic": "BDM Memory Core", "confidence": 0.9},
        {"topic": "Python dataclasses", "confidence": 1.0},
    ],
    "limitations": [
        "No consciousness claims",
        "SQLite persistence not yet implemented"
    ]
}
```

---

## Planned additions (M3 full implementation)

- `goals.py` — `ActiveGoal` with priority and status
- `limitations.py` — richer limitation model with source and severity
- `identity.py` — system identity description (name, version, current focus)

---

## What SelfModelState must never contain

- Claims about subjective experience
- Claims about consciousness or sentience
- Medical or clinical assessments
- Data that was not explicitly stored by the system — it is a record, not an inference engine
