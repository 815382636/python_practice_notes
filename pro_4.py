#python黑箱：输入与输出

#input() 函数暂停程序运行，同时等待键盘输入；直到回车被按下，函数的参数即为提示语，输入的类型永远是字符串型（str）。
#print() 函数则接受字符串、数字、字典、列表甚至一些自定义类的输出。

#生产环境中，强制类型转换加上try，except


#文件输入输出
#      NLP（自然语言处理）

#读取文件；
# 去除所有标点符号和换行符，并把所有大写变成小写；
# 合并相同的词，统计每个词出现的频率，并按照词频从大到小排序；
# 将结果按行输出到文件 out.txt。

import re

def parse(text):
    # 使用正则表达式去除标点符号和换行符
    text = re.sub(r'[^\w ]', ' ', text)

    # 转为小写
    text = text.lower()

    # 生成所有单词的列表
    word_list = text.split(' ')

    # 去除空白单词
    word_list = filter(None, word_list)

    # 生成单词和词频的字典
    word_cnt = {}
    for word in word_list:
        if word not in word_cnt:
            word_cnt[word] = 0
        word_cnt[word] += 1

    # 按照词频排序
    sorted_word_cnt = sorted(word_cnt.items(), key=lambda kv: kv[1], reverse=True)

    return sorted_word_cnt


with open('in.txt', 'r') as fin:
    text = fin.read()


word_and_freq = parse(text)

with open('out.txt', 'w') as fout:
    for word, freq in word_and_freq:
        fout.write('{} {}\n'.format(word, freq))



#JSON序列化


import json

params = {
    'symbol': '123456',
    'type': 'limit',
    'price': 123.4,
    'amount': 23
}

params_str = json.dumps(params)

print('after json serialization')
print('type of params_str = {}, params_str = {}'.format(type(params_str), params))

original_params = json.loads(params_str)

print('after json deserialization')
print('type of original_params = {}, original_params = {}'.format(type(original_params), original_params))
print("-----------------------------------------------------------------------------")


#文件JSON

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

print('after json deserialization')
print('type of original_params = {}, original_params = {}'.format(type(original_params), original_params))


#剩下两个问题，谷歌工具Protocol Buffer和  如何读取大信息量的文件

#读取大文件

large_size =100

with open("in.txt","r")as fin:
    text =""
    while True:
        str =fin.read(large_size)
        if not str:
            break
        text +=str
    # print(text)