"""
异步编程基础练习
学习要点：async/await、协程、事件循环
"""

import asyncio

async def say_hello():
    """协程函数"""
    print("Hello")
    await asyncio.sleep(1) # 模拟IO操作, 让出控制权
    print("World")

async def say_hi():
    """另一个协程"""
    print("Hi")
    await asyncio.sleep(0.5)
    print("There")

async def main():
    """主协程"""
    print("开始")

    # 顺序执行
    await say_hello()
    await say_hi()

    print("结束")

# 运行
if __name__ == "__main__":
    asyncio.run(main())

