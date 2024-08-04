# Functions are assigned to variables via starred assignment
def func1():
    return 75


def func2():
    return 77.98


def func3():
    return 'gwwbo'


def func4():
    return [39, 56, 85]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
