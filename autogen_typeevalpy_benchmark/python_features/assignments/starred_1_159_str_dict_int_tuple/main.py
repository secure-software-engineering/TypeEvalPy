# Functions are assigned to variables via starred assignment
def func1():
    return 'vvwkt'


def func2():
    return {'izqhx': 98, 'serih': 90, 'bnurr': 44}


def func3():
    return 11


def func4():
    return (28, 49, 58)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
