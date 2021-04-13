from flask import Flask, jsonify, request

app = Flask(__name__)

app.config["DEBUG"] = True

books = [
    {"id":1, "title":"Python", "author":"Mori"},
    {"id":2, "title":"C", "author":"Bob"},
    {"id":3, "title":"Nodejs", "author":"Mike"},
    {"id":4, "title":"go", "author":"Errick"}
]

@app.route("/api/v1/books", methods = ["GET"])
def api_all():
    return jsonify({"books":books})

@app.route("/api/v1/books/<int:id>", methods = ["GET"])
def api_one(id):    
    result = [book for book in books if book["id"] == id]
    return jsonify({"book":result[0]})


if __name__ == "__main__":
    app.run()