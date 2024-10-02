from urllib.parse import unquote
import requests

TARGET = "http://denied.amt.rs/"

print(unquote(requests.head(f"{TARGET}").headers['Set-Cookie']))
