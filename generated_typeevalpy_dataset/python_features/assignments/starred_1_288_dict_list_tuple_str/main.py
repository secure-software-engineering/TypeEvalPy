# Functions are assigned to variables via starred assignment
def func1():
    return {'eqrcj': 84, 'heutp': 13, 'xbwrj': 88}


def func2():
    return [75, 23, 82]


def func3():
    return (40, 99, 26)


def func4():
    return 'hrwcs'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
