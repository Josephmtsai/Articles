# -*- coding: utf-8 -*-
import pymongo


def insertRssFeeds(dataList, MONGO_URL):
    print(MONGO_URL)
    client = pymongo.MongoClient(MONGO_URL)
    print('start connect')
    db = client.articles
    db.articles.insert_many(dataList)
    print('insert data')
