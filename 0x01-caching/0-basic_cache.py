#!/usr/bin/env python3
"""
Basic Cache class that is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Object representation that will allow storing
    & retrieve items from dictionary"""
    def put(self, key, item):
        """Add item to cache."""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve item by key."""
        return self.cache_data.get(key, None)
