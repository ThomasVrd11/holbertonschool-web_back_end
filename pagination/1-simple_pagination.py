#!/usr/bin/env python3
""" simple pagination"""

import csv
import math
from typing import List, Tuple


def index_range(page, page_size):
    """ zerooooooooo"""
    end = page * page_size
    start = end - page_size
    return (start, end)


class Server:
    """ pagination """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """pagination"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                read = csv.reader(f)
                dataset = [row for row in read]
            self.__dataset = dataset[1:]
            return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """pagination"""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        self.database()
        start, end = index_range(page, page_size)
        if start >= len(self.__dataset):
            return []
        return self.__dataset[start:min(end, len(self.__dataset))]
