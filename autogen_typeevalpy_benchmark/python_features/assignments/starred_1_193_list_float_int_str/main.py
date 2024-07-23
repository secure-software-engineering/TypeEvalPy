# Functions are assigned to variables via starred assignment
def func1():
    return [89, 45, 44]


def func2():
    return 62.57


def func3():
    return 2


def func4():
    return 'egojq'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
