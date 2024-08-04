# Functions are assigned to variables via starred assignment
def func1():
    return 'zjumw'


def func2():
    return (55, 71, 68)


def func3():
    return {'qlkrb': 72, 'syegb': 52, 'mxczx': 54}


def func4():
    return 92.33

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
