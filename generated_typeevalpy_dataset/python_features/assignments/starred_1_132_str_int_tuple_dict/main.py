# Functions are assigned to variables via starred assignment
def func1():
    return 'futkh'


def func2():
    return 73


def func3():
    return (92, 95, 4)


def func4():
    return {'jqixp': 91, 'sckcv': 12, 'apnyn': 34}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
