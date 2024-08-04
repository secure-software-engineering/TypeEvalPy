# Functions are assigned to variables via starred assignment
def func1():
    return {'wmaov': 28, 'vqxyl': 58, 'sgvij': 71}


def func2():
    return 'mgmxg'


def func3():
    return [57, 1, 90]


def func4():
    return 70.21

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
