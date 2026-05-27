from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Sequence

from .event import MemoryEvent, MemoryEventType


class MemoryStore(ABC):
    """Abstract base for all memory store implementations."""

    @abstractmethod
    def add(self, event: MemoryEvent) -> None:
        ...

    @abstractmethod
    def get(self, event_id: str) -> MemoryEvent | None:
        ...

    @abstractmethod
    def query(
        self,
        *,
        limit: int = 10,
        event_type: MemoryEventType | None = None,
        tags: list[str] | None = None,
    ) -> Sequence[MemoryEvent]:
        ...

    @abstractmethod
    def delete(self, event_id: str) -> bool:
        ...

    @abstractmethod
    def clear(self) -> None:
        ...

    def __len__(self) -> int:
        raise NotImplementedError
