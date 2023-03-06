from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "phone",
        "country",
        "is_auto_generated",
        "created_at",
        "modified_at",
    )
    list_filter = (
        "country",
        "is_auto_generated",

    )


class ContactInline(admin.TabularInline):
    model = models.Contact


@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "created_at",
        "modified_at",
    )

    inlines = (ContactInline,)
