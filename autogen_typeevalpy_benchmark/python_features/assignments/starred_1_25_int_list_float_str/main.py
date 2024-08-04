# Functions are assigned to variables via starred assignment
def func1():
    return 92


def func2():
    return [27, 46, 63]


def func3():
    return 89.55


def func4():
    return 'pcomc'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
