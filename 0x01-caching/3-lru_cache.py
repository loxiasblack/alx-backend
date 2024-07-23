#!/usr/bin/env python3
""" 3. LRU Caching """
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache class """
    def __init__(self):
        """ instantiation """
        super().__init__()

    def put(self, key, item):
        """ put function """
        if key is None or item is None:
            return None
        if key in self.cache_data.keys():
            del self.cache_data[key]
            self.cache_data[key] = item
        if key not in self.cache_data.keys():
            self.cache_data[key] = item
        if len(self.cache_data.keys()) > BaseCaching.MAX_ITEMS:
            key_to_delete = list(self.cache_data.keys())[0]
            del self.cache_data[key_to_delete]
            print("DISCARD: {}".format(key_to_delete))

    def get(self, key):
        """ get function """
        item = self.cache_data.get(key)
        self.put(key, item)
        return item
