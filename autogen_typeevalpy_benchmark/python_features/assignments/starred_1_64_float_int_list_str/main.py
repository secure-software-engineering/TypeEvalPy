# Functions are assigned to variables via starred assignment
def func1():
    return 72.14


def func2():
    return 12


def func3():
    return [38, 81, 42]


def func4():
    return 'phrxs'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
