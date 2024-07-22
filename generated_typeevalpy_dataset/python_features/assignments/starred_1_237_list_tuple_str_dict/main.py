# Functions are assigned to variables via starred assignment
def func1():
    return [22, 7, 77]


def func2():
    return (14, 96, 70)


def func3():
    return 'gtzvo'


def func4():
    return {'dtziv': 96, 'pdkdb': 87, 'eylkn': 82}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
