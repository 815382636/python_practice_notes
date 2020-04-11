#面向对象  (OOP),Object Oriented Programming


class Document(): #类
    def __init__(self, title, author, context):   #构造函数，初始化对象时会调用
        print('init function called')
        self.title = title
        self.author = author
        # __开头的属性是私有属性，如果一个属性以 __ （注意，此处有两个 _） 开头，我们就默认这个属性是私有属性。
        # 私有属性，是指不希望在类的函数之外的地方被访问和修改的属性。
        self.__context = context

    def get_context_length(self):
        return len(self.__context)

    def intercept_context(self, length):
        self.__context = self.__context[:length]

harry_potter_book = Document('Harry Potter', 'J. K. Rowling', '... Forever Do not believe any thing is capable of thinking independently ...')

#————————————————————————————————————————————————————————————————————————————————————————————————————————


class Document():
    WELCOME_STR = 'Welcome! The context for this book is {}.'  #用全大写来表示常量

    def __init__(self, title, author, context):
        print('init function called')
        self.title = title
        self.author = author
        self.__context = context

    # 类函数，类函数最常用的功能是实现不同的 init 构造函数
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


empty_book = Document.create_empty_book('What Every Man Thinks About Apart from Sex', 'Professor Sheridan Simove')

print(empty_book.get_context_length())
print(empty_book.get_welcome('indeed nothing'))


#类的继承----------------------------------------------------------------------------


class Entity():
    def __init__(self, object_type):
        print('parent class init called')
        self.object_type = object_type

    def get_context_length(self):
        raise Exception('get_context_length not implemented')

    def print_title(self):
        print(self.title)


class Document(Entity):
    def __init__(self, title, author, context):
        print('Document class init called')
        Entity.__init__(self, 'document')
        self.title = title
        self.author = author
        self.__context = context

    def get_context_length(self):
        return len(self.__context)


class Video(Entity):
    def __init__(self, title, author, video_length):
        print('Video class init called')
        Entity.__init__(self, 'video')
        self.title = title
        self.author = author
        self.__video_length = video_length

    def get_context_length(self):
        return self.__video_length


harry_potter_book = Document('Harry Potter(Book)', 'J. K. Rowling',
                             '... Forever Do not believe any thing is capable of thinking independently ...')
harry_potter_movie = Video('Harry Potter(Movie)', 'J. K. Rowling', 120)


#抽象函数与抽象类-----------------------------------------------------------------------


from abc import ABCMeta, abstractmethod


class Entity(metaclass=ABCMeta):
    @abstractmethod
    def get_title(self):
        pass

    @abstractmethod
    def set_title(self, title):
        pass


class Document(Entity):
    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title


document = Document()
document.set_title('Harry Potter')
print(document.get_title())

entity = Entity()