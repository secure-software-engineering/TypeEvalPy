# Functions are assigned to variables via starred assignment
def func1():
    return 61.4


def func2():
    return [5, 68, 17]


def func3():
    return 'jmthc'


def func4():
    return 17

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
