# Functions are assigned to variables via starred assignment
def func1():
    return [86, 91, 60]


def func2():
    return 65


def func3():
    return 'ptdzk'


def func4():
    return 49.37

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
