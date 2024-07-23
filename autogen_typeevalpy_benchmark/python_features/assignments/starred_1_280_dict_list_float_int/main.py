# Functions are assigned to variables via starred assignment
def func1():
    return {'prmcs': 85, 'gmbpz': 69, 'lnanm': 30}


def func2():
    return [63, 100, 98]


def func3():
    return 5.51


def func4():
    return 47

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
