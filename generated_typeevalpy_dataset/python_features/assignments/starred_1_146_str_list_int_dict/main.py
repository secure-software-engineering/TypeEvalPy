# Functions are assigned to variables via starred assignment
def func1():
    return 'lvuce'


def func2():
    return [25, 45, 8]


def func3():
    return 50


def func4():
    return {'bccjl': 40, 'zmkaq': 74, 'wfsiw': 26}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
