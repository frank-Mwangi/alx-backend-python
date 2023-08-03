#!/usr/bin/env python3
"""
Summation of a mixed list of ints and floats
"""

from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Summation of mixed data types"""
    sum: float = 0.0
    for num in mxd_lst:
        sum += num
    return sum
