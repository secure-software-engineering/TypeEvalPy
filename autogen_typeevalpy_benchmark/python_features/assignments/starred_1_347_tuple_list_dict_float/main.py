# Functions are assigned to variables via starred assignment
def func1():
    return (90, 29, 64)


def func2():
    return [10, 92, 12]


def func3():
    return {'pqrdf': 99, 'zgahr': 23, 'tynfa': 4}


def func4():
    return 90.53

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
