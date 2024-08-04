# Functions are assigned to variables via starred assignment
def func1():
    return 57.82


def func2():
    return 'xnrpp'


def func3():
    return {'pkzeb': 89, 'tqabz': 25, 'juscf': 54}


def func4():
    return 16

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
