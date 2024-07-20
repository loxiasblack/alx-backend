#!/usr/bin/env python3
"""simple pagination"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """ index range function"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


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
        """implement get_page function"""
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        start, end = index_range(page, page_size)
        pages = []
        if start >= len(self.dataset()):
            return pages
        pages = self.dataset()
        return pages[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """return dictionary with all dataset"""
        all_data = self.dataset()
        data = self.get_page(page, page_size)
        next_page = page + 1
        start, end = index_range(next_page, page_size)
        if start >= len(all_data):
            next_page = None
        prev_page = page - 1
        if prev_page == 0:
            prev_page = None
        total_pages = math.floor(len(all_data) / page_size)

        return {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
