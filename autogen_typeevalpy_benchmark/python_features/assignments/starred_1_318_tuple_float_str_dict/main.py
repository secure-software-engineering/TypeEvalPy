# Functions are assigned to variables via starred assignment
def func1():
    return (31, 69, 3)


def func2():
    return 4.22


def func3():
    return 'sklnk'


def func4():
    return {'xhlms': 5, 'cgtdk': 16, 'cixom': 34}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
