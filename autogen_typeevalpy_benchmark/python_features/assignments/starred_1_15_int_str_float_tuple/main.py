# Functions are assigned to variables via starred assignment
def func1():
    return 8


def func2():
    return 'sftgy'


def func3():
    return 38.49


def func4():
    return (61, 78, 67)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
