#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Retrieve a hypermedia representation of a specific index of data.

        Args:
            index (int, optional): The starting index to retrieve data from.
                               Defaults to None, which will start from index 0.
        page_size (int): The number of items to retrieve. Defaults to 10.

        Returns:
            Dict: A dictionary containing pagination information, including:
            - "index": The starting index for the current page.
            - "next_index": The index for the next page if it exists.
            - "page_size": The number of items per page.
            - "total_items": The total number of items in the dataset.
            - "data": A list of items for the specified index range."""
        assert 0 <= len(self.__indexed_dataset)
        total_items = len(self.__indexed_dataset)
        index = index if index is not None else 0
        next_index = min(index + page_size, total_items)
        data = list(self.__indexed_dataset.values())[index:next_index]
        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "total_items": total_items,
            "data": data,
        }
