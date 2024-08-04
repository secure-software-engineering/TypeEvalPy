# Functions are assigned to variables via starred assignment
def func1():
    return 'thzhu'


def func2():
    return 95


def func3():
    return 97.4


def func4():
    return [77, 76, 13]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
