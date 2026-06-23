"""
闭包基础练习
学习要点：嵌套函数、外部变量引用、延迟执行

闭包三要素：
1. 嵌套函数（函数内部定义函数）
2. 外部变量引用（内部函数使用外部变量）
3. 返回函数对象（不执行，延迟调用）
"""

def outer_func(msg):
    """
    外部函数：负责接收参数并定义内部函数。
    这里的 msg 就是被内部函数引用的【外部变量】
    :return: 返回函数对象 inner_func
    """
    # 1. 嵌套函数: 在函数内部定义的函数
    def inner_func(msg2):
        # 2. 外部变量引用: 内部函数没有定义msg,而是记住了外部函数的msg
        print(f"{msg}, {msg2}!")

    # 3. 延时执行: 这里返回的是函数对象 inner_func, 而不是执行后的结果
    return inner_func

# 测试与验证
# 1. 调用外部函数, 传入参数, 得到内部函数(此时内部函数并没有被执行)
say_hello = outer_func("Hello")
say_hi = outer_func("Hi")

# 2. 调用内部函数, 输出结果
say_hello("world")
say_hi("Python")

# 使用闭包实现ATM小案例
def account_create(initial_amount=0):
    """
     创建账户，返回 ATM 操作函数
     余额被闭包保护，外部无法直接修改
     """
    def atm(num, deposit=True):
        nonlocal initial_amount

        # 边界检查
        if num < 0:
            print("金额不能为负数")
            return

        if not deposit and initial_amount < num:
            print(f"余额不足，当前余额: {initial_amount}")
            return

        if deposit:
            initial_amount += num
            print(f"存款, +{num}, 账户余额: {initial_amount}")
        else:
            initial_amount -= num
            print(f"取款, -{num}, 账户余额: {initial_amount}")
    return atm

atm = account_create()

atm(100)
atm(200)
atm(500, False)



