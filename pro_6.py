#自定义函数


#1.函数参数可以设置默认值
# 例：def func(param = 0)  ----------------当传参时覆盖

#2.Python 是 dynamically typed 的，可以接受任何数据类型（整型，浮点，字符串等等），因此生产环境中一般要进行数据类型判断
#  if not isinstance(l, list):
#      print('input is not type of list')

#3.Python支持函数嵌套
#def f1():
#  print('hello')
#  def f2():
#     print('world')
# f2()

#函数嵌套的优势：
#  （1）保证内部函数的隐私
#  （2）合理的使用函数嵌套，能够提高程序的运行效率

#求阶乘，下面程序使用了函数嵌套，外部函数进行了类型判断，内部函数进行运算，如果不进行函数嵌套，那么每一步的递归都需要进行类型判断，降低了运行效率
def factorial(input):
    # validation check
    if not isinstance(input, int):
        raise Exception('input must be an integer.')
    if input < 0:
        raise Exception('input must be greater or equal to 0' )
    ...

    def inner_factorial(input):
        if input <= 1:
            return 1
        return input * inner_factorial(input-1)
    return inner_factorial(input)

#4.局部变量与全局变量
#     （1）我们不能在函数内部随意改变全局变量的值。
#要修改全局变量的值，需要在函数内部用global再重新声明一遍
MIN_VALUE = 1
MAX_VALUE = 10
def validation_check(value):
    global MIN_VALUE
    ...
    MIN_VALUE += 1
    ...

#     （2）同样的，对于嵌套函数来说，里面的函数不能修改外部函数变量的值
#要修改外部函数变量的值，需要在里面的函数内部用nonlocal再声明一遍
def outer():
    x = "local"
    def inner():
        nonlocal x # nonlocal关键字表示这里的x就是外部函数outer定义的变量x
        x = 'nonlocal'
        print("inner:", x)
    inner()
    print("outer:", x)


#5.闭包
#闭包常常和装饰器（decorator）一起使用。

def nth_power(exponent):
    def exponent_of(base):
        return base**exponent
    return exponent_of

square =nth_power(2)      #求2的平方
cube =nth_power(3)        #求2的立方

print(square(2))
print(cube(2))










