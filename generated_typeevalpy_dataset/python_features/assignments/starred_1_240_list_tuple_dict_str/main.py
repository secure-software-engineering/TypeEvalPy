# Functions are assigned to variables via starred assignment
def func1():
    return [74, 90, 89]


def func2():
    return (78, 26, 70)


def func3():
    return {'lggkc': 91, 'afqov': 44, 'uthlj': 28}


def func4():
    return 'anjka'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
