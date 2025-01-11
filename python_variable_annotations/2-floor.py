#!/usr/bin/env python3

""" a type annotated function floor that takes a float arg and returns floor.
"""


import math


def floor(n: float) -> int:

    """function floor that takes float arg and returns floor.
    Args:
    n (float): parameter of type float

    Returns: int (the floor value of n)

    """

    return math.floor(n)
