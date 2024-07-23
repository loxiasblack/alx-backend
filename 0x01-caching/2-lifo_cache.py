#!/usr/bin/env python3
""" 2. LIFO Caching """


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ class LIFOCache """

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
        if len(self.cache_data.keys()) > BaseCaching.MAX_ITEMS:
            len_of_list = len(self.cache_data.keys())
            keys = list(self.cache_data.keys())[len_of_list - 2]
            del self.cache_data[keys]
            print("DISCARD: {}".format(keys))

    def get(self, key):
        """ get function """
        if key not in self.cache_data.keys() or key is None:
            return None
        return self.cache_data[key]
