# Functions are assigned to variables via starred assignment
def func1():
    return (40, 93, 49)


def func2():
    return 19.85


def func3():
    return [82, 50, 46]


def func4():
    return 86

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
