# -*- coding: utf-8 -*-
import pymongo
import os
MONGO_URL = os.environ.get('MONGODB_URI')


def insertRssFeeds(dataList):
    client = pymongo.MongoClient(MONGO_URL)
    print('sa')
    db = client.news
    db.articles.insert_many(dataList)
    print('sa')
