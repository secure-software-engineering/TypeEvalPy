# Functions are assigned to variables via starred assignment
def func1():
    return (37, 25, 11)


def func2():
    return [77, 90, 54]


def func3():
    return {'xccnn': 65, 'anulz': 25, 'flzhk': 6}


def func4():
    return 'aquwo'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
