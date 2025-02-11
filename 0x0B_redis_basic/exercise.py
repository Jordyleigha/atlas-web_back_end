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
