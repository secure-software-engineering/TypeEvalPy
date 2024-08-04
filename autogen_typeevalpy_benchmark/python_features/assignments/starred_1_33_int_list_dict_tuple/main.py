# Functions are assigned to variables via starred assignment
def func1():
    return 45


def func2():
    return [88, 71, 28]


def func3():
    return {'rtapm': 61, 'flnzc': 53, 'pdirp': 94}


def func4():
    return (46, 83, 4)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
