import functools
import math
from functools import wraps


# Декоратор для вычисления производных произвольных функций
def df_decorator(dx=0.01):
    def func_decorator(func):
        @wraps(func)
        def wrapper(x, *args, **kwargs):

            res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
            return res

        return wrapper

    return func_decorator


@df_decorator(dx=0.0001) # dx - точность
def sin_df(x):
    """Функция для вычисления производной синуса"""
    return math.sin(x)


df = sin_df(math.pi/3)
print(df)
print(sin_df.__doc__)
print(sin_df.__name__)
