#!/usr/bin/env python3
from pymongo import MongoClient


def log_stats():
    client = MongoClient()
    db = client.logs
    logs = db.nginx
    total_logs = logs.count_documents({})
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = logs.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    status_check_count = logs.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check_count} status check")


if __name__ == "__main__":
    log_stats()
