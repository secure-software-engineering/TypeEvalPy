# Functions are assigned to variables via starred assignment
def func1():
    return [45, 72, 94]


def func2():
    return {'xsqfr': 47, 'tjmmg': 2, 'steco': 38}


def func3():
    return 'ssdpg'


def func4():
    return 89.35

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
