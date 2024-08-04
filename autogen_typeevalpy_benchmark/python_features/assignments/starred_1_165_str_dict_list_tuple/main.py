# Functions are assigned to variables via starred assignment
def func1():
    return 'tonjh'


def func2():
    return {'awygu': 42, 'jgnhr': 11, 'qcklx': 62}


def func3():
    return [40, 44, 33]


def func4():
    return (49, 74, 28)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
