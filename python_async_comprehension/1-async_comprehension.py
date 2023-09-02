#!/usr/bin/env python3
"""Async comprehension coroutine"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collects ten random numbers in  a list and returns"""
    return ([i async for i in async_generator()])
