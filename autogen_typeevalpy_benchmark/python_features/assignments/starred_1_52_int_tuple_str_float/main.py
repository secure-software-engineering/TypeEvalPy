# Functions are assigned to variables via starred assignment
def func1():
    return 2


def func2():
    return (76, 80, 8)


def func3():
    return 'lgpla'


def func4():
    return 84.56

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
