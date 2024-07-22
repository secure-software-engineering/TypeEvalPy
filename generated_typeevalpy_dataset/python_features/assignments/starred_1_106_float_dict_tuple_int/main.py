# Functions are assigned to variables via starred assignment
def func1():
    return 87.14


def func2():
    return {'izdek': 42, 'ezmuv': 83, 'hdnbs': 90}


def func3():
    return (3, 44, 82)


def func4():
    return 61

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
