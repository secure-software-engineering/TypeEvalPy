# Functions are assigned to variables via starred assignment
def func1():
    return 'sasto'


def func2():
    return {'hrkzu': 35, 'pnipu': 60, 'yaefp': 26}


def func3():
    return 89.08


def func4():
    return [26, 41, 22]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
