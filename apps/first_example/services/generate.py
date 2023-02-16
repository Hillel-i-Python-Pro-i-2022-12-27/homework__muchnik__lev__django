from typing import NamedTuple
from collections.abc import Iterator

from faker import Faker


class User(NamedTuple):
    login: str
    email: str
    password: str

    def __str__(self):
        return f"{self.login} {self.email} {self.password}"

    __repr__ = __str__


faker = Faker()


def generate_user() -> User:
    return User(login=faker.first_name(), email=faker.free_email(), password=faker.word())


def generate_users(amount: int = 10) -> Iterator[User]:
    for _ in range(amount):
        yield generate_user()