#!/usr/bin/env python3
"""
Module that return tuple from string and int/float inputs
"""

from typing import Union, List, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Tuple from string and integer/float input"""
    square: float = v * v
    return k, square
