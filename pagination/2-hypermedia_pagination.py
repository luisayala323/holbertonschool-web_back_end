#!/usr/bin/env python3
"""Script that implements the get_hyper method that takes
the same arguments as get_page and returns a dictionary"""
import csv
from typing import List, Tuple, Dict
from math import ceil


class Server:
    """Class to paginate the database"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Method to retrieve a page of data"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        range: Tuple = self.index_range(page, page_size)
        pagination: List = self.dataset()

        return pagination[range[0]:range[1]]

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """Return a tuple representing the start and
        end index for pagination
        """
        end: int = page * page_size
        start: int = end - page_size

        return start, end

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Retrieve data for hypermedia pagination and
        return it as a dictionary
    """

        data = []
        try:
            data = self.get_page(page, page_size)
        except AssertionError:
            return {}  # Return an empty dictionary for invalid inputs

        dataset: List = self.dataset()
        total_pages: int = len(dataset) if dataset else 0
        total_pages = ceil(total_pages / page_size)
        prev_page: int = (page - 1) if (page - 1) >= 1 else None
        next_page: int = (page + 1) if (page + 1) <= total_pages else None

        hypermedia: Dict = {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages,
        }

        return hypermedia
