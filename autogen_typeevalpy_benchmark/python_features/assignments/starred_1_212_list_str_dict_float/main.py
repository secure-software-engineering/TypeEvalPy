# Functions are assigned to variables via starred assignment
def func1():
    return [49, 60, 91]


def func2():
    return 'vsigx'


def func3():
    return {'krrre': 95, 'dkrju': 90, 'lhgxm': 60}


def func4():
    return 79.44

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
