#!/usr/bin/env python3
"""
Function that returns values with the appropriate types
"""

from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Calculate length of each sequence in an iterable"""
    return [(i, len(i)) for i in lst]
