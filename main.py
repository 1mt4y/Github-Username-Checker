import requests
import concurrent.futures

def checkUsername(username):
    res = requests.get(f"https://github.com/{username}")
    if res.status_code == 404:
        print(f"[*] USERNAME AVAILABLE: {username}")
    else:
        print(f"[!] Username Unavailable: {username}")

with concurrent.futures.ThreadPoolExecutor() as executor: # Create the thread pool
    with open("usernames.txt") as h:
        for username in h.read().strip().split('\n'):
            executor.submit(checkUsername, username=username) # Schedule the execution of the checkUsername function