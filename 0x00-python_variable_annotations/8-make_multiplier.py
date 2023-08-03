#!/usr/bin/env python3
"""
Type-annotated function that returns a function
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns function that multiplies floats"""
    def mult(num: float):
        return num * multiplier
    return mult
