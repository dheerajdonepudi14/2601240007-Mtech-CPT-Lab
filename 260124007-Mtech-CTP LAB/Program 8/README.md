# Program 8 — Asynchronous Web Crawler — asyncio and aiohttp

## 1. Problem Statement

Develop an asynchronous web crawler using asyncio, aiohttp and retries and compare it against a sequential implementation.

The objective is to build a clear Python implementation that demonstrates the required concept and produces a verifiable result.

## 2. Algorithm / Concept Identification

| Item | Details |
|---|---|
| Program | 8 |
| Topic | Asynchronous Web Crawler — asyncio and aiohttp |
| Main concept | Asynchronous Web Crawler — asyncio and aiohttp |
| Language | Python |
| Approach | Practical implementation with typed, readable code |
| Output | Demonstration of the required behavior |

## 3. Step-by-Step Example

**Example:** Three URLs are requested. Sequential processing waits for each request; asyncio starts the I/O operations concurrently and retries failures.

### Working

1. Accept or define the required data.
2. Apply the concept specified in the exercise.
3. Validate important conditions and edge cases.
4. Display the result and relevant analysis.
5. Use the stated complexity/tooling/testing information where applicable.

## 4. Algorithm / Procedure

1. Start the Python program.
2. Prepare the required input or sample data.
3. Execute the main operation for the selected concept.
4. Handle invalid or exceptional conditions where appropriate.
5. Display the result.
6. Verify the behavior using the relevant complexity, testing, typing, concurrency or development workflow.

## 5. Implementation

~~~python
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
~~~

## 6. Input and Output

### Sample Input

The exact input depends on the program. Use the prompts displayed by the Python program.

### Sample Output

The program prints the calculated result and/or demonstration of the requested concept.

## 7. Complexity / Engineering Analysis

| Aspect | Analysis |
|---|---|
| Primary operation | Depends on the program's algorithm or workflow |
| Space | Depends on stored data, recursion, buffers or generated objects |
| Verification | Output, tests, type checking or timing as appropriate |

### Program-specific Notes

Sequential crawling waits on requests one after another. Asynchronous crawling overlaps I/O operations; network conditions determine the actual timing difference.

## 8. Important Points

- Keep the implementation aligned with the exercise statement.
- Use meaningful names and type hints where appropriate.
- Test edge cases before considering the implementation complete.
- For tooling or AI-assisted exercises, human verification remains part of the development process.

## 9. Conclusion

This program demonstrates **Asynchronous Web Crawler — asyncio and aiohttp** through a practical Python implementation. The code, example workflow and analysis are organized so the exercise can be executed and reviewed independently.
