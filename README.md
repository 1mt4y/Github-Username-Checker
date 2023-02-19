# Multithreaded Github Username Checker

- This script checks whether a username is available or not (username could be a user or an organization)
- It generates multiple HTTP GET requests using a **ThreadPoolExecutor** and checks their response status code.
  - If the status code is 404 then the username doesn't exist yet.
- We use a **ThreadPoolExecutor** which uses a pool of threads to execute calls asynchronously.
- **ThreadPoolExecutor** is part of the [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html) module which provides a high-level interface for asynchronously executing callables.

# Note:
- This script can be used to check the availability of usernames for *any* website, I just used Github as an example.
- In the case where the website doesn't respond with a 404 status code then you can still check the *response content* to see if it contains words like "404", "Does not exist" ...
