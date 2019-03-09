import feedparser
from dbHandler import rssFeedHandler
from time import mktime
from datetime import datetime


def dump(obj):
    for attr in dir(obj):
        print("obj.%s = %r\n" % (attr, getattr(obj, attr)))


def parser(url, MONGO_URL):
    rssFeedList = feedparser.parse(url)
    mongoRssDataList = []

    for rssFeed in rssFeedList['entries']:
        mongoRssData = {}
        mongoRssData['title'] = rssFeed['title']
        mongoRssData['description'] = rssFeed['description']
        mongoRssData['link'] = rssFeed['link']
        mongoRssData['storyimage'] = rssFeed['storyimage']
        mongoRssData['fullimage'] = rssFeed['fullimage']
        mongoRssData['tags'] = rssFeed['tags']
        mongoRssData['updateDate'] = datetime.fromtimestamp(
            mktime(rssFeed['updated_parsed']))
        mongoRssData['publishedDate'] = datetime.fromtimestamp(
            mktime(rssFeed['published_parsed']))
        mongoRssDataList.append(mongoRssData)
    rssFeedHandler.insertRssFeeds(mongoRssDataList, MONGO_URL)
