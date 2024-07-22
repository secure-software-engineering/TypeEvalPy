# Functions are assigned to variables via starred assignment
def func1():
    return 'txwge'


def func2():
    return [1, 99, 41]


def func3():
    return 71.9


def func4():
    return 24

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
