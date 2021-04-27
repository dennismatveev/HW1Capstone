import main
import pytest


def test_calculate_total():
    state = "NH"
    shopping_cart = [main.merchandise('banana', 1.00, 'Other')]
    assert round(main.calculate_total(state, shopping_cart), 2) == 1.00

    state = "MA"
    shopping_cart = [main.merchandise('banana', 1.00, 'Other')]
    assert round(main.calculate_total(state, shopping_cart), 2) == 1.06
    shopping_cart = [main.merchandise('Cereal', 4.49, 'WIC')]
    assert round(main.calculate_total(state, shopping_cart), 2) == 4.49

    state = "ME"
    shopping_cart = [main.merchandise('Jacket', 599.99, 'Clothing')]
    assert round(main.calculate_total(state, shopping_cart), 2) == 623.36
    shopping_cart = [main.merchandise('Snowboard', 175.99, "Other"), main.merchandise('Coat', 299.99, 'Clothing')]
    assert round(main.calculate_total(state, shopping_cart), 2) == 502.21

    with pytest.raises(AssertionError):
        state = "NH"
        shopping_cart = [main.merchandise('banana', -1.00, 'Other')]
        assert round(main.calculate_total(state, shopping_cart), 2) == 1.00

    with pytest.raises(UnboundLocalError):
        state = "WI"
        shopping_cart = [main.merchandise('banana', 1.00, 'Other')]
        assert round(main.calculate_total(state, shopping_cart), 2) == 1.00

    with pytest.raises(AssertionError):
        state = "MA"
        shopping_cart = [main.merchandise('banana', 1.00, 'IDK')]
        assert round(main.calculate_total(state, shopping_cart), 2) == 1.00

    with pytest.raises(AssertionError):
        state = "MA"
        shopping_cart = []
        assert round(main.calculate_total(state, shopping_cart), 2) == 1.00
