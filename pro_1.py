#
#
# python学习笔记
#
# 一、
# 列表和元组基础
# 	列表是动态的，长度大小不固定，可以随意地增加、删减或者改变元素（mutable）。
#   而元组是静态的，长度大小固定，无法增加删减或者改变（immutable）。
#
# 	Python 中的列表和元组都支持负数索引。
# 	列表和元组都支持切片操作。 l[1:3]
# 	两者也可以通过 list() 和 tuple() 函数相互转换
#
# 	count(item) 表示统计列表 / 元组中 item 出现的次数。index(item) 表示返回列表 /
#   元组中 item 第一次出现的索引。list.reverse() 和 list.sort() 分别表示原地倒转列表和排序（注意，元组没有内置的这两个函数)。
#   reversed() 和 sorted() 同样表示对列表 / 元组进行倒转和排序，reversed() 返回一个倒转后的迭代器（上文例子使用 list() 函数再将其转换为列表）；sorted() 返回排好序的新列表

# 元组不能增添与删除元素，列表可以
tup =(1,2,3,4)
tup1 =tup + (5,)
print(tup1)
list =[1,2,3,4]
list.append(5)
print(list)

# 元组和列表都支持负数索引
print(tup1[-1])
print(list[-1])

# 元组和列表都支持切片操作
print(tup1[1:3])
print(list[1:3])

# 元组和列表都可以随意嵌套
l =[(1,2),5]
print(l)
t =([1,2],5)
print(t)

# 元组和列表可以互相切换
# print(list(tup1))   -----------出现错误，因为使用了list变量
print(tuple(list))

# 列表和元组的内置函数   count 出现次数  index 第一次索引  reverse反转  sort排序
print(list.count(3))
print(list.index(3))
list.reverse()
print(list)
list.sort()
print(list)
# print(list(reversed(tup1)))
print(sorted(tup1))


# 列表比元组分配的空间要多，存储指针
l = [1, 2, 3]
print(l.__sizeof__())

tup = (1, 2, 3)
print(tup.__sizeof__())



# l = []
# l.__sizeof__() // 空列表的存储空间为40字节
# 40
# l.append(1)
# l.__sizeof__()
# 72 // 加入了元素1之后，列表为其分配了可以存储4个元素的空间 (72 - 40)/8 = 4
# l.append(2)
# l.__sizeof__()
# 72 // 由于之前分配了空间，所以加入元素2，列表空间不变
# l.append(3)
# l.__sizeof__()
# 72 // 同上
# l.append(4)
# l.__sizeof__()
# 72 // 同上
# l.append(5)
# l.__sizeof__()
# 104 // 加入元素5之后，列表的空间不足，所以又额外分配了可以存储4个元素的空间

# 为了减小每次增加 / 删减操作时空间分配的开销，Python 每次分配空间时都会额外多分配一些，
# 这样的机制（over-allocating）保证了其操作的高效性：增加 / 删除的时间复杂度均为 O(1)。




