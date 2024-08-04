# Functions are assigned to variables via starred assignment
def func1():
    return 15.58


def func2():
    return (79, 3, 95)


def func3():
    return 48


def func4():
    return [92, 18, 48]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
