import asyncio
from time import perf_counter, sleep

async def main():
    print("async-ready function")

# pornim event loop-ul de asyncio:
#asyncio.run(main())


async def task1():
    print("1: started task")
    #sleep(3) # blocking
    # dacă vrem să eliberăm scheduler-ul
    # să poată rula altă coroutină,
    # trebui să facem await!
    await asyncio.sleep(3)

    # !!! keyword-ul await este cel
    # care spune scheduler-ului
    # că poate rula în timpul ăsta altceva

    print("1: finished")

async def task2():
    print("2: started task")
    await asyncio.sleep(3)
    print("2: finished")

async def main():
    start = perf_counter()
    await asyncio.gather(
        task1(),
        task2(),
    )
    print("main took %ss" % (perf_counter() - start))

#asyncio.run(main())

# Repetăm exemplul cu requests:

import requests

URLS = [
    f"https://jsonplaceholder.typicode.com/albums/{num}"
    for num in range(1, 11)
]

# demo 1: de ce nu e așa simplu să treci pe async:
# library-urile pe care le foloseam deja
# sunt blocking
async def load_url(url):
    #import random
    #if random.choice([True, False]):
    #    raise Exception("Great choice!")
    response = requests.get(url)
    #          ^^ blocking, vrei nu vrei...

    print("» loaded")
    return response.json()

async def main():
    tasks = [
        load_url(url)
        for url in URLS
    ]

    results = await asyncio.gather(*tasks)

    for result in results:
        print(result)

print("#### chiar nu e async\n")
asyncio.run(main())
print("\n\n\n")


# demo 2: folosim un library async-ready
#
# $ pip install httpx

import httpx
import random

async def load_url(client, url):
    print("» awaiting", url)
    response = await client.get(url)
    await asyncio.sleep(random.randint(1, 3))
    print("« returning", url)
    return response.json()


async def main():
    async with httpx.AsyncClient() as client:
        tasks = [
            load_url(client, url)
            for url in URLS
        ]

        results = await asyncio.gather(*tasks)

        for result in results:
            print(result)

print("#### async, dar rezultate sincron\n")
asyncio.run(main())
print("\n\n\n")

# demo 2.1: improvement:
#           procesăm task-urile as completed:

async def main():
    async with httpx.AsyncClient() as client:
        tasks = [
            load_url(client, url)
            for url in URLS
        ]

        # în loc de gather, care await-ed este blocking
        # pănă când returnează ultimul task
        #results = await asyncio.gather(*tasks)

        # folosim:
        for task in asyncio.as_completed(tasks):
            result = await task
            print(result)

print("#### async, cu rezultate asincron\n")
asyncio.run(main())
print("\n\n\n")

