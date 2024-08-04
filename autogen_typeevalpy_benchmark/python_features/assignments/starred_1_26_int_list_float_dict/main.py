# Functions are assigned to variables via starred assignment
def func1():
    return 33


def func2():
    return [50, 32, 91]


def func3():
    return 51.03


def func4():
    return {'kqwrg': 40, 'ewczm': 51, 'drldn': 69}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
