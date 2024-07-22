# Functions are assigned to variables via starred assignment
def func1():
    return (88, 55, 18)


def func2():
    return {'yezie': 95, 'zjyta': 41, 'apwta': 99}


def func3():
    return 16.75


def func4():
    return 64

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
