#!/usr/bin/env python3
"""Type-annotated function sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of the list of floats and integers."""
    return sum(mxd_lst)
