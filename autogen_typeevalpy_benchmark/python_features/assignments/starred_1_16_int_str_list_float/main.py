# Functions are assigned to variables via starred assignment
def func1():
    return 52


def func2():
    return 'rcxsi'


def func3():
    return [6, 9, 88]


def func4():
    return 33.69

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
