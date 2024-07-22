# Functions are assigned to variables via starred assignment
def func1():
    return 51


def func2():
    return [52, 100, 45]


def func3():
    return (96, 80, 35)


def func4():
    return 2.48

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
