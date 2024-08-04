# Functions are assigned to variables via starred assignment
def func1():
    return [24, 24, 51]


def func2():
    return 31.76


def func3():
    return 9


def func4():
    return (34, 63, 43)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
