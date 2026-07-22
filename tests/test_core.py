from calculator import add, divide, multiply, subtract
||||||| parent of 4164bb1 (feat: add multiply() to calculator)
from calculator import add, subtract
from calculator import add, subtract, multiply


def test_add():
    assert add(2, 3) == 5


def test_add_zero():
    assert add(0, 0) == 0


def test_add_negatives():
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(2, 3) == 6


def test_multiply_zero():
    assert multiply(0, 5) == 0


def test_multiply_negatives():
    assert multiply(-1, 4) == -4


def test_divide():
    assert divide(6, 3) == 2.0


def test_divide_negatives():
    assert divide(-6, 3) == -2.0


def test_divide_by_zero():
    import pytest

    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(1, 0)
||||||| parent of 4164bb1 (feat: add multiply() to calculator)


def test_multiply():
    assert multiply(2, 3) == 6


def test_multiply_zero():
    assert multiply(0, 5) == 0


def test_multiply_negative():
    assert multiply(-1, 4) == -4
