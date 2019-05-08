from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)

api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument("sometext", type=str, help="Enter some text to pass to API")


class health(Resource):
    def get(self):
        return "Flask API is healthy.", 200


class api1(Resource):
    def post(self):
        args = parser.parse_args()
        resp = f"Got these arguments {args}"
        return resp, 200


api.add_resource(health, "/")
api.add_resource(api1, "/api1")

if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)
