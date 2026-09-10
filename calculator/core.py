"""Core calculator functions."""


def add(a, b):
    """Return a + b."""
    return a + b


def subtract(a, b):
    """Return a - b."""
    return a - b


def multiply(a, b):
    """Return a * b."""
    return a * b


def divide(a, b):
    """Return a / b as a float.

    Parameters:
        a: The numerator.
        b: The denominator.

    Returns:
        float: The result of dividing a by b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
||||||| parent of 4164bb1 (feat: add multiply() to calculator)


def multiply(a, b):
    """Return a * b."""
    return a * b
||||||| parent of 1b12a36 (feat: add power() function to calculator)
||||||| parent of 8776601 (feat: add power() function to calculator)


def power(a, b):
    """Return a raised to the power of b (a ** b).

    Args:
        a: The base.
        b: The exponent.

    Returns:
        The result of a ** b. Follows Python exponentiation semantics:
        ``a ** 0`` is 1 for any ``a``, negative exponents return floats
        (e.g. ``power(2, -1) == 0.5``), and negative bases work with
        integer exponents (e.g. ``power(-2, 3) == -8``).
    """
    return a ** b
||||||| parent of 6ca057a (feat: add divide() to calculator)
||||||| parent of a400393 (feat: add divide() to calculator)


def divide(a, b):
    """Return a / b.

    Args:
        a: The dividend.
        b: The divisor.

    Returns:
        The quotient a / b as a float.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("division by zero")
    return a / b
||||||| parent of 9a1cf6f (feat: add is_even() to calculator)
||||||| parent of ca2133d (feat: add is_even() to calculator)


def is_even(n):
    """Return True if n is even, False otherwise."""
    return n % 2 == 0
||||||| parent of e8150a3 (feat: add factorial() to calculator)
||||||| parent of 8de4b8a (feat: add factorial() to calculator)


def factorial(n):
    """Return n! (n factorial) for a non-negative integer n.

    Args:
        n: Non-negative integer.

    Returns:
        The product of all integers from 1 to n. factorial(0) is 1.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("factorial is not defined for negative integers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
