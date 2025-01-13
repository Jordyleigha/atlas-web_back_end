#!/usr/bin/env python3
""" measure_runtime coroutine measures the runtime of async_comprehension"""
import importlib
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measure_runtime coroutine measures the runtime of async_comprehension
    """
    start = time.time()
    await asyncio.gather(async_comprehension())
    end = time.time()
    return end - start