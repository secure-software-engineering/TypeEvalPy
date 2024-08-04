# Functions are assigned to variables via starred assignment
def func1():
    return 'drdtk'


def func2():
    return 19


def func3():
    return 42.32


def func4():
    return (65, 17, 20)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
