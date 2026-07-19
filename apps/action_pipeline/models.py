from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal

ActionType = Literal[
    "click", "input", "select", "navigate", "wait", "assert",
    "keypress", "upload", "custom",
]


@dataclass(frozen=True)
class RawEvent:
    id: str
    timestamp: int
    type: str
    target: dict[str, Any] = field(default_factory=dict)
    value: Any = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class Action:
    id: str
    timestamp: int
    type: ActionType
    target: dict[str, Any] = field(default_factory=dict)
    value: Any = None
    source_event_ids: tuple[str, ...] = ()
    confidence: float = 1.0
    notes: tuple[str, ...] = ()


@dataclass(frozen=True)
class Step:
    index: int
    type: ActionType
    target: dict[str, Any]
    value: Any
    source_event_ids: tuple[str, ...]
    confidence: float
    notes: tuple[str, ...] = ()

    def to_dict(self) -> dict[str, Any]:
        return {
            "index": self.index,
            "type": self.type,
            "target": self.target,
            "value": self.value,
            "sourceEventIds": list(self.source_event_ids),
            "confidence": self.confidence,
            "notes": list(self.notes),
        }
