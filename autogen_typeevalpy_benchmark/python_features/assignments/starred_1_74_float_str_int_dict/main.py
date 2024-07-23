# Functions are assigned to variables via starred assignment
def func1():
    return 40.83


def func2():
    return 'wtymp'


def func3():
    return 83


def func4():
    return {'tpacb': 61, 'zrupn': 94, 'ijooe': 5}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
