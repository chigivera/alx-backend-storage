#!/usr/bin/env python3
"""List all documents in a collection"""
from typing import List


def list_all(mongo_collection) -> List:
    """Lists all documents in a collection"""
    return list(mongo_collection.find()) 