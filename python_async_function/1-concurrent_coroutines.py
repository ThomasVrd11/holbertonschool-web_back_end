#!/usr/bin/env python3
""" asynchronous routines in Python """

import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ asynchronous routine that takes in two arguments """
    listeDeSchindler = []
    for i in range(n):
        listeDeSchindler.append(await wait_random(max_delay))
    return sorted(listeDeSchindler)
