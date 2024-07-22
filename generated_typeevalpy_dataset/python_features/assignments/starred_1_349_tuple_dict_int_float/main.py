# Functions are assigned to variables via starred assignment
def func1():
    return (84, 72, 69)


def func2():
    return {'pitcd': 55, 'wcjnp': 14, 'ydiiu': 28}


def func3():
    return 8


def func4():
    return 49.59

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
