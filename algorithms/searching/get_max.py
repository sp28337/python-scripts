def get_max2(a, b):
    return a if a > b else b


def get_max3(a, b, c):
    return get_max2(a, get_max2(b, c))
 

x, y, z = 5, 7, 10
print(get_max2(x, get_max2(y, z)))
print(get_max3(x, y, z))
