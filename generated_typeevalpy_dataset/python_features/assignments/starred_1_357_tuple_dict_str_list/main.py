# Functions are assigned to variables via starred assignment
def func1():
    return (87, 89, 76)


def func2():
    return {'xaohl': 97, 'fmjnx': 38, 'onmft': 55}


def func3():
    return 'fwatu'


def func4():
    return [94, 70, 85]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
