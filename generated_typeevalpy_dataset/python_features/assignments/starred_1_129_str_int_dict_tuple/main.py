# Functions are assigned to variables via starred assignment
def func1():
    return 'zsdih'


def func2():
    return 11


def func3():
    return {'bjupn': 81, 'zropl': 93, 'zmnlz': 27}


def func4():
    return (82, 10, 70)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
