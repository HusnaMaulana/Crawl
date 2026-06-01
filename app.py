import asyncio
from crawl4ai import *


async def main():
    async with AsyncWebCrawler() as crawler:
        results = await crawler.arun(
            url="https://polymarket.com/economy",
        )
        print(results.markdown)


if __name__ == "__main__":
    asyncio.run(main())
