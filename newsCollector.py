
from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/api/*": {"origins": r"*"}})


class HelloWorld(Resource):
    def get(self):
        return "Hello from flask-rest"


api.add_resource(HelloWorld, '/')
if __name__ == "__main__":
    app.run()
