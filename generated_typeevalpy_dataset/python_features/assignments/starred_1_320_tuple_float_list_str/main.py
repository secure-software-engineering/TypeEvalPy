# Functions are assigned to variables via starred assignment
def func1():
    return (74, 88, 81)


def func2():
    return 84.93


def func3():
    return [52, 66, 38]


def func4():
    return 'hivnc'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
