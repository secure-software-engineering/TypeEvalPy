# Functions are assigned to variables via starred assignment
def func1():
    return 86


def func2():
    return (39, 45, 46)


def func3():
    return 31.95


def func4():
    return 'rrsyk'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
