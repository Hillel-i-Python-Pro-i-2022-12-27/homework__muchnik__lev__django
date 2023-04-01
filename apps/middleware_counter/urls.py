from django.urls import path

from . import views

app_name = "logger-counter"

urlpatterns = [
    path("", views.LogsListView.as_view(), name="list"),
]
