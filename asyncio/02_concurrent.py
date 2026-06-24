import asyncio

async def task(name, delay):
    """模拟任务"""
    print(f"任务{name}开始")
    await asyncio.sleep(delay)
    print(f"任务{name}完成, 耗时{delay}秒")
    return name

async def main():
    """并发执行多个任务"""

    # 方法1: asyncio.gather 并发
    print("--- gather 并发 ---")
    results = await asyncio.gather(
        task("A", 2),
        task("B", 1),
        task("C", 3)
    )
    print(f"结果: {results}")

    # 方法2: 创建任务对象
    print("\n--- create_task 并发 ---")
    task1 = asyncio.create_task(task("X", 2))
    task2 = asyncio.create_task(task("Y", 1))

    result1 = await task1
    result2 = await task2
    print(f"结果: {result1}, {result2}")

if __name__ == "__main__":
    asyncio.run(main())