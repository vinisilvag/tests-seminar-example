import pytest
from faker import Faker


@pytest.fixture()
def fake():
    fake = Faker(["pt_BR"])
    # fake.seed_instance(42)
    return fake
