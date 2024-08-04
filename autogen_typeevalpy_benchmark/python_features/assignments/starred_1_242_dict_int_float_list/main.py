# Functions are assigned to variables via starred assignment
def func1():
    return {'qklcj': 98, 'plgvo': 33, 'veeep': 34}


def func2():
    return 39


def func3():
    return 68.7


def func4():
    return [36, 98, 32]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
