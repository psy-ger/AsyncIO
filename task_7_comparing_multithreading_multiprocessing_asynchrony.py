import requests
import asyncio
import aiohttp
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

URL = "https://httpbin.org/delay/1"
NUM_REQUESTS = 500


def sync_request(url):
    """Performs a synchronous HTTP GET request.

    Args:
        url (str): The URL to request.
    Returns:
        int: HTTP status code.
    """
    response = requests.get(url)
    return response.status_code


def run_sync():
    """Runs NUM_REQUESTS synchronously and prints the elapsed time."""
    start = time.time()
    for _ in range(NUM_REQUESTS):
        sync_request(URL)
    print(f"Sync: {time.time() - start:.2f} seconds")


def thread_request():
    """Runs NUM_REQUESTS using ThreadPoolExecutor and prints the elapsed time."""
    start = time.time()
    with ThreadPoolExecutor() as executor:
        list(executor.map(sync_request, [URL] * NUM_REQUESTS))
    print(f"Threads: {time.time() - start:.2f} seconds")


def process_request():
    """Runs NUM_REQUESTS using ProcessPoolExecutor and prints the elapsed time."""
    start = time.time()
    with ProcessPoolExecutor() as executor:
        list(executor.map(sync_request, [URL] * NUM_REQUESTS))
    print(f"Processes: {time.time() - start:.2f} seconds")


async def async_request(session, url):
    """Performs an asynchronous HTTP GET request using aiohttp.

    Args:
        session (aiohttp.ClientSession): The aiohttp session.
        url (str): The URL to request.
    Returns:
        int: HTTP status code.
    """
    async with session.get(url) as response:
        return response.status


async def run_async():
    """Runs NUM_REQUESTS asynchronously and prints the elapsed time."""
    start = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [async_request(session, URL) for _ in range(NUM_REQUESTS)]
        await asyncio.gather(*tasks)
    print(f"Async: {time.time() - start:.2f} seconds")


if __name__ == "__main__":
    print("Running sync...")
    run_sync()
    print("Running threads...")
    thread_request()
    print("Running processes...")
    process_request()
    print("Running async...")
    asyncio.run(run_async())
