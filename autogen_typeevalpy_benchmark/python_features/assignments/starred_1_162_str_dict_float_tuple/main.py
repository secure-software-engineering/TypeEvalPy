# Functions are assigned to variables via starred assignment
def func1():
    return 'mwkwz'


def func2():
    return {'mnedw': 26, 'fpxwe': 38, 'mltfr': 11}


def func3():
    return 79.84


def func4():
    return (17, 66, 79)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
