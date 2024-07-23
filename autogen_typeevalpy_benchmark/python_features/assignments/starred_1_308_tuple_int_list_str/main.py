# Functions are assigned to variables via starred assignment
def func1():
    return (9, 27, 61)


def func2():
    return 66


def func3():
    return [28, 23, 16]


def func4():
    return 'dkrod'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
