# Functions are assigned to variables via starred assignment
def func1():
    return 42.2


def func2():
    return (70, 17, 7)


def func3():
    return [81, 58, 91]


def func4():
    return 11

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
