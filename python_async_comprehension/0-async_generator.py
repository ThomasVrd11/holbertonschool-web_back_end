#!/usr/bin/env python3
"""Define and annotate variables with specified values."""

import random
import asyncio


async def async_generator() -> Generator[float, None, None]:
    """Coroutine"""
    for Audrey in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)