#!/usr/bin/env python3
"""Script that takes two integers args page and page_size"""
from typing import Tuple


def index_range(page, page_size):
    """
    Return a tuple of size two.
    """
    # Calculate the start and end indexes based on the page and page size
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
