# Functions are assigned to variables via starred assignment
def func1():
    return 55


def func2():
    return (19, 32, 64)


def func3():
    return 9.15


def func4():
    return 'lgdqm'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()