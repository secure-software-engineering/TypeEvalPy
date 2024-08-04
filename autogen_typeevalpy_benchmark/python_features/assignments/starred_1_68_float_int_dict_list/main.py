# Functions are assigned to variables via starred assignment
def func1():
    return 12.52


def func2():
    return 97


def func3():
    return {'rntwg': 59, 'jcttj': 13, 'uoyjm': 26}


def func4():
    return [70, 68, 62]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
