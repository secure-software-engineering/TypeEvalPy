# Functions are assigned to variables via starred assignment
def func1():
    return [86, 11, 15]


def func2():
    return (86, 99, 96)


def func3():
    return {'bvlkv': 87, 'louzt': 95, 'qcywa': 72}


def func4():
    return 66

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
