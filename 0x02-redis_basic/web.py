#!/usr/bin/env python3
"""
module documentaion
"""
import redis
import requests
from functools import wraps
from typing import Callable
redis_store = redis.Redis()


def cacher(method: Callable) -> Callable:
    """
    function
    """
    @wraps(method)
    def invoker(url) -> str:
        """
        func
        """
        redis_store.incr(f'count:{url}')
        rslt = redis_store.get(f'result:{url}')
        if rslt:
            return rslt.decode('utf-8')
        rslt = method(url)
        redis_store.set(f'count:{url}', 0)
        redis_store.setex(f'result:{url}', 10, rslt)
        return rslt
    return invoker


@cacher
def get_page(url: str) -> str:
    """
    function
    """
    return requests.get(url).text
