class Clock:
    __DAY = 86_400

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError('Right operand must be <int> or <Clock>')
        sc = other if isinstance(other, int) else other.seconds
        return sc

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError('Argument must be an integer')
        self.seconds = seconds % self.__DAY

    def __add__(self, other):
        sc = self.__verify_data(other)
        return Clock(self.seconds + sc)

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        print('__iadd__')
        sc = self.__verify_data(other)
        self.seconds += sc
        return self

    def __eq__(self, other):
        sc = self.__verify_data(other)
        return self.seconds == sc

    def __lt__(self, other):
        sc = self.__verify_data(other)
        return self.seconds < sc

    def __le__(self, other):
        sc = self.__verify_data(other)
        return self.seconds <= sc

    def __str__(self):
        return f"{self.__class__}: {self.get_time()}"

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f'{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}'

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, '0')


c1 = Clock(1000)
c2 = Clock(1000)
c3 = Clock(3000)

print(c1 >= c3)
