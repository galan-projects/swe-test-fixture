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
