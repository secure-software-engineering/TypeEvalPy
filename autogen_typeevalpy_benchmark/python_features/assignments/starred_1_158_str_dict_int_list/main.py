# Functions are assigned to variables via starred assignment
def func1():
    return 'ouxgb'


def func2():
    return {'zkozi': 30, 'ysycm': 86, 'wxuen': 1}


def func3():
    return 56


def func4():
    return [93, 98, 11]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
