# Functions are assigned to variables via starred assignment
def func1():
    return 75


def func2():
    return (7, 38, 46)


def func3():
    return 'mpmqx'


def func4():
    return [18, 76, 30]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
