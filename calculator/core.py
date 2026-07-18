"""Core calculator functions. NOTE: add() has a deliberate bug (issue #2)."""


def add(a, b):
    """Return a + b.

    BUG: currently returns a * b instead of a + b. See issue #2.
    """
    return a * b  # BUG: should be a + b


def subtract(a, b):
    """Return a - b."""
    return a - b
