# Functions are assigned to variables via starred assignment
def func1():
    return 39


def func2():
    return 'lqjub'


def func3():
    return [1, 23, 73]


def func4():
    return (100, 47, 25)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
