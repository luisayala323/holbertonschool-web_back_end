#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Retrieve and cache the dataset, excluding the header.

        Returns:
            List[List]: The cached dataset.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Exclude the header

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Create and cache an indexed version of the dataset.

        Returns:
            Dict[int, List]: The cached indexed dataset.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieve a page of data based on the given index and page size.
        """

        result_dataset = []
        index_data = self.indexed_dataset()
        keys_list = list(index_data.keys())

        # Ensure the index and index + page_size are within bounds
        assert index + page_size < len(keys_list)
        assert index < len(keys_list)

        if index not in index_data:
            start_index = keys_list[index]
        else:
            start_index = index

        for i in range(start_index, start_index + page_size):
            if i not in index_data:
                result_dataset.append(index_data[keys_list[i]])
            else:
                result_dataset.append(index_data[i])

        next_index: int = index + page_size

        if index in keys_list:
            next_index
        else:
            next_index = keys_list[next_index]

        hyper_dict = {
            'index': index,
            'next_index': next_index,
            'page_size': len(result_dataset),
            'data': result_dataset
        }

        return hyper_dict
