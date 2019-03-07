import feedparser
from dbHandler import rssFeedHandler


def parser(url):
    rssFeedList = feedparser.parse(url)
    mongoRssDataList = []

    for rssFeed in rssFeedList['entries']:
        mongoRssData = {}
        mongoRssData['title'] = rssFeed['title']
        mongoRssData['description'] = rssFeed['description']
        mongoRssData['links'] = rssFeed['links'][0].href
        mongoRssDataList.append(mongoRssData)
    rssFeedHandler.insertRssFeeds(mongoRssDataList)


parser("https://feeds.feedburner.com/ndtvnews-top-stories")
