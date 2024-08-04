# Functions are assigned to variables via starred assignment
def func1():
    return [60, 81, 32]


def func2():
    return (81, 53, 47)


def func3():
    return {'zsbdz': 50, 'unddk': 9, 'tnzvd': 82}


def func4():
    return 'qzfae'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
