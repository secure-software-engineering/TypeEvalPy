# Functions are assigned to variables via starred assignment
def func1():
    return (8, 44, 80)


def func2():
    return 85.63


def func3():
    return {'ewylx': 44, 'axafa': 9, 'ugfcq': 66}


def func4():
    return [9, 86, 9]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
