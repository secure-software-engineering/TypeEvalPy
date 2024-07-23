# Functions are assigned to variables via starred assignment
def func1():
    return {'xskqm': 5, 'psaxi': 16, 'ejpub': 25}


def func2():
    return 15.07


def func3():
    return [56, 73, 50]


def func4():
    return 'nfuey'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
