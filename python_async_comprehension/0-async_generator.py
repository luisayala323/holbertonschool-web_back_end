#!/usr/bin/env python3
"""Script for an asynchronous generator coroutine"""

import asyncio
import random
from typing import AsyncGenerator


# Define an asynchronous generator coroutine
async def async_generator() -> AsyncGenerator[float, None]:
    """Generator of random numbers with delays"""

    # Generate random numbers asynchronously in a loop
    for _ in range(10):
        # Asynchronously wait for 1 second
        await asyncio.sleep(1)

        # Yield a random float between 0 and 10
        yield random.uniform(0, 10)
