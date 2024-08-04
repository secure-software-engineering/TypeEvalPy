# Functions are assigned to variables via starred assignment
def func1():
    return 'bjhdg'


def func2():
    return 46


def func3():
    return (12, 95, 53)


def func4():
    return {'mqvif': 43, 'rkaow': 49, 'tkqtk': 89}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
