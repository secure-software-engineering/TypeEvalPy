# Functions are assigned to variables via starred assignment
def func1():
    return [41, 55, 65]


def func2():
    return {'tifsz': 81, 'htiyn': 25, 'rusud': 66}


def func3():
    return 27.39


def func4():
    return (5, 18, 13)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
