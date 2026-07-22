"""Core calculator functions."""


def add(a, b):
    """Return a + b."""
    return a + b


def subtract(a, b):
    """Return a - b."""
    return a - b


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
