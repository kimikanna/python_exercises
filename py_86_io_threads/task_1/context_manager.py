# Посмотрите видео про контекстный менеджер и повторите все действия из видео с файлом из пункта 2

import os
import aiohttp
import asyncio

with open('task_1/lorum2.txt', 'w+') as f:
    f.write('123\n')
    f.write('hello\n')
    f.seek(0)
    print(f.read())
print('end\n')

with os.scandir(".") as entries:
    for entry in entries:
        print(entry.name, "->", entry.stat().st_size, "byte(s)")
print()


async def main():

    async with aiohttp.ClientSession() as session:
        async with session.get('http://python.org/') as response:

            print("Python.org status:", response.status)
            print("Content-Type:", response.headers['content-type'])

            html = response.headers
            print('Content-Length:', html['Content-Length'])

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
