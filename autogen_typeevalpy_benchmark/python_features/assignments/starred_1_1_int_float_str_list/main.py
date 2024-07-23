# Functions are assigned to variables via starred assignment
def func1():
    return 31


def func2():
    return 82.22


def func3():
    return 'xkspd'


def func4():
    return [46, 70, 69]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
