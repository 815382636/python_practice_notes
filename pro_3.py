#字符串


# f""的应用  *******************************************************************
# f-string用大括号 {} 表示被替换字段，其中直接填入替换内容
# f-string的大括号 {} 可以填入表达式或调用函数，Python会求出其结果并填入返回的字符串内
# f-string大括号内所用的引号不能和大括号外的引号定界符冲突，可根据情况灵活切换 ' 和 "
name ="123"
print(f"i don t {name}")
print(f"3+5={3+5}")


#字符串基础
# 字符串是由独立字符组成的一个序列，通常包含在单引号（''）双引号（""）或者三引号之中（''' '''或""" """，两者一样）

s1 ="hello"
s2 ='hello'
s3 ='''hello'''
print(s1 ==s2 ==s3)

#Python 的字符串同样支持索引，切片和遍历等等操作
# [index:index+2]则表示第 index 个元素到 index+1 个元素组成的子字符串。
# Python 的字符串是不可变的（immutable）
# Python 中字符串的改变，通常只能通过创建新的字符串来完成。

s ='H'+s1[1:]
print(s)
s =s1.replace('h','H')
print(s)

# python 中没有java的StringBuffer
# 每次想要改变字符串，往往需要 O(n) 的时间复杂度



s = ''
for n in range(0, 100000):
    s += str(n)
# 自从 Python2.5 开始，每次处理字符串的拼接操作时（str1 += str2），Python 首先会检测 str1 还有没有其他的引用。
# 如果没有的话，就会尝试原地扩充字符串 buffer 的大小，而不是重新分配一块内存来创建新的字符串并拷贝。
# 这样的话，上述例子中的时间复杂度就仅为 O(n) 了。

# 另外，对于字符串拼接问题，除了使用加法操作符，我们还可以使用字符串内置的 join 函数。
# string.join(iterable)，表示把每个元素都按照指定的格式连接起来。
#join函数比+=的速度稍快

#分割函数 split()
#string.strip(str)，表示去掉首尾的空格的字符串；


#字符串的格式化 format
id=1
name ='jack'
print("id ={}的同学叫{}".format(id,name))














