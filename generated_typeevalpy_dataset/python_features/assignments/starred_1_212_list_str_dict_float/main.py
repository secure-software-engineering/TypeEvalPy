# Functions are assigned to variables via starred assignment
def func1():
    return [70, 95, 6]


def func2():
    return 'iwskr'


def func3():
    return {'vhxha': 29, 'mpwrw': 83, 'olvkd': 58}


def func4():
    return 24.53

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
