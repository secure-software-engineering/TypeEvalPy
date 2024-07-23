# Functions are assigned to variables via starred assignment
def func1():
    return 32


def func2():
    return [55, 48, 90]


def func3():
    return 39.54


def func4():
    return (55, 56, 35)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
