from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any


class MemoryEventType(str, Enum):
    INTERACTION = "interaction"
    FACT = "fact"
    CORRECTION = "correction"
    REFLECTION = "reflection"
    SYSTEM = "system"


@dataclass
class MemoryEvent:
    content: str
    event_type: MemoryEventType
    tags: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)
    salience: float = 1.0
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def __post_init__(self) -> None:
        if not 0.0 <= self.salience <= 1.0:
            raise ValueError(f"salience must be between 0.0 and 1.0, got {self.salience}")
