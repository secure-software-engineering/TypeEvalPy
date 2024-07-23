# Functions are assigned to variables via starred assignment
def func1():
    return {'ywikc': 97, 'epzoh': 29, 'mpmfi': 70}


def func2():
    return 13


def func3():
    return 67.58


def func4():
    return [73, 74, 28]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
