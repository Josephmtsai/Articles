import feedparser
from dbHandler import rssFeedHandler
from time import mktime
from datetime import datetime
import rssModel


def parser(MONGO_URL):
    mongoRssDataList = []
    for rssFeedInformation in rssModel.getRssFeedList():
        for subFeedPath in rssFeedInformation['subFeedPaths']:
            rssFeedList = feedparser.parse(
                rssFeedInformation['url'] + subFeedPath)
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
                mongoRssData['source'] = rssFeedInformation['name']
                mongoRssData['section'] = rssFeedList['title']
                mongoRssDataList.append(mongoRssData)
    if len(rssFeedHandler) > 0:
        rssFeedHandler.insertRssFeeds(mongoRssDataList, MONGO_URL)
        return "OK"
    return "Nothing Insert"
