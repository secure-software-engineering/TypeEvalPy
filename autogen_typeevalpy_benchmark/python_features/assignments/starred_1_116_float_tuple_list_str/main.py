# Functions are assigned to variables via starred assignment
def func1():
    return 72.46


def func2():
    return (1, 38, 5)


def func3():
    return [57, 76, 85]


def func4():
    return 'ugbwd'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
