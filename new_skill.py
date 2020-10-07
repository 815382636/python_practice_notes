import re
import json

# 替换标点和换行符
from functools import reduce

content = "r12r403fwntegg!<zewf,>lfe;wfl ewl;flwe'"
content = re.sub(r'[^\w ]', '', content)
print(content)

# ----------------------------------------------------------------------
# json的序列化
# json.loads json.dumps  针对于字符串
# json.load json.dump   针对于文件

params = {
    'symbol': '123456',
    'type': 'limit',
    'price': 123.4,
    'amount': 23
}

with open('params.json', 'w') as fout:
    params_str = json.dump(params, fout)

with open('params.json', 'r') as fin:
    original_params = json.load(fin)

# -----------------------------------------------------------------------
# 字符串的格式化
print(f"你是{3+2}")

# ---------------------------------------------------------------------------
# 返回元素及索引
l = [2, 434, 5, 465, 3]
for i, v in enumerate(l):
    print(f"第{i}个元素是{v}", end="\t")

# ------------------------------------------------------------------------
# 条件与循环简化
# expression1 if condition else expression2 for item in iterable
# expression for item in iterable if condition

# [(xx, yy) for xx in x for yy in y if xx != yy]


# -------------------------------------------------------------------------
# 处理异常
try:
    s = input('please enter two numbers separated by comma: ')
    num1 = int(s.split(',')[0].strip())
    num2 = int(s.split(',')[1].strip())
    ...
except ValueError as err:
    print('Value Error: {}'.format(err))
except IndexError as err:
    print('Index Error: {}'.format(err))
except Exception as err:
    print('Other error: {}'.format(err))

print('continue')

# ------------------------------------------------------------
# 函数 函数内部修改全局变量

MIN_VALUE = 1
MAX_VALUE = 10


def validation_check(value):
    global MIN_VALUE
    ...
    MIN_VALUE += 1
    ...


validation_check(5)


# 内部函数修改外部函数变量

def outer():
    x = "local"

    def inner():
        nonlocal x  # nonlocal关键字表示这里的x就是外部函数outer定义的变量x
        x = 'nonlocal'
        print("inner:", x)

    inner()
    print("outer:", x)


outer()


# -----------------------------------------------------
# 闭包

def nth_power(exponent):
    def exponent_of(base):
        return base ** exponent

    return exponent_of  # 返回值是exponent_of函数


square = nth_power(2)  # 计算一个数的平方
cube = nth_power(3)  # 计算一个数的立方

print(square(2))  # 计算2的平方
print(cube(2))  # 计算2的立方

# ------------------------------------------------------
# lambda
print([(lambda x: x * x)(x) for x in range(10)])

l = [(1, 20), (3, 0), (9, 10), (2, -1)]
l.sort(key=lambda x: x[1])  # 按列表中元组的第二个元素排序
print(l)

# --------------------------------------------------------
# 函数式编程

l = [1, 2, 3, 4, 5]
new_list = map(lambda x: x * 2, l)  # [2， 4， 6， 8， 10]
new_list = filter(lambda x: x % 2 == 0, l)  # [2, 4]
product = reduce(lambda x, y: x * y, l)  # 1*2*3*4*5 = 120
