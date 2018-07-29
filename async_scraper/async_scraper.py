import aiohttp
import asyncio


sites = set()
sites_html = dict()


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        for site in sites:
            html = await fetch(session, site)
            sites_html[site] = html


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
