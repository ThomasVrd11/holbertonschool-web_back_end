#!/usr/bin/env python3
"""class to handle simple pagination"""
import csv
import math
from typing import Tuple, List, Dict, Optional


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return start index and end index"""
    start_index = (page - 1) * page_size
    end_index = page * page_size
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
        """ return the appropriate page of the dataset"""
        assert isinstance(page, int) and page > 0, (
            "page must be an integers greater than 0")
        assert isinstance(page_size, int) and page_size > 0, (
            "page_size must be an integers greater than 0")
        indexRange = index_range(page, page_size)
        self.dataset()

        if indexRange[0] >= len(self.__dataset):
            return []
        else:
            return self.__dataset[indexRange[0]:indexRange[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10
                  ) -> Dict[str, Optional[int]]:
        """
        returns a dictionary containing the following key-value pairs:
            page_size: the length of the returned dataset page
            page: the current page number
            data: the dataset page (equivalent to return from previous task)
            next_page: number of the next page, None if no next page
            prev_page: number of the previous page, None if no previous page
            total_pages: the total number of pages in the dataset as an integer
        """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
