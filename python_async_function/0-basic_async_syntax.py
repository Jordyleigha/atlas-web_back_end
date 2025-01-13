#!/usr/bin/env python3

"""wait_random waits for random amount of time thens returns delayed time
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """wait for random delay between numbers 0 and 10

    Args:
    max_delay (int, optional): defaulted to 10

    Returns: float: delay seconds waited
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
