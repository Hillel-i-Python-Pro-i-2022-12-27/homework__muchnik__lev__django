from django.db import models


class Country(models.Model):

    name = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}"

    __repr__ = __str__


class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    is_auto_generated = models.BooleanField(default=False)
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name="contacts",
        default=None,
        null=True,
        blank=False,
    )

    def __str__(self) -> str:
        return f"{self.name} - {self.phone}"

    __repr__ = __str__
