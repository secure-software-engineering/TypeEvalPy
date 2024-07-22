# Functions are assigned to variables via starred assignment
def func1():
    return 'xvxlb'


def func2():
    return [36, 24, 47]


def func3():
    return (16, 60, 78)


def func4():
    return 37

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
