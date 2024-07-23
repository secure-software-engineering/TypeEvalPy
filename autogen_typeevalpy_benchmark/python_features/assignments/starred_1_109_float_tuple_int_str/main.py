# Functions are assigned to variables via starred assignment
def func1():
    return 15.72


def func2():
    return (5, 1, 89)


def func3():
    return 87


def func4():
    return 'dbxyw'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
