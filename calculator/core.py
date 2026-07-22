"""Core calculator functions."""


def add(a, b):
    """Return a + b."""
    return a + b


def subtract(a, b):
    """Return a - b."""
    return a - b


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
