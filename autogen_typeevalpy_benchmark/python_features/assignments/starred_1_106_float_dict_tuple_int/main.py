# Functions are assigned to variables via starred assignment
def func1():
    return 51.16


def func2():
    return {'osrnk': 68, 'fnnjo': 18, 'roagt': 6}


def func3():
    return (40, 64, 83)


def func4():
    return 48

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
