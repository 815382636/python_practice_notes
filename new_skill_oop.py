# OOP
from abc import ABCMeta, abstractmethod


class Document():
    WELCOME_STR = 'Welcome! The context for this book is {}.'  # 常量大写

    def __init__(self, title, author, context):  # 构造函数
        print('init function called')
        self.title = title
        self.author = author
        self.__context = context  # 私有变量

    # 类函数
    @classmethod
    def create_empty_book(cls, title, author):
        return cls(title=title, author=author, context='nothing')

    # 成员函数
    def get_context_length(self):
        return len(self.__context)

    # 静态函数
    @staticmethod
    def get_welcome(context):
        return Document.WELCOME_STR.format(context)


# 抽象函数抽象类


class Entity(metaclass=ABCMeta):
    @abstractmethod
    def get_title(self):
        pass

    @abstractmethod
    def set_title(self, title):
        pass


class Document1(Entity):
    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

