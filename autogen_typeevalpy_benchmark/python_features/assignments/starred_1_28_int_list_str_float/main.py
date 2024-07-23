# Functions are assigned to variables via starred assignment
def func1():
    return 7


def func2():
    return [87, 52, 97]


def func3():
    return 'nvdjf'


def func4():
    return 7.43

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
