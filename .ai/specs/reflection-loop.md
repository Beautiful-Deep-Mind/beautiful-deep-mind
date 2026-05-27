# Spec: ReflectionLoop

**Module:** `bdm.reflection.loop`
**File:** `packages/bdm-core/src/bdm/reflection/loop.py`
**Milestone:** M2 (stub exists, full implementation pending)

---

## Purpose

`ReflectionLoop` compares a candidate output against a set of prior memory events and returns a verdict: consistent, inconsistent, or uncertain. It is a post-generation review step, not a generation step.

The goal is not to prevent all inconsistencies — it is to make inconsistencies detectable and auditable before output reaches the user.

---

## Current state

The current implementation is a **stub**. It returns:
- `CONSISTENT` when no prior events are provided
- `UNCERTAIN` when prior events exist (real comparison not yet implemented)

This is intentional. The interface is stable; the logic is not yet written.

---

## Interface

```python
class ReflectionLoop:
    def review(
        self,
        candidate: str,
        prior_events: Sequence[MemoryEvent],
    ) -> ReflectionResult:
        ...
```

---

## `ReflectionVerdict`

```python
class ReflectionVerdict(str, Enum):
    CONSISTENT   = "consistent"
    INCONSISTENT = "inconsistent"
    UNCERTAIN    = "uncertain"
```

Three states, not two. `UNCERTAIN` is important: it covers cases where the comparison is inconclusive, the prior events are ambiguous, or confidence is too low to decide.

---

## `ReflectionResult`

```python
@dataclass
class ReflectionResult:
    verdict: ReflectionVerdict
    candidate: str
    prior_events: list[MemoryEvent]
    note: str = ""
    revised: str | None = None
```

- `note` — human-readable explanation of the verdict
- `revised` — an optional revised version of the candidate (only set if `verdict == INCONSISTENT` and a correction was generated)

---

## Planned implementation (M2)

The full implementation will support two comparison modes:

1. **Rule-based:** Detect explicit contradictions using pattern matching or negation detection. Fast, no LLM required.
2. **LLM-assisted:** Pass candidate + prior events to an LLM and ask for a consistency verdict. Slower, requires a provider.

The mode will be configurable at construction time.

---

## What ReflectionLoop must never do

- Modify memory directly — that is the `Updater`'s job
- Generate final output — it reviews candidates, it does not produce them
- Claim the system is "thinking" or "aware" in any logged output
- Block indefinitely — if comparison takes too long, return `UNCERTAIN`
