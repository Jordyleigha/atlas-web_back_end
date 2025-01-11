#!usr/bin/env python3

"""take float multiplier as arg and returns a function that multiplies a float
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiply(value: float) -> float:
        return value * multiplier

    """higher-order function to get the result of multiple args or returns

    Args:
    multiplier: a float

    Returns: a function that takes a float and returns a float
    """

    return multiply
