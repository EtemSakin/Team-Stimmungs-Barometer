from django.urls import path

from mood import views

urlpatterns = [
    path("", views.home, name="home"),
    path("vote/", views.vote, name="vote"),
]
