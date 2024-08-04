# Functions are assigned to variables via starred assignment
def func1():
    return 39


def func2():
    return [86, 96, 49]


def func3():
    return 'uipoi'


def func4():
    return {'fdwkq': 26, 'swsfg': 2, 'xvxjs': 12}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
