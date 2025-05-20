#!/usr/bin/env python3
"""Insert a document in a collection"""
from typing import Dict


def insert_school(mongo_collection, **kwargs) -> str:
    """Inserts a new document in a collection"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id 