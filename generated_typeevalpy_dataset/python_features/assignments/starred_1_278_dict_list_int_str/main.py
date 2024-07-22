# Functions are assigned to variables via starred assignment
def func1():
    return {'tdlor': 24, 'llles': 18, 'qbvfc': 9}


def func2():
    return [56, 76, 13]


def func3():
    return 65


def func4():
    return 'kpfsa'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
