# Functions are assigned to variables via starred assignment
def func1():
    return (94, 94, 9)


def func2():
    return 'vwyyr'


def func3():
    return [67, 77, 36]


def func4():
    return {'bsasd': 8, 'zdhkg': 98, 'sccpn': 74}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
