"""
This file is created to get the authentication token from the running django project and Performing the various operations after cusseessful login.
"""

import requests

url = "http://127.0.0.1:9999/hello/"
headers = {
    "X-API-Key": 'kX3xeD9AHF7VBTB1tuR0c9wqJ2W0zJiv7fLzW5Wn',
    "Accept": "application/json"
}

res = requests.get(url, headers=headers)
print("Hello : ", res.text)

url = "http://127.0.0.1:9999/login/"
data = {"username": 'krishna', 'password': 123456}
res = requests.post(url, json=data, headers=headers, verify=True)
print("get_token :", res.json())

user_token = res.json()["token"]
print(f"User token : ", user_token)

url = "http://127.0.0.1:9999/create_person/"
data = {
    "name": "Krishna",
    "age": 21
}
headers = {"Content-Type": "application/json", "Authorization": f"Bearer {user_token}"}
res = requests.post(url, json=data, headers=headers, verify=True)
print("Create Person :", res.text)
