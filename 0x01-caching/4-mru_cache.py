#!/usr/bin/env python3
"""MRU caching module.
"""
from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Class MRUCache inherits from BaseCaching and is a caching system"""
    def __init__(self):
        """Initialize"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache"""
        if key is None or item is None:
            return

        # If the cache is full and key is new, remove the MRU item
        if key not in self.cache_data and len(self.cache_data)
        >= BaseCaching.MAX_ITEMS:
            mru_key, _ = self.cache_data.popitem()
            print("DISCARD:", mru_key)

        # Add/update the item and move it to the end as the most recent
        self.cache_data[key] = item
        self.cache_data.move_to_end(key)

    def get(self, key):
        """Retrieves an item by key."""
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
