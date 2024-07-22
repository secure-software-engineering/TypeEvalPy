# Functions are assigned to variables via starred assignment
def func1():
    return 9


def func2():
    return 'ggcub'


def func3():
    return {'mwobp': 65, 'sfsiw': 22, 'hjklq': 72}


def func4():
    return [45, 56, 31]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
