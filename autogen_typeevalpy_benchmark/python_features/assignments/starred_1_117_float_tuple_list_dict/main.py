# Functions are assigned to variables via starred assignment
def func1():
    return 54.26


def func2():
    return (82, 22, 89)


def func3():
    return [16, 63, 71]


def func4():
    return {'piqqv': 15, 'nsrzx': 49, 'zojjn': 59}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
