#!/usr/bin/env python3
"""Script containing the task_wait_random function."""
import asyncio
from typing import Any
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returns an asyncio.Task that runs the wait_random coroutine."""
    cls_type = asyncio.create_task(wait_random(max_delay))
    return cls_type
