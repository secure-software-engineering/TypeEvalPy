# Functions are assigned to variables via starred assignment
def func1():
    return 76


def func2():
    return 'cxitc'


def func3():
    return (9, 51, 91)


def func4():
    return {'vdand': 37, 'jofgm': 65, 'ilowf': 65}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
