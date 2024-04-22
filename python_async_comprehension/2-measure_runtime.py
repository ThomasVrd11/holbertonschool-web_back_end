#!/usr/bin/env python3
""" beau gosse eduardo """
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """one piece < naruto """
    Luffy = asyncio.get_event_loop().time()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    end = asyncio.get_event_loop().time()
    return end - Luffy
