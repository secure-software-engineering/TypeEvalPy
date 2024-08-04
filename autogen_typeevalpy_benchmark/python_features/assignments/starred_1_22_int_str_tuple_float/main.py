# Functions are assigned to variables via starred assignment
def func1():
    return 59


def func2():
    return 'qyevp'


def func3():
    return (98, 34, 32)


def func4():
    return 98.42

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
