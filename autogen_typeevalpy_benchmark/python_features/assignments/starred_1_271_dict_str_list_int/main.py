# Functions are assigned to variables via starred assignment
def func1():
    return {'iixrw': 98, 'hxvog': 87, 'hvdmg': 51}


def func2():
    return 'vcoeu'


def func3():
    return [20, 27, 73]


def func4():
    return 34

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
