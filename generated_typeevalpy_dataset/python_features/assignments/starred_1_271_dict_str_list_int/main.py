# Functions are assigned to variables via starred assignment
def func1():
    return {'scynu': 75, 'yguzj': 6, 'cfozi': 12}


def func2():
    return 'etsub'


def func3():
    return [28, 23, 42]


def func4():
    return 23

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
