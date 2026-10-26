from django.db import IntegrityError, transaction
from django.test import Client, TestCase
from django.urls import reverse
from django.utils import timezone

from mood.models import MoodEntry


class VotingTests(TestCase):
    def test_home_shows_smileys_and_sets_private_cookie(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Wie fühlst du dich")
        self.assertIn("mood_browser", response.cookies)
        self.assertTrue(response.cookies["mood_browser"]["httponly"])

    def test_user_can_vote_once_per_day(self):
        self.client.get("/")
        first = self.client.post(reverse("vote"), {"score": "4"})
        self.assertRedirects(first, "/?status=thanks")
        second = self.client.post(reverse("vote"), {"score": "2"})
        self.assertRedirects(second, "/?status=already")
        self.assertEqual(MoodEntry.objects.count(), 1)
        self.assertEqual(MoodEntry.objects.first().score, 4)
        self.assertNotContains(self.client.get("/"), "Stimmung absenden")

    def test_different_browsers_can_vote(self):
        one, two = Client(), Client()
        one.get("/")
        two.get("/")
        one.post("/vote/", {"score": "1"})
        two.post("/vote/", {"score": "5"})
        self.assertEqual(MoodEntry.objects.count(), 2)

    def test_invalid_mood_is_rejected(self):
        for value in ("0", "6", "text", ""):
            response = self.client.post("/vote/", {"score": value})
            self.assertEqual(response.status_code, 400)
        self.assertEqual(MoodEntry.objects.count(), 0)

    def test_vote_rejects_get_and_uses_csrf(self):
        self.assertEqual(self.client.get("/vote/").status_code, 405)
        csrf_client = Client(enforce_csrf_checks=True)
        self.assertEqual(csrf_client.post("/vote/", {"score": "2"}).status_code, 403)

    def test_database_uniqueness(self):
        today = timezone.localdate()
        MoodEntry.objects.create(day=today, score=2, daily_voter_hash="a" * 64)
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                MoodEntry.objects.create(day=today, score=4, daily_voter_hash="a" * 64)
