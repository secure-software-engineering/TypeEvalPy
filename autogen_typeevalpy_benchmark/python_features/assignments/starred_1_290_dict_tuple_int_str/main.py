# Functions are assigned to variables via starred assignment
def func1():
    return {'vhmqd': 10, 'quzzr': 21, 'eiruj': 1}


def func2():
    return (65, 21, 79)


def func3():
    return 4


def func4():
    return 'ucdus'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
