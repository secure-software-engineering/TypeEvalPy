# Functions are assigned to variables via starred assignment
def func1():
    return 'vndtn'


def func2():
    return (15, 50, 67)


def func3():
    return 15


def func4():
    return 93.27

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
