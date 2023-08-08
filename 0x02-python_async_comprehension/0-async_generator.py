#!/usr/bin/env python3
"""
Async coroutine that yields random numbers in range 10
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """return a list of random numbers between 1 and 10"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
