#条件与循环

#字典的遍历
di = {"name":"zhangwei","year":13,"school":"qwe"}
for key in di.keys():
    print(key +"---")
for k,v in di.items():
    print(f"key ={k},value={v}")
for value in di.values():
    print(f"value ={value}")

#range的运用

l = [1, 2, 3, 4, 5, 6, 7]
for index in range(0, len(l)):
    if index < 5:
        print(l[index])

#Python 内置的函数 enumerate()。用它来遍历集合，不仅返回每个元素，并且还返回其对应的索引

for i,v  in enumerate(l):# i 是索引，v是i的值
    if i<5:
        print(v)

#运用continue、break来是代码更加精炼与简洁


# for和while语句的效率问题
#range() 函数是直接由 C 语言写的，调用它速度非常快。
# 而 while 循环中的“i += 1”这个操作，得通过 Python 的解释器间接调用底层的 C 语言；
# 并且这个简单的操作，又涉及到了对象的创建和删除（因为 i 是整型，是 immutable，i += 1 相当于 i = new int(i + 1)）。
# 所以，显然，for 循环的效率更胜一筹。

#条件与循环进阶


#expression1 if condition else expression2 for item in iterable
#与下面的相等
# for item in iterable:
#     if condition:
#         expression1
#     else:
#         expression2

#expression for item in iterable if condition   没有else的情况


# 将长度小于5的单词分割并打印
text = ' Today, is, Sunday'
text_sp =[s.strip() for s in text.split(",")if len(s)>5]
print(text_sp)


attributes = ['name', 'dob', 'gender']
values = [['jason', '2000-01-01', 'male'], ['mike', '1999-01-01', 'male'],['nancy', '2001-02-01', 'female']]
print([dict(zip(attributes, value)) for value in values])

# di[i]=j for i in attributes for j in values

