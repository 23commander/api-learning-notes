import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

print("Status:", response.status_code)

data = response.json()

# Print first user's name and email
print("First user:", data[0]["name"], "-", data[0]["email"])
