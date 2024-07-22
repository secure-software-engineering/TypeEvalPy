# Functions are assigned to variables via starred assignment
def func1():
    return [99, 76, 18]


def func2():
    return (90, 20, 29)


def func3():
    return 66.18


def func4():
    return 'mhljo'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
