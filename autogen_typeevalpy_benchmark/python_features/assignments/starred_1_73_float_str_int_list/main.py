# Functions are assigned to variables via starred assignment
def func1():
    return 97.58


def func2():
    return 'tdyzp'


def func3():
    return 85


def func4():
    return [83, 22, 62]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
