# Functions are assigned to variables via starred assignment
def func1():
    return 16.5


def func2():
    return (51, 77, 94)


def func3():
    return 60


def func4():
    return [90, 98, 20]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
