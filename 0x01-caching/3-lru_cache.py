#!/usr/bin/env python3
"""
LRU Caching Module
"""

from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    Class LRUCache inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        self.lru_order = OrderedDict()

    def put(self, key, item):
        """
        Assign the item value for the given key in self.cache_data.
        """
        if key and item:
            # Update or add the item in lru_order and cache_data
            self.lru_order[key] = item
            self.cache_data[key] = item
            # Move the accessed key to the end to mark it as most recently used
            self.lru_order.move_to_end(key)

            # If the cache exceeds MAX_ITEMS, remove the LRU item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                lru_key, _ = self.lru_order.popitem(last=False)
                del self.cache_data[lru_key]
                print("DISCARD:", lru_key)

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        """
        if key in self.cache_data:
            # Mark the key as recently used
            self.lru_order.move_to_end(key)
            return self.cache_data[key]
        return None
