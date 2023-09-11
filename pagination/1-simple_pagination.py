#!/usr/bin/env python3
"""Pagination Script with Server Class"""
import csv
from typing import List, Tuple


class Server:
    """Server class for database pagination"""

    # Path to the dataset file
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Retrieve and cache the dataset.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Exclude the header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a specific page of data.
        """
        # Validate input arguments
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # Calculate the start and end indexes for the requested page
        start_index, end_index = index_range(page, page_size)

        # Retrieve the dataset
        pagination = self.dataset()

        # Return the requested page of data
        return pagination[start_index:end_index]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indexes for a given page and page size.
    """
    end = page * page_size
    start = end - page_size

    return start, end
