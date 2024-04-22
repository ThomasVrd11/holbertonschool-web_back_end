#!/usr/bin/env python3
""" Arthur from holberton beautiful face angelic voice"""

import random
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Coroutine"""
    random_numbers = [beaudonnel async for beaudonnel in async_generator()]
    return random_numbers
