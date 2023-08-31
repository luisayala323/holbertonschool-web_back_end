#!/usr/bin/env python3
"""
Asynchronous coroutine named: wait_random.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    wait_random that waits for a random delay between
    0 and max_delay (included and float value) seconds
    and eventually returns it.
    """
    actual_delay = random.uniform(0, max_delay)
    await asyncio.sleep(actual_delay)
    return actual_delay

if __name__ == "__main__":
    import asyncio

    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))
