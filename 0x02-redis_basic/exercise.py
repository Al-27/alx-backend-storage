#!/usr/bin/env python3
"""
module documentaion
"""
import redis
from uuid import uuid4
import typing


type DATA = typing.Union[str, bytes, int, float]


class Cache:
    """ 
    class documentaion
    """

    def __init__(self):
        """
        func
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: DATA) -> str:
        """
        func
        """
        self._key = str(uuid4())
        self._redis.set(self._key, data)
        return self._key

    def get(self, key: str, fn: typing.Callable | None) -> DATA:
        """
        func
        """
        value = self._redis.get(key)
        value = fn(value) if fn else value
        return value

    def get_int(self, value: str) -> int:
        """
        func
        """
        return self.get(self._key, int)

    def get_str(self, value: str) -> str:
        """
        func
        """
        return self.get(self._key, str)
