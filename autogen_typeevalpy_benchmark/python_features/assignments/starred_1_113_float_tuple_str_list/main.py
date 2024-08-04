# Functions are assigned to variables via starred assignment
def func1():
    return 31.45


def func2():
    return (32, 28, 71)


def func3():
    return 'pclti'


def func4():
    return [34, 59, 39]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
