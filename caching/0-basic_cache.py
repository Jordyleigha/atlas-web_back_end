#!/bin/usr/env python3
""" class BasicCache inherits from BaseCaching and it a caching system"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ simple caching system that doesnt have a size limit
    attrs:
    cache_data(dict): the underlying in parent class dict storing
    cached items"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ adds an item to the cache
        args:
        key (_type_): key to associate with item
        item (_type_): value to store into the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ gets the item from the cache

        args:
        key (_type_): key of the item to get

        returns:
        any: value associated with the key or None if not found
        """
        return self.cache_data.get(key)
