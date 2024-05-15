#!/usr/bin/env python3
""" Module Documentation """


def insert_school(mongo_collection, **kwargs):
    """
    func
    """
    return mongo_collection.insert_one(kwargs).inserted_id