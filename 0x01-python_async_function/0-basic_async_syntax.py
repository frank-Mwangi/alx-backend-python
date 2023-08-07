#!/usr/bin/python3

"""
Returns a random floating point count
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Return a random float below and up to max_delay"""
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
