from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = "contacts"

urlpatterns = [

    path("contacts-list/", views.list_contacts, name="list"),
    path("contacts-create/", login_required(views.ContactCreateView.as_view()), name="create"),
    path("contacts-update/<int:pk>/", login_required(views.ContactUpdateView.as_view()), name="update"),
    path("contacts-delete/<int:pk>/", login_required(views.ContactDeleteView.as_view()), name="delete"),
    path("contacts-details/<int:pk>/", views.ContactDetailView.as_view(), name="details"),
]
