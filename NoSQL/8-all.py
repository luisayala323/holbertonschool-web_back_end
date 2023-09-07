#!/usr/bin/env python3
"""Function for listing all documents in a MongoDB collection"""

def list_all(mongo_collection):
    """
    List all documents in a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The PyMongo collection object.

    Returns:
        list: A list containing all documents in the collection.
    """
    return list(mongo_collection.find({}))