def getRssFeedList():
    rssFeedInformationList = []
    rssFeed = {}
    rssFeed['subFeedPaths'] = ['ndtvnews-top-stories', 'ndtvnews-latest', 'ndtvnews-trending-news',
                               'ndtvnews-india-news', 'ndtvnews-world-news', 'ndtvprofit-latest', 'ndtvmovies-latest', 'ndtvsports-latest',
                               'ndtvsports-cricket', 'gadgets360-latest', 'carandbike-latest', 'ndtvnews-cities-news', 'ndtvnews-south',
                               'ndtvnews-indians-abroad', 'ndtvcooks-latest', 'ndtvnews-offbeat-news', 'ndtvnews-people', 'ndtvkhabar-latest',
                               'latest-videos']
    rssFeed['Name'] = 'NdtvNews'
    rssFeed['url'] = 'https://feeds.feedburner.com/'
    rssFeedInformationList.append(rssFeed)
    return rssFeedInformationList
