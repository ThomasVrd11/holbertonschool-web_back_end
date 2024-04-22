#!/usr/bin/env python3
""" The task_wait_n function was created with the specified prototype."""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ spawn task_wait_random n times with the specified max_delay"""
    listounette = []
    for i in range(n):
        listounette.append(task_wait_random(max_delay))
    sor = await asyncio.gather(*listounette)
    return sorted(sor)
