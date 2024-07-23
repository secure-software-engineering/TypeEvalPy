# Functions are assigned to variables via starred assignment
def func1():
    return (90, 23, 56)


def func2():
    return {'rcfvo': 45, 'rdwua': 12, 'fhgcq': 66}


def func3():
    return 80.63


def func4():
    return 'nzpoe'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
