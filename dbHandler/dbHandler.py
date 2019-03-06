# -*- coding: utf-8 -*-
import pymongo
import os
MONGO_URL = os.environ.get('MONGODB_URI')


def insertStatus(status):
    client = pymongo.MongoClient(MONGO_URL)
    db = client.heroku_szv1xx0f
    db.status.insert_one(status)
