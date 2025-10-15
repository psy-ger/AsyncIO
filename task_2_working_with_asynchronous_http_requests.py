import asyncio
import aiohttp


async def fetch_content(url: str) -> str:
    """Fetches the content of the given URL asynchronously.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The content of the page or an error message.
    """
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()
                return await response.text()
    except Exception as e:
        return f"Error fetching {url}: {e}"


async def fetch_all(urls: list) -> list:
    """Fetches the content of all URLs in the list concurrently.

    Args:
        urls (list): List of URLs to fetch.

    Returns:
        list: List of page contents or error messages.
    """
    tasks = [fetch_content(url) for url in urls]
    return await asyncio.gather(*tasks)

# Example usage:
# if __name__ == "__main__":
#     urls = ["https://example.com", "https://google.com", "https://github.com"]
#     results = asyncio.run(fetch_all(urls))
#     for content in results:
#         print(content[:200])  # Print first 200 characters of each page
