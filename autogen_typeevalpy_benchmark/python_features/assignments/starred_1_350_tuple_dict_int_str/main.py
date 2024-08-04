# Functions are assigned to variables via starred assignment
def func1():
    return (52, 82, 86)


def func2():
    return {'tklzm': 1, 'mwvpn': 30, 'gojqx': 68}


def func3():
    return 43


def func4():
    return 'edmec'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
