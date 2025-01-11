#!/usr/bin/env python3

""" function sum_list take input_list of float as args and returns their sum
"""


from typing import List


def sum_list(input_list: List[float]) -> float:

    """function taking a float as args and return their sum as a float

    Args:
    sum_list: function name.
    input_list (float): floats to be added together.

    Return: float (the sum of the floats in the list)
    """

    return sum(input_list)
