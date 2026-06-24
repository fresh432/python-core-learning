# 列表推导式: 一次性计算所有, 内存占用大
list_comp = [x**2 for x in range(1000000)]
print(f"列表大小: {len(list_comp)}")

# 生成器表达式: 惰性求值, 几乎不占用内存
gen_exp = (x**2 for x in range(1000000))
print(f"生成器类型: {type(gen_exp)}")

# 需要时逐个获取
print(next(gen_exp)) # 0
print(next(gen_exp)) # 1
print(next(gen_exp)) # 4

# 生成器只能遍历一次
gen_exp2 = (x**2 for x in range(5))
print(list(gen_exp2)) # [0, 1, 4, 9, 16]
print(list(gen_exp2)) # [], 已耗尽







# 实用场景(文件读取生成器)
def read_large_file(file_path):
    """逐行读取大文件, 内存友好"""
    with open(file_path, 'r', encoding="utf-8") as f:
        for line in f:
            yield line.strip() # 逐行返回, 不一次性加载

# 使用场景: 处理大日志文件
# def process(line):
#     if "ERROR" in line:
#         print(f"发现错误日志: {line}")

# for line in read_large_file("huge.log"):
#     process(line)