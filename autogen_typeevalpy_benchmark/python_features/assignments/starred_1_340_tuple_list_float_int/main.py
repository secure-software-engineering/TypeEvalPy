# Functions are assigned to variables via starred assignment
def func1():
    return (97, 43, 8)


def func2():
    return [87, 68, 70]


def func3():
    return 65.07


def func4():
    return 70

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
