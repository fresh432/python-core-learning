"""
生成器基础练习
学习要点：yield、惰性求值、状态保存
"""

def simple_generator():
    """最简单的生成器"""
    print("开始")
    yield 1
    print("继续")
    yield 2
    print("结束")
    yield 3

# 测试
gen = simple_generator()
print(type(gen)) # <class 'generator'>

# 逐个获取
print(next(gen)) # 开始 -> 1
print(next(gen)) # 继续 -> 2
print(next(gen)) # 结束 -> 3

# 继续调用就会报错了
# print(next(gen)) # StopIteration

# 用 for 循环 (可以自动处理 StopIteration)
print("\n--- for 循环 ---")
for value in simple_generator():
    print(value)




# 斐波那契生成器
def fb(n):
    """生成前 n 个斐波那契数"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
    
# 测试
print("--- 斐波那契 ---")
for num in fb(10):
    print(num, end=" ")
print()