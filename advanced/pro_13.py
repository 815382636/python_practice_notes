# python装饰器

# 所谓的装饰器，其实就是通过装饰器函数，来修改原函数的一些功能，使得原函数不需要修改。
# 而实际工作中，装饰器通常运用在身份认证、日志记录、输入合理性检查以及缓存等多个领域中。合理使用装饰器，往往能极大地提高程序的可读性以及运行效率。


# 简单的装饰器
def my_decorator(func):
    def wrapper():
        print('wrapper of decorator')
        func()
    return wrapper

@my_decorator
def greet():
    print('hello world')

greet()

print("---------------------------------------------")

# 带参数的装饰器
def my_decorator1(func):
    def wrapper(message):
        print(f'message :{message}')
        func(message)
    return wrapper

@my_decorator1
def greet(message):
    print(message)

greet("hello world")


# 带多个参数的装饰器 *args, **kwargs


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('wrapper of decorator')
        func(*args, **kwargs)
    return wrapper

# 通过装饰器定义执行次数

def repeat(num):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num):
                print('wrapper of decorator')
                func(*args, **kwargs)
        return wrapper
    return my_decorator


@repeat(4)
def greet(message):
    print(message)

greet('hello world')


# 你会发现，greet() 函数被装饰以后，它的元信息变了。
# 元信息告诉我们“它不再是以前的那个 greet() 函数，而是被 wrapper() 函数取代了”。
# 为了解决这个问题，我们通常使用内置的装饰器@functools.wrap，它会帮助保留原函数的元信息（也就是将原函数的元信息，拷贝到对应的装饰器函数里）。
import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('wrapper of decorator')
        func(*args, **kwargs)

    return wrapper


@my_decorator
def greet(message):
    print(message)

# 输出 'greet'
greet.__name__

#装饰器的嵌套

# @decorator1
# @decorator2
# @decorator3
# def func():
#     ...
# =================
# decorator1(decorator2(decorator3(func)))


#身份认证的装饰器

# def authenticate(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         request = args[0]
#         if check_user_logged_in(request):  # 如果用户处于登录状态
#             return func(*args, **kwargs)  # 执行函数post_comment()
#         else:
#             raise Exception('Authentication failed')
#
#     return wrapper


# @authenticate
# def post_comment(request, ...)
#     ...


