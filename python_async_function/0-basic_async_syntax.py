#!/usr/bin/env python3
""" asynchronous routines in Python """

import asyncio
import random

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> float:
    """ asynchronous routine that takes in two arguments """
    ChongGoat = [wait_random(max_delay) for i in range(n)]
    return [await delay for delay in asyncio.as_completed(ChongGoat)]
