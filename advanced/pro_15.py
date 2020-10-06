# 迭代器与生成器


# 在 Python 中一切皆对象，对象的抽象就是类，而对象的集合就是容器。
# 所有的容器都是可迭代的（iterable）。
# 迭代器（iterator）提供了一个 next 的方法。调用这个方法后，你要么得到这个容器的下一个对象，要么得到一个 StopIteration 的错误。
# 你不需要像列表一样指定元素的索引，因为字典和集合这样的容器并没有索引一说。
# 而可迭代对象，通过 iter() 函数返回一个迭代器，再通过 next() 函数就可以实现遍历。for in 语句将这个过程隐式化

#判断是否可迭代
def is_iterable(param):
    try:
        iter(param)
        return True
    except TypeError:
        return False


params = [
    1234,
    '1234',
    [1, 2, 3, 4],
    set([1, 2, 3, 4]),
    {1: 1, 2: 2, 3: 3, 4: 4},
    (1, 2, 3, 4)
]

for param in params:
    print('{} is iterable? {}'.format(param, is_iterable(param)))


# 生成器：生成器是懒人版本的迭代器。

# [i for i in range(100000000)]就可以生成一个包含一亿元素的列表。每个元素在生成后都会保存到内存中，
# 它们占用了巨量的内存，内存不够的话就会出现 OOM 错误。
list_1 = [i for i in range(100000000)]
print(sum(list_1))
# 生成器的概念:在你调用 next() 函数的时候，才会生成下一个变量。
# 生成器在 Python 的写法是用小括号括起来，(i for i in range(100000000))，即初始化了一个生成器。
# 生成器并不会像迭代器一样占用大量内存，只有在被使用的时候才会调用。而且生成器在初始化的时候，并不需要运行一次生成操作,因此耗时明显比迭代器短。
list_2 = (i for i in range(100000000))
print(sum(list_2))



def generator(k):
    i = 1
    while True:
        yield i ** k
        i += 1

gen_1 = generator(1) #--------------生成了一个生成器
gen_3 = generator(3) #--------------生成了一个生成器
print(gen_1)
print(gen_3)

def get_sum(n):
    sum_1, sum_3 = 0, 0
    for i in range(n):
        next_1 = next(gen_1) # ----------调用生成器的next指针
        next_3 = next(gen_3)
        print('next_1 = {}, next_3 = {}'.format(next_1, next_3))
        sum_1 += next_1
        sum_3 += next_3
    print(sum_1 * sum_1, sum_3)

get_sum(8)









