import unittest

from apps.action_pipeline.models import RawEvent
from apps.action_pipeline.pipeline import ActionPipeline


class ActionPipelineTest(unittest.TestCase):
    def test_orders_deduplicates_and_masks_secret(self) -> None:
        events = [
            RawEvent("2", 20, "input", {"testId": "password"}, "secret", {"field": "password"}),
            RawEvent("1", 10, "click", {"ariaLabel": "Login"}),
            RawEvent("duplicate", 20, "input", {"testId": "password"}, "secret", {"field": "password"}),
        ]
        result = ActionPipeline().run("session-1", events)
        self.assertEqual([step["type"] for step in result["steps"]], ["click", "input"])
        self.assertEqual(result["steps"][1]["value"], "[REDACTED]")

    def test_unknown_event_is_explicitly_ambiguous(self) -> None:
        result = ActionPipeline().run("session-2", [RawEvent("1", 1, "drag", {})])
        self.assertEqual(result["steps"][0]["type"], "custom")
        self.assertTrue(result["ambiguities"])


if __name__ == "__main__":
    unittest.main()
