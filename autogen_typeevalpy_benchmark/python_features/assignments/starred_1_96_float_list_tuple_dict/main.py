# Functions are assigned to variables via starred assignment
def func1():
    return 25.63


def func2():
    return [55, 78, 55]


def func3():
    return (37, 42, 27)


def func4():
    return {'icwkb': 36, 'lunat': 37, 'uidnl': 95}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
