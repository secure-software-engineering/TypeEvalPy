# Functions are assigned to variables via starred assignment
def func1():
    return 'dpfwp'


def func2():
    return 79.69


def func3():
    return {'qxajl': 9, 'zjlou': 95, 'igrsk': 92}


def func4():
    return [59, 88, 1]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
