import asyncio
import random
import time


async def demo(x):
    await asyncio.sleep(x)
    return f'wait time:{x}'


async def main():
    print(f'start at:{time.strftime("%T")}')
    list = [random.randint(1, 5)for i in range(90)]
    print(list)
    tasks = [demo(i) for i in list]
    print(await asyncio.gather(*tasks))
    print(f'end at:{time.strftime("%T")}')
    return 10

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    print(loop.run_until_complete(main()))
