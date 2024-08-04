# Functions are assigned to variables via starred assignment
def func1():
    return (27, 39, 95)


def func2():
    return 94


def func3():
    return 'zgnjb'


def func4():
    return 22.22

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
