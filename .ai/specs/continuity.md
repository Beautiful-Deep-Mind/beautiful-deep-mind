# Spec: ContinuityContext

**Module:** `bdm.continuity.context`
**File:** `packages/bdm-core/src/bdm/continuity/context.py`
**Milestone:** M4 (stub exists)

---

## Purpose

`ContinuityContext` manages the serialization and restoration of session state across interactions. It ensures that a new session begins with access to relevant prior context rather than from a blank state.

---

## Current state

The stub implementation:
- `save(episodic_records, self_model, session_id)` — creates and stores a `SessionSnapshot`
- `load(session_id)` — retrieves a snapshot by session ID
- `latest()` — retrieves the most recent snapshot by `created_at`
- `all_session_ids()` — lists all stored session IDs

All storage is in-memory. Persistence to disk is deferred to M4 full implementation.

---

## `SessionSnapshot`

```python
@dataclass
class SessionSnapshot:
    session_id: str
    episodic_records: list[EpisodicRecord]
    self_model_summary: dict[str, Any]
    created_at: datetime
```

`SessionSnapshot` is designed to be serializable. All fields must remain JSON-compatible when persistence is added.

---

## Planned additions (M4 full implementation)

- `session.py` — `Session` model with open/close lifecycle
- `summary.py` — generates a compact text summary from a snapshot (for LLM context injection)
- `tracker.py` — detects significant changes between sessions
- `reconstruction.py` — rebuilds context from a chain of summaries

---

## Privacy constraint

`SessionSnapshot` may contain sensitive content from prior interactions. Any persistence implementation must:

1. Store data in a location the user controls
2. Provide a documented path for deleting all stored snapshots
3. Never transmit snapshots to a remote service without explicit user consent

This constraint must be preserved in all future implementations.

---

## Cold start protocol

When a new session begins after a gap:

1. Load the latest snapshot via `ContinuityContext.latest()`
2. Generate a summary of the snapshot via `summary.py`
3. Inject the summary into the session context (not the full snapshot)
4. The full snapshot is available for detailed queries during the session

Do not inject full history into every session. Summarize.
