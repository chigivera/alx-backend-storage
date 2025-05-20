#!/usr/bin/env python3
"""Update topics of a school"""
from typing import List


def update_topics(mongo_collection, name: str, topics: List[str]) -> None:
    """Updates topics of a school document"""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    ) 