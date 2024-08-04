# Functions are assigned to variables via starred assignment
def func1():
    return 'upefc'


def func2():
    return [36, 80, 70]


def func3():
    return 23


def func4():
    return 52.48

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
