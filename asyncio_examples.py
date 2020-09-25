import asyncio
import aiohttp
import time


def write_file(data):
    """Записать фаил на диск. Это синхронная задача, но будет внутри async функции"""
    with open(f'{time.time_ns()}.jpg', 'wb') as file:
        file.write(data)


async def fetch_content(url, session):
    """Запуск сессии в async режиме"""
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        write_file(data)


async def main():
    p1 = time.perf_counter()
    url = 'https://loremflickr.com/320/240'
    tasks = []

    # Сформировать задачи и сложить их списком
    async with aiohttp.ClientSession() as session:
        for _ in range(10):
            task = asyncio.create_task(fetch_content(url, session))
            tasks.append(task)

        # Собрать все задачи для запуска
        await asyncio.gather(*tasks)

    # Вывести затраченное время
    print(time.perf_counter() - p1)

if __name__ == '__main__':
    # Запустить все async сформированные задачи (tasks)
    asyncio.run(main())
