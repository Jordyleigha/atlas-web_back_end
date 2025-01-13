#!/usr/bin/env python3
""" wait_random waits for a random amount of time then returns delayed time
"""

import asyncio
import random
from typing import List


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """wait for random delay between 0 and 10

    Args:
        max_delay (int, optional): Defaults to 10.

    Returns: float: delay seconds waited
    """
    delays = []
    for _ in range(n):
        delay = random.uniform(0, max_delay)
        await asyncio.sleep(delay)
        delays.append(delay)
    return sorted(delays)
