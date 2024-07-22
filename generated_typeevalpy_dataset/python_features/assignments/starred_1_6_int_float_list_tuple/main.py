# Functions are assigned to variables via starred assignment
def func1():
    return 27


def func2():
    return 31.52


def func3():
    return [23, 99, 33]


def func4():
    return (21, 5, 27)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
