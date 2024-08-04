# Functions are assigned to variables via starred assignment
def func1():
    return 19.6


def func2():
    return 'vdogp'


def func3():
    return (46, 34, 13)


def func4():
    return 27

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
