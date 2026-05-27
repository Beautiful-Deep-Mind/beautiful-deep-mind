import pytest

from bdm.memory.event import MemoryEvent, MemoryEventType


def test_event_has_auto_id_and_timestamp():
    event = MemoryEvent(content="hello", event_type=MemoryEventType.INTERACTION)
    assert event.id
    assert event.created_at is not None


def test_two_events_have_different_ids():
    a = MemoryEvent(content="a", event_type=MemoryEventType.FACT)
    b = MemoryEvent(content="b", event_type=MemoryEventType.FACT)
    assert a.id != b.id


def test_salience_default_is_one():
    event = MemoryEvent(content="x", event_type=MemoryEventType.SYSTEM)
    assert event.salience == 1.0


def test_salience_out_of_range_raises():
    with pytest.raises(ValueError):
        MemoryEvent(content="x", event_type=MemoryEventType.SYSTEM, salience=1.5)

    with pytest.raises(ValueError):
        MemoryEvent(content="x", event_type=MemoryEventType.SYSTEM, salience=-0.1)


def test_tags_default_empty():
    event = MemoryEvent(content="x", event_type=MemoryEventType.INTERACTION)
    assert event.tags == []
