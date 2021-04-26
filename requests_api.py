import requests

# httpbin.org

r = requests.get('http://httpbin.org/get')

print(r.status_code)
print(r.ok)
print(r.headers)
print(r.headers.keys())

