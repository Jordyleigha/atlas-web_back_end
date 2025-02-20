#!/usr/bin/env python3
"""function that inserts a new document in a collection based on kwargs"""


from pymongo import MongoClient

client = MongoClient()


def insert_school(mongo_collection, **kwargs):
    """ add new document
    """
    doc = mongo_collection.insert_one(kwargs)
    return doc.inserted_id
