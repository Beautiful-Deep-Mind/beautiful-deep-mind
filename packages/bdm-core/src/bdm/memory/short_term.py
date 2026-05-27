from __future__ import annotations

from collections import deque
from typing import Sequence

from .event import MemoryEvent, MemoryEventType
from .store import MemoryStore


class ShortTermBuffer(MemoryStore):
    """In-memory FIFO buffer for the active session context.

    Automatically evicts the oldest event when capacity is exceeded.
    Contents are not persisted across sessions — use LongTermStore for that.
    """

    def __init__(self, capacity: int = 64) -> None:
        self._capacity = capacity
        self._events: deque[MemoryEvent] = deque(maxlen=capacity)
        self._index: dict[str, MemoryEvent] = {}

    def add(self, event: MemoryEvent) -> None:
        if len(self._events) == self._capacity:
            evicted = self._events[0]
            self._index.pop(evicted.id, None)
        self._events.append(event)
        self._index[event.id] = event

    def get(self, event_id: str) -> MemoryEvent | None:
        return self._index.get(event_id)

    def query(
        self,
        *,
        limit: int = 10,
        event_type: MemoryEventType | None = None,
        tags: list[str] | None = None,
    ) -> Sequence[MemoryEvent]:
        results = list(self._events)
        if event_type is not None:
            results = [e for e in results if e.event_type == event_type]
        if tags:
            tag_set = set(tags)
            results = [e for e in results if tag_set.intersection(e.tags)]
        return list(reversed(results))[:limit]

    def delete(self, event_id: str) -> bool:
        event = self._index.pop(event_id, None)
        if event is None:
            return False
        try:
            self._events.remove(event)
        except ValueError:
            pass
        return True

    def clear(self) -> None:
        self._events.clear()
        self._index.clear()

    def __len__(self) -> int:
        return len(self._events)
