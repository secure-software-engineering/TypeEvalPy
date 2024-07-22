# Functions are assigned to variables via starred assignment
def func1():
    return 42


def func2():
    return [9, 11, 26]


def func3():
    return (77, 76, 88)


def func4():
    return {'pizam': 11, 'koqbc': 53, 'snvan': 84}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
