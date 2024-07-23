# Functions are assigned to variables via starred assignment
def func1():
    return 'jdkde'


def func2():
    return 27


def func3():
    return (64, 80, 27)


def func4():
    return 85.38

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
