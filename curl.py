import requests
import time

TS = time.time()

headers = {
            "X-Timestamp": str(TS),
            "Accept-Encoding": "identity",
            "X-Content-Type": "application/octet-stream",
            "X-Size": "35",
            "X-Etag": "f2e6121b3f1ada44e881396e93ada62d"
          }

url = "http://127.0.0.4:6041/sdb4/538/AUTH_test/C3/fake_object." + str(TS)


# print(TS)

res = requests.put(url=url, headers = headers)

print(res.status_code)
print(res.content)