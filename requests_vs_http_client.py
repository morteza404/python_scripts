from http.client import HTTPConnection
import requests

# we should run simple server:
# python3 -m http.server
# http.client is so much faster than requests

conn = HTTPConnection(host="0.0.0.0", port=8000)

for i in range(1000):
    conn.request("GET", "/")
    resp = conn.getresponse()
    body = resp.read()
    print(resp.status)
conn.close()

with requests.Session() as session:
    for i in range(1000):
        resp = session.get(url = "http://0.0.0.0:8000")
        print(resp.status_code)
