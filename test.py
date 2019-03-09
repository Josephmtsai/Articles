"""
import os
import settings
import rsshandler.rsshandler
MONGO_URL = os.environ.get('MONGODB_URI')
rsshandler.rsshandler.parser(
    "https://feeds.feedburner.com/ndtvnews-top-stories", MONGO_URL)
"""


def test():
    assert 200 == 200


test()
