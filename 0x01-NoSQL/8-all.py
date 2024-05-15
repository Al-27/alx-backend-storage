#!/usr/bin/env python3
""" Module Documentation """


def list_all(mongo_collection):
    """
    func
    """
    curs = mongo_collection.find({})
    
    docs = [doc for d in curs]
    return docs