import asyncio

async def async_func(task_no):
    print(f"{task_no}:Velotio...")
    await asyncio.sleep(1)
    print(f"{task_no}...Blog!")

async def main():    
    tasks = []
    for i in range(3):
        tasks.append(async_func(i))
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
    