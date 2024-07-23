# Functions are assigned to variables via starred assignment
def func1():
    return [7, 20, 47]


def func2():
    return {'blshm': 35, 'grrut': 6, 'wvesa': 35}


def func3():
    return (4, 88, 85)


def func4():
    return 69.87

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
