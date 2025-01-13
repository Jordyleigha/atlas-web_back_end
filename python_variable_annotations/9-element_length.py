#!/usr/bin/env python3

"""annotate the function parameters & return vaules of the type
"""


from typing import List, Tuple, Any\



def element_length(lst: List[Any]) -> List[Tuple[Any, int]]:

    """calculate the length of each element in a list.

    Args:
    lst: a list of elements of any type

    Returns: list of tuples
    """

    return [(i, len(i)) for i in lst]
