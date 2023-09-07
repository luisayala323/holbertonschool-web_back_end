#!/usr/bin/env python3
"""Function for inserting data into a MongoDB collection"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document into a MongoDB collection based on keyword arguments.

    Args:
        mongo_collection (pymongo.collection.Collection): The PyMongo collection object.
        **kwargs: Keyword arguments representing the document fields.

    Returns:
        str: The _id of the newly inserted document.
    """
    # Insert the document into the collection and capture the new _id
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
