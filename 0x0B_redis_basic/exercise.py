#!/usr/bin/env python3

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def call_history(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        # create keys for inputs and outputs
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        # normalize input args and store in redis
        self._redis.rpush(input_key, str(args))
        # call the org method to get output
        output = method(self, *args, **kwargs)
        # store the output in redis
        self._redis.rpush(output_key, str(output))
        return output
    return wrapper


def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        # use the qualified name of the method as a key
        key = method.__qualname__
        # increment the count in redis
        self._redis.incr(key)
        # call the org method and return its result
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    def __init__(self) -> None:
        # Initialize the Redis client and flush the database
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls  # decorate the store method with count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        # generate a random key using uuid
        key = str(uuid.uuid4())
        # store the data in Redis with the generated key
        self._redis.set(key, data)
        # return the generated key
        return key

    def get(self, key: str, fn:
            Optional[callable] =
            None) -> Optional[Union[str, bytes, int, float]]:
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
