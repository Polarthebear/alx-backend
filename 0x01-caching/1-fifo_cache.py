#!/usr/bin/env python3
"""
FIFOCache that is a caching systems
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    Class inherits from BaseCaching
    """

    def __init__(self):
        """
        Initialize method
        """
        super().__init__()
        self.key_indexes = []

    def put(self, key, item):
        """
        Assign dictionary, item value for key.
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                return

            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                item_discarded = self.key_indexes.pop(0)
                del self.cache_data[item_discarded]
                print("DISCARD:", item_discarded)

            self.cache_data[key] = item
            self.key_indexes.append(key)

    def get(self, key):
        """
        Return value linked to key.
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
