#!/usr/bin/env python3

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
