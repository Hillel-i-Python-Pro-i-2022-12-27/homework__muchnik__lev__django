from django.urls import path
from . import views
from django.urls import include

app_name = "contacts"

urlpatterns = [
    path(
        "contacts/",
        include(
            [
                path("list/", views.list_contacts, name="list"),
            ]
        ),
    ),
]