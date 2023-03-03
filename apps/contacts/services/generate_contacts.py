import typing
from faker import Faker
from apps.contacts import models


def generate_contacts(amount: int = 10, is_mark_as_autogenerated: bool = False) -> typing.Iterator[models.Contact]:
    fake = Faker()
    for _ in range(amount):
        yield models.Contact(
            name=fake.name(),
            phone=fake.random_number(digits=5),
            is_auto_generated=is_mark_as_autogenerated
        )
