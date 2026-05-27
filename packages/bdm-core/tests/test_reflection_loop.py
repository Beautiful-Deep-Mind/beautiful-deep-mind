from bdm.memory.event import MemoryEvent, MemoryEventType
from bdm.reflection.loop import ReflectionLoop, ReflectionVerdict


def _event(content: str) -> MemoryEvent:
    return MemoryEvent(content=content, event_type=MemoryEventType.INTERACTION)


class TestReflectionLoop:
    def setup_method(self):
        self.loop = ReflectionLoop()

    def test_no_prior_events_returns_consistent(self):
        result = self.loop.review("some output", prior_events=[])
        assert result.verdict == ReflectionVerdict.CONSISTENT

    def test_with_prior_events_returns_uncertain(self):
        prior = [_event("prior statement")]
        result = self.loop.review("new output", prior_events=prior)
        assert result.verdict == ReflectionVerdict.UNCERTAIN

    def test_result_carries_candidate(self):
        result = self.loop.review("candidate text", prior_events=[])
        assert result.candidate == "candidate text"

    def test_result_carries_prior_events(self):
        prior = [_event("a"), _event("b")]
        result = self.loop.review("x", prior_events=prior)
        assert len(result.prior_events) == 2
