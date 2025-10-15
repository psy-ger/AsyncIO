import asyncio
import random


async def download_page(url: str):
    """Simulates downloading a webpage.

    Args:
        url (str): The URL of the page to download.
    """
    load_time = random.randint(1, 5)
    await asyncio.sleep(load_time)
    print(f"Downloaded {url} in {load_time} seconds")


async def main(urls: list):
    """Downloads a list of webpages concurrently.

    Args:
        urls (list): A list of URLs to download.
    """
    tasks = [download_page(url) for url in urls]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    urls = ["https://example.com", "https://google.com", "https://github.com"]
    asyncio.run(main(urls))

    # Adding assert for verification
    assert len(urls) == 3, "The list of URLs must contain 3 elements"
    print("Program executed successfully!")
