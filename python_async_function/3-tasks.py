#!/usr/bin/env python3
""" task_wait_n """

import asyncio

wait_n = __import__('0-basic_async_syntax').wait_random

def task_wait_n(n: int, max_delay: int) -> asyncio.Task:
    """ return a asyncio.Task """
    return asyncio.create_task(wait_n(n, max_delay))
