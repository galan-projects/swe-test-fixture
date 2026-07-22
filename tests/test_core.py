from calculator import add, subtract, power


def test_add():
    assert add(2, 3) == 5


def test_add_zero():
    assert add(0, 0) == 0


def test_add_negatives():
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 3) == 2


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
