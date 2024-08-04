# Functions are assigned to variables via starred assignment
def func1():
    return {'zdlwm': 20, 'klori': 1, 'mntzs': 65}


def func2():
    return (62, 58, 72)


def func3():
    return 29


def func4():
    return [35, 57, 11]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
