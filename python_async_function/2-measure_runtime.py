#!/usr/bin/env python3
"""
measure_time function example code
"""

import asyncio
import time

# Import the wait_n function from the 1-concurrent_coroutines module
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:

    """
    Measure the average time taken per call for the wait_n function.

    :param n: Number of tasks to create.
    :param max_delay: Maximum delay for each task.
    :return: Average time taken per call.
    """

    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    average_time_per_call = total_time / n

    return average_time_per_call


if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
