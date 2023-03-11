from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.urls import reverse_lazy
from apps.contacts.models import Contact


def list_contacts(request):
    return render(
        request=request,
        template_name="contacts/contacts_list.html",
        context={
            "contacts": Contact.objects.all(),
        },
    )


class ContactCreateView(CreateView):
    model = Contact
    fields = (
        "name",
        "phone",
        "avatar",
        "country",
    )
    success_url = reverse_lazy("contacts:list")


class ContactUpdateView(UpdateView):
    model = Contact
    fields = (
        "id",
        "name",
        "phone",
        "avatar",
        "country",
    )
    success_url = reverse_lazy("contacts:list")


class ContactDeleteView(DeleteView):
    model = Contact
    success_url = reverse_lazy("contacts:list")


class ContactDetailView(DetailView):
    model = Contact
    pk_url_kwarg = "pk"
