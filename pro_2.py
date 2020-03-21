
# 二、字典和集合
#   相比于列表和元组，字典的性能更优，特别是对于查找、添加和删除操作，字典都能在常数时间复杂度内完成。

di ={"name":"Liming","age":17}
print(di)
se ={1,2,3}
print(se)

# 访问使用get函数
print(di.get("name"))
print(di.get("a"))

#判断元素是否在集合中
print(1 in se)

#字典和集合的增加删除
di["location"] ="zibo"
di.pop("age")
print(di)

se.add(4)
se.remove(3)
print(se)

# 字典的升序排列
d_sorted_by_key =sorted(di.items(),key= lambda x:x[0])
print(d_sorted_by_key)
# 字典的降序排列 ，集合直接用sorted即可
d_sorted_by_key =sorted(di.items(),key= lambda x:x[1])
print(d_sorted_by_key)

# 由于集合是高度优化的哈希表，里面元素不能重复，并且其添加和查找操作只需 O(1) 的复杂度








