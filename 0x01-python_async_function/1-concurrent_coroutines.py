#!/user/bin/env python3
"""
Executing multiple coroutines with async
"""

from typing import List
import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Return a list of all delays"""
    delay_list: List[float] = []
    for i in range(0, n):
        delay: float = wait_random(max_delay)
        delay_list.append(delay)
    return [await delay for delay in asyncio.as_completed(delay_list)]
