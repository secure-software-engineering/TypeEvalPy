# Functions are assigned to variables via starred assignment
def func1():
    return 'anfds'


def func2():
    return 33


def func3():
    return (67, 76, 98)


def func4():
    return 32.94

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
