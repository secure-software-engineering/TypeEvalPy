# Functions are assigned to variables via starred assignment
def func1():
    return 89


def func2():
    return (15, 39, 59)


def func3():
    return 'zrlfr'


def func4():
    return 47.77

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
