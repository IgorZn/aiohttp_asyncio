import aiohttp
import asyncio
from bs4 import BeautifulSoup


# async def fetch(session, url):
#     async with session.get(url) as response:
#         return await response.text()
#
#
# async def main(*args):
#     if args:
#         for url in args:
#             async with aiohttp.ClientSession() as session:
#                 html = await fetch(session, url)
#                 print(html)

async def fetch_site(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')
            print(url)
            return html

async def main():
    task1 = asyncio.create_task(fetch_site('https://python.org'))
    task2 = asyncio.create_task(fetch_site('https://ya.ru'))
    task3 = asyncio.create_task(fetch_site('https://google.com'))

    await asyncio.gather(
        task1,
        task2,
        task3
    )



if __name__ == '__main__':
    # urls = ['http://python.org', 'https://aiohttp.readthedocs.io/en/stable/index.html']
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main(*urls))
    asyncio.run(main())
