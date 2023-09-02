#!/usr/bin/env python3
"""Script for an asynchronous generator coroutine"""

import asyncio
import random
from typing import Generator


# Define an asynchronous generator coroutine

async def async_generator() -> Generator[float, None, None]:
    """Generator of random numbers with delays"""
    for _ in range(10):
        # Asynchronously wait for 1 second
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
