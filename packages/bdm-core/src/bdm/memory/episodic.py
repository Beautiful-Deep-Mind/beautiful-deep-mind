from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass
class EpisodicRecord:
    """A structured record of a single interaction episode.

    Episodic records carry temporal and contextual metadata that plain
    MemoryEvents do not. They are intended for long-term retrieval where
    the when and under-what-context matter as much as the what.
    """

    summary: str
    tags: list[str] = field(default_factory=list)
    source_event_ids: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)
    salience: float = 1.0
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    session_id: str | None = None

    def __post_init__(self) -> None:
        if not self.summary.strip():
            raise ValueError("EpisodicRecord summary must not be empty")
        if not 0.0 <= self.salience <= 1.0:
            raise ValueError(f"salience must be between 0.0 and 1.0, got {self.salience}")
