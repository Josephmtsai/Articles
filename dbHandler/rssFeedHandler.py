# -*- coding: utf-8 -*-
import pymongo


def insertRssFeeds(dataList, MONGO_URL):
    print(MONGO_URL)
    client = pymongo.MongoClient(MONGO_URL)
    print('start connect')
    db = client.heroku_v53vw3t0
    db.articles.insert_many(dataList)
    print('insert data')
