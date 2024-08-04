# Functions are assigned to variables via starred assignment
def func1():
    return 18.89


def func2():
    return {'hfzpq': 91, 'lnazy': 74, 'ixquk': 30}


def func3():
    return 63


def func4():
    return (44, 40, 6)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
