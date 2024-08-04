# Functions are assigned to variables via starred assignment
def func1():
    return 80


def func2():
    return (20, 21, 13)


def func3():
    return {'pgobi': 45, 'fluca': 77, 'dnlaq': 95}


def func4():
    return 'qsjfg'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
