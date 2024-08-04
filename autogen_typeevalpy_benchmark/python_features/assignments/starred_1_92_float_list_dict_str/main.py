# Functions are assigned to variables via starred assignment
def func1():
    return 35.35


def func2():
    return [30, 69, 50]


def func3():
    return {'cgvqo': 49, 'tpaqf': 55, 'udqwh': 87}


def func4():
    return 'etheu'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
