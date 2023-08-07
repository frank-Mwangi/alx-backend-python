#!/usr/bin/env python3
"""
Executing multiple coroutines with async
"""

from typing import List
import asyncio

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Return a list of all delays"""
    delay_list: List[float] = []
    for i in range(0, n):
        delay: float = task_wait_random(max_delay)
        delay_list.append(delay)
    return [await delay for delay in asyncio.as_completed(delay_list)]
