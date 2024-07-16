import time


def timer(func):
    def wrapped(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        difference = round(end - start, 6)
        print('Time running of function {name}: {time}'.format(name=func.__name__,
                                                               time=difference))
        return res

    return wrapped


@timer
def get_nod(a, b):                  # SLOW version
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


@timer
def get_fast_nod(a, b):              # FAST version
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a


res = get_nod(2, 100000)
res2 = get_fast_nod(2, 100000)
print(res)
print(res2)
