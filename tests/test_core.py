import pytest

from calculator import add, factorial, subtract


def test_add():
    assert add(2, 3) == 5


def test_add_zero():
    assert add(0, 0) == 0


def test_add_negatives():
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 3) == 2


def test_factorial_zero():
    assert factorial(0) == 1


def test_factorial_one():
    assert factorial(1) == 1


def test_factorial_positive():
    assert factorial(5) == 120


def test_factorial_negative_raises():
    with pytest.raises(ValueError):
        factorial(-1)
