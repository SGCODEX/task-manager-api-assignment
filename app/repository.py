import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)

db = client["task_db"]

tasks_collection = db["tasks"]

from datetime import datetime

def create_task(task_dict):
    task_dict["created_at"] = datetime.utcnow()
    task_dict["updated_at"] = datetime.utcnow()

    result = tasks_collection.insert_one(task_dict)

    return str(result.inserted_id)

# def get_all_tasks():
#     tasks = list(tasks_collection.find())

#     for task in tasks:
#         task["_id"] = str(task["_id"])

#     return tasks

def get_all_tasks(skip, limit):
    tasks = list(
        tasks_collection.find().skip(skip).limit(limit)
    )

    for task in tasks:
        task["_id"] = str(task["_id"])

    return tasks

from bson import ObjectId

def get_task_by_id(task_id):
    task = tasks_collection.find_one({"_id": ObjectId(task_id)})

    if task:
        task["_id"] = str(task["_id"])

    return task

def update_task(task_id, task_dict):
    from bson import ObjectId
    from datetime import datetime

    task_dict["updated_at"] = datetime.utcnow()

    result = tasks_collection.update_one(
        {"_id": ObjectId(task_id)},
        {"$set": task_dict}
    )

    return result.modified_count

def delete_task(task_id):
    from bson import ObjectId

    result = tasks_collection.delete_one({"_id": ObjectId(task_id)})

    return result.deleted_count

def complete_task(task_id):
    from bson import ObjectId
    from datetime import datetime

    result = tasks_collection.update_one(
        {"_id": ObjectId(task_id)},
        {
            "$set": {
                "status": "completed",
                "updated_at": datetime.utcnow()
            }
        }
    )

    return result.modified_count