#!/usr/bin/env python3
"""
    Python function that returns the list of
     school having a specific topic:
"""
import pymongo


def schools_by_topic(mongo_collection, topic: str) -> list:
    """
    Retrieve a list of schools from a MongoDB collection
    that match a specific topic.

    """

    sch: list = []
    query = {"topics": topic}

    for school in mongo_collection.find(query):
        sch.append(school)

    return sch
