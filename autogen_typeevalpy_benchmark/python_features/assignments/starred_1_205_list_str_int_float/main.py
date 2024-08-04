# Functions are assigned to variables via starred assignment
def func1():
    return [76, 12, 32]


def func2():
    return 'vtxxj'


def func3():
    return 96


def func4():
    return 23.1

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
