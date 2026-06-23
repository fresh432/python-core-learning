"""
带参数的装饰器
学习要点：三层嵌套、装饰器工厂
"""

from functools import wraps

def repeat(times):
    """接收参数的装饰器工厂"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}")

if __name__ == "__main__":
    greet("World")