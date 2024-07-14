class DataBase:
    # ссылка на экземпляр класса
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        # если объект будет удалён сборщиком мусора, то атрибут __instance
        # вновь примет значение None и мы снова сможем создать объект
        DataBase.__instance = None

    def __init__(self, user, password, port):
        self.user = user
        self.password = password
        self.port = port

    def connect(self):
        print(f'connecting with DataBase: {self.user}, {self.password}, {self.port}')

    def close(self):
        print('closing connection...')

    def read(self):
        return 'data from DataBase'

    def write(self, data):
        print(f'writing into DataBase: {data}')


db = DataBase('root','1234', 80)
db2 = DataBase('root2','5678', 40)

print(id(db), id(db2))

db.connect()
db2.connect()