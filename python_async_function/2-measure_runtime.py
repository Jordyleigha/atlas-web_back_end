#!/usr/bin/env python3
"""measures total execution time for wait_n(n, max_delay)
and returns total_time/n"""

import importlib
from typing import List
import time
import asyncio


concurrent_coroutines = importlib.import_module('1-concurrent_coroutines')
wait_n = concurrent_coroutines.wait_n


async def measure_time_async(n: int, max_delay: int) -> float:

    """measures average time to execute a concurrent tasks
    """
    start_time = time.time()
    await wait_n(n, max_delay)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n


def measure_time(n: int, max_delay: int) -> float:
    """measures average time to execute a concurrent tasks"""
    return asyncio.run(measure_time_async(n, max_delay))
