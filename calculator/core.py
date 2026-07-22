"""Core calculator functions."""


def add(a, b):
    """Return a + b."""
    return a + b


def subtract(a, b):
    """Return a - b."""
    return a - b


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
