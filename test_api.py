import requests

url = "http://127.0.0.1:5000/data"

response = requests.post(url, json={"name": "Johnkerby"})
print(response.json())
