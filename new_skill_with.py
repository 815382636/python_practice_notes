class DBConnectionManager:
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
        self.connection = None

    def __enter__(self):
        self.connection = DBClient(self.hostname, self.port)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()


with DBConnectionManager('localhost', '8080') as db_client:
    pass


class FileManager:
    def __init__(self, name, mode):
        print('calling __init__ method')
        self.name = name
        self.mode = mode
        self.file = None

    def __enter__(self):
        print('calling __enter__ method')
        self.file = open(self.name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('calling __exit__ method')
        if self.file:
            self.file.close()


with FileManager('test.txt', 'w') as f:
    print('ready to write to file')
    f.write('hello world')
