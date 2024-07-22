# Functions are assigned to variables via starred assignment
def func1():
    return (76, 24, 60)


def func2():
    return 7


def func3():
    return 6.89


def func4():
    return {'cauza': 37, 'egwnh': 5, 'bujmp': 60}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
