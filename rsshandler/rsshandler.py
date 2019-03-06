import feedparser


def parser(url):
    rssDataList = feedparser.parse(url)
    print(rssDataList['feed'])
    for rssData in rssDataList['entries']:
        print(rssData)
        break


parser("https://feeds.feedburner.com/ndtvnews-top-stories")
