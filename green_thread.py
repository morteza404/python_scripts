import time
import requests
from eventlet import greenpool

def get_status(u):
    status = requests.get(u).status_code
    return status

urls = ["http://varzesh3.com", "http://virgool.io", "http://tarafdari.com"]
p = greenpool.GreenPile(2)
start = time.time()
for url in urls:
    p.spawn(get_status, url)
print(list(p))
end = time.time()
print(end - start)
