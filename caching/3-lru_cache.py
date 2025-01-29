#!/usr/bin/env python3
"""inherits from BaseCaching and uses a LRU system"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """when cache reaches max size it discards the most recent added item"""

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
                self.order.remove(key)
            self.cache_data[key] = item
            self.order.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                least_key = self.order.pop(0)
                del self.cache_data[least_key]
                print(f"DISCARD: {least_key}")

    def get(self, key):
        """gets item from cache from given key
        args:
        key: key of item from cache

        returns:
        any: value with key if in cache or None if not found"""
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
