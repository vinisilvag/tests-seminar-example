import uuid
from datetime import datetime


class User:
    def __init__(self, name, email, cpf, phone, balance=0.0):
        self.id = uuid.uuid4()
        self.name = name
        self.email = email
        self.cpf = cpf
        self.phone = phone
        self.balance = float(balance)
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self.transactions.append(("deposit", amount, datetime.now()))

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        self.transactions.append(("withdraw", amount, datetime.now()))

    def transfer_to(self, other_user, amount):
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.withdraw(amount)
        other_user.deposit(amount)
        self.transactions.append(("transfer_out", amount, datetime.now()))
        other_user.transactions.append(("transfer_in", amount, datetime.now()))

    def transaction_history(self):
        return sorted(self.transactions, key=lambda t: t[2], reverse=True)

    def __repr__(self):
        return f"<User {self.name} ({self.cpf}) - balance: R${self.balance:.2f}>"
