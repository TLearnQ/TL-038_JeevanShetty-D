
import requests

url = "https://httpbin.org/delete"
headers = {
    "Authorization": "Bearer mytoken"
}

response = requests.delete(url, headers=headers)

print("HTTP Status Code:", response.status_code)
