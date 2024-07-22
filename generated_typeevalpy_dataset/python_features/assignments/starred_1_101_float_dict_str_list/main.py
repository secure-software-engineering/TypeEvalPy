# Functions are assigned to variables via starred assignment
def func1():
    return 28.38


def func2():
    return {'pftfc': 98, 'hxfch': 63, 'vaptg': 21}


def func3():
    return 'fhghv'


def func4():
    return [49, 69, 98]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
