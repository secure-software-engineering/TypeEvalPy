# Functions are assigned to variables via starred assignment
def func1():
    return [42, 15, 18]


def func2():
    return 16


def func3():
    return (37, 74, 15)


def func4():
    return 'apekq'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
