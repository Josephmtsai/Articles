
from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
import os
import settings
import rsshandler.rsshandler
MONGO_URL = os.environ.get('MONGODB_URI')
app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/api/*": {"origins": r"*"}})
settings.init()


class HelloWorld(Resource):
    def get(self):
        return "Hello from flask-rest"


class UpdateRssFeed(Resource):
    def get(self):
        return rsshandler.rsshandler.parser(MONGO_URL)


api.add_resource(HelloWorld, '/')
api.add_resource(UpdateRssFeed, '/crawler')


if __name__ == "__main__":
    app.run()
