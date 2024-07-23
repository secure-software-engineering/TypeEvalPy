# Functions are assigned to variables via starred assignment
def func1():
    return (21, 78, 19)


def func2():
    return 98


def func3():
    return 'lnqxn'


def func4():
    return [78, 82, 22]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
