#!/usr/bin/env python3

from typing import Iterable, List, Tuple, Sequence

"""
Duck types
"""


def element_length(lst: Iterable[Sequence]) -> list[Tuple[Sequence, int]]:
    """Return a tuple containing a sequence and an int"""
    return [(i, len(i)) for i in lst]
