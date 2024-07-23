# Functions are assigned to variables via starred assignment
def func1():
    return {'gdfhr': 35, 'sjxsm': 5, 'kfrbd': 95}


def func2():
    return (63, 10, 77)


def func3():
    return 'iivfu'


def func4():
    return 63

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
