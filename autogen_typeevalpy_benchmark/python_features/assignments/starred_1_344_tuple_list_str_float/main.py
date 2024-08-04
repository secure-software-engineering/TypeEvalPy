# Functions are assigned to variables via starred assignment
def func1():
    return (52, 93, 99)


def func2():
    return [53, 77, 27]


def func3():
    return 'fmfzd'


def func4():
    return 53.75

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
