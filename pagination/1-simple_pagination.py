#!/usr/bin/env python3
"""class to handle simple pagination"""
import csv
import math
from typing import Tuple, List


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
