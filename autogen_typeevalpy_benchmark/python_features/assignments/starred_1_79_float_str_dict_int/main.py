# Functions are assigned to variables via starred assignment
def func1():
    return 73.78


def func2():
    return 'vvwtu'


def func3():
    return {'ralmx': 52, 'dwjlb': 3, 'vzsrx': 38}


def func4():
    return 14

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
