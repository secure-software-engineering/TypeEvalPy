# Functions are assigned to variables via starred assignment
def func1():
    return {'jjkdq': 35, 'znunt': 57, 'bvhvn': 61}


def func2():
    return 'bmxso'


def func3():
    return (10, 86, 81)


def func4():
    return 9.52

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
