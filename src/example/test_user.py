from datetime import datetime

import pytest

from data_factory import make_user
from user import User


def test_deposit_increases_balance(fake):
    user = make_user(100.0)
    initial_balance = user.balance
    user.deposit(200.50)
    assert user.balance == pytest.approx(initial_balance + 200.50)


def test_withdraw_decreases_balance(fake):
    user = User(fake.name(), fake.email(), fake.cpf(), fake.cellphone_number())
    user.deposit(300)
    initial_balance = user.balance
    user.withdraw(100)
    assert user.balance == pytest.approx(initial_balance - 100)


def test_transfer_moves_money_between_users(fake):
    sender, receiver = (
        User(fake.name(), fake.email(), fake.cpf(), fake.cellphone_number()),
        User(fake.name(), fake.email(), fake.cpf(), fake.cellphone_number()),
    )
    sender.deposit(500)
    receiver.deposit(100)
    sender.transfer_to(receiver, 200)
    assert sender.balance == pytest.approx(300)
    assert receiver.balance == pytest.approx(300)


def test_cannot_withdraw_more_than_balance(fake):
    user = User(fake.name(), fake.email(), fake.cpf(), fake.cellphone_number())
    with pytest.raises(ValueError, match="Insufficient funds"):
        user.withdraw(user.balance + 1)


def test_transaction_history_is_ordered(fake):
    user = User(fake.name(), fake.email(), fake.cpf(), fake.cellphone_number())
    user.deposit(100)
    user.withdraw(20)
    user.deposit(50)
    history = user.transaction_history()
    assert all(isinstance(t[2], datetime) for t in history)
    assert history == sorted(history, key=lambda t: t[2], reverse=True)


def test_fake_users_have_unique_cpfs(fake):
    users = [
        User(fake.name(), fake.email(), fake.cpf(), fake.cellphone_number())
        for _ in range(50)
    ]
    cpfs = [u.cpf for u in users]
    assert len(cpfs) == len(set(cpfs))
