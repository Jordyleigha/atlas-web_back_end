#!/usr/bin/env python3
"""a simple function that takes two ints args and returns the tuple
of size two containg a start and end index"""

import csv
import math
from typing import List, Tuple


def index_range(page, page_size):
    """return a tuple of start and end index for pagination

    args:
    page(int): current page number (1-indexed)
    page_size(int): number of items per page

    returns:
    tuple: tuple containing the start index and end index
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieve a specific page of data from the dataset.

    Args:
        page (int): The page number to retrieve (1-indexed). Defaults to 1.
        page_size (int): The number of items per page. Defaults to 10.

    Returns:
        List[List]: A list containing the items for the specified page.
                     If the start index is beyond the length of the dataset,
                     an empty list is returned"""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)
        if start_index >= len(dataset):
            return []
        return dataset[start_index:end_index]
