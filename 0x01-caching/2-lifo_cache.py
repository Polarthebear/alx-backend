#!/usr/bin/env python3
"""
FIFOCache that is a caching systems
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        self.key_indexes = []

    def put(self, key, item):
        """
        Func must assign to dictionary the item value for the key
        """
        if key and item:
            if key in self.cache_data:
                # Update key order if key already exists
                self.key_indexes.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                # Remove the last recently added item in LIFO order
                last_key = self.key_indexes.pop()
                del self.cache_data[last_key]
                print("DISCARD:", last_key)

            self.cache_data[key] = item
            self.key_indexes.append(key)

    def get(self, key):
        """
        Return value in self.cache_data linked to key
        """
        return self.cache_data.get(key)
