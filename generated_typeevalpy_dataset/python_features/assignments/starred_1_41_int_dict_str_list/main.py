# Functions are assigned to variables via starred assignment
def func1():
    return 82


def func2():
    return {'tgrge': 37, 'wsgiv': 14, 'alyrb': 37}


def func3():
    return 'yucjb'


def func4():
    return [68, 96, 98]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
