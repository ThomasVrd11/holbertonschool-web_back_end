#!/usr/bin/env python3
"""Log stats"""

from pymongo import MongoClient


def log_stats():
    """ func no idea what it does tbh"""
    cl = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = cl.logs.nginx
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"    method {method}: {count}")
    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()
