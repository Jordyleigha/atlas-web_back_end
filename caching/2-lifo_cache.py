#!/usr/bin/env python3
"""inherits from BaseCaching and uses a LIFO system"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """when the cache hits max size it will discard the most recent added
    item"""

    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        """adds an item to the cache
        args:
        key (_type_): key to associate with item
        item (_type_): value to store into the cache"""

        if key is not None and item is not None:
            if key in self.cache_data:
                return
            if key not in self.cache_data:
                self.order.append(key)
                self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last_key = self.order.pop(-2)
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")

    def get(self, key):
        """gets item from cache from given key
        args:
        key: key of item from cache

        returns:
        any: value with key if in cache or None if not found"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
