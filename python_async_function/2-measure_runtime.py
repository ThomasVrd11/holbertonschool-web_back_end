#!/usr/bin/env python3
"""function with integers n and max_delay as arguments"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """return the total time divided by n"""
    superman = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    batman = time.perf_counter()
    total_time = batman - superman
    return total_time / n
