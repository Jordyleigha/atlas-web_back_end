#!/usr/bin/env python3
"""function that lists all documents in a collection"""


from pymongo import MongoClient

client = MongoClient()


def list_all(mongo_collection):
    """ pymongo command for getting all documents in collection
    """
    res = []
    for doc in mongo_collection.find({}):
        res.append(doc)
    return res
