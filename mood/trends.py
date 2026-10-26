"""K-anonymous aggregation: days with fewer than five votes reveal no score."""
from datetime import timedelta

from django.conf import settings
from django.db.models import Avg, Count
from django.utils import timezone

from .models import MoodEntry

DAY_LABELS = ("Mo", "Di", "Mi", "Do", "Fr", "Sa", "So")


def build_week_trend(today=None):
    today = today or timezone.localdate()
    first = today - timedelta(days=6)
    aggregates = {
        row["day"]: row
        for row in MoodEntry.objects.filter(day__range=(first, today))
        .values("day")
        .annotate(count=Count("id"), average=Avg("score"))
    }
    points = []
    visible_total = 0
    weighted_sum = 0.0
    eligible_days = 0
    minimum = settings.MOOD_MIN_GROUP_SIZE
    for index in range(7):
        day = first + timedelta(days=index)
        aggregate = aggregates.get(day, {})
        actual_count = aggregate.get("count", 0)
        allowed = actual_count >= minimum
        average = round(float(aggregate["average"]), 2) if allowed else None
        if allowed:
            eligible_days += 1
            visible_total += actual_count
            weighted_sum += float(aggregate["average"]) * actual_count
        points.append({
            "label": DAY_LABELS[day.weekday()],
            "date_label": day.strftime("%d.%m."),
            "date": day.isoformat(),
            "average": average,
            "count": actual_count if allowed else None,
            "has_votes": actual_count > 0,
        })
    return {
        "points": points,
        "minimum": minimum,
        "eligible_days": eligible_days,
        "visible_votes": visible_total,
        "average_score": round(weighted_sum / visible_total, 2) if visible_total else None,
    }
