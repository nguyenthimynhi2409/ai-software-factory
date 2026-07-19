from __future__ import annotations

import argparse
import time
from pathlib import Path
from typing import Any

from .models import RawEvent
from .pipeline import ActionPipeline


def to_markdown(result: dict[str, Any], url: str) -> str:
    lines = ["# Recorded Test Steps", "", f"- URL: `{url}`", f"- Session: `{result['sessionId']}`", "", "## Steps", "", "| # | Action | Target | Value | Confidence |", "|---:|---|---|---|---:|"]
    for step in result["steps"]:
        target = step["target"].get("value") or "(unknown)"
        value = str(step["value"] or "").replace("|", "\\|").replace("\n", " ")
        lines.append(f"| {step['index']} | `{step['type']}` | `{target}` | `{value}` | {step['confidence']:.2f} |")
    if result["ambiguities"]:
        lines.extend(["", "## Review Required", ""])
        for item in result["ambiguities"]:
            lines.append(f"- Step {item['step']}: {'; '.join(item['notes'])}")
    return "\n".join(lines) + "\n"


def record(url: str, output: Path, headless: bool = False) -> None:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as error:
        raise SystemExit("Install Playwright first: python3 -m pip install playwright && python3 -m playwright install chromium") from error

    events: list[dict[str, Any]] = []
    started = int(time.time() * 1000)
    sequence = 0

    def add_event(event_type: str, target: dict[str, Any] | None = None, value: Any = None) -> None:
        nonlocal sequence
        sequence += 1
        events.append({"id": f"e{sequence}", "timestamp": int(time.time() * 1000) - started, "type": event_type, "target": target or {}, "value": value, "metadata": {}})

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=headless)
        page = browser.new_page()
        page.expose_function("__recordEvent", lambda event: add_event(event["type"], event.get("target"), event.get("value")))
        page.add_init_script("""
        (() => {
          const target = e => ({testId: e.getAttribute('data-testid') || undefined, ariaLabel: e.getAttribute('aria-label') || undefined, role: e.getAttribute('role') || undefined, tag: e.tagName.toLowerCase()});
          document.addEventListener('click', e => { const x=e.target.closest('button,a,input,select,textarea,[role="button"]'); if(x) window.__recordEvent({type:'click',target:target(x)}); }, true);
          document.addEventListener('change', e => { const x=e.target; if(x.matches('input,select,textarea')) window.__recordEvent({type:x.tagName.toLowerCase()==='select'?'select':'input',target:target(x),value:x.value}); }, true);
          document.addEventListener('keydown', e => { if(['Enter','Escape','Tab'].includes(e.key)) window.__recordEvent({type:'keypress',target:target(e.target),value:e.key}); }, true);
        })();
        """)
        page.on("framenavigated", lambda frame: add_event("navigate", {"url": frame.url}) if frame == page.main_frame else None)
        page.goto(url)
        print(f"Recording at {url}. Perform actions, then press Enter here to stop.")
        input()
        browser.close()

    result = ActionPipeline().run(f"browser-{started}", [RawEvent(**event) for event in events])
    output.write_text(to_markdown(result, url), encoding="utf-8")
    print(f"Saved {len(result['steps'])} step(s) to {output}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Record browser actions to Markdown test steps")
    parser.add_argument("url")
    parser.add_argument("-o", "--output", type=Path, default=Path("recorded-steps.md"))
    args = parser.parse_args()
    record(args.url, args.output)


if __name__ == "__main__":
    main()
