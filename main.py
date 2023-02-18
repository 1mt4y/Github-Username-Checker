import requests
with open("usernames.txt") as f:
    for username in f.read().split('\n'):
        url = f"https://github.com/{username}"
        res = requests.get(url)
        if res.status_code == 404:
            print(f'USERNAME AVAILABLE: {username}')