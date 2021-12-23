import asyncio
import time


def time_print(*args, **kwargs) -> str:
    t = time.perf_counter()

    minute = int(t / 60)
    second = t % 60

    print(f'{minute:02d}:{second:05.2f}', end=' ')
    print(*args, **kwargs)


async def clean():
    time_print("拖地: 开始拖地！！")
    await asyncio.sleep(1)
    time_print("拖地: 拖地完成！！")

async def wash():
    time_print("洗衣服: 开始洗衣服...")
    await asyncio.sleep(2)
    time_print("洗衣服: 洗衣服完毕...")

async def main():
    await asyncio.gather(wash(), clean())

if __name__ == "__main__":
    asyncio.run(main())
