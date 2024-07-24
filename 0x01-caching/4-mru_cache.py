#!/usr/bin/env python3
""" 4. MRU Caching """
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ class MRUCache """
    def __init__(self):
        """ inherit the instantiation """
        super().__init__()

    def put(self, key, item):
        """ put function to the cache """
        if key is None or item is None:
            return
        if key not in self.cache_data.keys():
            self.cache_data[key] = item
        if key in self.cache_data.keys():
            del self.cache_data[key]
            self.cache_data[key] = item
        if len(self.cache_data.keys()) > BaseCaching.MAX_ITEMS:
            len_of_keys = len(self.cache_data.keys())
            key_to_delete = list(self.cache_data.keys())[len_of_keys - 2]
            del self.cache_data[key_to_delete]
            print("DISCARD: {}".format(key_to_delete))

    def get(self, key):
        """ get the item with key """
        if key is None or key not in self.cache_data.keys():
            return None
        item = self.cache_data.get(key)
        self.put(key, item)
        return item
