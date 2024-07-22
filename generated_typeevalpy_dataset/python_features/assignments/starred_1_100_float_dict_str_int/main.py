# Functions are assigned to variables via starred assignment
def func1():
    return 36.89


def func2():
    return {'axsxj': 70, 'fbrvn': 20, 'bqlwp': 12}


def func3():
    return 'mdhnp'


def func4():
    return 64

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
