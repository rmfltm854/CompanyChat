import requests
import json

# URL
# 127.0.0.1은 localhost로 대체 가능
url = "http://127.0.0.1:8000/GetVectorStore"

# headers
headers = {
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

print("response: ", response)
print("response.text: ", response.text)