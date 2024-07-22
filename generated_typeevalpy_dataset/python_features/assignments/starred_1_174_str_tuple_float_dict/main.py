# Functions are assigned to variables via starred assignment
def func1():
    return 'znqmc'


def func2():
    return (9, 47, 42)


def func3():
    return 21.22


def func4():
    return {'gelxl': 38, 'fdked': 32, 'ordyz': 30}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
