# Functions are assigned to variables via starred assignment
def func1():
    return {'utlso': 42, 'nwwbu': 72, 'fbgpn': 64}


def func2():
    return 62


def func3():
    return 9.43


def func4():
    return (43, 41, 90)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
