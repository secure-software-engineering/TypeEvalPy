# Functions are assigned to variables via starred assignment
def func1():
    return 'mnref'


def func2():
    return 39.28


def func3():
    return (36, 84, 29)


def func4():
    return 50

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
