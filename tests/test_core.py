from calculator import add, subtract, divide

import pytest


def test_add():
    assert add(2, 3) == 5


def test_add_zero():
    assert add(0, 0) == 0


def test_add_negatives():
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 3) == 2


def test_divide():
    assert divide(6, 3) == 2.0


def test_divide_float_result():
    assert divide(7, 2) == 3.5


def test_divide_negatives():
    assert divide(-6, 3) == -2.0
    assert divide(6, -3) == -2.0
    assert divide(-6, -3) == 2.0


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)
