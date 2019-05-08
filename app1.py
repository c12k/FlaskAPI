from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)


class health(Resource):
    def get(self):
        return "Flask API is healthy.", 200


api.add_resource(health, "/")


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)
