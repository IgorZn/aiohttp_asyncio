import aiohttp
import asyncio


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main(*args):
    if args:
        for url in args:
            async with aiohttp.ClientSession() as session:
                html = await fetch(session, url)
                print(html)

if __name__ == '__main__':
    urls = ['http://python.org', 'https://aiohttp.readthedocs.io/en/stable/index.html']
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(*urls))
