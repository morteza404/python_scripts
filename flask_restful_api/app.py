from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {"hello": "world"}

    def post(self):
        json_data = request.get_json(force=True)
        firstname = json_data["firstname"]
        lastname = json_data["lastname"]
        return jsonify(firstname=firstname, lastname=lastname)

api.add_resource(HelloWorld, "/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)