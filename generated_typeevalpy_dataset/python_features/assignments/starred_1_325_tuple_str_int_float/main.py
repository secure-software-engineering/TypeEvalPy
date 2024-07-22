# Functions are assigned to variables via starred assignment
def func1():
    return (78, 59, 15)


def func2():
    return 'mqccz'


def func3():
    return 41


def func4():
    return 24.19

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
