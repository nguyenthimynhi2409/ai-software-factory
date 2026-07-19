from __future__ import annotations

from collections.abc import Iterable

from .models import Action, Step


def generate_steps(actions: Iterable[Action]) -> list[Step]:
    """Convert normalized actions into auditable, replay-oriented steps."""
    steps: list[Step] = []
    for action in actions:
        notes = list(action.notes)
        if action.type in {"click", "input", "select", "assert"} and action.target["strategy"] == "unknown":
            notes.append("Target is not stable; manual review required")
        steps.append(Step(
            index=len(steps) + 1,
            type=action.type,
            target=action.target,
            value=action.value,
            source_event_ids=action.source_event_ids,
            confidence=action.confidence,
            notes=tuple(notes),
        ))
    return steps
