from datetime import date
from typing import List

from order import Order, Status


class User:
    def __init__(self, name: str, email: str, avatar_url: str, birthdate: date):
        self.name = name
        self.email = email
        self.avatar_url = avatar_url
        self.birthdate = birthdate
        self.orders: List[Order] = []

    def age(self) -> int:
        today = date.today()
        return (
            today.year
            - self.birthdate.year
            - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
        )

    def add_order(self, order: Order):
        self.orders.append(order)

    def total_spent(self) -> float:
        return sum(order.total() for order in self.orders)

    def has_pending_orders(self) -> bool:
        return any(order.status == Status.PENDING for order in self.orders)
