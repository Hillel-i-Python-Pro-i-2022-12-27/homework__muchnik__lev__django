from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class RequestLog(models.Model):
    path = models.CharField(max_length=300)
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="users",
        null=True,
        blank=False,
    )
    session_id = models.CharField(max_length=100, null=True, default="Unknown session")
    counter = models.SmallIntegerField(max_length=None, null=True, default=0)
    visit_time = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.path} - {self.user}"

    __repr__ = __str__
