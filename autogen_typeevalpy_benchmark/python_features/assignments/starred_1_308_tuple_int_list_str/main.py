# Functions are assigned to variables via starred assignment
def func1():
    return (86, 28, 25)


def func2():
    return 42


def func3():
    return [51, 72, 94]


def func4():
    return 'vfldt'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
