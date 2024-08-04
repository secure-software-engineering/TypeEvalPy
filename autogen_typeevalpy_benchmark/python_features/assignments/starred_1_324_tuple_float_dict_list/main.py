# Functions are assigned to variables via starred assignment
def func1():
    return (34, 4, 100)


def func2():
    return 71.9


def func3():
    return {'okxjo': 35, 'bksgx': 25, 'uahng': 96}


def func4():
    return [61, 60, 5]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
