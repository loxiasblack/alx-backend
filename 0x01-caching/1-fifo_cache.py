#!/usr/bin/env python3
""" 1. FIFO caching """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class """
    def __init__(self):
        """ instantiation """
        super().__init__()

    def put(self, key, item):
        """ put function """
        if key is None or item is None:
            return
        if key not in self.cache_data.keys():
            self.cache_data[key] = item
        if key in self.cache_data.keys():
            del self.cache_data[key]
            self.cache_data[key] = item
        if len(list(self.cache_data.keys())) > BaseCaching.MAX_ITEMS:
            key_to_delete = list(self.cache_data.keys())[0]
            del self.cache_data[key_to_delete]
            print("DISCARD: {}".format(key_to_delete))

    def get(self, key):
        """ get function """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
