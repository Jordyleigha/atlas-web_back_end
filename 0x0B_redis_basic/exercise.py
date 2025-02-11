#!/usr/bin/env python3

import redis
import uuid
from typing import Union


class Cache:
    def __init__(self) -> None:
        # Initialize the Redis client and flush the database
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        # generate a random key using uuid
        key = str(uuid.uuid4())
        # store the data in Redis with the generated key
        self._redis.set(key, data)
        # return the generated key
        return key

    def get(self, key: str, fn: Optional[callable] = None) -> Optional[Union[str, bytes, int, float]]:
        # retrieve the data from redis
        value = self._redis.get(key)
        # if the key does not exist, return None
        if value is None:
            return None
        # if a conversion function is provided, apply it
        if fn:
            return fn(value)
        # return the raw value (bytes) if no function is provided
        return value

    def get_str(self, key: str) -> Optional[str]:
        # retrieve the value as a string
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        # retrieve the value as an integer
        return self.get(key, fn=int)
