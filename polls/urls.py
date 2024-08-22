from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("/api/polls", views.index, name="index"),

    # "URLS" => "  /polls
]

# "URLS" => "  /polls
# "URLS" => "  /polls/api/polls
#