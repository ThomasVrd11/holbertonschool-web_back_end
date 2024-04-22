#!/usr/bin/env python3

"""
Returns a list of tuples containing elements and their lengths
"""

from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """Returns a list of tuples containing elements and their lengths.

    Args:
        lst (List[str]): The input list of strings.

    Returns:
        A list of tuples.
    """
    return [(i, len(i)) for i in lst]
