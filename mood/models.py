from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class MoodEntry(models.Model):
    """A vote with a day-specific pseudonym; no identity or IP is stored."""

    day = models.DateField(db_index=True)
    score = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    daily_voter_hash = models.CharField(max_length=64)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["day", "daily_voter_hash"],
                name="one_vote_per_day_and_browser",
            )
        ]
        ordering = ["-day"]

    def __str__(self):
        return f"Abstimmung vom {self.day.isoformat()}"
