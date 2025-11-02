from data_factory import make_fake_user


def test_user_total_spent_and_pending_orders():
    user = make_fake_user(num_orders=3)
    total = user.total_spent()

    assert total > 0
    assert user.has_pending_orders()

    for o in user.orders:
        o.mark_as_paid()
    assert not user.has_pending_orders()


def test_order_with_expensive_item():
    user = make_fake_user()
    user.orders[0].items.append(("Super Laptop", 6000.0, 1))

    assert user.orders[0].has_expensive_item(5000.0)
