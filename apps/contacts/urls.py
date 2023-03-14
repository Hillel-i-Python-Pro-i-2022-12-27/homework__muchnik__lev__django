from django.urls import path
from . import views


app_name = "contacts"

urlpatterns = [

    path("contacts-list/", views.list_contacts, name="list"),
    path("contacts-create/", views.ContactCreateView.as_view(), name="create"),
    path("contacts-update/<int:pk>/", views.ContactUpdateView.as_view(), name="update"),
    path("contacts-delete/<int:pk>/", views.ContactDeleteView.as_view(), name="delete"),
    path("contacts-details/<int:pk>/", views.ContactDetailView.as_view(), name="details"),

]
