from time import time
import aiohttp
import asyncio
from bs4 import BeautifulSoup
import pprint


async def fetch_content(url, session):
    print(f"load  {url}")
    async with session.get(url) as response:
        html = await response.text()
        soup = BeautifulSoup(html, 'html.parser')
        print(f"{url} has loaded")
        return soup.find_all('meta')[:10]


async def main():
    urls = [
        'https://ya.ru',
        'https://ok.ru',
        'https://python.org',
    ]

    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(3):
            task = asyncio.create_task(fetch_content(urls[i], session))
            tasks.append(task)

        a, b, c = await asyncio.gather(*tasks)

    # just to show
    for i in [a, b, c]:
        pprint.pprint(i)


if __name__ == '__main__':
    t0 = time()
    asyncio.run(main())
    print('Time to process requests:', time() - t0)
