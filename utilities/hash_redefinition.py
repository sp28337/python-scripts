class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)
print(id(p1), id(p2), sep='\n')
print(hash(p1), hash(p2))

d = {}
d[p1] = 1
d[p2] = 2
print(d)