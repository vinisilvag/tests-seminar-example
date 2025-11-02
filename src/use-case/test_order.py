import pytest
from data_factory import make_fake_order
from order import Status


def test_order_total_calculation():
    order = make_fake_order(num_items=5)
    manual_total = sum(price * qty for _, price, qty in order.items)

    assert abs(order.total() - manual_total) < 1e-6


def test_order_discount_application():
    order = make_fake_order()
    total_before = order.total()

    order.apply_discount(10)
    total_after = order.total()

    assert total_after <= total_before


def test_order_invalid_discount():
    order = make_fake_order()
    with pytest.raises(ValueError):
        order.apply_discount(150)


def test_order_status_transition():
    order = make_fake_order()
    order.mark_as_paid()

    assert order.status == Status.PAID

    with pytest.raises(ValueError):
        order.mark_as_paid()
