# Functions are assigned to variables via starred assignment
def func1():
    return 'oqtge'


def func2():
    return 60


def func3():
    return [16, 19, 79]


def func4():
    return (45, 12, 38)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
