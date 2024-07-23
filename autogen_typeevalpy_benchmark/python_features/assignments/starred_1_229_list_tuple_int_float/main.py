# Functions are assigned to variables via starred assignment
def func1():
    return [59, 51, 20]


def func2():
    return (19, 52, 100)


def func3():
    return 83


def func4():
    return 45.23

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
