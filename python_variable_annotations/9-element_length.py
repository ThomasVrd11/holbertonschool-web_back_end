#!/usr/bin/env python3
"""Type-annotated function element_length"""
from typing import List


def element_length(input_list: List[str]) -> List[int]:
    """Return a list of the lengths of the strings in input_list."""
    return [len(s) for s in input_list]
