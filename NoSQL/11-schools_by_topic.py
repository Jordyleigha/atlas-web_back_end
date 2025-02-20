#!/usr/bin/env python3
""" topic search module
"""

from pymongo import MongoClient

client = MongoClient()


def schools_by_topic(mongo_collection, topic):
    """ search for topic
    """
    res = []
    for doc in mongo_collection.find({'topics': topic}):
        res.append(doc)
    return res
