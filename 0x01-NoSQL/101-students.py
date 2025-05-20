#!/usr/bin/env python3
"""Get top students by average score"""
from typing import List


def top_students(mongo_collection) -> List:
    """Returns all students sorted by average score"""
    pipeline = [
        {
            "$project": {
                "name": 1,
                "averageScore": {
                    "$avg": "$topics.score"
                }
            }
        },
        {
            "$sort": {
                "averageScore": -1
            }
        }
    ]
    return list(mongo_collection.aggregate(pipeline)) 