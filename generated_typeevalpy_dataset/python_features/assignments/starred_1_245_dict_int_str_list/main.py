# Functions are assigned to variables via starred assignment
def func1():
    return {'ftleq': 34, 'atfdi': 35, 'qfhpn': 40}


def func2():
    return 73


def func3():
    return 'zzurz'


def func4():
    return [57, 84, 81]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
