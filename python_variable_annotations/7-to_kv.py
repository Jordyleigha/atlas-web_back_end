#!/usr/bin/env python3

"""taking a str int and/or float and return as a tuple
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:

    """function name: to_kv

    Args:
    k: a string
    v: an integer or float

    returns: a tuple containing a string and a float
    """

    return (k, float(v ** 2))
