# A program demonstrating the use of the reduce() function from the functools module in Python.
from functools import reduce


def multiply(x, y):
    return x * y


numbers = [<value1>, <value1>]
product = reduce(multiply, numbers)
