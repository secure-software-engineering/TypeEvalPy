# Functions are assigned to variables via starred assignment
def func1():
    return {'zvocc': 98, 'avsub': 42, 'cgsxr': 24}


def func2():
    return 42


def func3():
    return 'nhpdz'


def func4():
    return (67, 11, 91)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
