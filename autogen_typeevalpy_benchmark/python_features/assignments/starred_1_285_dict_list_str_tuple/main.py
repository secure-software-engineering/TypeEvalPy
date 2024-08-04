# Functions are assigned to variables via starred assignment
def func1():
    return {'yihnw': 54, 'tzgax': 1, 'ydyzz': 89}


def func2():
    return [43, 78, 56]


def func3():
    return 'elrbs'


def func4():
    return (27, 33, 49)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
