# Functions are assigned to variables via starred assignment
def func1():
    return [43, 2, 35]


def func2():
    return 'nkihk'


def func3():
    return 36


def func4():
    return 75.7

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
