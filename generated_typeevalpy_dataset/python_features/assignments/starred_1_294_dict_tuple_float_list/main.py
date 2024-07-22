# Functions are assigned to variables via starred assignment
def func1():
    return {'guqal': 54, 'qcvgw': 13, 'eoxxo': 13}


def func2():
    return (8, 79, 76)


def func3():
    return 59.81


def func4():
    return [34, 76, 14]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
