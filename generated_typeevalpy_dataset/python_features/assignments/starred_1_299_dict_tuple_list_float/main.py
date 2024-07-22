# Functions are assigned to variables via starred assignment
def func1():
    return {'nfuql': 27, 'tmrfv': 62, 'pgjsi': 35}


def func2():
    return (68, 63, 100)


def func3():
    return [56, 82, 64]


def func4():
    return 85.99

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
