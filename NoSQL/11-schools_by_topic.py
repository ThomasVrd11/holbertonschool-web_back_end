#!/usr/bin/env python3
"""onz"""


def schools_by_topic(mongo_collection, topic):
    """return topics"""

    return (mongo_collection.find({"topics": topic}))
