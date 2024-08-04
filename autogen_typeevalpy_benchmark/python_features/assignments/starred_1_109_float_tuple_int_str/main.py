# Functions are assigned to variables via starred assignment
def func1():
    return 1.01


def func2():
    return (93, 60, 94)


def func3():
    return 75


def func4():
    return 'krwvo'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
