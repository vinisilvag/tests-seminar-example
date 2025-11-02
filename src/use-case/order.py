from enum import Enum
from typing import List, Tuple


class Status(Enum):
    PENDING = "PENDING"
    PAID = "PAID"


class Order:
    def __init__(self, items: List[Tuple[str, float, int]]):
        self.items = items
        self.status = Status.PENDING

    def total(self) -> float:
        return sum(price * qty for _, price, qty in self.items)

    def apply_discount(self, percent: float):
        if not (0 <= percent <= 100):
            raise ValueError("Percentual de desconto inválido")
        discounted = []
        for name, price, qty in self.items:
            discounted.append((name, price * (1 - percent / 100), qty))
        self.items = discounted

    def mark_as_paid(self):
        if self.status != Status.PENDING:
            raise ValueError("Pedido não pode ser pago novamente.")
        self.status = Status.PAID

    def has_expensive_item(self, threshold: float) -> bool:
        return any(price > threshold for _, price, _ in self.items)
