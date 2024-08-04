# Functions are assigned to variables via starred assignment
def func1():
    return (31, 55, 64)


def func2():
    return 54.72


def func3():
    return 'xomko'


def func4():
    return [82, 25, 19]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
