import copy
import functools
import os
import psutil

# 浅拷贝和深拷贝
l1 = [[1, 2], (30, 40)]
l2 = copy.deepcopy(l1)


# ----------------------------------------------------------------
# Python 的参数传递是赋值传递 （pass by assignment），或者叫作对象的引用传递（pass by object reference）。
# Python 里所有的数据类型都是对象，所以参数传递时，只是让新变量与原变量指向相同的对象而已，
# 并不存在值传递或是引用传递一说。

# ----------------------------------------------------------------
# 装饰器

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('wrapper of decorator')
        func(*args, **kwargs)

    return wrapper


@my_decorator
def greet(message):
    print(message)


# 带自定义参数的装饰器

def repeat(num):
    def my_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(num):
                print('wrapper of decorator')
                func(*args, **kwargs)

        return wrapper

    return my_decorator


@repeat(4)
def greet(message):
    print(message)


# 类装饰器

class Count:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print('num of calls is: {}'.format(self.num_calls))
        return self.func(*args, **kwargs)


@Count
def example():
    print("hello world")


# -----------------------------------------------------------------------------
# 迭代器与生成器
# 生成器并不会像迭代器一样占用大量内存，只有在被使用的时候才会调用。
# 而且生成器在初始化的时候，并不需要运行一次生成操作，
# 相比于 test_iterator() ，test_generator() 函数节省了一次生成一亿个元素的过程，因此耗时明显比迭代器短。

# 显示当前 python 程序占用的内存大小
def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024
    print('{} memory used: {} MB'.format(hint, memory))


# 迭代器
def test_iterator():
    show_memory_info('initing iterator')
    list_1 = [i for i in range(100000000)]
    show_memory_info('after iterator initiated')
    print(sum(list_1))
    show_memory_info('after sum called')


# 生成器 中括号与小括号的问题
def test_generator():
    show_memory_info('initing generator')
    list_2 = (i for i in range(100000000))
    show_memory_info('after generator initiated')
    print(sum(list_2))
    show_memory_info('after sum called')


# example

def index_normal(L, target):
    result = []
    for i, num in enumerate(L):
        if num == target:
            result.append(i)
    return result


print(index_normal([1, 6, 2, 4, 5, 2, 8, 6, 3, 2], 2))


def index_generator(L, target):
    for i, num in enumerate(L):
        if num == target:
            yield i


print(list(index_generator([1, 6, 2, 4, 5, 2, 8, 6, 3, 2], 2)))
