import asyncio

async def async_func(task_no):
    print(f"{task_no}:Velotio...")
    await asyncio.sleep(1)
    print(f"{task_no}...Blog!")

async def main():
    tasks = [async_func(i) for i in range(3)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
    