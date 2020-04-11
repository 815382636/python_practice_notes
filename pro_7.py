#匿名函数 lambda

#1.lambda的简单用法
#求2的平方
square =lambda x:x**2
print(square(2))

#2.lambda主要用途是减少代码的复杂度。
# 需要注意的是 lambda 是一个表达式，并不是一个语句；
# 它只能写成一行的表达形式，语法上并不支持多行。
# 匿名函数通常的使用场景是：程序中需要使用一个函数完成一个简单的功能，并且该函数只调用一次。

#输出10以内的数的平方
print([(lambda x: x*x)(x)for x in range(10)])

# 按列表中元组的第二个元素排序
l = [(1, 20), (3, 0), (9, 10), (2, -1)]
l.sort(key=lambda x: x[1])
print(l)

#3.Python函数式编程
#所谓函数式编程，是指代码中每一块都是不可变的（immutable），都由纯函数（pure function）的形式组成。
# 这里的纯函数，是指函数本身相互独立、互不影响，对于相同的输入，总会有相同的输出，没有任何副作用。

#以下不是纯函数，因为函数在传入的列表上进行修改，会对原参进行修改
def multiply_2(l):
    for index in range(0, len(l)):
        l[index] *= 2
    return l
#以下是纯函数
def multiply_2_pure(l):
    new_list = []
    for item in l:
        new_list.append(item * 2)
    return new_list


#4. 函数式编程的优点，主要在于其纯函数和不可变的特性使程序更加健壮，易于调试（debug）和测试；缺点主要在于限制多
#Python 主要提供了这么几个函数：map()、filter() 和 reduce()，通常结合匿名函数 lambda 一起使用。

# （1）map(function, iterable) 函数 ,map后是map类型，不要忘了强制类型转换
l =[1,2,3,4,5]
l_double =map(lambda x:x*2,l)
print(list(l_double))

#  （2）filter(function, iterable) 函数
l = [1, 2, 3, 4, 5]
new_list = filter(lambda x: x % 2 == 0, l) # [2, 4]
print(list(new_list))

#  (3)reduce(function, iterable) 函数，它通常用来对一个集合做一些累积操作   reduce需要从functools库中导入
from functools import reduce
l = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, l) # 1*2*3*4*5 = 120
print(product)
