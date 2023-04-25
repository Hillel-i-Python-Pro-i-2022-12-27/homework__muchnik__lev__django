from django.urls import path

from . import views

app_name = "logger-counter"

urlpatterns = [
    path("", views.LogsListView.as_view(), name="list"),
    path("list-users/", views.UserListView.as_view(), name="list_user"),
    path("list-sessions/", views.SessionsListView.as_view(), name="list_sessions"),
]
