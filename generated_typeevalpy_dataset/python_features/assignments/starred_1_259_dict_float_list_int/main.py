# Functions are assigned to variables via starred assignment
def func1():
    return {'samcz': 72, 'hccis': 90, 'ajkjl': 72}


def func2():
    return 83.91


def func3():
    return [51, 41, 72]


def func4():
    return 35

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
