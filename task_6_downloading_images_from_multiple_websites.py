import asyncio
import aiohttp


async def download_image(url: str, filename: str):
    """Downloads an image from the given URL and saves it to the specified filename.

    Args:
        url (str): The URL of the image to download.
        filename (str): The filename to save the image as.
    """
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()
                with open(filename, 'wb') as f:
                    while True:
                        chunk = await response.content.read(1024)
                        if not chunk:
                            break
                        f.write(chunk)
        print(f"Downloaded {url} as {filename}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")


async def main():
    images = [
        # (url, filename) pairs
        ("https://via.placeholder.com/150", "image1.png"),
        ("https://via.placeholder.com/200", "image2.png"),
        ("https://via.placeholder.com/250", "image3.png"),
    ]
    tasks = [download_image(url, filename) for url, filename in images]
    await asyncio.gather(*tasks)

# Example usage:
# if __name__ == "__main__":
#     asyncio.run(main())
