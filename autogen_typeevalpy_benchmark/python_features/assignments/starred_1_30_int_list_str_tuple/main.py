# Functions are assigned to variables via starred assignment
def func1():
    return 92


def func2():
    return [13, 97, 59]


def func3():
    return 'moykx'


def func4():
    return (75, 22, 60)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
