# Functions are assigned to variables via starred assignment
def func1():
    return 'nuufc'


def func2():
    return {'hnsxb': 68, 'zoyxt': 33, 'dqogs': 65}


def func3():
    return 87


def func4():
    return [85, 51, 28]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
