from __future__ import annotations

from collections.abc import Iterable
from typing import Any

from .analyzer import generate_steps
from .models import RawEvent
from .normalizer import normalize


class ActionPipeline:
    def run(self, session_id: str, events: Iterable[RawEvent]) -> dict[str, Any]:
        normalized = normalize(events)
        steps = generate_steps(normalized)
        return {
            "sessionId": session_id,
            "summary": f"Generated {len(steps)} step(s)",
            "preconditions": [],
            "steps": [step.to_dict() for step in steps],
            "ambiguities": [
                {"step": step.index, "notes": list(step.notes)}
                for step in steps if step.notes
            ],
            "sensitiveDataRemoved": True,
        }
