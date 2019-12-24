import aiohttp
import asyncio
from bs4 import BeautifulSoup
import pprint


async def fetch_site(url):
    print(f"load  {url}")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')
            print(f"{url} has loaded")
            return soup.find_all('meta')[:10]


async def main():
    task1 = asyncio.create_task(fetch_site('https://python.org'))
    task2 = asyncio.create_task(fetch_site('https://ya.ru'))
    task3 = asyncio.create_task(fetch_site('https://google.com'))

    a, b, c = await asyncio.gather(
        task1,
        task2,
        task3
    )

    # print all lists, just to show
    for i in [a, b, c]:
        pprint.pprint(i)
        print(len(i))


if __name__ == '__main__':
    asyncio.run(main())
