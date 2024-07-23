# Functions are assigned to variables via starred assignment
def func1():
    return [13, 1, 63]


def func2():
    return (38, 78, 85)


def func3():
    return 84.65


def func4():
    return {'ftshe': 18, 'myyoj': 90, 'ssxtv': 32}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
