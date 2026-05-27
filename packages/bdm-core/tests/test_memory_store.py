import pytest

from bdm.memory.event import MemoryEvent, MemoryEventType
from bdm.memory.short_term import ShortTermBuffer
from bdm.memory.long_term import LongTermStore


def _event(content: str, event_type: MemoryEventType = MemoryEventType.INTERACTION, tags: list[str] | None = None) -> MemoryEvent:
    return MemoryEvent(content=content, event_type=event_type, tags=tags or [])


class TestShortTermBuffer:
    def test_add_and_get(self):
        buf = ShortTermBuffer()
        e = _event("hello")
        buf.add(e)
        assert buf.get(e.id) is e

    def test_len(self):
        buf = ShortTermBuffer()
        buf.add(_event("a"))
        buf.add(_event("b"))
        assert len(buf) == 2

    def test_capacity_evicts_oldest(self):
        buf = ShortTermBuffer(capacity=2)
        e1 = _event("first")
        e2 = _event("second")
        e3 = _event("third")
        buf.add(e1)
        buf.add(e2)
        buf.add(e3)
        assert len(buf) == 2
        assert buf.get(e1.id) is None
        assert buf.get(e3.id) is e3

    def test_delete(self):
        buf = ShortTermBuffer()
        e = _event("to delete")
        buf.add(e)
        assert buf.delete(e.id) is True
        assert buf.get(e.id) is None

    def test_delete_missing_returns_false(self):
        buf = ShortTermBuffer()
        assert buf.delete("nonexistent") is False

    def test_query_by_event_type(self):
        buf = ShortTermBuffer()
        buf.add(_event("a", MemoryEventType.FACT))
        buf.add(_event("b", MemoryEventType.INTERACTION))
        results = buf.query(event_type=MemoryEventType.FACT)
        assert len(results) == 1
        assert results[0].content == "a"

    def test_query_by_tags(self):
        buf = ShortTermBuffer()
        buf.add(_event("tagged", tags=["important"]))
        buf.add(_event("plain"))
        results = buf.query(tags=["important"])
        assert len(results) == 1

    def test_clear(self):
        buf = ShortTermBuffer()
        buf.add(_event("x"))
        buf.clear()
        assert len(buf) == 0


class TestLongTermStore:
    def test_add_and_get(self):
        store = LongTermStore()
        e = _event("fact")
        store.add(e)
        assert store.get(e.id) is e

    def test_query_limit(self):
        store = LongTermStore()
        for i in range(5):
            store.add(_event(f"item {i}"))
        assert len(store.query(limit=3)) == 3

    def test_delete(self):
        store = LongTermStore()
        e = _event("removable")
        store.add(e)
        assert store.delete(e.id) is True
        assert store.get(e.id) is None

    def test_clear(self):
        store = LongTermStore()
        store.add(_event("a"))
        store.clear()
        assert len(store) == 0
