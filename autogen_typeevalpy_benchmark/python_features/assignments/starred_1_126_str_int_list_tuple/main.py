# Functions are assigned to variables via starred assignment
def func1():
    return 'vevip'


def func2():
    return 24


def func3():
    return [44, 44, 7]


def func4():
    return (74, 77, 20)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
