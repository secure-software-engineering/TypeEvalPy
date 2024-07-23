# Functions are assigned to variables via starred assignment
def func1():
    return 'afdes'


def func2():
    return 21


def func3():
    return (69, 54, 46)


def func4():
    return {'dhuil': 26, 'bwipu': 7, 'nbwdg': 28}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
