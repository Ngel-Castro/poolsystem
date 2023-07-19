import pymongo
import os
import datetime

from pymongo import MongoClient

mongo_user = os.environ.get("MONGO_USER")
mongo_pass = os.environ.get("MONGO_PASS")

client = MongoClient("mongodb://%s:%s@localhost:30007/" % (mongo_user, mongo_pass))
db = client["poolsystem"]
collection = db["pool"]
timestamp = datetime.datetime.now()

post = {"_id": 0, "ph": 7.2, "chlorine": 1, "salt": 2200, "date": timestamp}

collection.insert_one(post)
