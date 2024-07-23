# Functions are assigned to variables via starred assignment
def func1():
    return 87


def func2():
    return 'vfzww'


def func3():
    return {'ylgux': 44, 'oipwf': 54, 'megan': 65}


def func4():
    return 21.94

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
