"""
类装饰器练习
学习要点：__init__ 接收被装饰函数，__call__ 实现调用逻辑
"""
import time

class Timer:
    """计时装饰器：记录函数执行时间"""

    def __init__(self, func):
        self.func = func
        self.call_count = 0

    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.func(*args, **kwargs)
        end = time.time()

        self.call_count += 1
        print(f"[Timer] {self.func.__name__} 第{self.call_count}次调用，耗时 {end - start:.4f}s")

        return result

@Timer
def slow_function(n):
    """模拟耗时操作"""
    time.sleep(0.1)
    return sum(range(n))

if __name__ == "__main__":
    # 测试
    result1 = slow_function(1000)
    print(f"结果: {result1}")

    result2 = slow_function(500)
    print(f"结果: {result2}")