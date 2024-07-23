# A program demonstrating the use of the reduce() function from the functools module in Python.
from functools import reduce


def multiply(x, y):
    return x * y


numbers = [78, 78]
product = reduce(multiply, numbers)
