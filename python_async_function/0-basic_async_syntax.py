#!/usr/bin/env python3
""" asynchronous routines in Python """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ ça me fait chier de commenter """
    NicolasTaillepierre = random.uniform(0, max_delay)
    await asyncio.sleep(NicolasTaillepierre)
    return NicolasTaillepierre
