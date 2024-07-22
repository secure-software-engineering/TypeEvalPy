# Functions are assigned to variables via starred assignment
def func1():
    return {'fubuo': 5, 'fpxal': 14, 'nrnup': 20}


def func2():
    return [58, 2, 73]


def func3():
    return 'fbxqa'


def func4():
    return 11

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
