#!/usr/bin/env python3
"""
Async coroutine that yields random numbers in range 10
"""

import asyncio
import random
from typing import Iterator


async def async_generator() -> Iterator[float]:
    """return a list of random numbers between 1 and 10"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
