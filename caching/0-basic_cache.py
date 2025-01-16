#!/bin/usr/env python3

"""create a class that inherits from BaseCaching and is a caching system
"""


class BasicCache:
    """BasicCache defines:
    - constants of caching system
    - where the data is stored (in BaseCaching dictionary)
    """
    MAX_ITEMS = 4

    def __init__(sefl):
        """Initiliaze
        """
        self.cache_data = {}

        def print_cache(self):
            """print the cache
            """
            print("Current cache:")
            for key in sorted(self.cache_data.keys()):
                print("{}: {}" .format(key, self.cache_data.get(key)))
