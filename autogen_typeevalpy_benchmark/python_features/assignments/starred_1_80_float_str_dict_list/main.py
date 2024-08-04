# Functions are assigned to variables via starred assignment
def func1():
    return 80.43


def func2():
    return 'gmwip'


def func3():
    return {'tbrvg': 88, 'rptju': 77, 'nikzw': 76}


def func4():
    return [71, 98, 16]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
