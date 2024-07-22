# A program demonstrating the use of the reduce() function from the functools module in Python.
from functools import reduce


def multiply(x, y):
    return x * y


numbers = [72.5, 72.5]
product = reduce(multiply, numbers)
