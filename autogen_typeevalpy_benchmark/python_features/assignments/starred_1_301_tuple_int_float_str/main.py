# Functions are assigned to variables via starred assignment
def func1():
    return (25, 51, 42)


def func2():
    return 32


def func3():
    return 95.59


def func4():
    return 'eixbj'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
