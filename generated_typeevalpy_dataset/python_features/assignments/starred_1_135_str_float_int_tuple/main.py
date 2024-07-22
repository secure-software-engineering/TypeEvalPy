# Functions are assigned to variables via starred assignment
def func1():
    return 'yxlfk'


def func2():
    return 68.27


def func3():
    return 8


def func4():
    return (85, 19, 61)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
