#!/usr/bin/env python3
"""Type-annotated function element_length"""
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """je comprends pas en fait pk ca passe pas"""
    return [(i, len(i)) for i in lst]
