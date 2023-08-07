#!/usr/bin/env python3
"""
The measure time module
"""

from time import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the total execution time"""
    start_time: float = time()
    asyncio.run(wait_n(n, max_delay))
    end_time: float = time()
    total_time: float = end_time - start_time
    return total_time / n
