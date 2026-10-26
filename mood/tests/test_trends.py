from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from mood.models import MoodEntry
from mood.trends import build_week_trend


class TrendTests(TestCase):
    def _add_votes(self, day, scores):
        for index, score in enumerate(scores):
            MoodEntry.objects.create(
                day=day, score=score,
                daily_voter_hash=f"{day.isoformat()}-{index}".ljust(64, "x"),
            )

    def test_fewer_than_five_votes_do_not_expose_average(self):
        self._add_votes(timezone.localdate(), [1, 1, 1, 1])
        trend = build_week_trend()
        self.assertIsNone(trend["points"][-1]["average"])
        self.assertIsNone(trend["points"][-1]["count"])
        self.assertEqual(trend["visible_votes"], 0)
        self.assertIsNone(trend["average_score"])

    def test_five_votes_show_average_and_count(self):
        self._add_votes(timezone.localdate(), [4, 4, 4, 4, 5])
        trend = build_week_trend()
        self.assertEqual(trend["points"][-1]["average"], 4.2)
        self.assertEqual(trend["points"][-1]["count"], 5)
        self.assertEqual(trend["visible_votes"], 5)
        self.assertEqual(trend["average_score"], 4.2)

    def test_old_votes_are_excluded(self):
        today = timezone.localdate()
        self._add_votes(today - timedelta(days=7), [5] * 6)
        self.assertEqual(build_week_trend()["visible_votes"], 0)

    def test_weekly_average_is_vote_weighted(self):
        today = timezone.localdate()
        self._add_votes(today, [5] * 10)
        self._add_votes(today - timedelta(days=1), [1] * 5)
        self.assertEqual(build_week_trend(today)["average_score"], 3.67)

    def test_response_contains_chart_and_accessible_table(self):
        self._add_votes(timezone.localdate(), [4] * 5)
        response = self.client.get("/")
        self.assertContains(response, 'id="trend-data"')
        self.assertContains(response, "Barrierefreie Wochenübersicht")
        self.assertEqual(response.context["trend"]["points"][-1]["average"], 4.0)

    def test_empty_week_is_safe(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(response.context["trend"]["average_score"])
        self.assertEqual(len(response.context["trend"]["points"]), 7)
