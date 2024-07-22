# Functions are assigned to variables via starred assignment
def func1():
    return [28, 73, 17]


def func2():
    return 11.29


def func3():
    return (34, 54, 24)


def func4():
    return 88

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
