#!/usr/bin/env python3

""" taking a list of floats and integers and return their sum as a float
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:

    """taking a mixed list of ints and floats and return their sum as a float

    Args:
    mxd_lst: a list of integers and floats

    Returns: float (the sum of the numbers in the list)
    """

    return float(sum(mxd_lst))
