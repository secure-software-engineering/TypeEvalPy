# Functions are assigned to variables via starred assignment
def func1():
    return 49


def func2():
    return 9.61


def func3():
    return 'ievkp'


def func4():
    return (39, 25, 79)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
