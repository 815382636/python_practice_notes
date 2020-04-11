#运用面向对象的方法实现一个搜索引擎

#一个搜索引擎由搜索器、索引器、检索器和用户接口四个部分组成。
#搜索器，通俗来讲就是我们常提到的爬虫（scrawler），它能在互联网上大量爬取各类网站的内容，送给索引器。
#索引器拿到网页和内容后，会对内容进行处理，形成索引（index），存储于内部的数据库等待检索。
#最后的用户接口很好理解，是指网页和 App 前端界面，例如百度和谷歌的搜索页面。
#用户通过用户接口，向搜索引擎发出询问（query），询问解析后送达检索器；检索器高效检索后，再将结果返回给用户。


#  1. 建立了5个txt文件，（1.txt~5.txt）

#  2. 定义 SearchEngineBase 基类
class SearchEngineBase(object):
    def __init__(self):
        pass

    #add_corpus() 函数负责读取文件内容，将文件路径作为 ID，连同内容一起送到 process_corpus 中。
    def add_corpus(self, file_path):
        with open(file_path, 'r') as fin:
            text = fin.read()
        self.process_corpus(file_path, text)

    #process_corpus 需要对内容进行处理，然后文件路径为 ID ，将处理后的内容存下来。处理后的内容，就叫做索引（index）。
    def process_corpus(self, id, text):
        raise Exception('process_corpus not implemented.')

    #search 则给定一个询问，处理询问，再通过索引检索，然后返回。
    def search(self, query):
        raise Exception('search not implemented.')

#main() 函数提供搜索器和用户接口
def main(search_engine):
    for file_path in ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt']:
        search_engine.add_corpus(file_path)

    while True:
        query = input("please write you want:")
        results = search_engine.search(query)
        print('found {} result(s):'.format(len(results)))
        for result in results:
            print(result)


class SimpleEngine(SearchEngineBase):
    def __init__(self):
        super(SimpleEngine, self).__init__()
        self.__id_to_texts = {}

    def process_corpus(self, id, text):
        self.__id_to_texts[id] = text

    def search(self, query):
        results = []
        for id, text in self.__id_to_texts.items():
            if query in text:
                results.append(id)
        return results
#仅能对单词或连在一起的句子进行搜索
#search_engine = SimpleEngine()
#main(search_engine)


#--------------------------------------------

import re

# 词袋模型，可以对不连在一起的句子进行搜索
class BOWEngine(SearchEngineBase):
    def __init__(self):
        super(BOWEngine, self).__init__()
        self.__id_to_words = {}

    def process_corpus(self, id, text):
        self.__id_to_words[id] = self.parse_text_to_words(text)

    def search(self, query):
        query_words = self.parse_text_to_words(query)
        results = []
        for id, words in self.__id_to_words.items():
            if self.query_match(query_words, words):
                results.append(id)
        return results

    @staticmethod
    def query_match(query_words, words):
        for query_word in query_words:
            if query_word not in words:
                return False
        return True

    @staticmethod
    def parse_text_to_words(text):
        # 使用正则表达式去除标点符号和换行符
        text = re.sub(r'[^\w ]', ' ', text)
        # 转为小写
        text = text.lower()
        # 生成所有单词的列表
        word_list = text.split(' ')
        # 去除空白单词
        word_list = filter(None, word_list)
        # 返回单词的 set
        return set(word_list)


search_engine = BOWEngine()
main(search_engine)


#-----------------------景霄第12课

