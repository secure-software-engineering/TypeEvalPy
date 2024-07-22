# Functions are assigned to variables via starred assignment
def func1():
    return 64.57


def func2():
    return 68


def func3():
    return 'bjqxc'


def func4():
    return [95, 72, 15]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
