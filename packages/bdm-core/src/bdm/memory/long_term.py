from __future__ import annotations

from typing import Sequence

from .event import MemoryEvent, MemoryEventType
from .store import MemoryStore


class LongTermStore(MemoryStore):
    """Persistent store for events that should survive across sessions.

    Currently backed by a plain in-memory dict. Persistence (file, DB)
    will be added in a later phase.
    """

    def __init__(self) -> None:
        self._events: dict[str, MemoryEvent] = {}

    def add(self, event: MemoryEvent) -> None:
        self._events[event.id] = event

    def get(self, event_id: str) -> MemoryEvent | None:
        return self._events.get(event_id)

    def query(
        self,
        *,
        limit: int = 10,
        event_type: MemoryEventType | None = None,
        tags: list[str] | None = None,
    ) -> Sequence[MemoryEvent]:
        results = list(self._events.values())
        if event_type is not None:
            results = [e for e in results if e.event_type == event_type]
        if tags:
            tag_set = set(tags)
            results = [e for e in results if tag_set.intersection(e.tags)]
        results.sort(key=lambda e: e.created_at, reverse=True)
        return results[:limit]

    def delete(self, event_id: str) -> bool:
        return self._events.pop(event_id, None) is not None

    def clear(self) -> None:
        self._events.clear()

    def __len__(self) -> int:
        return len(self._events)
