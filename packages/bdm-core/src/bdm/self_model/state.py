from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Iterator


@dataclass
class TopicEntry:
    topic: str
    confidence: float = 1.0
    note: str = ""
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def __post_init__(self) -> None:
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError(f"confidence must be between 0.0 and 1.0, got {self.confidence}")


class SelfModelState:
    """Lightweight representation of the system's known knowledge state.

    This is a data structure, not a claim about self-awareness.
    It tracks what topics the system has recorded knowledge about,
    confidence levels, and acknowledged limitations.
    """

    def __init__(self) -> None:
        self._topics: dict[str, TopicEntry] = {}
        self._limitations: list[str] = []

    def set_topic(self, topic: str, confidence: float = 1.0, note: str = "") -> None:
        self._topics[topic] = TopicEntry(topic=topic, confidence=confidence, note=note)

    def get_topic(self, topic: str) -> TopicEntry | None:
        return self._topics.get(topic)

    def remove_topic(self, topic: str) -> bool:
        return self._topics.pop(topic, None) is not None

    def topics(self) -> Iterator[TopicEntry]:
        return iter(self._topics.values())

    def add_limitation(self, description: str) -> None:
        self._limitations.append(description)

    def limitations(self) -> list[str]:
        return list(self._limitations)

    def summary(self) -> dict:
        return {
            "topic_count": len(self._topics),
            "topics": [
                {"topic": e.topic, "confidence": e.confidence}
                for e in self._topics.values()
            ],
            "limitations": self._limitations,
        }
