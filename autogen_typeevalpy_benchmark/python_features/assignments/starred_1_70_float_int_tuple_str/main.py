# Functions are assigned to variables via starred assignment
def func1():
    return 25.19


def func2():
    return 54


def func3():
    return (4, 43, 67)


def func4():
    return 'lzdja'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
