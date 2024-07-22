# Functions are assigned to variables via starred assignment
def func1():
    return (65, 70, 75)


def func2():
    return [95, 75, 28]


def func3():
    return 'clwdi'


def func4():
    return 43.93

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
