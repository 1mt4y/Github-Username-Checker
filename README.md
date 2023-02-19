# Multithreaded Github Username Checker
Checks whether a username is available or not (username could be a user or an organization)


This script generates multiple HTTP **GET** requests using a **ThreadPoolExecutor** and checks its response status code.
If the status code is 404 then the username doesn't exist yet.


ThreadPoolExecutor uses a pool of threads to execute calls concurrently.
ThreadPoolExecutor is part of the concurrent.futures module which provides a high-level interface for asynchronously executing callables.
