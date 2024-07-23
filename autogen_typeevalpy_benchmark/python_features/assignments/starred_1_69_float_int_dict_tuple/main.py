# Functions are assigned to variables via starred assignment
def func1():
    return 24.0


def func2():
    return 15


def func3():
    return {'kaepg': 20, 'dcjfj': 23, 'ynfbs': 14}


def func4():
    return (9, 51, 56)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
