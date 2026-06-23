"""
装饰器基础练习
学习要点：函数作为参数、闭包、语法糖
"""


def my_decorator(func):
    """最简单的装饰器"""
    def wrapper():
        print("=== 函数执行前 ===")
        func()
        print("=== 函数执行后 ===")
    return wrapper


@my_decorator
def say_hello():
    print("Hello, World!")


if __name__ == "__main__":
    say_hello()