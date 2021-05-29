import asyncio

async def clean():
    print("拖地: 开始拖地！！")
    await asyncio.sleep(1)
    print("拖地: 拖地完成！！")

async def wash():
    print("洗衣服: 拿衣服到洗衣机去洗")
    print("洗衣服: 开始洗衣服...")
    await asyncio.sleep(2)
    print("洗衣服: 洗衣服完毕...")

async def main():
    await asyncio.gather(wash(), clean())

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
