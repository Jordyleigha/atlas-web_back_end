#!/usr/bin/env python3
"""wtask_wait_random that takes an integer max_delay
and returns a asyncio.Task."""
import asyncio
import importlib
from typing import List


basic_async_syntax = importlib.import_module('0-basic_async_syntax')
wait_random = basic_async_syntax.wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """task_wait_random that takes an integer max_delay
    and returns a asyncio.Task"""
    return asyncio.create_task(wait_random(max_delay))