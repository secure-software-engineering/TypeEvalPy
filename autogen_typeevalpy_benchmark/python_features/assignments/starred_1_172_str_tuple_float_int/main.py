# Functions are assigned to variables via starred assignment
def func1():
    return 'fngza'


def func2():
    return (27, 75, 2)


def func3():
    return 61.28


def func4():
    return 34

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
