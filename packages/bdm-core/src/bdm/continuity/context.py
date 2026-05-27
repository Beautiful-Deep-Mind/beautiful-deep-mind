from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from bdm.memory.episodic import EpisodicRecord
from bdm.self_model.state import SelfModelState


@dataclass
class SessionSnapshot:
    """Serialisable snapshot of session state for cross-session persistence."""

    session_id: str
    episodic_records: list[EpisodicRecord]
    self_model_summary: dict[str, Any]
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


class ContinuityContext:
    """Manages serialisation and restoration of session state.

    Persistence backend (file, DB) is not yet implemented.
    Currently operates in-memory only.
    """

    def __init__(self) -> None:
        self._snapshots: dict[str, SessionSnapshot] = {}

    def save(
        self,
        episodic_records: list[EpisodicRecord],
        self_model: SelfModelState,
        session_id: str | None = None,
    ) -> SessionSnapshot:
        sid = session_id or str(uuid.uuid4())
        snapshot = SessionSnapshot(
            session_id=sid,
            episodic_records=list(episodic_records),
            self_model_summary=self_model.summary(),
        )
        self._snapshots[sid] = snapshot
        return snapshot

    def load(self, session_id: str) -> SessionSnapshot | None:
        return self._snapshots.get(session_id)

    def latest(self) -> SessionSnapshot | None:
        if not self._snapshots:
            return None
        return max(self._snapshots.values(), key=lambda s: s.created_at)

    def all_session_ids(self) -> list[str]:
        return list(self._snapshots.keys())
