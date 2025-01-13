#!/usr/bin/env python3
"""wait_n returns a list of all the delays in ascending order
because of concurrency"""
import asyncio
import importlib
from typing import List


basic_async_syntax = importlib.import_module('0-basic_async_syntax')
wait_random = basic_async_syntax.wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """asynchronously waited for multiple random delays
    and returns in ascending order

    Args:
        n (int): num of concurrent tasks
        max_delay (int): max delay value

    Returns:
        List[float]: sorted list of delays
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = [await task for task in tasks]
    return sorted(delays)
