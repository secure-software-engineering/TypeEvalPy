# Functions are assigned to variables via starred assignment
def func1():
    return {'aejdr': 61, 'oetqs': 47, 'qaarq': 80}


def func2():
    return [78, 61, 35]


def func3():
    return 83


def func4():
    return 46.61

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
