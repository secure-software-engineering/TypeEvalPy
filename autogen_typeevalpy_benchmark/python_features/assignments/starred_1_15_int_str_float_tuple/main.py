# Functions are assigned to variables via starred assignment
def func1():
    return 32


def func2():
    return 'jggru'


def func3():
    return 51.41


def func4():
    return (37, 21, 50)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
