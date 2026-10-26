"""Anonymous voting: a cookie is used only to deduplicate per browser/day."""
import hashlib
import hmac
import re
import secrets

from django.conf import settings
from django.db import IntegrityError, transaction
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.http import require_GET, require_POST

from .forms import MOODS, MoodForm
from .models import MoodEntry

COOKIE_NAME = "mood_browser"
COOKIE_PATTERN = re.compile(r"^[A-Za-z0-9_-]{40,100}$")


def _token(request: HttpRequest) -> str:
    candidate = request.COOKIES.get(COOKIE_NAME, "")
    return candidate if COOKIE_PATTERN.fullmatch(candidate) else secrets.token_urlsafe(32)


def _daily_hash(day, token: str) -> str:
    data = f"mood-v1:{day.isoformat()}:{token}".encode("utf-8")
    return hmac.new(settings.SECRET_KEY.encode("utf-8"), data, hashlib.sha256).hexdigest()


def _with_cookie(response: HttpResponse, token: str) -> HttpResponse:
    response.set_cookie(
        COOKIE_NAME,
        token,
        max_age=180 * 24 * 60 * 60,
        secure=not settings.DEBUG,
        httponly=True,
        samesite="Lax",
    )
    return response


@require_GET
def home(request: HttpRequest) -> HttpResponse:
    today = timezone.localdate()
    token = _token(request)
    has_voted = MoodEntry.objects.filter(
        day=today, daily_voter_hash=_daily_hash(today, token)
    ).exists()
    context = {
        "form": MoodForm(),
        "moods": MOODS,
        "has_voted": has_voted,
        "status": request.GET.get("status", ""),
    }
    return _with_cookie(render(request, "mood/home.html", context), token)


@require_POST
def vote(request: HttpRequest) -> HttpResponse:
    form = MoodForm(request.POST)
    token = _token(request)
    if not form.is_valid():
        response = render(request, "mood/home.html", {
            "form": form,
            "moods": MOODS,
            "has_voted": False,
            "status": "invalid",
        }, status=400)
        return _with_cookie(response, token)

    today = timezone.localdate()
    daily_hash = _daily_hash(today, token)
    if MoodEntry.objects.filter(day=today, daily_voter_hash=daily_hash).exists():
        status = "already"
    else:
        try:
            with transaction.atomic():
                MoodEntry.objects.create(
                    day=today,
                    score=int(form.cleaned_data["score"]),
                    daily_voter_hash=daily_hash,
                )
            status = "thanks"
        except IntegrityError:
            status = "already"
    response = HttpResponseRedirect(reverse("home") + "?status=" + status)
    return _with_cookie(response, token)
