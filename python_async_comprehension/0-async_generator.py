#!/usr/bin/env python3
""" fan2Audrey"""

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Coroutine"""
    for Audrey in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
