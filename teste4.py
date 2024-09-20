import asyncio

# undetected-playwright here!
from undetected_playwright.async_api import async_playwright, Playwright


async def run(playwright: Playwright):
    args = []
    
    # disable navigator.webdriver:true flag
    args.append("--disable-blink-features=AutomationControlled")
    browser = await playwright.chromium.launch(headless=False,
                                               args=args)
    page = await browser.new_page()
    await page.goto("https://nowsecure.nl/#relax")
    input("Press ENTER to continue to Creep-JS:")
    await page.goto("https://nowsecure.nl/#relax")
    await page.goto("https://abrahamjuliot.github.io/creepjs/")
    input("Press ENTER to exit:")
    await browser.close()


async def main():
    async with async_playwright() as playwright:
        await run(playwright)


if __name__ == "__main__":
    loop = asyncio.SelectorEventLoop()
    loop.run_until_complete(main())
    # asyncio.run(main) # should work for non-Windows as well