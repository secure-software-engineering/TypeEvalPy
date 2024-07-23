# Functions are assigned to variables via starred assignment
def func1():
    return {'nczgi': 86, 'jeqli': 86, 'rbdyd': 90}


def func2():
    return 27.13


def func3():
    return (59, 31, 69)


def func4():
    return [79, 54, 83]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
