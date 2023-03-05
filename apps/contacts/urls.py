from django.urls import path
from . import views
from django.urls import include


app_name = "contacts"

urlpatterns = [
    path(
        "contact/",
        include(
            [

                path("list/", views.list_contacts, name="list"),
                path("contacts-create/", views.ContactCreateView.as_view(), name="create"),
                path("contacts-update/<int:pk>/", views.ContactUpdateView.as_view(), name="update"),
                path("contactsdelete/<int:pk>/", views.ContactDeleteView.as_view(), name="delete"),
                path("details/<int:pk>/", views.ContactDetailView.as_view(), name="details"),
            ]
        )
    )
]
