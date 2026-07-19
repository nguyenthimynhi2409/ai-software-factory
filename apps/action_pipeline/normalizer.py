from __future__ import annotations

import re
from collections.abc import Iterable

from .models import Action, RawEvent

SECRET_PATTERN = re.compile(r"password|passwd|token|secret|cookie|authorization", re.I)


def _mask(value: object, key: str = "") -> object:
    if SECRET_PATTERN.search(key):
        return "[REDACTED]"
    if isinstance(value, dict):
        return {name: _mask(item, name) for name, item in value.items()}
    if isinstance(value, list):
        return [_mask(item, key) for item in value]
    return value


def _target(event: RawEvent) -> dict[str, object]:
    target = _mask(event.target)
    if not isinstance(target, dict):
        return {}
    for key in ("testId", "ariaLabel", "role", "css", "xpath"):
        if target.get(key):
            return {"strategy": key, "value": target[key]}
    if target.get("url"):
        return {"strategy": "url", "value": target["url"]}
    return {"strategy": "unknown", "value": None}


def normalize(events: Iterable[RawEvent]) -> list[Action]:
    """Sort events, discard exact duplicates and map raw events to actions."""
    ordered = sorted(events, key=lambda event: (event.timestamp, event.id))
    actions: list[Action] = []
    previous: tuple[str, str, str] | None = None
    mapping = {
        "click": "click", "input": "input", "change": "input",
        "select": "select", "navigate": "navigate", "wait": "wait",
        "assert": "assert", "keypress": "keypress", "upload": "upload",
    }
    for event in ordered:
        signature = (event.type, repr(event.target), repr(event.value))
        if signature == previous:
            continue
        previous = signature
        action_type = mapping.get(event.type, "custom")
        notes: tuple[str, ...] = ()
        confidence = 1.0
        if action_type == "custom":
            confidence = 0.4
            notes = (f"Unsupported raw event type: {event.type}",)
        value_key = str(event.metadata.get("field", event.type))
        actions.append(Action(
            id=event.id,
            timestamp=event.timestamp,
            type=action_type,
            target=_target(event),
            value=_mask(event.value, value_key),
            source_event_ids=(event.id,),
            confidence=confidence,
            notes=notes,
        ))
    return actions
