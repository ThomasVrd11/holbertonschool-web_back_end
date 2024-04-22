#!/usr/bin/python3
"""Type-annotated function element_length that takes a list input_list of strings as argument and returns a list of integers representing the lengths of each string in input_list."""
from typing import List

def element_length(input_list: List[str]) -> List[int]:
    """Return a list of the lengths of the strings in input_list."""
    return [len(s) for s in input_list]
