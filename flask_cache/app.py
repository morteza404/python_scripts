from flask import Flask
from cachetools import cached, TTLCache

app = Flask(__name__)
app.config["DEBUG"] = True

cache = TTLCache(maxsize=100, ttl=60)

@cached(cache)
def get_data():
    data = open("test.txt").read()
    return data

@app.route("/")
def home():
    return get_data()

if __name__ == "__main__":
    app.run()