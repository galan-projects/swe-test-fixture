from calculator import add, divide, multiply, subtract
||||||| parent of 4164bb1 (feat: add multiply() to calculator)
from calculator import add, subtract
from calculator import add, subtract, multiply
||||||| parent of 1b12a36 (feat: add power() function to calculator)
||||||| parent of 8776601 (feat: add power() function to calculator)
from calculator import add, subtract
from calculator import add, subtract, power
||||||| parent of 6ca057a (feat: add divide() to calculator)
||||||| parent of a400393 (feat: add divide() to calculator)
from calculator import add, subtract
from calculator import add, subtract, divide

import pytest
||||||| parent of 9a1cf6f (feat: add is_even() to calculator)
||||||| parent of ca2133d (feat: add is_even() to calculator)
from calculator import add, subtract
from calculator import add, subtract, is_even
||||||| parent of e8150a3 (feat: add factorial() to calculator)
||||||| parent of 8de4b8a (feat: add factorial() to calculator)
from calculator import add, subtract
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
||||||| parent of 1b12a36 (feat: add power() function to calculator)
||||||| parent of 8776601 (feat: add power() function to calculator)


def test_power():
    assert power(2, 3) == 8
    assert power(5, 2) == 25


def test_power_zero_exponent():
    assert power(5, 0) == 1
    assert power(0, 0) == 1
    assert power(-3, 0) == 1


def test_power_zero_base():
    assert power(0, 5) == 0


def test_power_negative_base():
    assert power(-2, 3) == -8
    assert power(-2, 2) == 4


def test_power_negative_exponent():
    assert power(2, -1) == 0.5
    assert power(4, -2) == 0.0625
    assert power(-2, -2) == 0.25
||||||| parent of 6ca057a (feat: add divide() to calculator)
||||||| parent of a400393 (feat: add divide() to calculator)


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
||||||| parent of 9a1cf6f (feat: add is_even() to calculator)
||||||| parent of ca2133d (feat: add is_even() to calculator)


def test_is_even_positive_even():
    assert is_even(4) is True


def test_is_even_positive_odd():
    assert is_even(3) is False


def test_is_even_zero():
    assert is_even(0) is True


def test_is_even_negative_even():
    assert is_even(-2) is True


def test_is_even_negative_odd():
    assert is_even(-3) is False
||||||| parent of e8150a3 (feat: add factorial() to calculator)
||||||| parent of 8de4b8a (feat: add factorial() to calculator)


def test_factorial_zero():
    assert factorial(0) == 1


def test_factorial_one():
    assert factorial(1) == 1


def test_factorial_positive():
    assert factorial(5) == 120


def test_factorial_negative_raises():
    with pytest.raises(ValueError):
        factorial(-1)
