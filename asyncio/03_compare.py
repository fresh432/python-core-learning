import asyncio
import time
import httpx

def sync_task(name, delay):
    """同步任务: 阻塞等待"""
    print(f"同步任务{name}开始")
    time.sleep(delay) # 阻塞
    print(f"同步任务{name}完成")
    return name

async def async_task(name, delay):
    """异步任务: 非阻塞等待"""
    print(f"异步任务{name}开始")
    await asyncio.sleep(delay) # 非阻塞, 让出控制权
    print(f"异步任务{name}完成")
    return name

def main_sync():
    """同步主函数"""
    start = time.time()
    sync_task("A", 2)
    sync_task("B", 1)
    print(f"同步总耗时: {time.time() - start:.2f}秒")

async def main_async():
    """异步主函数"""
    start = time.time()
    await asyncio.gather(
        async_task("A", 2),
        async_task("B", 1)
    )
    print(f"异步总耗时: {time.time() - start:.2f}秒")







# async def fetch_url(client, url):
#     """异步获取网页"""
#     print(f"开始获取: {url}")
#     response = await client.get(url)
#     print(f"完成: {url}, 状态码: {response.status_code}")
#     return len(response.text)
#
# async def main():
#     """并发获取多个网页"""
#     urls = [
#         "https://www.example.com",
#         "https://www.python.org",
#         "https://www.github.com"
#     ]
#
#     async with httpx.AsyncClient() as client:
#         tasks = [fetch_url(client, url) for url in urls]
#         results = await asyncio.gather(*tasks)
#         print(f"各页面长度: {results}")


if __name__ == "__main__":
    # asyncio.run(main())
    print("=== 同步 ===")
    main_sync()
    print("\n=== 异步 ===")
    asyncio.run(main_async())
