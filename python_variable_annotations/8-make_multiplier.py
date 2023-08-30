#!/usr/bin/env python3
"""Function to create a multiplier function."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Create a function that multiplies a float by a given multiplier."""
    def multiplier_function(d: float) -> float:
        return d * multiplier
    return multiplier_function
