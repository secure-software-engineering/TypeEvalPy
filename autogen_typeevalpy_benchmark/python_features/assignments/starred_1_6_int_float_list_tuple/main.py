# Functions are assigned to variables via starred assignment
def func1():
    return 57


def func2():
    return 90.28


def func3():
    return [76, 49, 100]


def func4():
    return (20, 70, 39)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
