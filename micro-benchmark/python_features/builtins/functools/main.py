#
from functools import reduce


def multiply(x, y):
    return x * y


numbers = [1, 2, 3, 4, 5]
product = reduce(multiply, numbers)
