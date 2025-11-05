from faker import Faker
from user import User

fake = Faker(["pt_BR"])


def make_user(balance=0.0):
    return User(fake.name(), fake.email(), fake.cpf(), fake.cellphone_number(), balance)
