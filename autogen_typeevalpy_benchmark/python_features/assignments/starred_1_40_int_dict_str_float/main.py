# Functions are assigned to variables via starred assignment
def func1():
    return 83


def func2():
    return {'adfdt': 83, 'dqbnv': 77, 'ahozk': 45}


def func3():
    return 'defep'


def func4():
    return 82.26

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
