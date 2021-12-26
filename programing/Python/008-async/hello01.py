import asyncio


async def say_after_async(delay: int):
    print("hello")
    await asyncio.sleep(delay)
    print("world")


def main():
    asyncio.run(say_after_async(1))


if __name__ == '__main__':
    main()
