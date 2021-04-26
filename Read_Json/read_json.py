import json
# from pprint import pprint

with open('test.json') as f:
    data = json.load(f)

# pprint(data)

# pprint(data['username'])

print(data)

username = data['username']
password = data['password']
city = data['city']

print(f"username is : {username}")
print(f"password is : {password}")
print(f"city is : {city}")