import requests

url = "https://api.github.com"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Success! Data received.")
    print("Keys:", list(data.keys()))
else:
    print("Failed with status:", response.status_code)
