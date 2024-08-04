# Functions are assigned to variables via starred assignment
def func1():
    return 'ujbzw'


def func2():
    return 94.98


def func3():
    return (42, 93, 84)


def func4():
    return 85

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
