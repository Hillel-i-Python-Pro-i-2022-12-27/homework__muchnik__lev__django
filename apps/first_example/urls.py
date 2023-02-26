from django.urls import path
from apps.first_example import views
from django.urls import include

app_name = "first_example"

urlpatterns = [
  path(
        "users",
        include(
            [
                path("", views.UsersView.as_view(), name="users"),
                path("<int:amount>", views.UsersView.as_view(), name="users"),
            ]
        ),
    ),
]