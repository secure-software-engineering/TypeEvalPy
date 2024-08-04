# Functions are assigned to variables via starred assignment
def func1():
    return (99, 15, 74)


def func2():
    return 95.53


def func3():
    return 'uzxne'


def func4():
    return 97

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
