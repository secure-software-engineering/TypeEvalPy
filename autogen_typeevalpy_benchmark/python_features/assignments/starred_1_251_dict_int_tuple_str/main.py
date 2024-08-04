# Functions are assigned to variables via starred assignment
def func1():
    return {'vupvm': 75, 'rafaj': 60, 'xback': 1}


def func2():
    return 4


def func3():
    return (88, 70, 37)


def func4():
    return 'htocs'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
