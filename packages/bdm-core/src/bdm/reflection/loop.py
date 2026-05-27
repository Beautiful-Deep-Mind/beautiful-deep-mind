from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Sequence

from bdm.memory.event import MemoryEvent


class ReflectionVerdict(str, Enum):
    CONSISTENT = "consistent"
    INCONSISTENT = "inconsistent"
    UNCERTAIN = "uncertain"


@dataclass
class ReflectionResult:
    verdict: ReflectionVerdict
    candidate: str
    prior_events: list[MemoryEvent]
    note: str = ""
    revised: str | None = None


class ReflectionLoop:
    """Compares a candidate output against prior memory events.

    This is a rule-based stub. LLM-assisted comparison will be added
    when the interface layer is available.
    """

    def review(
        self,
        candidate: str,
        prior_events: Sequence[MemoryEvent],
    ) -> ReflectionResult:
        if not prior_events:
            return ReflectionResult(
                verdict=ReflectionVerdict.CONSISTENT,
                candidate=candidate,
                prior_events=[],
                note="No prior events to compare against.",
            )

        # Placeholder: real comparison logic goes here.
        return ReflectionResult(
            verdict=ReflectionVerdict.UNCERTAIN,
            candidate=candidate,
            prior_events=list(prior_events),
            note="Rule-based comparison not yet implemented.",
        )
