#!/usr/bin/env python3
""" logging module
"""

from pymongo import MongoClient

client = MongoClient()


def log_stats():
    """print nginx logs
    """

    db = client.logs

    doc_count = db.nginx.count_documents({})
    print(f"{doc_count} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        method_count = db.nginx.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    status = db.nginx.count_documents({"method": "GET", "path": "/status"})
    print(f"{status} status check")
