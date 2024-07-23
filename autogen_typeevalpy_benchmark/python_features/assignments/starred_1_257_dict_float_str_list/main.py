# Functions are assigned to variables via starred assignment
def func1():
    return {'qxgnl': 57, 'kpsri': 58, 'ohvcf': 55}


def func2():
    return 30.92


def func3():
    return 'rlqpj'


def func4():
    return [75, 62, 34]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
