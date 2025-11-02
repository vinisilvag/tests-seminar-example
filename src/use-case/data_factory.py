from datetime import date
from random import randint, uniform

from faker import Faker
from order import Order
from user import User

fake = Faker()


def make_fake_item() -> tuple[str, float, int]:
    name = fake.word().capitalize()
    price = round(uniform(10, 2000), 2)
    quantity = randint(1, 5)
    return (name, price, quantity)


def make_fake_order(num_items: int = 3) -> Order:
    items = [make_fake_item() for _ in range(num_items)]
    return Order(items)


def make_fake_user(num_orders: int = 2) -> User:
    name = fake.name()
    email = fake.email()
    avatar_url = fake.image_url()
    birth_year = date.today().year - randint(18, 70)
    birthdate = date(birth_year, randint(1, 12), randint(1, 28))
    user = User(name, email, avatar_url, birthdate)

    for _ in range(num_orders):
        order = make_fake_order(randint(1, 5))
        user.add_order(order)

    return user
