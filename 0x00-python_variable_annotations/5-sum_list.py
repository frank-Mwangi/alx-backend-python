#!/usr/bin/env python3
"""
Sum of floats
"""


def sum_list(input_list: list[float]) -> float:
    """returns sum of a list of floats"""
    sum: float = 0.0
    for num in input_list:
        sum += num
    return sum
