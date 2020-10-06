# with 语句
# open() 函数对应于 close() 函数，也就是说，如果你打开了文件，在完成读取任务后，就应该立刻关掉它。
# 而如果你使用了 with 语句，就不需要显式调用 close()。
# 在 with 的语境下任务执行完毕后，close() 函数会被自动调用，代码也简洁很多。
# 最后需要注意的是，所有 I/O 都应该进行错误处理。
# 因为 I/O 操作可能会有各种各样的情况出现，而一个健壮（robust）的程序，需要能应对各种情况的发生，
# 而不应该崩溃（故意设计的情况除外）。


# 首先，我们要清楚 NLP 任务的基本步骤，也就是下面的四步：
# 读取文件；去除所有标点符号和换行符，并把所有大写变成小写；
# 合并相同的词，统计每个词出现的频率，并按照词频从大到小排序；
# 将结果按行输出到文件 out.txt。
import re
import json


def deal_with_content(content):
    # 替换标点和换行符
    content = re.sub(r'[^\w ]', ' ', content)
    content = content.lower()
    content_list = content.split(" ")
    content_list = filter(None, content_list)
    word_dic = {}
    for i in content_list:
        if word_dic.get(i):
            word_dic[i] = word_dic[i] + 1
        else:
            word_dic[i] = 1
    word_dic = sorted(word_dic.items(), key=lambda kv: kv[1], reverse=True)
    return word_dic


with open("in.txt", "r") as file:
    content = file.read()
    word_dic = deal_with_content(content)
    with open("out.txt", "w") as write_file:
        for k, v in word_dic:
            write_file.write(f"{k},{v}\n")

# json的序列化
# json.loads json.dumps  针对于字符串
# json.load json.dump   针对于文件

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
