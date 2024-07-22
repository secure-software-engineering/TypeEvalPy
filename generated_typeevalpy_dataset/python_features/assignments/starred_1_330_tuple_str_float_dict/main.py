# Functions are assigned to variables via starred assignment
def func1():
    return (19, 28, 5)


def func2():
    return 'uytny'


def func3():
    return 12.85


def func4():
    return {'pvlfx': 50, 'yhkrk': 64, 'nhekf': 78}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
