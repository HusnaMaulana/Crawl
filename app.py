import asyncio
from base64 import b64decode
from crawl4ai import (
    AsyncWebCrawler,
    CacheMode,
    CrawlerRunConfig,
)  # <-- 1. Import CrawlerRunConfig


async def main():
    # 2. Put your settings inside the config object
    run_config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        pdf=True,
        screenshot=True,
        scan_full_page=True,  # <-- Enable full page scanning for better PDF and screenshot results
    )

    async with AsyncWebCrawler() as crawler:
        # 3. Pass the config object into arun()
        result = await crawler.arun(
            url="https://id.wikipedia.org/wiki/Prabowo_Subianto",
            config=run_config,  # <-- Apply the settings here
        )

        if result.success:
            if result.screenshot:
                with open("screenshot.png", "wb") as f:
                    f.write(b64decode(result.screenshot))
                print("Screenshot saved at: screenshot.png")
            else:
                print("No screenshot data was returned.")

            if result.pdf:
                with open("page.pdf", "wb") as f:
                    f.write(result.pdf)
                print("PDF saved at: page.pdf")
            else:
                print("No PDF data was returned.")


if __name__ == "__main__":
    asyncio.run(main())
