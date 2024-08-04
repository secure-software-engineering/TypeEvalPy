# Functions are assigned to variables via starred assignment
def func1():
    return [57, 63, 98]


def func2():
    return {'wqixp': 7, 'vvylc': 5, 'ybcsl': 36}


def func3():
    return (79, 4, 22)


def func4():
    return 'xghyv'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
