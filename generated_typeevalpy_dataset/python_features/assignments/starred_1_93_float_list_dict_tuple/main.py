# Functions are assigned to variables via starred assignment
def func1():
    return 94.62


def func2():
    return [71, 68, 56]


def func3():
    return {'ertwe': 67, 'khdkn': 29, 'xexjd': 59}


def func4():
    return (14, 85, 19)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
