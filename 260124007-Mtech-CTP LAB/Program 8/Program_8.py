import asyncio
import time
from typing import List

import aiohttp


URLS: List[str] = [
    "https://example.com",
    "https://www.python.org",
    "https://httpbin.org/get",
]


async def fetch_async(
    session: aiohttp.ClientSession,
    url: str,
    retries: int = 3
) -> str:
    for attempt in range(1, retries + 1):
        try:
            async with session.get(url, timeout=10) as response:
                return f"{url} -> HTTP {response.status}"
        except (aiohttp.ClientError, asyncio.TimeoutError) as exc:
            if attempt == retries:
                return f"{url} -> failed after retries: {exc}"
            await asyncio.sleep(2 ** (attempt - 1))

    return f"{url} -> failed"


async def asynchronous_crawl(urls: List[str]) -> None:
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(
            *(fetch_async(session, url) for url in urls)
        )
        for result in results:
            print(result)


def sequential_crawl(urls: List[str]) -> None:
    import requests

    for url in urls:
        try:
            response = requests.get(url, timeout=10)
            print(f"{url} -> HTTP {response.status_code}")
        except requests.RequestException as exc:
            print(f"{url} -> failed: {exc}")


async def main() -> None:
    print("--- Sequential implementation ---")
    start = time.perf_counter()
    sequential_crawl(URLS)
    sequential_time = time.perf_counter() - start

    print(f"Sequential time: {sequential_time:.2f} seconds")

    print("\n--- Asynchronous implementation ---")
    start = time.perf_counter()
    await asynchronous_crawl(URLS)
    async_time = time.perf_counter() - start

    print(f"Asynchronous time: {async_time:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
