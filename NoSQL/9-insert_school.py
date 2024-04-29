#!/usr/bin/env python3
"""nuf """


def insert_school(mongo_collection, **kwargs):
    """get me out of here ffs"""
    return mongo_collection.insert_one(kwargs).inserted_id
