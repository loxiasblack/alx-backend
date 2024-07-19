#!/usr/bin/env python3
"""pagination function"""


def index_range(page: int, page_size: int) -> tuple:
    """function that return tupe of the first and last index item in a list"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
