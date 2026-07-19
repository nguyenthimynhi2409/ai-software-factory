from __future__ import annotations

import argparse
import json
from pathlib import Path

from .models import RawEvent
from .pipeline import ActionPipeline


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate replayable steps from recorded events")
    parser.add_argument("input", type=Path, help="JSON file containing sessionId and events")
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    if not isinstance(payload, dict) or "events" not in payload:
        parser.error("input JSON must contain 'sessionId' and 'events' fields")
    if not isinstance(payload["events"], list):
        parser.error("input JSON field 'events' must be an array")
    events = [RawEvent(**event) for event in payload["events"]]
    print(json.dumps(ActionPipeline().run(payload["sessionId"], events), indent=2))


if __name__ == "__main__":
    main()
