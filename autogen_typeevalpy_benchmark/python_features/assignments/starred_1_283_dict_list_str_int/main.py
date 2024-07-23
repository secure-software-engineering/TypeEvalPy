# Functions are assigned to variables via starred assignment
def func1():
    return {'xmnko': 51, 'useqv': 88, 'isdda': 4}


def func2():
    return [15, 93, 85]


def func3():
    return 'fkrio'


def func4():
    return 58

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
