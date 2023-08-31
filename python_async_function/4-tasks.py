#!/usr/bin/env python3
"""Return a list of all the delays"""

import asyncio
from typing import List

# Import the task_wait_random function from the 3-tasks module
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Simulate asynchronous waiting for random durations using tasks.

    :param n: Number of tasks to create.
    :param max_delay: Maximum delay for each task.
    :return: List of delays in the order of completion.
    """
    delay_list: List[float] = []
    tasks: List[asyncio.Task] = []

    # Create n asynchronous tasks
    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    # Await tasks as they complete and store the delays
    for task in asyncio.as_completed(tasks):
        delay = await task
        delay_list.append(delay)

    return delay_list

if __name__ == "__main__":
    # Example usage: Run the task_wait_n function and print the result
    n = 5
    max_delay = 9
    result = asyncio.run(task_wait_n(n, max_delay))
    print(result)
