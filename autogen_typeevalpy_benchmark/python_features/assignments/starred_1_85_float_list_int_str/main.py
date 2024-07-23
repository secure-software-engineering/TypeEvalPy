# Functions are assigned to variables via starred assignment
def func1():
    return 23.57


def func2():
    return [22, 13, 52]


def func3():
    return 87


def func4():
    return 'qganq'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
