from http.client import HTTPConnection
import requests

# we should run simple server:
# python3 -m http.server
# http.client is so much faster than requests

###
The reason Requests is slower is because it does substantially more than httplib. 
httplib can be thought of as the bottom layer of the stack: 
it does the low-level wrangling of sockets. 
Requests is two layers further up, and adds things like cookies, 
connection pooling, additional settings, and kinds of other fun things. 
This is necessarily going to slow things down. We simply have to compute a lot more than httplib does
###

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
