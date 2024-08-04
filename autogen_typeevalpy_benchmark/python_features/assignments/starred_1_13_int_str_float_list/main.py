# Functions are assigned to variables via starred assignment
def func1():
    return 14


def func2():
    return 'lcnkz'


def func3():
    return 52.22


def func4():
    return [55, 15, 11]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
