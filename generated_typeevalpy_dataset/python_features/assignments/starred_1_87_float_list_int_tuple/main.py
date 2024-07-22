# Functions are assigned to variables via starred assignment
def func1():
    return 42.88


def func2():
    return [47, 55, 99]


def func3():
    return 72


def func4():
    return (14, 30, 13)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
