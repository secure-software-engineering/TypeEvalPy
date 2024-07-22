# Functions are assigned to variables via starred assignment
def func1():
    return {'uasmr': 27, 'ixssy': 20, 'gijsw': 100}


def func2():
    return [87, 78, 12]


def func3():
    return 90


def func4():
    return 3.47

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
