class Integer:
    # после создания экземпляра(instance) класса Integer, автоматически срабатывает метод __set_name__
    # owner - ссылка на класс Point3D
    def __set_name__(self, owner, name: str) -> None:
        self.name = ''.join(('_', name))

    def __get__(self, instance, owner):
        # owner - ссылка на класс Point3D
        # self - ссылается на экз. класса Integer
        # instanse - ссылается на экз. класса Point3D
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        # обращаемся к словарю __dict__ (отвечает за формирование всех локальных свойств экземпляра класса)
        # self - ссылается на экз. класса Integer
        # instanse - ссылается на экз. класса Point3D
        instance.__dict__[self.name] = value


class Point3D:
    # x, y, z - дескрипторы
    x = Integer()
    y = Integer()
    z = Integer()

    # после создания экземпляра класса Point3D, срабатывает инициализатор(конструктор),
    # в инициализаторе происходит обращение к дескрипторам класса (x, y, z) и присваивается значения
    # которые передаются в аргументах конструктора, в момент присваивания срабатывает метод __set__
    # self - ссылается на экз. класса Integer
    # instanse - ссылается на экз. класса Point3D
    #
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # @classmethod
    # def verify_coord(cls, coord):
    #     if type(coord) is not int:
    #         raise TypeError('Coordinates must be an integer')
    #
    # @property
    # def x(self):
    #     return self._x
    #
    # @x.setter
    # def x(self, coord):
    #     self.verify_coord(coord)
    #     self._x = coord
    #
    # @property
    # def y(self):
    #     return self._y
    #
    # @y.setter
    # def y(self, coord):
    #     self.verify_coord(coord)
    #     self._y = coord
    #
    # @property
    # def z(self):
    #     return self._z
    #
    # @z.setter
    # def z(self, coord):
    #     self.verify_coord(coord)
    #     self._z = coord


p = Point3D(1, 2, 3)
print(p.__dict__)