#!/usr/bin/env python3
""" 0. Basic dictionary"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """class BasicCache"""

    def put(self, key, item):
        """ put function """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ get function """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
